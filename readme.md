Обидва алгоритми знайшли шлях від "Борщагівка" до "Мінська", але маршрути, які вони знайшли, відрізняються

### DFS:
кількість ітерацій: **56**  
довжина: **24**  
шлях: ['Борщагівка', 'Київ-Волинський', 'Караваєві Дачі', 'Вокзальна(ел)', 'Вокзальна', 'Університет', 'Театральна', 'Золоті ворота', 'Палац спорту', 'Площа Українських Героїв', 'Майдан Незалежності', 'Хрещатик', 'Арсенальна', 'Дніпро', 'Гідропарк', 'Лівобережна', 'Лівобережна(ел)', 'Микільська Слобідка', 'Воскресенка', 'Райдужний', 'Почайна(ел)', 'Почайна', 'Оболонь', 'Мінська'] 

### BFS:
кількість ітерацій: **81**  
довжина: **10**  
шлях: ['Борщагівка', 'Святошин(ел)', 'Берестейська(ел)', 'Сирець(ел)', 'Пріорка', 'Куренівська', 'Почайна(ел)', 'Почайна', 'Оболонь', 'Мінська']

**DFS** знадобилось **менше ітерацій** для знаходження шляху, проте **шлях не найкоротший**.  
**BFS** знадобилось **більше ітерацій** для знаходження шляху, проте **шлях найкоротший**.

Різниця полягає у порядку, яким відвідуються вершини графа. DFS вибирає один з можливих шляхів та просувається по ньому, поки не досягне кінцевої вершини. DFS відвідав кілька станцій Київського метрополітену, а потім пересікся з міською електричкою і знайшов кінцеву вершину "Мінська". Знайдений шлях не є найкоротшим, але DFS може бути швидшим в деяких випадках, де шлях знаходиться ближче до початкової вершини і займає менше ітерацій.

BFS, натомість, спочатку відвідує всі сусідні вершини, що знаходяться на одному рівні від стартової вершини, перш ніж рухатися на більш глибокий рівень. У нашому випадку, BFS рухається від "Борщагівка" до "Мінська", перевіряючи всі можливі шляхи. Він спочатку переходить до "Святошин(ел)", потім до "Берестейська(ел)", далі до "Сирець(ел)", "Пріорка", "Куренівська" і так далі, поки не досягне "Мінська". Такий процес дозволяє знайти найкоротший шлях. BFS (пошук в ширину) завжди знаходить найкоротший шлях в неорієнтованому графі з невагомими ребрами.

В нашому випадку DFS знайшов шлях, що потребував менше ітерацій (56) порівняно з BFS (81). Однак, DFS може зайти глибше у граф, перш ніж знайти рішення, що може призвести до більшого часу виконання у випадку дуже глибоких графів. 