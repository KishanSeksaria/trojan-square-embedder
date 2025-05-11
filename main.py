from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import os

app = FastAPI()

model_path = os.path.join(os.path.dirname(__file__), "local_model")
model = SentenceTransformer(model_path)

class EmbedRequest(BaseModel):
  textToEmbed: str

@app.post("/embed")
async def embed_text(data: EmbedRequest):
  embeddings = model.encode([data.textToEmbed]).tolist()
  return {"embeddings": embeddings}
