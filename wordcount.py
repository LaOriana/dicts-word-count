text_file = open('test.txt')

def word_count(text_file):

    words = {}

    for line in text_file:
        new_line = line.rstrip().split(' ')

        for word in new_line:
            if word not in words:
                words[word] = 1
            else:
                words[word] = words[word] + 1
                
    for key, value in words.items():
        print(f'{key} {value}')

word_count(text_file)