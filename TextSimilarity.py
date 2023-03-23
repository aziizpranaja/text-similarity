from multilingual_clip import pt_multilingual_clip
from numpy.linalg import norm
import transformers
import numpy as np
import torch


class TextSimilarity:
    def __init__(self, name_model="M-CLIP/XLM-Roberta-Large-Vit-L-14"):
        self.name_model = name_model
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(self.name_model)
        self.model = pt_multilingual_clip.MultilingualCLIP.from_pretrained(self.name_model)
        self.model.eval()

    def predict(self, text_1, text_2):
        with torch.no_grad():
            embeddings = self.model.forward([text_1, text_2], self.tokenizer)
            embeddings_1, embeddings_2 = embeddings.cpu().detach().numpy()
        cosine = np.dot(embeddings_1,embeddings_2)/(norm(embeddings_1)*norm(embeddings_2))
        return cosine