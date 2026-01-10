from typing import Any, Dict
from graph.chains.generation import generation_chain
from graph.state import GraphSate


def generate(state: GraphSate)-> Dict[str, Any]: 
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"question": question, "documents":documents, "generation":generation}