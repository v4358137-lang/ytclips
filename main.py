from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os, uuid, shutil, json, subprocess
from pathlib import Path

app = FastAPI(title="ClipForge API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

def update_status(job_id, status, progress, clips=[], error=""):
    with open(OUTPUT_DIR / f"{job_id}_status.json", "w") as f:
        json.dump({"status": status, "progress": progress, "clips": clips, "error": error}, f)

def get_duration(path):
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", path],
        capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except:
        return 0.0

def process_video(job_id, input_path, max_clips, clip_duration):
    try:
        update_status(job_id, "analyzing", 20)
        job_dir = OUTPUT_DIR / job_id
        job_dir.mkdir(exist_ok=True)

        duration = get_duration(input_path)
        if duration == 0:
            raise Exception("Could not read video duration")

        # Split evenly
        num = min(max_clips, max(1, int(duration // clip_duration)))
        chunk = duration / num
        clips_info = []

        for i in range(num):
            start = i * chunk
            end = min((i + 1) * chunk, duration)
            clip_name = f"clip_{i+1:02d}.mp4"
            clip_path = str(job_dir / clip_name)

            update_status(job_id, f"cutting clip {i+1}/{num}", 30 + int(60*(i/num)))

            subprocess.run([
                "ffmpeg", "-y",
                "-ss", str(start),
                "-i", input_path,
                "-t", str(end - start),
                "-c:v", "libx264", "-c:a", "aac",
                "-preset", "fast", "-crf", "28",
                clip_path
            ], capture_output=True)

            clips_info.append({
                "name": clip_name,
                "url": f"/outputs/{job_id}/{clip_name}",
                "start": round(start, 1),
                "end": round(end, 1),
                "duration": round(end - start, 1),
                "index": i + 1
            })

        if os.path.exists(input_path):
            os.remove(input_path)

        update_status(job_id, "done", 100, clips_info)

    except Exception as e:
        update_status(job_id, "error", 0, [], str(e))

@app.post("/upload")
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...),
                 max_clips: int = 5, clip_duration: int = 60, method: str = "scene"):
    job_id = str(uuid.uuid4())
    input_path = UPLOAD_DIR / f"{job_id}_{file.filename}"
    with open(input_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    update_status(job_id, "queued", 0)
    background_tasks.add_task(process_video, job_id, str(input_path), max_clips, clip_duration)
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def status(job_id: str):
    f = OUTPUT_DIR / f"{job_id}_status.json"
    if not f.exists():
        return {"status": "not_found", "progress": 0, "clips": []}
    return json.load(open(f))

@app.get("/download/{job_id}/{clip_name}")
def download(job_id: str, clip_name: str):
    path = OUTPUT_DIR / job_id / clip_name
    if not path.exists():
        raise HTTPException(404, "Not found")
    return FileResponse(str(path), media_type="video/mp4", filename=clip_name)

@app.get("/health")
def health():
    return {"status": "ok"}
