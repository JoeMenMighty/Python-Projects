def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

def jump_wall():
    count = 0
    while wall_in_front():
        turn_left()
        move()
        turn_right()
        count += 1
    move()
    turn_right()
    for num in range(count):
        move()
    turn_left()
    

while not at_goal():
    if not front_is_clear():
        jump_wall()
    else:
        move()