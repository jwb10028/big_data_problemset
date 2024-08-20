import sys

def read_input(input):
    for line in input:
        yield line.strip().split('\t')

def main():
    # Read total words count from a local file (i.e. total occurrence count)
    with open('uni.txt', 'r') as f:
        total_words = int(f.read().strip())

    data = read_input(sys.stdin)
    # Process each line, which contains a word and its count
    for words in data:
        word = words[0]
        count = int(words[1])
        prob = count / float(total_words)  # Ensure division is float division
        print("%s\t%.6f\t%d|%d" % (word, prob, count, total_words))

if __name__ == '__main__':
    main()