import sys
import pygame, os

def make_toh(n, moves_printout, moves_list):
    ''' Function inputs: n number of discs, moves_printout (printout of instructions)
    moves_list (list of instructions to move the disc)
    Modifies triangle_list: all the depth 1 (bottom) triangles are added 
    to this list (using recursion relative to the input triangle)
    '''
    