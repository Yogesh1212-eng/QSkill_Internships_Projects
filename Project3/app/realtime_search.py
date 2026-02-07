import requests
from config.config import SERP_API_KEY

def google_search(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERP_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # ✅ Answer box (best case)
    if "answer_box" in data and "answer" in data["answer_box"]:
        return data["answer_box"]["answer"]

    # ✅ Organic results (FIXED KEY NAME)
    if "organic_results" in data and len(data["organic_results"]) > 0:
        return data["organic_results"][0].get("snippet", "No snippet found")

    return "No real-time data found."
