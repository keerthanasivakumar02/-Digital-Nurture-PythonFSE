from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.courses.router import router as course_router
from app.auth.router import router as auth_router

app = FastAPI(
    title="Hands-On 9 - Authentication & Security",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Authentication Routes
app.include_router(auth_router)

app.include_router(course_router)
@app.get("/")
def home():
    return {
        "message": "Welcome to Hands-On 9 Authentication API"
    }