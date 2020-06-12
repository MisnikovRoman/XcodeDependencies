# libraries
import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

def showGraph(graph):
    df = pd.DataFrame(graph)

    # Build your graph
    G = nx.from_pandas_edgelist(df, 'from', 'to')

    # Plot it
    nx.draw(G, with_labels=True)
    plt.show()
