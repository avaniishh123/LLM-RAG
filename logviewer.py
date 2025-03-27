from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

@app.get("/logs", response_class=HTMLResponse)
def view_logs():
    if not os.path.exists("function_logs.txt"):
        return "<h3>No logs found.</h3>"

    with open("function_logs.txt", "r") as f:
        lines = f.readlines()

    html = "<h2>Function Execution Logs</h2><ul>"
    for line in reversed(lines):
        html += f"<li><code>{line.strip()}</code></li>"
    html += "</ul>"

    return html
