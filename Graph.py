import matplotlib.pyplot as plt
import networkx as nx
import tkinter as tk

def show_graph():

    G = nx.DiGraph()

    edges =  [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (5, 6), (2, 6), (3, 7), (6, 7), (7, 8), (5, 8)]
    G.add_edges_from(edges)

    nx.draw(G, with_labels = True, arrows = True, node_size = 500, node_color = "Pink", font_size = 10)

    plt.show() 

root = tk.Tk()
root.title("Graph")
button = tk.Button(root, text = "Show Graph", command = show_graph)
button.pack(padx = 20, pady = 20)

root.mainloop()
