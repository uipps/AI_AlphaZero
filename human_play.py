# -*- coding: utf-8 -*-
"""
human VS AI models
Input your move in the format: 2,3

玩家1（player1）：human(人)
玩家2（player2）：computer(电脑)

python human_play.py --file best_policy_6_6_4.model2 --width 6 --num 4 --player2_first 0 --two_computer 1
python human_play.py --file best_policy_8_8_5.model --width 8 --num 5 --player2_first 0 --two_computer 1
python human_play.py --file best_policy_tensorflow_10_10_5.model --width 10 --num 5 --two_computer 1
python human_play.py --file best_policy_pytorch_6_6_4.model --width 6 --num 4 --player2_first 0 --two_computer 0   要修改代码，from pytorch库
"""

from __future__ import print_function
import pickle
import sys
import argparse
from game import Board, Game
from mcts_pure import MCTSPlayer as MCTS_Pure
from mcts_alphaZero import MCTSPlayer
from policy_value_net_numpy import PolicyValueNetNumpy
# from policy_value_net import PolicyValueNet  # Theano and Lasagne
#from policy_value_net_pytorch import PolicyValueNet  # Pytorch
from policy_value_net_tensorflow import PolicyValueNet # Tensorflow
# from policy_value_net_keras import PolicyValueNet  # Keras


class Human(object):
    """
    human player
    """

    def __init__(self):
        self.player = None

    def set_player_ind(self, p):
        self.player = p

    def get_action(self, board):
        try:
            location = input("Your move: ")
            if isinstance(location, str):  # for python3
                location = [int(n, 10) for n in location.split(",")]
            move = board.location_to_move(location)
        except Exception as e:
            move = -1
        if move == -1 or move not in board.availables:
            print("invalid move")
            move = self.get_action(board)
        return move

    def __str__(self):
        return "Human {}".format(self.player)


def run():
    #n = 4
    #width, height = 6, 6
    #model_file = 'best_policy_6_6_4.model'
    #start_player=1
    c_puct=5
    n_playout=400       # set larger n_playout for better performance

    ''' 获取命令行参数 '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='best_policy_6_6_4.model', help='model file , default 6*6，4 in a row')
    parser.add_argument('--width', type=int, default=6, help='width and height is the same! , default 6')
    parser.add_argument('--num', type=int, default=4, help='num in row, default 4')
    parser.add_argument('--player2_first', type=int, default=1, help='0:player1(humen) first; 1:player2(computer) first ; default 1')
    parser.add_argument('--two_computer', type=int, default=0, help='1:tow computer play; other wise: human and computer; default 0')
    #parser.add_argument('--two_human', type=int, default=0, help='1:tow humen play; other wise: human and computer; default 0')

    args = parser.parse_args()
    n = args.num
    width = height = args.width
    model_file = args.file
    start_player = args.player2_first
    two_computer = args.two_computer

    if len(sys.argv) == 1:
        parser.print_help()

    try:
        board = Board(width=width, height=height, n_in_row=n)
        game = Game(board)

        # ############### human VS AI ###################
        # load the trained policy_value_net in either Theano/Lasagne, PyTorch or TensorFlow
        if 'tensorflow' in model_file.lower() or 'pytorch' in model_file.lower():  # 文件名中包含tensorflow，pytorch
            best_policy = PolicyValueNet(width, height, model_file = model_file)
            mcts_player = MCTSPlayer(best_policy.policy_value_fn, c_puct=5, n_playout=400)
        else:
            # load the provided model (trained in Theano/Lasagne) into a MCTS player written in pure numpy
            try:
                policy_param = pickle.load(open(model_file, 'rb'))
            except:
                policy_param = pickle.load(open(model_file, 'rb'),
                                encoding='bytes')  # To support python3
            best_policy = PolicyValueNetNumpy(width, height, policy_param)
            mcts_player = MCTSPlayer(best_policy.policy_value_fn, c_puct, n_playout)

        # uncomment the following line to play with pure MCTS (it's much weaker even with a larger n_playout)
        # mcts_player = MCTS_Pure(c_puct=5, n_playout=1000)

        # human player, input your move in the format: 2,3
        #human = Human()
        if 1 == two_computer:
            human = MCTSPlayer(best_policy.policy_value_fn, c_puct, n_playout)
        else:
            human = Human()

        # set start_player=0 for human first
        game.start_play(human, mcts_player, start_player, is_shown=1)
    except KeyboardInterrupt:
        print('\n\rquit')


if __name__ == '__main__':
    run()
