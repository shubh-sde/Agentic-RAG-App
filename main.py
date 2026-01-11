from graph.graph_workflow import graph
from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__": 
    print ("Hello advance RAG...")
    print(graph.invoke(input= {"question": "What is agent"}))