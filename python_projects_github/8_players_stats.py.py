players = [
    {'name': 'Cristiano Ronaldo', 'position': 'Forward',
        'jersey': 10, 'goals': 25, 'assists': 18},
    {'name': 'Kevin De Bruyne', 'position': 'Midfielder',
        'jersey': 17, 'goals': 10, 'assists': 22},
    {'name': 'Virgil van Dijk', 'position': 'Defender',
        'jersey': 4, 'goals': 3, 'assists': 2},
    {'name': 'Thibaut Courtois', 'position': 'Goalkeeper',
        'jersey': 1, 'goals': 0, 'assists': 0}
]

positions = {player['position'] for player in players}
print(positions)

for player in players:
    if player['name'] == 'Cristiano Ronaldo':
        player['goals'] = 69
        player['assists'] = 30

print(players)

statistic_goal = []
for player in players:
    statistic_goal.append(player['goals'])

statistic_assists = []
for player in players:
    statistic_assists.append(player['assists'])

print(statistic_goal + statistic_assists)

avarage_goal = sum(statistic_goal) / len(statistic_goal)
avarage_assists = sum(statistic_assists) / len(statistic_assists)

print(avarage_goal)
print(avarage_assists)


def add_player():
    name = input("Введіть ім'я гравця: ")
    position = input("Введіть позицію гравця: ")
    jersey = int(input("Введіть номер на футболці: "))
    goals = int(input("Введіть кількість голів: "))
    assists = int(input("Введіть кількість асистів: "))

    player = {
        'name': name,
        'position': position,
        'jersey': jersey,
        'goals': goals,
        'assists': assists
    }
    players.append(player)


add_player()
print(players)
