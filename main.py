from fastapi import FastAPI
import httpx

app = FastAPI()
API_KEY = ""

@app.get("/")
def home():
    return {"message": "MovieMood API funcionando"}

@app.get("/buscar filme")
async def buscar_filme(titulo: str):
    url = "http://www.omdbapi.com/"

    params = {
        "apikey": API_KEY,
        "s": titulo
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)

    dados = response.json()

    filmes = []
    for filme in dados["Search"]:
        filmes.append({
            "titulo" : filme["Title"],
            "ano" : filme["Year"],
            "poster" : filme["Poster"],
            "imdb_id": filme["imdbID"]
        })
    return filmes
