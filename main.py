@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

:root {
  --bg: #0a0a0f;
  --surface: #13131a;
  --surface2: #1c1c26;
  --border: #2a2a3a;
  --accent: #7c3aed;
  --accent2: #a855f7;
  --accent-glow: rgba(124, 58, 237, 0.3);
  --success: #10b981;
  --error: #ef4444;
  --text: #f1f0ff;
  --text-muted: #888aaa;
  --radius: 14px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  min-height: 100vh;
  background-image: radial-gradient(ellipse at 20% 50%, rgba(124,58,237,0.08) 0%, transparent 60%),
                    radial-gradient(ellipse at 80% 20%, rgba(168,85,247,0.06) 0%, transparent 60%);
}

/* HEADER */
.header {
  text-align: center;
  padding: 48px 20px 32px;
  border-bottom: 1px solid var(--border);
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 10px;
}

.logo-icon {
  font-size: 2rem;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.logo-text {
  font-family: 'Syne', sans-serif;
  font-size: 2.2rem;
  font-weight: 800;
  background: linear-gradient(135deg, #c4b5fd, #f0abfc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.tagline {
  color: var(--text-muted);
  font-size: 0.95rem;
  font-weight: 300;
}

/* MAIN */
.main {
  max-width: 820px;
  margin: 0 auto;
  padding: 40px 20px 60px;
}

/* UPLOADER */
.drop-zone {
  border: 2px dashed var(--border);
  border-radius: var(--radius);
  padding: 60px 30px;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s;
  background: var(--surface);
  margin-bottom: 28px;
}

.drop-zone:hover, .drop-zone.dragging {
  border-color: var(--accent);
  background: rgba(124,58,237,0.06);
  box-shadow: 0 0 30px var(--accent-glow);
}

.drop-zone.has-file {
  border-color: var(--success);
  border-style: solid;
}

.drop-icon, .file-icon { font-size: 3rem; margin-bottom: 12px; }
.drop-title, .file-name {
  font-family: 'Syne', sans-serif;
  font-size: 1.2rem;
  font-weight: 700;
  margin-bottom: 6px;
}
.drop-sub, .file-size { color: var(--text-muted); font-size: 0.85rem; }
.file-change { color: var(--accent2); font-size: 0.8rem; margin-top: 6px; }

/* SETTINGS */
.settings {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
  margin-bottom: 24px;
}

.settings-title {
  font-family: 'Syne', sans-serif;
  font-size: 1rem;
  font-weight: 700;
  margin-bottom: 18px;
  color: var(--accent2);
}

.settings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
}

.setting-item { display: flex; flex-direction: column; gap: 8px; }
.setting-item label { font-size: 0.85rem; color: var(--text-muted); }
.setting-item strong { color: var(--text); }

.setting-item select, .setting-item input[type="range"] {
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  padding: 8px 12px;
  font-family: 'DM Sans', sans-serif;
  font-size: 0.9rem;
  outline: none;
  cursor: pointer;
}

.setting-item select:focus { border-color: var(--accent); }
.setting-item input[type="range"] { padding: 4px 0; accent-color: var(--accent); }

/* BUTTONS */
.upload-btn {
  width: 100%;
  padding: 16px;
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  border: none;
  border-radius: var(--radius);
  color: white;
  font-family: 'Syne', sans-serif;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  box-shadow: 0 4px 24px var(--accent-glow);
}

.upload-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 32px var(--accent-glow);
}

.upload-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.method-info {
  margin-top: 12px;
  font-size: 0.82rem;
  color: var(--text-muted);
  text-align: center;
}

/* ERRORS */
.error-msg {
  background: rgba(239,68,68,0.1);
  border: 1px solid rgba(239,68,68,0.3);
  border-radius: 8px;
  padding: 12px 16px;
  color: #fca5a5;
  font-size: 0.9rem;
  margin-bottom: 16px;
}

