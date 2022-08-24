from urllib.request import Request
from fastapi import FastAPI, Request, HTTPException
from models import Item
from sentence_transformers import SentenceTransformer, util


def initialize():
    app = FastAPI()
    model = SentenceTransformer(
        'distiluse-base-multilingual-cased-v1', device='cuda')

    return app, model


app, model = initialize()


@app.post('/text-similarity')
def text_similarity(request: Request, item: Item):
    """ 
    Check text similarity
    """
    # validate if responses are empty
    if item.expected_response == '' or item.student_response == '':
        raise HTTPException(
            status_code=400, detail="Invalid responses provided, the responses mustn't be empty")

    # Encode sentences to get its embeddings
    embedding1 = model.encode(item.expected_response, convert_to_tensor=True)
    embedding2 = model.encode(item.student_response, convert_to_tensor=True)

    # Compute similarity
    cosine_scores = util.pytorch_cos_sim(embedding1, embedding2)

    return {"similarity_score": round(cosine_scores.item() * 10, 2)}
