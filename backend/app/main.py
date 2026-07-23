from fastapi import FastAPI

app = FastAPI(
    title="Elif AI",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"message": "Elif AI API çalışıyor"}

@app.get("/health")
async def health():
    return {"status": "ok"}
