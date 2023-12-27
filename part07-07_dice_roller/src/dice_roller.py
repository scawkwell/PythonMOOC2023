# Write your solution here
def roll(die : str):
    from random import choice
    dice_names = "ABC"
    dice_values = [ [3, 3, 3, 3, 3, 6],
                    [2, 2, 2, 5, 5, 5],
                    [1, 4, 4, 4, 4, 4] ]

    return choice(dice_values[dice_names.find(die)])

def play(die_1 : str, die_2 : str, times : int):
    count = 0
    win, loss, draw = 0, 0, 0

    while count < times:
        die_1_value = roll(die_1)
        die_2_value = roll(die_2)
        if die_1_value == die_2_value:
            draw += 1
        elif die_1_value > die_2_value:
            win += 1
        else: 
            loss +=1
        count += 1
    return win, loss, draw

if __name__ == "__main__":
    print(play("B", "B", 100))