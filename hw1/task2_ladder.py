import sys


num_steps = int(sys.argv[1])
space = " "
grille = "#"

if __name__ == '__main__':
    for i in range(num_steps):
        grille_num = i + 1
        print(space * (num_steps - grille_num) + grille * grille_num)
