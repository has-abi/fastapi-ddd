import uvicorn

from src.app import create_app

app = create_app()


if __name__ == "__main__":
    uvicorn.run(
        "src.server:app", host="0.0.0.0", port=8000, reload=True, log_level="info"
    )
