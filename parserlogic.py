#!/usr/bin/python


import re 
from pathlib import Path
import os
import chess
from chess import *
import chess.pgn
from chess.pgn import *



'''
class MyGameBuilder(GameBuilder):
    def visit_header(self, tagname: str, tagvalue: str) -> None:
        self.found_headers = True
        pass

'''    
with open("temp1.pankify",'r') as olala:
    lokation1 = olala.readline()
    lokation1 = Path(lokation1)
    #print(type(lokation1))

with open("temp2.pankify",'r') as olala:
    lokation2 = olala.readline()
    lokation2 = Path(lokation2)
    #print(type(lokation))
    
game_list = []

with open(lokation1, 'r', encoding="utf-8") as work_dis:
    #add all games to game_list array
    while True:
        game = chess.pgn.read_game(work_dis)
        if game:
            board = game.board()
            fens = board.fen()
            exporter = chess.pgn.StringExporter(headers=False, variations=True,comments = True, columns= None)
            move_string = fens + "\t" + game.accept(exporter) + "\n"
            with open(lokation2,'a',encoding="utf-8") as gg:
                gg.write(move_string)
                
        if game is None:
            break

        game_list.append(game)
        
 


print("its working!")

a = game_list[99]
board = a.board()
print(a. headers)
        
'''
print(len(game_list))
print(type(game_list[0]))
gametest = game_list[0]
#fengen =  gametest.mainline_moves()
print(board.fen())  
    
# print out moves => call mainline() on game_list
'''





