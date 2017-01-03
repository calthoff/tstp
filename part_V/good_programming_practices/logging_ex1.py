# IF YOU ARE READING THIS YOU ARE READING 
# AN OUTDATED VERSION OF THE BOOK.
# I am working with Amazon to resolve this.
# The new version is much better and has correctly formatted code examples
# In the book.
# Please email me at cory@theselftaughtprogrammer.io
# For an updated version

import logging


logging.basicConfig(level=logging.INFO)


def add(a, b):
    logging.info('Function add was called.')
    c = a + b
    logging.info('Calculation is finished.')
    return c


add(10, 10)
