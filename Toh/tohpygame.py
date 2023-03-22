import sys
import learningpygame, os




def make_toh(n, moves_printout, moves_list):
    ''' Function inputs: n number of discs, moves_printout (printout of instructions)
    moves_list (list of instructions to move the disc)
    Modifies triangle_list: all the depth 1 (bottom) triangles are added 
    to this list (using recursion relative to the input triangle)
    '''
    (x0,y0) = moves_printout[0]
    (x1,y1) = moves_printout[1]
    (x2,y2) = moves_printout[2]

    if n == 1:
        moves_list.append(moves_printout)
        return None
