from typing import Any, Dict

from graph.state import GraphSate
from ingestion import retriever


def retrieve(state: GraphSate) -> Dict[str, Any]: 
    print ("----retriever----")
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents":documents, "question": question}