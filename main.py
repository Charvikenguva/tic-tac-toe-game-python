
instructions = """
This will be your tic tac toe game board!!

1  |2  |3
---|---|---
4  |5  |6
---|---|---
7  |8  |9

INSTRUCTIONS:
1.Insert the spot number(1-9) to put your sign on the board
2.You must fill all 9 spots to get the result of the game
3.player 1 will start the game followed by player 2

"""

sign_dictionary=[]
for i in range(9):
    sign_dictionary.append(" ")


def print_board(sign_dictionary):
    board=f"""

    {sign_dictionary[0]}  |{sign_dictionary[1]}  |{sign_dictionary[2]}
    ---|---|---
    {sign_dictionary[3]}  |{sign_dictionary[4]}  |{sign_dictionary[5]}
    ---|---|---
    {sign_dictionary[6]}  |{sign_dictionary[7]}  |{sign_dictionary[8]}
     
    """
    print(board)


index_list=[]
def take_input(player_name):
    while True:
        x=int(input(f"{player_name}:"))
        x=x-1
        if 0<= x <10:
            if x in index_list:
                print("This spot is blocked.")
                continue
            index_list.append(x)
            return x
        print("please enter number between 1-9")


def result_calculate(sign_dictionary,player_one,player_two):
    if(
        sign_dictionary[0]==sign_dictionary[1]==sign_dictionary[2]=='x' or
        sign_dictionary[3]==sign_dictionary[4]==sign_dictionary[5]=='x' or
        sign_dictionary[6]==sign_dictionary[7]==sign_dictionary[8]=='x' or
        sign_dictionary[0]==sign_dictionary[3]==sign_dictionary[6]=='x' or
        sign_dictionary[1]==sign_dictionary[4]==sign_dictionary[7]=='x' or
        sign_dictionary[2]==sign_dictionary[5]==sign_dictionary[8]=='x' or
        sign_dictionary[0]==sign_dictionary[4]==sign_dictionary[8]=='x' or
        sign_dictionary[2]==sign_dictionary[4]==sign_dictionary[6]=='x' 
    ):
        print(f'Congratulations {player_one}. You won the game!!')
        quit("Thankyou both for playing the game. Have a good day.")

    elif(
        sign_dictionary[0]==sign_dictionary[1]==sign_dictionary[2]=='0' or
        sign_dictionary[3]==sign_dictionary[4]==sign_dictionary[5]=='0' or
        sign_dictionary[6]==sign_dictionary[7]==sign_dictionary[8]=='0' or
        sign_dictionary[0]==sign_dictionary[3]==sign_dictionary[6]=='0' or
        sign_dictionary[1]==sign_dictionary[4]==sign_dictionary[7]=='0' or
        sign_dictionary[2]==sign_dictionary[5]==sign_dictionary[8]=='0' or
        sign_dictionary[0]==sign_dictionary[4]==sign_dictionary[8]=='0' or
        sign_dictionary[2]==sign_dictionary[4]==sign_dictionary[6]=='0' 
    ):
         print(f'Congratulations {player_two}. You WON the game!!')
         quit("Thankyou both for playing the game. Have a good day.")
        
    else:
        return

        

def main():
    print("welcome to the tic tac toe game!!")
    player_one=input("Enter player_one name: ")
    player_two=input("Enter player_two name: ")
    print(f"ThankYou for joining the game {player_one} and {player_two}.Lets start the game and have some fun.")

    print(instructions)
    print(f"{player_one}, your sign will be - x")
    print(f"{player_two}, your sign will be - 0")

    input("Enter any key to start the game:")

    print_board(sign_dictionary)

    for i in range(0,9):
        if i%2==0:
            index=take_input(player_one)
            sign_dictionary[index]='x'
        else:
            index=take_input(player_two)
            sign_dictionary[index]='0'


        print_board(sign_dictionary)
        result_calculate(sign_dictionary,player_one,player_two)
    print("This is a tie!! Nobody won the game.. Play again")


main()