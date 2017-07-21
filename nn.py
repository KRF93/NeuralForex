import sys
import os
import random

class NeuralNetwork() :
    def __init__(self):
        pass

    def run(self, args):
        print(args)

if __name__ == "__main__":
    nn = NeuralNetwork();
    nn.run([[1,3,5,6], [245.6, 250.9, 251.4, 248.6]])
