from lexer import *
from parser import Parser
from simulator import Simulator


def main():
    filename = 'test/test_array.pas'
    token_list = Lexer(filename).scan()
    instruction_list = Parser(token_list).start_parser()
    Simulator(instruction_list).simulator()


main()
