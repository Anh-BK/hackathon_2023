import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.load_env import ENV

env = ENV()

from api.v1 import api_v1_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/healthcheck/")
def healthcheck():
    return 'Health - OK'

app.include_router(api_v1_router, prefix='/api/v1')

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=env.API_PORT, debug=True)
