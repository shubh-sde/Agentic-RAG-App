from dotenv import load_dotenv

from graph.chains.router import RouteQuery, question_router
load_dotenv()

import pprint
from graph.chains.hallunication_grader import GradeHallucination, hallucination_grader
from graph.chains.generation import generation_chain
from graph.chains.retreival_grade import retrieval_grader, GradeDocument
from ingestion import retriever


# def test_retrieval_grader_answer_yes() -> None: 
#     question = "agent memory"
#     docs = retriever.invoke(question)
#     doc_text= docs[1].page_content

#     res: GradeDocument = retrieval_grader.invoke({"question": question, "document": doc_text})
#     assert res.binary_score == "yes"


# def test_retrieval_grader_answer_no() -> None: 
#     question = "love couple"
#     docs = retriever.invoke(question)
#     doc_text= docs[1].page_content

#     res: GradeDocument = retrieval_grader.invoke({"question": question, "document": doc_text})
#     assert res.binary_score == "no"


# def test_generation_chain() -> None: 
#     question ="agent memory"
#     documents = retriever.invoke(question)
#     generation = generation_chain.invoke({"context": documents, "question": question})
#     print(generation)


# def test_hallunication_answer_yes() -> None: 
#     question ="agent memory"
#     documents = retriever.invoke(question)
#     generation = generation_chain.invoke({"context": documents, "question": question})
#     res:GradeHallucination = hallucination_grader.invoke({"documents":documents,"generation": generation})
#     assert res.binary_score


# def test_hallunication_answer_no() -> None: 
#     question ="agent memory"
#     documents = retriever.invoke(question)
#     # generation = generation_chain.invoke({"context": documents, "question": question})
#     res:GradeHallucination = hallucination_grader.invoke({"documents":documents,"generation": "love nd war"})
#     assert not res.binary_score

def test_router_to_vectorstore() -> None: 
    question = "agent memory"
    res: RouteQuery = question_router.invoke({"question":question})
    assert res.datasource == "vectorstore"

def test_router_to_web_search() -> None: 
    question = "love and war"
    res: RouteQuery = question_router.invoke({"question":question})
    assert res.datasource == "websearch"