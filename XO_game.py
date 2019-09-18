import random

autoplay = 1
loadgame = 0
q_learn = 0.1

score = {"ai":0, "player":0}
count = 0
steps = {}
game = []
steps = {}
game_step = []
#---------------------------------------------------------------------------
def view_field():
    print(f'{field[1]}║{field[2]}║{field[3]}\n═╬═╬═')
    print(f'{field[4]}║{field[5]}║{field[6]}\n═╬═╬═')
    print(f'{field[7]}║{field[8]}║{field[9]}')
# ---------------------------------------------------------------------------
def ai_step():
    mb = mb_steps()
    for i in range(0,len(mb)):
        txt = f'{str_game()}{mb[i]}'
        if steps.get(txt) == None:
            steps[txt] = 1
    while True:
        step = random.randint(1,9)
        if field[step] != "X" and field[step] != "O":
            break
    return step
# ---------------------------------------------------------------------------
def player_step(key = 0):
    while True:
        if key == 0:
            step = int(input('Выберите поле: '))
        else:
            step = random.randint(1,9)
        if field[step] != "X" and field[step] != "O":
            break
    return step
# ---------------------------------------------------------------------------
def check_win():
    if field[1] == field[2] and field[3] == field[2]:
        if field[1] == 'X':
            return 1
        else:
            return 0
    if field[1] == field[4] and field[4] == field[7]:
        if field[1] == 'X':
            return 1
        else:
            return 0
    if field[1] == field[5] and field[5] == field[9]:
        if field[1] == 'X':
            return 1
        else:
            return 0
    if field[7] == field[8] and field[8] == field[9]:
        if field[7] == 'X':
            return 1
        else:
            return 0
    if field[7] == field[5] and field[5] == field[3]:
        if field[7] == 'X':
            return 1
        else:
            return 0
    if field[9] == field[6] and field[6] == field[3]:
        if field[9] == 'X':
            return 1
        else:
            return 0
    if field[5] == field[4] and field[4] == field[6]:
        if field[5] == 'X':
            return 1
        else:
            return 0
    if field[5] == field[8] and field[8] == field[2]:
        if field[5] == 'X':
            return 1
        else:
            return 0
    return -1
#---------------------------------------------------------------------------
def str_game():
    txt = ""
    for i in range(0,len(game)):
        txt += game[i]
    return txt
#---------------------------------------------------------------------------
def mb_steps():
    mb = []
    for i in range(1,10):
        if field[i] != "X" and field[i] != "O":
            mb.append(f'{i}O')
    return mb
#---------------------------------------------------------------------------

if loadgame == 0:
    steps = {}
while True:
    count += 1
    print(f'Game # {count}')
    field = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    view_field()
    game = []
    game_step = []
    i = 0
    player = random.randint(0, 1)
    while i < 9:
        i += 1
        if player == 0:
            step = ai_step()
            field[step] = 'O'
            print(f'AI сходил')
            game.append(f'{step}O')
            game_step.append(str_game())
            player = 1
        else:
            step = player_step(autoplay)
            field[step] = 'X'
            game.append(f'{step}X')
            player = 0
        view_field()
        if check_win() == 1:
            print('Поздравляем вас с победой!')
            score["player"] += 1
            for i in range(0, len(game_step)):
                steps[game_step[i]] -= q_learn
            break
        elif check_win() == 0:
            print('Победил AI!')
            score["ai"] += 1
            for i in range(0,len(game_step)):
                steps[game_step[i]] += q_learn
            break

    if i == 9 and check_win() == -1:
        print('Ничья!')
    #print(steps)
    #print(game_step)
    print(f'Счет   Игрок {score["player"]}:{score["ai"]} AI')
    if input('Нажмите ENTER') == 'y':
        break
