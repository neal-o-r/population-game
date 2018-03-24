import random
from collections import namedtuple
import os

def get_pops(l):
        p = []
        for i in l:
                p.append(i.replace('"', "").split(','))
        return p

def make_pop_tuples(c):

        County = namedtuple('County', ['Rank', 'Name'])
        return list(map((lambda x: County(int(x[0]), x[1])),
                get_pops(c)))

def make_bracket(b):

        random.shuffle(b)
        pairs = []
        for i in range(0, len(b) - 1, 2):
                pairs.append((b[i], b[i+1]))

        return pairs


def ask_pair(p):
        text = f"""Which has the larger population?
                1. {p[0].Name}
                2. {p[1].Name}\n"""
        guess = int(input(text))
        answer = 1 if p[0].Rank < p[1].Rank else 2

        return p[guess - 1], guess == answer

def play_a_game(bracket):
        score = 0
        game = bracket.copy()

        win = False
        i = 0
        while len(game) > 1:
                next_round = []
                for p in game:
                        os.system('clear')
                        if i > 0:
                                if win: print("Right!")
                                else: print("Wrong!")

                        print(f"\nCurrent Score: {score}/{i}\n")

                        n, win = ask_pair(p)
                        if win: score += 1
                        next_round.append(n)
                        i += 1

                game = make_bracket(next_round)


if __name__ == '__main__':
        with open('pops.csv') as f:
                contents = f.read().splitlines()

        bracket = make_bracket(make_pop_tuples(contents))
        play_a_game(bracket)
