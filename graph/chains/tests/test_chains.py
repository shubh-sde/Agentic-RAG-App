import pprint
from dotenv import load_dotenv
load_dotenv()

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


def test_generation_chain() -> None: 
    question ="agent memory"
    documents = retriever.invoke(question)
    generation = generation_chain.invoke({"context": documents, "question": question})
    print(generation)