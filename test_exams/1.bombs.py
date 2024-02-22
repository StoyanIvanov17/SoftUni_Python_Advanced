from collections import deque

bomb_effects = deque(map(int, input().split(', ')))
bomb_casings = deque(map(int, input().split(', ')))

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

success = False


def bombings():
    if the_sum == 40:
        bomb_effects.popleft()
        bomb_casings.pop()
    elif the_sum == 60:
        bomb_effects.popleft()
        bomb_casings.pop()
    elif the_sum == 120:
        bomb_effects.popleft()
        bomb_casings.pop()


while bomb_effects and bomb_casings:
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        success = True
        print('Bene! You have successfully filled the bomb pouch!')
        break

    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]
    the_sum = current_effect + current_casing

    if the_sum == 40:
        datura_bombs += 1
        bombings()
    elif the_sum == 60:
        cherry_bombs += 1
        bombings()
    elif the_sum == 120:
        smoke_decoy_bombs += 1
        bombings()
    else:
        bomb_casings[-1] -= 5


if not success:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
else:
    print('Bomb Effects: empty')

if bomb_casings:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
else:
    print('Bomb Casings: empty')


print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")




