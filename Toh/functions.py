
# Creates an empty list for appending the list of moves as a solution to the Towers of Hanoi problem
moves_list = []


def moves(n, left):

    '''This function writes the instructions for the towers of Hanoi problem. The recursive
     function moves() writes the moves needed to move n discs to the left (if left is True) or to the
     right (if left is False).'''
    
    # n is the number of discs
    # left is the direction to move the pile indicated by a boolean value

    if n == 0: 
        return
    
    # Using recursion to solve the Towers of Hanoi

    moves(n-1, not left) 

    if left:
        moves_list.append([str(n), 'left'])

    else:
        moves_list.append([str(n), 'right'])

    moves(n-1, not left)
    


    



# def moves_printout():

#     ''' This function displays a printout of the sequence of 
#     configurations of a solution to the problem for n discs
#     '''

#     # Checks for input errors

#     while True:
#         try:

#             n = int(input("Enter the number of discs: "))

#         except ValueError:

#             print("You must enter a number")
#             continue
        
#         else:
            
#             break

#     while True:

#         left = input("Enter left or right: ")

#         if left.lower() == "left":
#             left = True
#             break

#         elif left.lower() == 'right':
#             left = False
#             break

#     moves(n, left)

#     # Printout of a sequence of moves to solve the Towers of Hanoi

#     for i in range(len(moves_list)):
#         print(moves_list[i])

def moves_printout(n):

    ''' This function displays a printout of the sequence of 
    configurations of a solution to the problem for n discs
    '''

    left = True


    moves(n, left)

    # Printout of a sequence of moves to solve the Towers of Hanoi

    for i in range(len(moves_list)):
        print(moves_list[i])

