def count_characters_from_file(file):
    d = {}
    with open(file, "r") as f:
        while True:
            char = f.read(1)
            if not char:
                break
            char = char.rstrip() # verwijdert de \n
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
    return d

def count_words_from_file(file):
    d = {}
    with open(file, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.rstrip().replace('.', ' ').replace('!', ' ').replace('?', ' ')
            words = line.split(" ")
            for word in words:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1 
    return d

if __name__ == "__main__":
    print(count_characters_from_file("./files/file1.txt"))
    print(count_words_from_file("./files/file1.txt"))