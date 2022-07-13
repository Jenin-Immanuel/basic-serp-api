from serp_mod import google_search

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return { "info": "Initalized API" }




query = input("Enter the term you want to search on google:")
results = google_search(query)
for i in results:
    print(i)