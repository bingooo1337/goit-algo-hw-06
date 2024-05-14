import networkx as nx
import matplotlib.pyplot as plt

metro_graph = nx.Graph()

red_line_stations = [
    "Академмістечко", "Житомирська", "Святошин", "Нивки",
    "Берестейська", "Шулявська", "Політехнічний інститут",
    "Вокзальна", "Університет", "Театральна", "Хрещатик",
    "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна",
    "Дарниця", "Чернігівська", "Лісова"
]

green_line_stations = [
    "Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота",
    "Палац спорту", "Кловська", "Печерська", "Звіринецька",
    "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська",
    "Вирлиця", "Бориспільська", "Червоний хутір"
]

blue_line_stations = [
    "Героїв Дніпра", "Мінська", "Оболонь", "Почайна",
    "Тараса Шевченка", "Контрактова площа", "Поштова площа",
    "Майдан Незалежності", "Площа Українських Героїв",
    "Олімпійська", "Палац «Україна»", "Либідська",
    "Деміївська", "Голосіївська", "Васильківська",
    "Виставковий центр", "Іподром", "Теремки"
]

metro_graph.add_nodes_from(red_line_stations)
metro_graph.add_nodes_from(green_line_stations)
metro_graph.add_nodes_from(blue_line_stations)


def add_edges_for_line(line_stations):
    for i in range(len(line_stations) - 1):
        metro_graph.add_edge(line_stations[i], line_stations[i+1])


add_edges_for_line(red_line_stations)
add_edges_for_line(green_line_stations)
add_edges_for_line(blue_line_stations)

# transfers between lines
metro_graph.add_edge("Хрещатик", "Майдан Незалежності")
metro_graph.add_edge("Театральна", "Золоті ворота")
metro_graph.add_edge("Площа Українських Героїв", "Палац спорту")

print("Кількість вершин:", metro_graph.number_of_nodes())
print("Кількість ребер:", metro_graph.number_of_edges())
print("Ступені вершин:", metro_graph.degree())

for station in metro_graph.nodes():
    if station in red_line_stations:
        metro_graph.nodes[station]['color'] = 'red'
    elif station in green_line_stations:
        metro_graph.nodes[station]['color'] = 'green'
    elif station in blue_line_stations:
        metro_graph.nodes[station]['color'] = 'blue'

for edge in metro_graph.edges():
    if edge[0] in red_line_stations and edge[1] in red_line_stations:
        metro_graph.edges[edge]['color'] = 'red'
    elif edge[0] in green_line_stations and edge[1] in green_line_stations:
        metro_graph.edges[edge]['color'] = 'green'
    elif edge[0] in blue_line_stations and edge[1] in blue_line_stations:
        metro_graph.edges[edge]['color'] = 'blue'
    else:
        metro_graph.edges[edge]['color'] = 'purple'

pos = nx.spring_layout(metro_graph, seed=55)

red_nodes = [
    node for node in metro_graph.nodes()
    if metro_graph.nodes[node]['color'] == 'red'
]
green_nodes = [
    node for node in metro_graph.nodes()
    if metro_graph.nodes[node]['color'] == 'green'
]
blue_nodes = [
    node for node in metro_graph.nodes()
    if metro_graph.nodes[node]['color'] == 'blue'
]

nx.draw_networkx_nodes(metro_graph, pos, nodelist=red_nodes,
                       node_color='r', label="Red Line")
nx.draw_networkx_nodes(metro_graph, pos, nodelist=green_nodes,
                       node_color='g', label="Green Line")
nx.draw_networkx_nodes(metro_graph, pos, nodelist=blue_nodes,
                       node_color='b', label="Blue Line")

for color in ['red', 'green', 'blue', 'purple']:
    edges = [
        edge for edge in metro_graph.edges()
        if metro_graph.edges[edge]['color'] == color
    ]
    nx.draw_networkx_edges(metro_graph, pos, edgelist=edges, edge_color=color)

nx.draw_networkx_labels(metro_graph, pos, font_size=8)
plt.legend()
plt.axis('off')
plt.show()
