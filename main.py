from graph.graph import graph
from dotenv import load_dotenv
load_dotenv

if __name__ == "main": 
    print ("Hello advance RAG")
    print(graph.invoke(input= {"question": "What is agent memory"}))