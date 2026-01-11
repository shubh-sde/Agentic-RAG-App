from typing import Any, Dict

from langchain_core.documents import Document
from graph.state import GraphSate

from langchain_tavily import TavilySearch

from dotenv import load_dotenv
load_dotenv()

web_search_tool = TavilySearch(max_results=3)

def web_search(state: GraphSate) -> Dict[str, Any]:
    print("--- Web search started ---")
    question = state["question"]
    documents = state["documents"]

    tavilySearch = web_search_tool.invoke({"query": question})['results']

    # As max result is 3, joining up the data of search result
    joined_search_result = "\n".join([tavily_result["content"] for tavily_result in tavilySearch])

    web_results = Document(page_content=joined_search_result)
    if documents is not None: 
        documents.append(web_results)
    else: 
        documents = [web_results]

    return {"question": question, "documents": documents}