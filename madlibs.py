#Credit Pizza Pizza ClassroomJr.com

#Scrapped idea. Using REGEX for multiple delimiter splitting. Would not join correctly at the end without splitting punctuation.
#import re
#split_mad_story = re.split("\s|\.|,|!|", mad_story)


print("Pizza was invented by a ____(adjective)____ ____(nationality)____ chef named ____(first+last name)____. To make a pizza, you need to take a lump of ____(noun)____, and make a thin, round ____(adjective)____ ____(noun)____. Then you cover it with ____(adjective)____ sauce, ____(adjective)____ cheese, and fresh chopped ____(plural noun)____ . When it is done, cut it into ____(number)____ ____(shape)____. Some kids like ____(food)____ pizza the best, but my favorite is the ____(food)____ pizza. If I could, I would eat pizza ____(number)____ times a day!")

mad_story = "Pizza was invented by a ADJECTIVE NATIONALITY chef named FIRSTLASTNAME . To make a pizza , you need to take a lump of NOUN , and make a thin , round ADJECTIVE NOUN . Then you cover it with ADJECTIVE sauce , ADJECTIVE cheese , and fresh chopped PLNOUN . When it is done , cut it into NUMBER SHAPE . Some kids like FOOD pizza the best , but my favorite is the FOOD pizza . If I could , I would eat pizza NUMBER times a day !"
split_mad_story = mad_story.split(" ")

def input_noun():
    return input("Please enter a noun: ")
def input_plnoun():
    return input("Please enter a plural noun: ")
def input_firstlastname():
    return input("Please enter a first and last name: ")
def input_verb():
    return input("Please enter a verb: ")
def input_nationality():
    return input("Please enter a nationality: ")
def input_adj():
    return input("Please enter an adjective: ")
def input_num():
    return input("Please enter a number: ")
def input_shape():
    return input("Please enter a shape: ")
def input_food():
    return input("Please enter a food: ")

replacer = {
    "NOUN": input_noun,
    "PLNOUN": input_plnoun,
    "FIRSTLASTNAME": input_firstlastname,
    "VERB": input_verb,
    "NATIONALITY": input_nationality,
    "ADJECTIVE": input_adj,
    "NUMBER": input_num,
    "SHAPE": input_shape,
    "FOOD": input_food,
}

def finder():
    for index in range(0,len(split_mad_story)):
        if split_mad_story[index] == "NOUN":
            split_mad_story[index] = replacer["NOUN"]()
        elif split_mad_story[index] == "PLNOUN":
            split_mad_story[index] = replacer["PLNOUN"]()
        elif split_mad_story[index] == "FIRSTLASTNAME":
            split_mad_story[index] = replacer["FIRSTLASTNAME"]()
        elif split_mad_story[index] == "VERB":
            split_mad_story[index] = replacer["VERB"]()
        elif split_mad_story[index] == "NATIONALITY":
            split_mad_story[index] = replacer["NATIONALITY"]()
        elif split_mad_story[index] == "ADJECTIVE":
            split_mad_story[index] = replacer["ADJECTIVE"]()
        elif split_mad_story[index] == "NUMBER":
            split_mad_story[index] = replacer["NUMBER"]()
        elif split_mad_story[index] == "SHAPE":
            split_mad_story[index] = replacer["SHAPE"]()
        elif split_mad_story[index] == "FOOD":
            split_mad_story[index] = replacer["FOOD"]()
        else:
            continue
finder()
#print(split_mad_story)
### UNDER CONSTRUCTION
def joiner():
    print(' '.join(split_mad_story))

joiner()

def test():
    input_noun()
    input_plnoun()
    input_firstlastname()
    input_verb()
    input_nationality()
    input_adj()
    input_num()
    input_shape()
    input_food()
    finder()
test()




#Old method
"""
noun_dict = {
    "adj1": input("Enter an adjecive: ")
    "nationality1": input("Enter a nationality: ")
    "firstlastname1": input("Enter a first and last name: ")
    "noun1": input("Enter a noun: ")
    "adj2": input("Enter an adjective: ")
    "noun2": input("Enter a noun: ")
    "adj3": input("Enter an adjective: ")
    "adj4": input("Enter another adjective: ")
    "plnoun1": input("Enter a plural noun: ")
    "num1": input("Enter a number: ")
    "shape1": input("Enter a shape: ")
    "food1": input("Enter a food: ")
    "food2": input("Enter another food: ")
    "num2": input("Enter a number: ")
}


print(noun_dict["noun1"])
"""

#BACKUP. Do not delete or remove comments
"""
Pizza was invented by a adj1 nationality1 chef named firstlastname1 .
To make a pizza, you need to take a lump of noun1, and make a thin, round adj2 noun2 .
 Then you cover it with adj3 sauce, adj4 cheese, and fresh chopped plnoun1 .
 When it is done, cut it into num1 shape1.
 Some kids like food1 pizza the best, but my favorite is the food2 pizza.
 If I could, I would eat pizza num2 times a day!
"""
