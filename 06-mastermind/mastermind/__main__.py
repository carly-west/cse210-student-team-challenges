# from game.director import Director

# director = Director()
# director.start_game()

spot = -1
rand_num = ['1', '2', '3', '4']
guess = ['4', '2', '3', '8']
rand_to_print = ['*', '*', '*', '*']
# Compare guess to list
for i in guess:
    spot += 1
    if i in rand_num:
        rand_to_print[spot] = "O"
    # for x in rand_num:
    #     if i = x


print(rand_to_print)
