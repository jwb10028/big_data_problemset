#!/usr/bin/env python
"""An advanced Mapper, using Python iterators and generators."""

import sys
import re


def read_input(input):
    for line in input:
        # Remove chars not in set
        line = re.sub(r'[^a-zA-Z0-9\s]', '', line).lower()

        # Split line into words
        words = line.split()
        
        # keep returning each word
        yield words


def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)

    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        for word in words:
            print('%s%s%d' % (word, separator, 1))


# how to test locally in bash/linus: cat  | python mapper.py
if __name__ == "__main__":
    main()