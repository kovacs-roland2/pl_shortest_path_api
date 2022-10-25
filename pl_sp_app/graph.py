def ret_data(player1, player2):
    import pickle
    import networkx as nx
    import pandas as pd
    graph = pickle.load(open('pl_graph.sav','rb'))
    sp = nx.shortest_path(graph, player1, player2)
    player1 = []
    player2 = []
    clubs = []
    seasons = []
    for i in range(len(sp)-1):
        player1.append(sp[i])
        player2.append(sp[i+1])
        clubs.append(graph.get_edge_data(sp[i], sp[i+1]).get('Club'))
        seasons.append(graph.get_edge_data(sp[i], sp[i+1]).get('Season'))
    result_df = pd.DataFrame(list(zip(player1, clubs, seasons, player2)),
                columns =['Player1', 'Club', 'Season', 'Player2'])
    return result_df