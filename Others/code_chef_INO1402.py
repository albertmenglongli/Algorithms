'''https://www.codechef.com/IOIPRAC/problems/INOI1402'''

def build_graph(edge_info, num_V):
    G = [[float('inf') for _ in range(num_V)] for _ in range(num_V)]
    for v1, v2, w in edge_info:
        G[v1][v2] = G[v2][v1] = w
    return G

def floyd(G, num_V):
    for k in range(num_V):
        for i in range(num_V):
            if i == k:
                continue
            for j in range(num_V):
                if j == i or j == k:
                    continue
                new_weight = G[i][k] + G[k][j]
                if G[i][j] > new_weight:
                    G[i][j] = new_weight

line_1_input = raw_input("")
num_V = int(line_1_input.split(" ")[0])
num_E = int(line_1_input.split(" ")[1])
edge_info = list()
for _ in range(num_E):
    line_x_input = raw_input("").strip()
    edge_info.append((int(line_x_input.split(" ")[0]) - 1, int(line_x_input.split(" ")[1]) - 1, int(line_x_input.split(" ")[2])))

floyd(build_graph(edge_info, num_V), num_V)
print max([max(filter(lambda x: x != float('inf'), sub_array)) for sub_array in G])
