import uvicorn
from app.main import app

def start():
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, log_config="logging.yaml")

if __name__ == "__server__":
    start()
