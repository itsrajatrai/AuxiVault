from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import auth
from app.models import user
from app.routers import bookmark



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
app.include_router(bookmark.router)



Base.metadata.create_all(bind=engine)

print("You are running the backend server. Visit http://localhost:8000/docs to see the API documentation.")


