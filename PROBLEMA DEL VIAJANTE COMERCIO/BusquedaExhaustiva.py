import networkx as nx
import matplotlib.pyplot as plt

def shortest_path(graph, path):
    length = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
    return length

# Crear el grafo no dirigido
G = nx.Graph()

# Agregar los países como nodos
countries = [
    'Perú', 'Ecuador', 'Colombia', 'Bolivia', 'Chile', 'Argentina', 'Brasil', 'Uruguay', 'Venezuela',
    'Paraguay', 'Alemania', 'Francia', 'Reino Unido', 'Italia', 'España', 'Portugal', 'Países Bajos',
    'Bélgica', 'Suiza', 'Suecia'
]
G.add_nodes_from(countries)

# Agregar las conexiones entre los países (aristas)
connections = [
    ('Perú', 'Ecuador', 50),
    ('Ecuador', 'Colombia', 70),
    ('Colombia', 'Bolivia', 60),
    ('Bolivia', 'Chile', 40),
    ('Chile', 'Argentina', 30),
    ('Argentina', 'Brasil', 200),
    ('Brasil', 'Uruguay', 300),
    ('Brasil', 'Venezuela', 250),
    ('Uruguay', 'Paraguay', 180),
    ('Paraguay', 'Alemania', 400),
    ('Alemania', 'Francia', 300),
    ('Francia', 'Reino Unido', 200),
    ('Reino Unido', 'Italia', 250),
    ('Italia', 'España', 180),
    ('España', 'Portugal', 100),
    ('Portugal', 'Países Bajos', 170),
    ('Países Bajos', 'Bélgica', 90),
    ('Bélgica', 'Suiza', 120),
    ('Suiza', 'Suecia', 300),
    ('Perú', 'Bolivia', 90),
    ('Ecuador', 'Chile', 110),
    ('Colombia', 'Argentina', 150),
    ('Bolivia', 'Brasil', 180),
    ('Chile', 'Uruguay', 250),
    ('Argentina', 'Venezuela', 210),
    ('Brasil', 'Paraguay', 140),
    ('Uruguay', 'Alemania', 320),
    ('Paraguay', 'Francia', 260),
    ('Alemania', 'Italia', 290),
    ('Francia', 'España', 230),
    ('Italia', 'Portugal', 270),
    ('España', 'Países Bajos', 150),
    ('Portugal', 'Bélgica', 190),
    ('Países Bajos', 'Suiza', 220),
    ('Bélgica', 'Suecia', 280),
    ('Suiza', 'Reino Unido', 260),
    ('Suecia', 'Venezuela', 280)
]
G.add_weighted_edges_from(connections)

# Definir las posiciones de los nodos manualmente
pos = {
    'Perú': (1, 3),
    'Ecuador': (1, 1),
    'Colombia': (3, 3),
    'Bolivia': (2, 4),
    'Chile': (3, 5),
    'Argentina': (6, 4),
    'Brasil': (4, 2),
    'Uruguay': (6, 1),
    'Venezuela': (3, 2),
    'Paraguay': (5, 3),
    'Alemania': (9, 5),
    'Francia': (10, 3),
    'Reino Unido': (10, 5),
    'Italia': (8, 4),
    'España': (7, 2),
    'Portugal': (6, 3.3),
    'Países Bajos': (9, 3.3),
    'Bélgica': (8, 2),
    'Suiza': (9, 1),
    'Suecia': (11, 1)
}

source_node = 'Ecuador'
target_node = 'Suecia'

# Obtener todos los caminos posibles
all_paths = nx.all_simple_paths(G, source_node, target_node)

# Encontrar el camino mínimo que pase por todos los vértices
min_cost = float('inf')
min_path = None
for path in all_paths:
    if set(countries).issubset(path):
        path_cost = shortest_path(G, path)
        if path_cost < min_cost:
            min_cost = path_cost
            min_path = path

# Encontrar el camino mínimo sin restricción de pasar por todos los vértices
#min_cost = float('inf')
#min_path = None
#for path in all_paths:
#    path_cost = shortest_path(G, path)
#    if path_cost < min_cost:
#        min_cost = path_cost
#        min_path = path


# Visualizar el grafo con los caminos
plt.figure(figsize=(10, 6))

# Agregar el título
plt.title("Búsqueda Exhaustiva - Camino Mínimo")

# Dibujar el grafo
nx.draw_networkx(G, pos, with_labels=True, node_color='lightblue')

# Dibujar el camino mínimo con un color rojo
min_edges = [(min_path[i], min_path[i+1]) for i in range(len(min_path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=min_edges, edge_color='red', width=2)

# Dibujar los nodos de inicio y fin con colores especiales
node_colors = ['green' if node == source_node or node == target_node else 'lightblue' for node in G.nodes]
nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

# Dibujar las etiquetas de los precios de las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='black')

# Mostrar el costo mínimo
plt.text(0.1, -0.1, f"Costo mínimo: {min_cost}", transform=plt.gca().transAxes)

plt.show()
