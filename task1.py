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

suburban_stations = [
    "Дарниця(ел)", "Русанівка", "Лівобережна(ел)", "Микільська Слобідка",
    "Воскресенка", "Райдужний", "Почайна(ел)", "Куренівська", "Пріорка",
    "Сирець(ел)", "Берестейська(ел)", "Святошин(ел)", "Борщагівка",
    "Київ-Волинський", "Караваєві Дачі", "Вокзальна(ел)", "Протасів Яр",
    "Київ-Деміївський", "Видубичі(ел)", "Березняки", "Дарниця(ел)"
]

metro_graph.add_nodes_from(red_line_stations)
metro_graph.add_nodes_from(green_line_stations)
metro_graph.add_nodes_from(blue_line_stations)
metro_graph.add_nodes_from(suburban_stations)


def add_edges_for_line(line_stations):
    for i in range(len(line_stations) - 1):
        metro_graph.add_edge(line_stations[i], line_stations[i+1])


add_edges_for_line(red_line_stations)
add_edges_for_line(green_line_stations)
add_edges_for_line(blue_line_stations)
add_edges_for_line(suburban_stations)

# transfers between lines
metro_graph.add_edge("Хрещатик", "Майдан Незалежності")
metro_graph.add_edge("Театральна", "Золоті ворота")
metro_graph.add_edge("Площа Українських Героїв", "Палац спорту")

metro_graph.add_edge("Лівобережна", "Лівобережна(ел)")
metro_graph.add_edge("Почайна", "Почайна(ел)")
metro_graph.add_edge("Сирець", "Сирець(ел)")
metro_graph.add_edge("Берестейська", "Берестейська(ел)")
metro_graph.add_edge("Святошин", "Святошин(ел)")
metro_graph.add_edge("Вокзальна", "Вокзальна(ел)")
metro_graph.add_edge("Видубичі", "Видубичі(ел)")


def main():
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
        elif station in suburban_stations:
            metro_graph.nodes[station]['color'] = 'grey'

    for edge in metro_graph.edges():
        if edge[0] in red_line_stations and edge[1] in red_line_stations:
            metro_graph.edges[edge]['color'] = 'red'
        elif edge[0] in green_line_stations and edge[1] in green_line_stations:
            metro_graph.edges[edge]['color'] = 'green'
        elif edge[0] in blue_line_stations and edge[1] in blue_line_stations:
            metro_graph.edges[edge]['color'] = 'blue'
        elif edge[0] in suburban_stations and edge[1] in suburban_stations:
            metro_graph.edges[edge]['color'] = 'grey'
        else:
            metro_graph.edges[edge]['color'] = 'purple'

    pos = nx.spring_layout(metro_graph, seed=34)

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
    suburban_nodes = [
        node for node in metro_graph.nodes()
        if metro_graph.nodes[node]['color'] == 'grey'
    ]

    nx.draw_networkx_nodes(metro_graph, pos, nodelist=red_nodes,
                           node_color='r', label="Red Line")
    nx.draw_networkx_nodes(metro_graph, pos, nodelist=green_nodes,
                           node_color='g', label="Green Line")
    nx.draw_networkx_nodes(metro_graph, pos, nodelist=blue_nodes,
                           node_color='b', label="Blue Line")
    nx.draw_networkx_nodes(metro_graph, pos, nodelist=suburban_nodes,
                           node_color='#808080', label="Suburban")

    for color in ['red', 'green', 'blue', 'purple', 'grey']:
        edges = [
            edge for edge in metro_graph.edges()
            if metro_graph.edges[edge]['color'] == color
        ]
        nx.draw_networkx_edges(
            metro_graph, pos, edgelist=edges, edge_color=color)

    nx.draw_networkx_labels(metro_graph, pos, font_size=8)
    plt.legend()
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
