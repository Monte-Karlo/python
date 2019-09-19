import random

autoplay = 1
count_game = 10000
key_text = 0
loadgame = 0
q_learn = 0.1
rand_chance = 5

score = {"ai":0, "player":0}
count = 0
steps = {}
game = []
steps = {}
game_step_ai = []
game_step_pl = []
#---------------------------------------------------------------------------
def view_field():
    print(f'{field[1]}║{field[2]}║{field[3]}\n═╬═╬═')
    print(f'{field[4]}║{field[5]}║{field[6]}\n═╬═╬═')
    print(f'{field[7]}║{field[8]}║{field[9]}')
# ---------------------------------------------------------------------------
def ai_step():
    mb = mb_steps('O')
    buf_steps = {}
    for i in range(0,len(mb)):
        txt = f'{str_game()}{mb[i]}'
        if steps.get(txt) == None:
            steps[txt] = 1
        buf_steps[txt] = steps[txt]
    #
    max_step = max(buf_steps, key = buf_steps.get)
    if random.randint(1,100) > rand_chance:
        step = int(max_step[-2])
    else:
        while True:
            step = random.randint(1,9)
            if field[step] != "X" and field[step] != "O":
                break
    return step
# ---------------------------------------------------------------------------
def player_step(key = 0):
    mb = mb_steps('X')
    buf_steps = {}
    for i in range(0, len(mb)):
        txt = f'{str_game()}{mb[i]}'
        if steps.get(txt) == None:
            steps[txt] = 1
        buf_steps[txt] = steps[txt]
        # while True:
    max_step = max(buf_steps, key=buf_steps.get)
    if key == 0:
        step = int(input('Выберите поле: '))
    else:
        step = int(max_step[-2])
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
def mb_steps(let):
    mb = []
    for i in range(1,10):
        if field[i] != "X" and field[i] != "O":
            mb.append(f'{i}{let}')
    return mb
#---------------------------------------------------------------------------

if loadgame == 0:
    steps = {}
j = 0
while True:
    j += 1
    if j == count_game:
        autoplay = 0
        key_text = 1
    count += 1
    if key_text:
        print(f'Game # {count}')
    field = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    #view_field()
    game = []
    game_step_pl = []
    game_step_ai = []
    i = 0
    player = random.randint(0, 1)
    while i < 9:
        i += 1
        if player == 0:
            step = ai_step()
            field[step] = 'O'
            if key_text:
                print(f'AI сходил')
            game.append(f'{step}O')
            game_step_ai.append(str_game())
            player = 1
        else:
            step = player_step(autoplay)
            field[step] = 'X'
            game.append(f'{step}X')
            game_step_pl.append(str_game())
            player = 0
        if key_text:
            view_field()
            print('-=-=-=-=-=-')
        if check_win() == 1:
            if key_text:
                print('Поздравляем вас с победой!')
            score["player"] += 1
            for i in range(0, len(game_step_ai)):
                steps[game_step_ai[i]] -= q_learn
            for i in range(0, len(game_step_pl)):
                steps[game_step_pl[i]] += q_learn
            break
        elif check_win() == 0:
            if key_text:
                print('Победил AI!')
            score["ai"] += 1
            for i in range(0,len(game_step_ai)):
                steps[game_step_ai[i]] += q_learn
            for i in range(0, len(game_step_pl)):
                steps[game_step_pl[i]] -= q_learn
            break
    if i == 9 and check_win() == -1:
        print('Ничья!')
    #print(steps)
    #print(game_step)
    print(f'Счет   Игрок {score["player"]}:{score["ai"]} AI')
    if key_text:
        if input('Нажмите ENTER') == 'y':
            break
