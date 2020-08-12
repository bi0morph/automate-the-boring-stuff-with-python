#! /usr/bin/env python3

import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start program')
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.debug('User did input: %s' % guess)

toss = ['tails', 'heads'][random.randint(0, 1)]
logging.debug('flip the coin: %s' % toss)
if toss == guess:
    logging.debug('User guessed')
    print('You got it!')
else:
    logging.debug('User did not guess')
    print('Nope! Guess again!')
    guess = input()
    logging.debug('User did input one more time: %s' % guess)
    if toss == guess:
        logging.debug('User guessed')
        print('You got it!')
    else:
        logging.debug('User did not guess even in second time')
        print('Nope. You are really bad at this game.')
logging.debug('End program')
