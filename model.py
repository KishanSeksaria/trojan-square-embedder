import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
save_path = os.path.join(os.path.dirname(__file__), "local_model")
print("Saving model to:", save_path)
model.save(save_path)
