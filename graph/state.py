import operator
from typing import List, TypedDict, Annotated

class GraphSate(TypedDict):

    """
    Represents the state of our graph

    Attributes : 
        question: question
        generation: LLM generation 
        web_search: whether to add search
        documents: list of documents
    """

    question: str
    generation: str
    web_search: bool
    documents: Annotated[List[str], operator.add]

