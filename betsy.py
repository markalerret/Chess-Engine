# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 15:41:12 2020

@author: malerret
"""

import sys

def generate_board(board):
    pos = 'x'*21 + board[:8] + 'xx' + board[8:16] + 'xx' + board[16:24] + 'xx' + board[24:32] + 'xx' + board[32:40] + 'xx' + board[40:48] + 'xx' + board[48:56] + 'xx' + board[56:64] + 'x'*21
    
    return pos

def visualize_board(board):
    vis_board = [board[110:120], board[100:110], board[90:100], board[80:90], board[70:80], board[60:70], board[50:60], board[40:50], board[30:40], board[20:30], board[10:20], board[:10]]
    for element in vis_board:
        print(element)
        
def generate_output(board):
    pos = board[21:29] + board[31:39] + board[41:49] + board[51:59] + board[61:69] + board[71:79] + board[81:89] + board[91:99]
     
    return pos

#return all legal moves for white pawns
def white_parakeet_moves(current_position):
    parakeets = []
    keet_loc = 0
    parakeet_moves = []
    
    for square in current_position:
        if square =='P':
            parakeets.append(keet_loc)
        keet_loc += 1

    for i in parakeets:
        if current_position[i+10] == '.':
            parakeet_moves.append(['P', i, i+10])
        if 30<i<39:
            if current_position[i+10] == current_position[i+20] == '.':
                parakeet_moves.append(['P', i, i+20])
        if current_position[i+9] in black_pieces:
            parakeet_moves.append(['P', i, i+9])
        if current_position[i+11] in black_pieces:
            parakeet_moves.append(['P', i, i+11])
            
    return parakeet_moves
    
#return all legal moves for white bishops
def white_bluejay_moves(current_position):
    bluejays = []
    jay_loc = 0
    bluejay_moves = []
    
    for square in current_position:
        if square == 'B':
            bluejays.append(jay_loc)
        jay_loc += 1
    
    for i in bluejays:
        n=1
        while n:
            if current_position[i+(9*n)] == '.':
                bluejay_moves.append(['B', i, i+(9*n)])
                n += 1
            elif current_position[i+(9*n)] == 'x':
                break
            elif current_position[i+(9*n)] in white_pieces:
                break
            elif current_position[i+(9*n)] in black_pieces:
                bluejay_moves.append(['B', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(11*n)] == '.':
                bluejay_moves.append(['B', i, i+(11*n)])
                n += 1
            elif current_position[i+(11*n)] == 'x':
                break
            elif current_position[i+(11*n)] in white_pieces:
                break
            elif current_position[i+(11*n)] in black_pieces:
                bluejay_moves.append(['B', i, i+(11*n)])
                break
        n=1
        while n:
            if current_position[i-(9*n)] == '.':
                bluejay_moves.append(['B', i, i-(9*n)])
                n += 1
            elif current_position[i-(9*n)] == 'x':
                break
            elif current_position[i-(9*n)] in white_pieces:
                break
            elif current_position[i-(9*n)] in black_pieces:
                bluejay_moves.append(['B', i, i-(9*n)])
                break
        n=1
        while n:
            if current_position[i-(11*n)] == '.':
                bluejay_moves.append(['B', i, i-(11*n)])
                n += 1
            elif current_position[i-(11*n)] == 'x':
                break
            elif current_position[i-(11*n)] in white_pieces:
                break
            elif current_position[i-(11*n)] in black_pieces:
                bluejay_moves.append(['B', i, i-(11*n)])
                break
        
    return bluejay_moves

#return all legal moves for white knights
def white_nighthawk_moves(current_position):
    nighthawks = []
    hawk_loc = 0
    nighthawk_moves = []
    
    for square in current_position:
        if square == 'N':
            nighthawks.append(hawk_loc)
        hawk_loc += 1
    
    for i in nighthawks:
        if current_position[i+8] in black_pieces or current_position[i+8] == '.':
            nighthawk_moves.append(['N', i, i+8])
        if current_position[i-8] in black_pieces or current_position[i-8] == '.':
            nighthawk_moves.append(['N', i, i-8])
            
        if current_position[i+12] in black_pieces or current_position[i+12] == '.':
            nighthawk_moves.append(['N', i, i+12])
        if current_position[i-12] in black_pieces or current_position[i-12] == '.':
            nighthawk_moves.append(['N', i, i-12])
            
        if current_position[i+19] in black_pieces or current_position[i+19] == '.':
            nighthawk_moves.append(['N', i, i+19])
        if current_position[i-19] in black_pieces or current_position[i-19] == '.':
            nighthawk_moves.append(['N', i, i-19])
        if current_position[i+21] in black_pieces or current_position[i+21] == '.':
            nighthawk_moves.append(['N', i, i+21])
        if current_position[i-21] in black_pieces or current_position[i-21] == '.':
            nighthawk_moves.append(['N', i, i-21])
      
    return nighthawk_moves

#return all legal moves for white rooks
def white_robin_moves(current_position):
    robins = []
    robin_loc = 0
    robin_moves = []
    
    for square in current_position:
        if square == 'R':
            robins.append(robin_loc)
        robin_loc += 1
        
    for i in robins:
        n=1
        while n:
            if current_position[i+(1*n)] == '.':
                robin_moves.append(['R', i, i+(1*n)])
                n += 1
            elif current_position[i+(1*n)] == 'x':
                break
            elif current_position[i+(1*n)] in white_pieces:
                break
            elif current_position[i+(1*n)] in black_pieces:
                robin_moves.append(['R', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(10*n)] == '.':
                robin_moves.append(['R', i, i+(10*n)])
                n += 1
            elif current_position[i+(10*n)] == 'x':
                break
            elif current_position[i+(10*n)] in white_pieces:
                break
            elif current_position[i+(10*n)] in black_pieces:
                robin_moves.append(['R', i, i+(10*n)])
                break
        n=1
        while n:
            if current_position[i-(1*n)] == '.':
                robin_moves.append(['R', i, i-(1*n)])
                n += 1
            elif current_position[i-(1*n)] == 'x':
                break
            elif current_position[i-(1*n)] in white_pieces:
                break
            elif current_position[i-(1*n)] in black_pieces:
                robin_moves.append(['R', i, i-(1*n)])
                break
        n=1
        while n:
            if current_position[i-(10*n)] == '.':
                robin_moves.append(['R', i, i-(10*n)])
                n += 1
            elif current_position[i-(10*n)] == 'x':
                break
            elif current_position[i-(10*n)] in white_pieces:
                break
            elif current_position[i-(10*n)] in black_pieces:
                robin_moves.append(['R', i, i-(10*n)])
                break
    
    return robin_moves

#return all legal moves for white queens
def white_quetzal_moves(current_position):
    quetzals = []
    quetzal_loc = 0
    quetzal_moves = []
    
    for square in current_position:
        if square == 'Q':
            quetzals.append(quetzal_loc)
        quetzal_loc += 1
        
    for i in quetzals:
        n=1
        while n:
            if current_position[i+(9*n)] == '.':
                quetzal_moves.append(['Q', i, i+(9*n)])
                n += 1
            elif current_position[i+(9*n)] == 'x':
                break
            elif current_position[i+(9*n)] in white_pieces:
                break
            elif current_position[i+(9*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(11*n)] == '.':
                quetzal_moves.append(['Q', i, i+(11*n)])
                n += 1
            elif current_position[i+(11*n)] == 'x':
                break
            elif current_position[i+(11*n)] in white_pieces:
                break
            elif current_position[i+(11*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i+(11*n)])
                break
        n=1
        while n:
            if current_position[i-(9*n)] == '.':
                quetzal_moves.append(['Q', i, i-(9*n)])
                n += 1
            elif current_position[i-(9*n)] == 'x':
                break
            elif current_position[i-(9*n)] in white_pieces:
                break
            elif current_position[i-(9*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i-(9*n)])
                break
        n=1
        while n:
            if current_position[i-(11*n)] == '.':
                quetzal_moves.append(['Q', i, i-(11*n)])
                n += 1
            elif current_position[i-(11*n)] == 'x':
                break
            elif current_position[i-(11*n)] in white_pieces:
                break
            elif current_position[i-(11*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i-(11*n)])
                break
            
        n=1
        while n:
            if current_position[i+(1*n)] == '.':
                quetzal_moves.append(['Q', i, i+(1*n)])
                n += 1
            elif current_position[i+(1*n)] == 'x':
                break
            elif current_position[i+(1*n)] in white_pieces:
                break
            elif current_position[i+(1*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(10*n)] == '.':
                quetzal_moves.append(['Q', i, i+(10*n)])
                n += 1
            elif current_position[i+(10*n)] == 'x':
                break
            elif current_position[i+(10*n)] in white_pieces:
                break
            elif current_position[i+(10*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i+(10*n)])
                break
        n=1
        while n:
            if current_position[i-(1*n)] == '.':
                quetzal_moves.append(['Q', i, i-(1*n)])
                n += 1
            elif current_position[i-(1*n)] == 'x':
                break
            elif current_position[i-(1*n)] in white_pieces:
                break
            elif current_position[i-(1*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i-(1*n)])
                break
        n=1
        while n:
            if current_position[i-(10*n)] == '.':
                quetzal_moves.append(['Q', i, i-(10*n)])
                n += 1
            elif current_position[i-(10*n)] == 'x':
                break
            elif current_position[i-(10*n)] in white_pieces:
                break
            elif current_position[i-(10*n)] in black_pieces:
                quetzal_moves.append(['Q', i, i-(10*n)])
                break
            
    return quetzal_moves
    
#return all legal moves for white king
def white_kingfisher_moves(current_position):
    kingfishers = []
    kingfisher_loc = 0
    kingfisher_moves = []
    
    for square in current_position:
        if square == 'K':
            kingfishers.append(kingfisher_loc)
        kingfisher_loc += 1
        
    for i in kingfishers:
        if current_position[i+10] in black_pieces or current_position[i+10] == '.':
            kingfisher_moves.append(['K', i, i+10])
        if current_position[i-10] in black_pieces or current_position[i-10] == '.':
            kingfisher_moves.append(['K', i, i-10])
        if current_position[i+1] in black_pieces or current_position[i+1] == '.':
            kingfisher_moves.append(['K', i, i+1])
        if current_position[i-1] in black_pieces or current_position[i-1] == '.':
            kingfisher_moves.append(['K', i, i-1])
        if current_position[i+9] in black_pieces or current_position[i+9] == '.':
            kingfisher_moves.append(['K', i, i+9])
        if current_position[i-9] in black_pieces or current_position[i-9] == '.':
            kingfisher_moves.append(['K', i, i-9])
        if current_position[i+11] in black_pieces or current_position[i+11] == '.':
            kingfisher_moves.append(['K', i, i+11])
        if current_position[i-11] in black_pieces or current_position[i-11] == '.':
            kingfisher_moves.append(['K', i, i-11])
    
    return kingfisher_moves

#return all legal moves for black pawns
def black_parakeet_moves(current_position):
    parakeets = []
    keet_loc = 0
    parakeet_moves = []
    
    for square in current_position:
        if square =='p':
            parakeets.append(keet_loc)
        keet_loc += 1

    for i in parakeets:
        if current_position[i-10] == '.':
            parakeet_moves.append(['p', i, i-10])
        if 80<i<89:
            if current_position[i-10] == current_position[i-20] == '.':
                parakeet_moves.append(['p', i, i-20])
        if current_position[i-9] in white_pieces:
            parakeet_moves.append(['p', i, i-9])
        if current_position[i-11] in white_pieces:
            parakeet_moves.append(['p', i, i-11])
            
    return parakeet_moves
    
#return all legal moves for black bishops
def black_bluejay_moves(current_position):
    bluejays = []
    jay_loc = 0
    bluejay_moves = []
    
    for square in current_position:
        if square == 'b':
            bluejays.append(jay_loc)
        jay_loc += 1
    
    for i in bluejays:
        n=1
        while n:
            if current_position[i+(9*n)] == '.':
                bluejay_moves.append(['b', i, i+(9*n)])
                n += 1
            elif current_position[i+(9*n)] == 'x':
                break
            elif current_position[i+(9*n)] in black_pieces:
                break
            elif current_position[i+(9*n)] in white_pieces:
                bluejay_moves.append(['b', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(11*n)] == '.':
                bluejay_moves.append(['b', i, i+(11*n)])
                n += 1
            elif current_position[i+(11*n)] == 'x':
                break
            elif current_position[i+(11*n)] in black_pieces:
                break
            elif current_position[i+(11*n)] in white_pieces:
                bluejay_moves.append(['b', i, i+(11*n)])
                break
        n=1
        while n:
            if current_position[i-(9*n)] == '.':
                bluejay_moves.append(['b', i, i-(9*n)])
                n += 1
            elif current_position[i-(9*n)] == 'x':
                break
            elif current_position[i-(9*n)] in black_pieces:
                break
            elif current_position[i-(9*n)] in white_pieces:
                bluejay_moves.append(['b', i, i-(9*n)])
                break
        n=1
        while n:
            if current_position[i-(11*n)] == '.':
                bluejay_moves.append(['b', i, i-(11*n)])
                n += 1
            elif current_position[i-(11*n)] == 'x':
                break
            elif current_position[i-(11*n)] in black_pieces:
                break
            elif current_position[i-(11*n)] in white_pieces:
                bluejay_moves.append(['b', i, i-(11*n)])
                break
        
    return bluejay_moves

#return all legal moves for black knights
def black_nighthawk_moves(current_position):
    nighthawks = []
    hawk_loc = 0
    nighthawk_moves = []
    
    for square in current_position:
        if square == 'n':
            nighthawks.append(hawk_loc)
        hawk_loc += 1
    
    for i in nighthawks:
        if current_position[i+8] in white_pieces or current_position[i+8] == '.':
            nighthawk_moves.append(['n', i, i+8])
        if current_position[i-8] in white_pieces or current_position[i-8] == '.':
            nighthawk_moves.append(['n', i, i-8])
            
        if current_position[i+12] in white_pieces or current_position[i+12] == '.':
            nighthawk_moves.append(['n', i, i+12])
        if current_position[i-12] in white_pieces or current_position[i-12] == '.':
            nighthawk_moves.append(['N', i, i-12])
            
        if current_position[i+19] in white_pieces or current_position[i+19] == '.':
            nighthawk_moves.append(['n', i, i+19])
        if current_position[i-19] in white_pieces or current_position[i-19] == '.':
            nighthawk_moves.append(['n', i, i-19])
        if current_position[i+21] in white_pieces or current_position[i+21] == '.':
            nighthawk_moves.append(['n', i, i+21])
        if current_position[i-21] in white_pieces or current_position[i-21] == '.':
            nighthawk_moves.append(['n', i, i-21])
      
    return nighthawk_moves

#return all legal moves for black rooks
def black_robin_moves(current_position):
    robins = []
    robin_loc = 0
    robin_moves = []
    
    for square in current_position:
        if square == 'r':
            robins.append(robin_loc)
        robin_loc += 1
        
    for i in robins:
        n=1
        while n:
            if current_position[i+(1*n)] == '.':
                robin_moves.append(['r', i, i+(1*n)])
                n += 1
            elif current_position[i+(1*n)] == 'x':
                break
            elif current_position[i+(1*n)] in black_pieces:
                break
            elif current_position[i+(1*n)] in white_pieces:
                robin_moves.append(['r', i, i+(1*n)])
                break
        n=1
        while n:
            if current_position[i+(10*n)] == '.':
                robin_moves.append(['r', i, i+(10*n)])
                n += 1
            elif current_position[i+(10*n)] == 'x':
                break
            elif current_position[i+(10*n)] in black_pieces:
                break
            elif current_position[i+(10*n)] in white_pieces:
                robin_moves.append(['r', i, i+(10*n)])
                break
        n=1
        while n:
            if current_position[i-(1*n)] == '.':
                robin_moves.append(['r', i, i-(1*n)])
                n += 1
            elif current_position[i-(1*n)] == 'x':
                break
            elif current_position[i-(1*n)] in black_pieces:
                break
            elif current_position[i-(1*n)] in white_pieces:
                robin_moves.append(['r', i, i-(1*n)])
                break
        n=1
        while n:
            if current_position[i-(10*n)] == '.':
                robin_moves.append(['r', i, i-(10*n)])
                n += 1
            elif current_position[i-(10*n)] == 'x':
                break
            elif current_position[i-(10*n)] in black_pieces:
                break
            elif current_position[i-(10*n)] in white_pieces:
                robin_moves.append(['r', i, i-(10*n)])
                break
    
    return robin_moves

#return all legal moves for black queens
def black_quetzal_moves(current_position):
    quetzals = []
    quetzal_loc = 0
    quetzal_moves = []
    
    for square in current_position:
        if square == 'q':
            quetzals.append(quetzal_loc)
        quetzal_loc += 1
        
    for i in quetzals:
        n=1
        while n:
            if current_position[i+(9*n)] == '.':
                quetzal_moves.append(['q', i, i+(9*n)])
                n += 1
            elif current_position[i+(9*n)] == 'x':
                break
            elif current_position[i+(9*n)] in black_pieces:
                break
            elif current_position[i+(9*n)] in white_pieces:
                quetzal_moves.append(['q', i, i+(9*n)])
                break
        n=1
        while n:
            if current_position[i+(11*n)] == '.':
                quetzal_moves.append(['q', i, i+(11*n)])
                n += 1
            elif current_position[i+(11*n)] == 'x':
                break
            elif current_position[i+(11*n)] in black_pieces:
                break
            elif current_position[i+(11*n)] in white_pieces:
                quetzal_moves.append(['q', i, i+(11*n)])
                break
        n=1
        while n:
            if current_position[i-(9*n)] == '.':
                quetzal_moves.append(['q', i, i-(9*n)])
                n += 1
            elif current_position[i-(9*n)] == 'x':
                break
            elif current_position[i-(9*n)] in black_pieces:
                break
            elif current_position[i-(9*n)] in white_pieces:
                quetzal_moves.append(['q', i, i-(9*n)])
                break
        n=1
        while n:
            if current_position[i-(11*n)] == '.':
                quetzal_moves.append(['q', i, i-(11*n)])
                n += 1
            elif current_position[i-(11*n)] == 'x':
                break
            elif current_position[i-(11*n)] in black_pieces:
                break
            elif current_position[i-(11*n)] in white_pieces:
                quetzal_moves.append(['q', i, i-(11*n)])
                break
            
        n=1
        while n:
            if current_position[i+(1*n)] == '.':
                quetzal_moves.append(['q', i, i+(1*n)])
                n += 1
            elif current_position[i+(1*n)] == 'x':
                break
            elif current_position[i+(1*n)] in black_pieces:
                break
            elif current_position[i+(1*n)] in white_pieces:
                quetzal_moves.append(['q', i, i+(1*n)])
                break
        n=1
        while n:
            if current_position[i+(10*n)] == '.':
                quetzal_moves.append(['q', i, i+(10*n)])
                n += 1
            elif current_position[i+(10*n)] == 'x':
                break
            elif current_position[i+(10*n)] in black_pieces:
                break
            elif current_position[i+(10*n)] in white_pieces:
                quetzal_moves.append(['q', i, i+(10*n)])
                break
        n=1
        while n:
            if current_position[i-(1*n)] == '.':
                quetzal_moves.append(['q', i, i-(1*n)])
                n += 1
            elif current_position[i-(1*n)] == 'x':
                break
            elif current_position[i-(1*n)] in black_pieces:
                break
            elif current_position[i-(1*n)] in white_pieces:
                quetzal_moves.append(['q', i, i-(1*n)])
                break
        n=1
        while n:
            if current_position[i-(10*n)] == '.':
                quetzal_moves.append(['q', i, i-(10*n)])
                n += 1
            elif current_position[i-(10*n)] == 'x':
                break
            elif current_position[i-(10*n)] in black_pieces:
                break
            elif current_position[i-(10*n)] in white_pieces:
                quetzal_moves.append(['q', i, i-(10*n)])
                break
            
    return quetzal_moves
    
#return all legal moves for black king
def black_kingfisher_moves(current_position):
    kingfishers = []
    kingfisher_loc = 0
    kingfisher_moves = []
    
    for square in current_position:
        if square == 'k':
            kingfishers.append(kingfisher_loc)
        kingfisher_loc += 1
        
    for i in kingfishers:
        if current_position[i+10] in white_pieces or current_position[i+10] == '.':
            kingfisher_moves.append(['k', i, i+10])
        if current_position[i-10] in white_pieces or current_position[i-10] == '.':
            kingfisher_moves.append(['k', i, i-10])
        if current_position[i+1] in white_pieces or current_position[i+1] == '.':
            kingfisher_moves.append(['k', i, i+1])
        if current_position[i-1] in white_pieces or current_position[i-1] == '.':
            kingfisher_moves.append(['k', i, i-1])
        if current_position[i+9] in white_pieces or current_position[i+9] == '.':
            kingfisher_moves.append(['k', i, i+9])
        if current_position[i-9] in white_pieces or current_position[i-9] == '.':
            kingfisher_moves.append(['k', i, i-9])
        if current_position[i+11] in white_pieces or current_position[i+11] == '.':
            kingfisher_moves.append(['k', i, i+11])
        if current_position[i-11] in white_pieces or current_position[i-11] == '.':
            kingfisher_moves.append(['k', i, i-11])
    
    return kingfisher_moves
    
def white_legal_moves(current_position):    
    legal_moves = []
        
    #parakeet_moves
    p = white_parakeet_moves(current_position)
    for move in p:
        legal_moves.append(move)

    #robin_moves
    r = white_robin_moves(current_position)
    for move in r:
        legal_moves.append(move)
        
    #nighthawk_moves
    n = white_nighthawk_moves(current_position)
    for move in n:
        legal_moves.append(move)
        
    #bluejay_moves 
    b = white_bluejay_moves(current_position)
    for move in b:
        legal_moves.append(move)
    
    #quetzal_moves
    q = white_quetzal_moves(current_position)
    for move in q:
        legal_moves.append(move)
        
    #kingfisher_moves
    k = white_kingfisher_moves(current_position)
    for move in k:
        legal_moves.append(move)
    
    #return legal_moves
    return legal_moves

def black_legal_moves(current_position):    
    legal_moves = []
    
    #parakeet_moves
    p = black_parakeet_moves(current_position)
    for move in p:
        legal_moves.append(move)
        
    #robin_moves
    r = black_robin_moves(current_position)
    for move in r:
        legal_moves.append(move)
        
    #nighthawk_moves
    n = black_nighthawk_moves(current_position)
    for move in n:
        legal_moves.append(move)
        
    #bluejay_moves 
    b = black_bluejay_moves(current_position)
    for move in b:
        legal_moves.append(move)
    
    #quetzal_moves
    q = black_quetzal_moves(current_position)
    for move in q:
        legal_moves.append(move)
        
    #kingfisher_moves
    k = black_kingfisher_moves(current_position)
    for move in k:
        legal_moves.append(move)
    
    #return legal_moves
    return legal_moves

def generate_white_successor(current_position):
    move_list = white_legal_moves(current_position)
    next_move = move_list[0]
    piece = next_move[0]
    move_from = next_move[1]
    move_to = next_move[2]
    
    #queening a white pawn (not working yet)
    #if piece == 'P':
        #if 90 < move_to < 99:
            #new_position = current_position[:move_from] + '.' + current_position[move_from+1:move_to] + 'Q' + current_position[move_to+1:]
    
    if move_to > move_from:
        new_position = current_position[:move_from] + '.' + current_position[move_from+1:move_to] + piece + current_position[move_to+1:]
        
    elif move_to < move_from:
        new_position = current_position[:move_to] + piece + current_position[move_to+1:move_from] + '.' + current_position[move_from+1:]

    #visualize_board(new_position)    
    return new_position 

def generate_black_successor(current_position):
    move_list = black_legal_moves(current_position)
    next_move = move_list[0]
    piece = next_move[0]
    move_from = next_move[1]
    move_to = next_move[2]
    
    #queening a black pawn (not working yet)
    #if piece == 'p':
        #if 20 < move_to < 29:
            #new_position = current_position[:move_to] + 'q' + current_position[move_to+1:move_from] + '.' + current_position[move_from+1:]


    if move_to > move_from:
        new_position = current_position[:move_from] + '.' + current_position[move_from+1:move_to] + piece + current_position[move_to+1:]
        
    elif move_to < move_from:
        new_position = current_position[:move_to] + piece + current_position[move_to+1:move_from] + '.' + current_position[move_from+1:]
    
    #visualize_board(new_position)
    return new_position  

def minimax(board):
    #if sys.argv[1] == 'w':
    first_move = generate_white_successor(board)
    second_move = generate_black_successor(first_move)
    third_move = generate_white_successor(second_move)
    fourth_move = generate_black_successor(third_move)
    fifth_move = generate_white_successor(fourth_move)
    #evaluation function
    
    print(visualize_board(fifth_move))
    return fifth_move

def evaluation(board):
    white_score = 0
    black_score = 0
    for square in board:
        if square == 'P':
            white_score = white_score + (eval_func['p'])
        if square == 'N':
            white_score = white_score + (eval_func['n'])
        if square == 'B':
            white_score = white_score + (eval_func['b'])
        if square == 'R':
            white_score = white_score + (eval_func['r'])
        if square == 'Q':
            white_score = white_score + (eval_func['q'])
        if square == 'K':
            white_score = white_score + (eval_func['k'])
            
        if square == 'p':
            black_score = black_score + (eval_func['p'])
        if square == 'n':
            black_score = black_score + (eval_func['n'])
        if square == 'b':
            black_score = black_score + (eval_func['b'])
        if square == 'r':
            black_score = black_score + (eval_func['r'])
        if square == 'q':
            black_score = black_score + (eval_func['q'])
        if square == 'k':
            black_score = black_score + (eval_func['k'])
    
    return white_score - black_score


    

#### Main Program
init_pos = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr' #sys.argv[3]
white_pieces = 'RNBQKP'
black_pieces = 'rnbqkp'

eval_func ={
	'p': 100,
	'r': 500,
	'n': 325,
	'b': 330,
	'q': 900,
	'k': 20000
}

board = generate_board(init_pos) #sys.argv[2]
#visualize_board(board)

minimax(board)
