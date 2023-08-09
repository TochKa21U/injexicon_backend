from apisrc import main
import uvicorn
import os

PORT = os.getenv("PORT", 8888)
CURRENT_ENV = os.getenv("CURRENT_ENV","DEV")

if __name__ == "__main__":
    if CURRENT_ENV == "PROD":
        uvicorn.run("apisrc.main:app",port=PORT,log_level="warning",reload=False)
    uvicorn.run("apisrc.main:app",port=PORT,log_level="info",reload=True)
    