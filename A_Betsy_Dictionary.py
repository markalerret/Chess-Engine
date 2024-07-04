# -*- coding: utf-8 -*-
"""
# Team akjoshi-malerret-rossdm
# Assignment02_Part02_Addendum
# A program to create a scoring dictionary/heuristic
# Date: 10/26/2020  1:00pm EDT
# Author(s): David Ross - in consultation with Mark Lerret
# - Note: extra print comments were used for testing progress

@author: David Ross LT
"""
# Load Modules
import sys
import json

# init_pos = 'RNBQKBNRPPPPPPPP................................pppppppprnbqkbnr'
# white_pieces = 'RNBQKP'
# black_pieces = 'rnbqkp'

# Imports board position files
def import_board(filename):
    file_data = open(filename, 'r')
    lines1 = file_data.readlines()
    line_nbr = len(lines1)
    # print(len(lines1))
    file_data.close()

    data_file = open(filename, 'r')
    raw_board = []
    for row in range(line_nbr):
        new_line = [0,0,0,0,0,0,0,0]
        raw_line = data_file.readline()
        # print(raw_line)
        data_line = raw_line.split(",")
        if len(data_line) == 9:
            del data_line[8]
        # print(data_line)
        for col in range(8):
            new_line[col] = int(data_line[col])
        raw_board.append(new_line)
        # print(data_init)
    return raw_board

# Creates key, value pairs by piece + position
def create_pairs(piece, board, value_set):
    if piece in "Pp":
        piece_base = 100
    elif piece in "Nn":
        piece_base = 325
    elif piece in 'Bb':
        piece_base = 330
    elif piece in 'Rr':
        piece_base = 500
    elif piece in 'Qq':
        piece_base = 900
    elif piece in 'KkEe':
        piece_base = 20000
        
    row_ctr = 0
    for row in board:
        col_ctr = 0
        board_row = board[row_ctr]
        for col in board_row: 
            new_pair = ["", 0]
            new_pair[0] = piece + str(9 - row_ctr) + str(col_ctr + 1)
            new_pair[1] = piece_base + board_row[col_ctr]
            # print(new_pair)
            value_set.append(new_pair)
            col_ctr += 1
        row_ctr += 1
   
    return value_set

def score_dict(value_set):
    evaltn_dictnry = {}
    row_ctr = 0
    for row in range(len(value_set)):                    
        evaltn_dictnry[value_set[row_ctr][0]] = str(value_set[row_ctr][1])
        row_ctr += 1
    return evaltn_dictnry

# Main program    
if __name__ == "__main__":
    print("Program to create Betsy scoring boards from external sources.\n")
    value_set = []
    
    # Load Parakeet positions
    filename = 'pawn_csv.txt'
    board = import_board(filename)
    # White pawns
    piece = 'P'
    value_set = create_pairs(piece, board, value_set)
    # Black pawns
    piece = 'p'
    value_set = create_pairs(piece, board, value_set)

    
    # Load Nighthawk positions
    filename = 'knight_csv.txt'
    board = import_board(filename)
    # White Nighthawks
    piece = 'N'
    value_set = create_pairs(piece, board, value_set)
    # Black Nighthawks
    piece = 'n'
    value_set = create_pairs(piece, board, value_set)

    # Load Blue Jay positions
    filename = 'bishop_csv.txt'
    board = import_board(filename)
    # White Blue Jays
    piece = 'B'
    value_set = create_pairs(piece, board, value_set)
    # Black Blue Jays
    piece = 'b'
    value_set = create_pairs(piece, board, value_set)
    
    # Load Robin positions
    filename = 'rook_csv.txt'
    board = import_board(filename)
    # White Robins
    piece = 'R'
    value_set = create_pairs(piece, board, value_set)
    # Black Robins
    piece = 'r'
    value_set = create_pairs(piece, board, value_set)
    
    # Load Quetzcal positions
    filename = 'queen_csv.txt'
    board = import_board(filename)
    # White Quetzcal
    piece = 'Q'
    value_set = create_pairs(piece, board, value_set)
    # Black Quetzcal
    piece = 'q'
    value_set = create_pairs(piece, board, value_set)
    
    # Load Kingfisher positions - early/mid game
    filename = 'king_mid_csv.txt'
    board = import_board(filename)
    # White Kingfisher
    piece = 'K'
    value_set = create_pairs(piece, board, value_set)
    # Black Kingfisher
    piece = 'k'
    value_set = create_pairs(piece, board, value_set)
    
    # Load Kingfisher positions - end game
    filename = 'king_end_csv.txt'
    board = import_board(filename)
    # White Kingfisher - end
    piece = 'E'
    value_set = create_pairs(piece, board, value_set)
    # Black Kingfisher - end
    piece = 'e'
    value_set = create_pairs(piece, board, value_set)
    
    # Create dictionary
    evaltn_dictnry = score_dict(value_set)
    row_ctr = 0
    # for row in evaltn_dictnry:
        # print(row, evaltn_dictnry[row])
        # row_ctr + 1
    print(len(evaltn_dictnry))

    with open('betsy_dt.json', 'w') as outfile:
        json.dump(evaltn_dictnry, outfile)

    # To load the betsy_dt.jsn into memory:
    #   with open('betsy_dt.json') as json_file:
    #       evaltn_dictnry2 = json.load(json_file)
        
# End main after creating betsy_dt.json