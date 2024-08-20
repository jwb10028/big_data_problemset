import sys


# receive the output of a mapper, (key, [value, value, ...])
def read_mapper_output(input, separator='\t'):
    for line in input:
        #  return each (key, [value, value, ...]) tuple, though there should only be one per line
        yield line.rstrip().split(separator)


def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    total = 0

    for words in data:
        total+=1
    
    print("%d" % (total))

if __name__=='__main__':
    main()