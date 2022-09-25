import random


def input_game_mode():
    while True:
        try:
            game_mode = int(
                input('enter 1 if u wanna play with bot and 2 if u want to play woth person: '))
            if 1 <= game_mode <= 2:
                break
            else:
                print('You write wrong int, try again')
        except ValueError:
            print('It doesnt number, try again')
    return game_mode


def input_limit():
    while True:
        try:
            limit = int(input('Enter max of candys how u can put in 1 round'))
            if limit > 0:
                break
            else:
                print('Int have to be more than 0')
        except ValueError:
            print('It doesnt number, try again')
    return limit


def input_total(limit):
    while True:
        try:
            total = int(input('How many candys at all: '))
            if total > limit:
                break
            else:
                print('Less candys for game, try again')
        except ValueError:
            print('It doesnt number, try again')
    return total


def draw():
    queue = random.randint(1, 2)
    if queue == 1:
        print('first player start')
    else:
        print('Second player start')
    return queue


def step(total, limit, player):
    if player == 1:
        while True:
            try:
                m = int(
                    input(f'first player cant take more than {limit} candys: '))
                if 0 < m < limit+1:
                    break
                else:
                    print(
                        f'number {m} not in that diaposon (1-{limit}).\n Try again')
            except ValueError:
                print('It doesnt number, try again')

    else:
        while True:
            try:
                m = int(
                    input(f'Second player cant take more than {limit} candys: '))
                if 0 < m < limit+1:
                    break
                else:
                    print(
                        f'number {m} not in that diaposon (1-{limit}).\n Try again')
            except ValueError:
                print('It doesnt number, try again')
    total = total - m
    print(f'Candys: {total}')
    return total


def step_bot(total, limit):
    m = (total - 1) % (limit + 1)
    total = total - m
    print(f'Bot take {m} candys')
    print(f'All candys: {total}')
    return total


game_mode = input_game_mode()
limit = input_limit()
total = input_total(limit)

if game_mode == 1:
    player = 1
    if total > limit:
        while total > limit:
            if player == 1:
                total = step(total, limit, player)
                player = 2
            else:
                total = step_bot(total, limit)
                player = 1
    if total <= limit:
        while total > 0:
            limit = total
            if player == 1:
                total = step(total, limit, player)
                player = 2
            else:
                total = step_bot(total, limit)
                player = 1
    if player == 1:
        print('First player win')
    else:
        print('bot win')
else:
    player = draw()
    if total > limit:
        while total > limit:
            total = step(total, limit, player)
            if player == 1:
                player = 2
            else:
                player == 1
    if player == 1:
        print('First player win')
    else:
        print('second player win')
