from fastapi import FastAPI

app = FastAPI(title="AI Engineering API")

@app.get("/")
def home():
    return {"message": "AI Engineering Started!"}

@app.get("/health")
def health():
    return {"status": "healthy"}