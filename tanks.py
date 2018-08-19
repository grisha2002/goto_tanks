import random
def make_choice(x,y,field):
   
    width = len(field) 
    height = len(field[0])
    actions = ["go_up","go_down","go_left","go_right","fire_up","fire_down","fire_left","fire_right"]
      
    for i in range(y-1,-1,-1):
        if field[x][i] ==-1:
            break
        if field[x][i] not in[-1,0,1]:
            return "fire_down"
            break
    for i in range(y+1, height):
        if field[x][i] ==-1:
            break
        if field[x][i] not in[-1,0,1]:
            return "fire_up"
            break
    for i in range(x-1,-1,-1):
        if field[i][y] ==-1:
            break
        if field[i][y] not in[-1,0,1]:
            return "fire_left"
            break
    for i in range(x+1, width):
        if field[i][y] ==-1:
            break
        if field[i][y] not in[-1,0,1]:
            return "fire_right"
            break
    left_coin=1000
    right_coin=1000
    up_coin=1000
    down_coin=1000
    
    for i in range(y-1,-1,-1):
        if field[x][i] ==-1:
            break
        if field[x][i]==1:
            up_coin=abs(y-i)
            break
    for i in range(y+1, height):
        if field[x][i] ==-1:
            break
        if field[x][i]==1:
            down_coin=abs(y-i)
            break
    for i in range(x-1,-1,-1):
        if field[i][y] ==-1:
            break
        if field[i][y]==1:
            left_coin=abs(x-i)
            break
    for i in range(x+1, width):
        if field[i][y] ==1:
            break
        if field[i][y]==1:
            right_coin=abs(x-i)
            break
    if up_coin == min([left_coin,right_coin,up_coin,down_coin,999]):
        return "go_up"
    if down_coin == min([left_coin,right_coin,up_coin,down_coin,999]):
        return "go_down"
    if left_coin == min([left_coin,right_coin,up_coin,down_coin,999]):
        return "go_left"
    if right_coin== min([left_coin,right_coin,up_coin,down_coin,999]):
        return "go_right"
   
    return random.choice(actions)





