from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth
from app.models import user



app = FastAPI()
# Allow frontend requests (adjust origin if needed)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "AuxiVault backend is working"}


app.include_router(auth.router)


Base.metadata.create_all(bind=engine)


