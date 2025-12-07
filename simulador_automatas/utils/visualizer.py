import networkx as nx
from matplotlib.figure import Figure

def draw_automaton(automaton, is_nfa=False):
    fig = Figure(figsize=(6, 5), facecolor='white')
    ax = fig.add_subplot(111)

    G = nx.DiGraph()

    for st in automaton.states:
        G.add_node(st)

    edge_map = {}
    for (src, sym), dsts in automaton.transitions.items():
        if not is_nfa:
            dsts = [dsts]
        for dst in dsts:
            key = (src, dst)
            if key not in edge_map:
                edge_map[key] = set()
            edge_map[key].add(sym)

    for (src, dst), symbols in edge_map.items():
        G.add_edge(src, dst, label=",".join(sorted(symbols)))

    pos = nx.spring_layout(G, k=1.5, iterations=50) if G.nodes else {}

    node_colors = []
    for st in G.nodes():
        if st == automaton.start_state and st in automaton.final_states:
            node_colors.append("#a8e6cf")  # verde suave - inicio y final
        elif st == automaton.start_state:
            node_colors.append("#88d8f7")  # azul suave - inicio
        elif st in automaton.final_states:
            node_colors.append("#ffb3ba")  # rosa suave - final
        else:
            node_colors.append("#e8e8e8")  # gris claro - normal

    nx.draw(
        G, pos, ax=ax,
        with_labels=True,
        node_color=node_colors,
        node_size=2000,
        font_size=12,
        font_weight='bold',
        font_color='#2c3e50',
        edge_color='#7f8c8d',
        arrows=True,
        arrowstyle='->',
        arrowsize=20,
        width=2
    )

    edge_labels = nx.get_edge_attributes(G, "label")
    if edge_labels:
        # Etiquetas de transiciones con color distintivo según el tipo de autómata
        label_color = '#9b59b6' if is_nfa else '#e74c3c'  # morado para NFA, rojo para DFA
        
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=edge_labels,
            ax=ax, 
            font_size=10, 
            font_color=label_color,
            font_weight='bold',
            bbox=dict(
                boxstyle='round,pad=0.3', 
                facecolor='white', 
                edgecolor='none', 
                alpha=0.8
            )
        )

    # Título según el tipo de autómata
    title = "Autómata Finito No Determinista" if is_nfa else "Autómata Finito Determinista"
    ax.set_title(title, fontsize=14, fontweight='bold', color='#4a90e2', pad=20)
    
    ax.axis("off")
    return fig