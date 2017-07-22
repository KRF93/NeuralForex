import sys
import os
import random

from api import AlphaVantage

class NeuralNetwork() :
    def __init__(self):
        pass

    def start_av_api(self):
        av = AlphaVantage.AlphaVantage()

    def run(self, args):
        pass

if __name__ == "__main__":
    nn = NeuralNetwork();
    nn.start_av_api()
    nn.run([[1,3,5,6], [245.6, 250.9, 251.4, 248.6]])
