import uvicorn

from src.core.config import settings


def main():
    uvicorn.run("src.main:app", host=settings.HOST, port=settings.PORT, reload=settings.ENVIRONMENT == "development")


if __name__ == "__main__":
    main()
