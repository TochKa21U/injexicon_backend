import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apisrc.routes import user_routes, challange_routes
from apisrc.db.database import create_tables
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# Disable tracing on LangChain
os.environ["LANGCHAIN_HANDLER"] = ""

# Cors Settings
cors_allowed_origins_str = os.getenv("CORS_ALLOWED_ORIGINS", "")
origins = cors_allowed_origins_str.split(",") if cors_allowed_origins_str else ["*"]
origins=["*"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Call create tables here
create_tables()

@app.get("/health")
def getHealthCheck():
    return "ok"

@app.get("/")
def getHealthCheck():
    return {"apiVersion":"0.0.1","update":"060823"}

app.include_router(user_routes.router,tags=["Users"],prefix="/users")
app.include_router(challange_routes.router,tags=["Challanges"],prefix="/challanges")