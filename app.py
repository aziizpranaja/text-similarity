import uvicorn
from utils import check_score
from pydantic import BaseModel
from fastapi import FastAPI, status
from TextSimilarity import TextSimilarity
from starlette.responses import JSONResponse

class RequestBody(BaseModel):
    text_1: str
    text_2: str 

app = FastAPI(docs_url=None, redoc_url=None)
text_similarity = TextSimilarity()

@app.post("/penilaian")
async def penilaian(data_request: RequestBody):
    if not data_request.text_2:
        return JSONResponse({
            "probability": 0,
            "score": 0
        }, status_code=status.HTTP_200_OK)
    try:
        probability = text_similarity.predict(data_request.text_1, data_request.text_2)
        return_value = check_score(float(probability))
        return JSONResponse(
            return_value
        , status_code=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return JSONResponse({
            "errors": "Please contact your administrator"
        }, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=53540)
