from typing import Dict, Any
from graph.chains.retreival_grade import retrieval_grader, GradeDocument
from graph.state import GraphSate

def grade_documents(state: GraphSate) -> Dict[str, Any]:
    """
    Determine whether the retrieved documents are relevant to the question
    if any document is not relevant, we will pass a flag to run the web search

    Args: 
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and update the web search state
    """ 
    print ("------ Checking documents relevant to the question-----")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = False

    for d in documents: 
        score: GradeDocument = retrieval_grader.invoke({"question": question, "document": d.page_content})
        grade = score.binary_score
        if grade.lower == "yes":
            print("---- FOUND RELEVANT DOCUMENT----")
            filtered_docs.append(d)
        else: 
            print("---- NOT FOUND RELEVANT DOCUMENT----")
            web_search = True
            continue
    return {"documents":filtered_docs, "question": question, "web_search":web_search}
