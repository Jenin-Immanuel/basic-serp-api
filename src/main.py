from serp_mod import google_search

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/api")
async def root(q: str | None = None):
    if q == None:
        raise HTTPException(status_code=404, detail="Query not given")
    return google_search(q)
