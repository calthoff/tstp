

import logging


logging.basicConfig(level=logging.INFO)


def add(a, b):
    logging.info('Function add was called.')
    c = a + b
    logging.info('Calculation is finished.')
    return c


add(10, 10)
