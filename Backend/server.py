from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn
# from Database import dbInitializer            #do not delete! uncomment when loading for the first time
from Routes import transactionsRouter
from Routes import loginRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(loginRouter.router)
app.include_router(transactionsRouter.router)


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)