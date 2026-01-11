from dotenv import load_dotenv
load_dotenv()

from .chains.answer_grader import answer_grader
from .chains.hallunication_grader import hallucination_grader
from .const import WEB_SEARCH_NODE, GRADE_DOC_NODE, GENERATE_NODE, RETRIEVE_NODE
from .state import GraphSate

from langgraph.graph import StateGraph, END
from .nodes import grade_documents, retrieve,generate, web_search

def grade_generation_grounded_in_documents_question(state: GraphSate) -> str: 
    print("---- Checking Hallucination ----")
    question = state["question"]
    docs = state["documents"]
    generation = state["generation"]

    score = hallucination_grader.invoke(
        {"documents": docs, "generation":generation}
    )

    if hallucination_grade := score.binary_score:
        print("---DECISION: Generation is grounded in documents ")
        print("---Grade Generation VS Question")
        score = answer_grader.invoke(
        {"question": question, "generation":generation}
        )
        if answer_grade := score.binary_score:
            print("---DECISION: Generation addresses question")
            return "useful"
        else :
            print("---DECISION: Generation does not address question ")
            return "not useful"
    else:
        print("---DECISION: Generation is not grounded in documents ")
        return "not supported"

def decide_to_generate(state: GraphSate) -> str: 
    print(" ---- Assessing Grade documents ----")
    if state["web_search"]:
        print("-- Not all documents are relevant to question")
        return WEB_SEARCH_NODE
    else :
        return GENERATE_NODE


work_flow = StateGraph(GraphSate)
work_flow.add_node(WEB_SEARCH_NODE, web_search)
work_flow.add_node(GRADE_DOC_NODE, grade_documents)
work_flow.add_node(GENERATE_NODE, generate)
work_flow.add_node(RETRIEVE_NODE, retrieve)

work_flow.set_entry_point(RETRIEVE_NODE)
work_flow.add_edge(RETRIEVE_NODE, GRADE_DOC_NODE)
work_flow.add_conditional_edges(GRADE_DOC_NODE, decide_to_generate, {
    WEB_SEARCH_NODE: WEB_SEARCH_NODE,
    GENERATE_NODE: GENERATE_NODE
}, )

# work_flow.add_conditional_edges(GENERATE_NODE, grade_generation_grounded_in_documents_question, {
#     "not supported":GENERATE_NODE,
#     "not useful": WEB_SEARCH_NODE,
#     "useful": END
# })
work_flow.add_edge(WEB_SEARCH_NODE, GENERATE_NODE)

work_flow.add_edge(GENERATE_NODE, END)

graph = work_flow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="rag_flow.png")


if __name__ == "__main__":
    print("")