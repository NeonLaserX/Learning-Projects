import string

# for bullet points only use special characters

def insert_bullet_point(path, symbol):
    file = []

    if not symbol in string.punctuation:
        raise Exception("bullet point must be a special character")

    # copying contents from file to python program

    with open(file= path, mode= "r") as f:
        for line in f:
            file.append(line)
    
    # inserting bullet points in the text

    index = 0
    for line in file:
        line = symbol + " " + line
        file[index] = line
        index += 1

    # writing content back to file

    with open(file= path, mode= "w") as f:
        for line in file:
            f.write(line)

def remove_bullet_point(path):
    file = []
    bullet_points = string.punctuation + " "

    # copying contents from file to python program

    with open(file= path, mode= "r") as f:
        for line in f:
            file.append(line)

    # removing bullet points

    index = 0
    for line in file:
        line = line.lstrip(bullet_points)
        file[index] = line
        index += 1

    # writing content back to file

    with open(file= path, mode= "w") as f:
        for line in file:
            f.write(line)

def main():    
    remove_bullet_point(path= "text.txt")
    
if __name__ == "__main__":
    main()