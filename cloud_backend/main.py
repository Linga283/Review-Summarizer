from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow all CORS origins for demo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data for demo (replace with API call or scraping logic if needed)
SAMPLE_REVIEWS = [
    "This product is amazing! It exceeded my expectations.",
    "Not worth the price. Poor quality and bad customer service.",
    "Decent product for the money. Does the job.",
    "Absolutely love it! Will buy again.",
    "Terrible experience. The product broke after one week.",
    "Good value for money. Satisfied with the purchase.",
    "Product is okay, but shipping was slow.",
]

# HuggingFace summarization API (free tier, limited usage)
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HF_HEADERS = {"Authorization": "Bearer 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"}  # User's HuggingFace token

class SummarizeRequest(BaseModel):
    url: str

@app.post("/summarize")
async def summarize(req: SummarizeRequest):
    # For demo, use sample reviews. Replace this part with real API/scraping if possible.
    reviews = SAMPLE_REVIEWS
    text = " ".join(reviews)
    summary = ""
    try:
        # Call HuggingFace summarization API
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json={"inputs": text[:1024]})
        if response.ok:
            summary = response.json()[0]['summary_text']
        else:
            summary = "Summary unavailable (API limit or error)."
    except Exception as e:
        summary = f"Summary error: {str(e)}"
    # Calculate like/dislike (dummy for demo)
    like_percentage = 70
    dislike_percentage = 30
    return {
        "summary": summary,
        "like_percentage": like_percentage,
        "dislike_percentage": dislike_percentage,
        "sample_reviews": reviews
    }
