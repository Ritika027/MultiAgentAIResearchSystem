from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print

# Load environment variables
load_dotenv()

# Get API key safely
api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY not found. Check your .env file")

tavily = TavilyClient(api_key=api_key)

#1st tool is to fetch recent information from the web. This is crucial for an agent to stay updated and make informed decisions based on the latest data. The tool will use the Tavily API to perform web searches and return relevant results.
@tool
def web_search(query: str) -> str:
    """
    Search the web for recent and reliable information on a topic.
    Returns Titles, URLs, and snippets.
    """
    results = tavily.search(query=query, max_results=5)
    out = []

    for r in results.get('results', []):  # safe access
        out.append(
            f"Title: {r.get('title')}\n"
            f"URL: {r.get('url')}\n"
            f"Snippet: {r.get('content', '')[:300]}\n"
        )

    return "\n----\n".join(out)


# Test
# if __name__ == "__main__":
#     print(web_search.invoke("What are the recent news"))


@tool
def scrape_url(url: str) -> str:
    """Scrape and return clean text content from a given URL for deeper reading."""
    try:
        resp = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"

# print(scrape_url.invoke("https://www.hindustantimes.com/india-news/noida-protests-domestic-workers-go-on-strike-in-sector-121-cleo-county-demand-pay-raise-101776168682549.html"))
