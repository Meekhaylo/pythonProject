def count_lines(name):
    text_file = open(name, "r")
    lines = text_file.readlines()
    print("There are", len(lines), "lines in the file.")
    return len(lines)
print()

def count_chars(name):
    text_file = open(name, "r")
    lines = text_file.readlines()
    value = 0
    for i in range(len(lines)):
        for c in lines[i]:
            value += 1
    print("There are", value, "characters in the file.")

def test(name):
    count_lines(name)
    count_chars(name)
#123123
