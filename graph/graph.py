from dotenv import load_dotenv

from graph.state import GraphSate
load_dotenv()

from const import GENERATE_NODE, GRADE_DOC_NODE,RETRIEVE_NODE, WEB_SEARCH_NODE
from langgraph.graph import StateGraph, END
from nodes import grade_documents, retrieve,generate, web_search

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
work_flow.add_edge(WEB_SEARCH_NODE, GENERATE_NODE)
work_flow.add_edge(GENERATE_NODE, END)

graph = work_flow.compile()
graph.get_graph().draw_mermaid_png(output_file_path="flow.png")


if __name__ == "__main__":
    print("")