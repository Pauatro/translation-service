from fastapi import FastAPI

app = FastAPI()

@app.get("/translate/{language}")
async def root(language):
    return {"message": language}


