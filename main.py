from fastapi import FastAPI, Path, HTTPException,Query
from generate_answer import get_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://aman-ai-assistant.vercel.app"
    ],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "ok"}

@app.get('/response')
def get_response(query: str =Query(..., min_length=2, max_length=300)) ->str:
    try:
         answer = get_answer(query=query)
    except Exception as e:
        print("Error", e)
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            raise HTTPException(
                status_code=429,
                detail="The assistant is busy right now. Please try again in a minute.",
            )
        raise HTTPException(status_code=500, detail="Something went wrong. Please try again.")
    
    return answer