from collections import defaultdict

def transpose(G):
    GT = defaultdict(set)
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT


def dfs_topsort(G):
    S, res = set(), []

    def recurse(u):
        if u in S:
            return
        S.add(u)
        for v in G[u]:
            recurse(v)
        res.append(u)

    for u in G:
        recurse(u)
    res.reverse()
    return res


def walk(G, u, seen):
    res = {u}

    def recurse(u):
        for v in G[u]:
            if v in seen:
                continue
            else:
                seen.add(v)
                res.add(v)
                recurse(v)

    recurse(u)
    return res


def generate_G():
    G = defaultdict(set)
    G['a'] = {'b', 'c'}
    G['b'] = {'d', 'e', 'i'}
    G['c'] = {'d'}
    G['d'] = {'a', 'h'}
    G['e'] = {'f'}
    G['f'] = {'g'}
    G['g'] = {'e', 'h'}
    G['h'] = {'i'}
    G['i'] = {'h'}
    return G


def scc(G):
    GT = transpose(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen: continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs


def draw_G(raw_G):
    import networkx as nx
    import matplotlib
    # generate postscript output by default from http://matplotlib.org/faq/usage_faq.html#what-is-a-backend
    matplotlib.use('PS')
    import matplotlib.pyplot as plt
    import pylab
    G = nx.DiGraph()
    G.add_nodes_from(raw_G.keys())
    G.add_edges_from([(u, v) for u in raw_G for v in raw_G[u]], weight=1)
    pos = nx.spring_layout(G)
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    nx.draw_networkx_edges(G, pos, alpha=0.3)
    nx.draw(G, pos=pos, node_size=250, with_labels=True, )
    plt.axis('off')
    plt.savefig("kosaraju.png")


if __name__ == "__main__":
    raw_G = generate_G()
    print scc(raw_G)
    # [set(['a', 'c', 'b', 'd']), set(['e', 'g', 'f']), set(['i', 'h'])]
    
    #draw_G(raw_G)
