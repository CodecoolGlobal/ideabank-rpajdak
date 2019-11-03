# Put your code here
import sys
arg = sys.argv

ideas = []

def idea_bank():
    i = 0
    while i == 0:
        new_idea = input("What is your new idea?: ")
        n = len(ideas) + 1
        number = 0
        # print(" ".join(idea_to_add))
        for x in range(0, n):
            number = str(n) + "."
        idea_to_add = number , new_idea
        idea_to_add = " ".join(idea_to_add) 
        ideas.append(idea_to_add)
        ideas_to_file = '\n'.join(ideas)
        file = open("ideas.txt", "w")
        file.write(ideas_to_file)
        file.close()
        print(type(ideas))
        print(ideas_to_file)
idea_bank()