/* PROCESSING */
.processing {
  text-align: center;
  padding: 40px 20px;
}

.processing-icon { font-size: 4rem; margin-bottom: 16px; animation: spin 2s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }

.processing-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.8rem;
  font-weight: 800;
  margin-bottom: 8px;
}

.processing-sub { color: var(--text-muted); margin-bottom: 32px; }

.progress-bar-wrap {
  background: var(--surface2);
  border-radius: 999px;
  height: 10px;
  overflow: hidden;
  margin-bottom: 10px;
}

.progress-bar {
  height: 100%;
  background: linear-gradient(90deg, var(--accent), var(--accent2));
  border-radius: 999px;
  transition: width 0.5s ease;
  box-shadow: 0 0 12px var(--accent-glow);
}

.progress-label { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 32px; }

.steps { display: flex; flex-direction: column; gap: 10px; max-width: 320px; margin: 0 auto; }

.step {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.9rem;
  padding: 8px 14px;
  border-radius: 8px;
  background: var(--surface);
}

.step.done { color: var(--success); }
.step.active { color: var(--accent2); background: rgba(124,58,237,0.1); font-weight: 500; }
.step.pending { color: var(--text-muted); }

/* RESULTS */
.results-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 28px;
  flex-wrap: wrap;
  gap: 12px;
}

.results-title {
  font-family: 'Syne', sans-serif;
  font-size: 1.6rem;
  font-weight: 800;
}

.reset-btn {
  padding: 10px 20px;
  background: var(--surface2);
  border: 1px solid var(--border);
  border-radius: 8px;
  color: var(--text);
  font-family: 'DM Sans', sans-serif;
  cursor: pointer;
  transition: all 0.2s;
}

.reset-btn:hover { border-color: var(--accent); color: var(--accent2); }

.clips-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 20px;
  margin-bottom: 36px;
}

.clip-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  transition: all 0.2s;
}

.clip-card:hover {
  border-color: var(--accent);
  box-shadow: 0 4px 20px var(--accent-glow);
}

.clip-number {
  font-family: 'Syne', sans-serif;
  font-size: 0.8rem;
  font-weight: 700;
  color: var(--accent2);
  padding: 10px 14px 0;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.clip-video {
  width: 100%;
  max-height: 240px;
  background: #000;
  display: block;
  margin: 8px 0;
}

.clip-meta {
  display: flex;
  justify-content: space-between;
  padding: 0 14px 10px;
  font-size: 0.8rem;
  color: var(--text-muted);
}

.clip-actions {
  display: flex;
  gap: 8px;
  padding: 0 14px 14px;
}

.download-btn, .share-btn {
  flex: 1;
  padding: 9px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-family: 'DM Sans', sans-serif;
  cursor: pointer;
  text-align: center;
  text-decoration: none;
  transition: all 0.2s;
  border: none;
}

.download-btn {
  background: linear-gradient(135deg, var(--accent), var(--accent2));
  color: white;
}

.share-btn {
  background: var(--surface2);
  border: 1px solid var(--border);
  color: var(--text);
}

.share-btn:hover { border-color: var(--accent2); color: var(--accent2); }

/* TIPS */
.tips {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  padding: 24px;
}

.tips h3 {
  font-family: 'Syne', sans-serif;
  font-size: 1rem;
  margin-bottom: 14px;
}

.tips ul { list-style: none; display: flex; flex-direction: column; gap: 8px; }
.tips li { font-size: 0.9rem; color: var(--text-muted); }

/* FOOTER */
.footer {
  text-align: center;
  padding: 20px;
  color: var(--text-muted);
  font-size: 0.8rem;
  border-top: 1px solid var(--border);
}

@media (max-width: 600px) {
  .logo-text { font-size: 1.6rem; }
  .clips-grid { grid-template-columns: 1fr; }
  .settings-grid { grid-template-columns: 1fr; }
}
