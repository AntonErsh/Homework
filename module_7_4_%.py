team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_team2 = 42
time_team2 = 18015.2
time_team1 = team1_time = 1552.5
score_team1 = 40
task_total = score_team1 + score_team2
time_avg = (time_team2 + time_team1) / task_total


def solve_challenge() -> str:

    """
    Данная функция определяет исход битвы комманд team1 и team2
    """

    if score_team1 > score_team2:
        return f'Победа команды {team1}'
    if score_team1 < score_team2:
        return f'Победа команды {team2}'
    if score_team1 == score_team2 or time_team1 < time_team2:
        return 'Победа команды {}'.format(team1)
    if score_team1 == score_team2 or time_team1 > time_team2:
        return 'Победа команды {}'.format(team2)
    if score_team1 == score_team2 or time_team1 == time_team2:
        return 'Победила дружба'


print('В команде %s участников: %s! ' % (team1, team1_num))
print('Итого сегодня в командах участников: %(1)s, %(2)s! ' % {'1': team1_num, '2': team2_num})
print("Команда {} решила задач: {score} !".format(team2, score=score_team2))
print("{} решили задачи за {time} !".format(team2, time=time_team2))
print(f'Команды решили {score_team1} и {score_team2} задач. ')
print(f'Сегодня было решено {task_total} задач, в среднем по {round(time_avg, 1)} секунды на задачу!')
print(f'Результат битвы: {solve_challenge()}')
