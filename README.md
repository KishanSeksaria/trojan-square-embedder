This is just a simple FastAPI app to generate embeddings using Hugging Face's `sentence-transformers/all-MiniLM-L6-v2` model.

It exposes a single endpoint `/embed` that takes a string and returns its embeddings.

I made this to work with my `trojan-square` project.