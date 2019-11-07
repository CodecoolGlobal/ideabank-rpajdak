import sys
data = sys.argv[1:]
data = str(data)[1:][:-1]
arg = data
ideas = []
def display_ideas():
    file = open("ideas.txt", "r")
    content =file.read()
    print(content)
    file.close()
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
        print(ideas_to_file)
def remove_idea():
    file = open("ideas.txt", "r")
    content =file.read().split()
    file.close()
    print(type(content))
    for i in range(0,len(content)):
        if i % 2 == 0:
           content[i]=content[i] + content[i + 1]
    print(content)
#if arg == "'--list'":
#    display_ideas()
#else:
#    idea_bank()
remove_idea()