from random import randint as rand
from datetime import datetime as time
from json_parser import parse_to_var
from answer import answer
from randomizer import randomize_phrases

########################################################################
# Data #
########################################################################
file = "data.json"
salutaions = parse_to_var(file, "salutaions")

adoption = parse_to_var(file, "adoption")

questions = parse_to_var(file, "questions")

jokes = parse_to_var(file, "jokes")

unclear_response = parse_to_var(file, "unclear_response")


user_in = ""



########################################################################
# Logic Functions #
########################################################################

def getdaytime():
    h = time.now().hour
    switcher = {
        0: "night",
        1: "night",
        2: "night",
        3: "night",
        4: "night",
        5: "morning",
        6: "morning",
        7: "morning",
        8: "morning",
        9: "morning",
        10: "morning",
        11: "noon",
        12: "noon",
        13: "noon",
        14: "noon",
        15: "afternoon",
        16: "afternoon",
        17: "afternoon",
        18: "evening",
        19: "evening",
        20: "evening",
        21: "evening",
        22: "evening",
        23: "evening",
    }

    return switcher.get(h, "none")


def multi_word_AND_check(words_array_one,words_array_two,user_in):
    part1 = bool
    part2 = bool

    for w1 in words_array_one:
        if w1 == words_array_one[0]:
            part1 = w1 in user_in
        else:
            part1 = part1 or w1 in user_in
    
    for w2 in words_array_two:
        if w2 == words_array_two[0]:
            part2 = w2 in user_in
        else:
            part2 = part2 or w2 in user_in

    return part1 and part2

# def multi_word_check(words_array_one,user_in):
#     part = bool

#     for w1 in words_array_one:
#         w1 = str(w1).lower()
#         if w1 == words_array_one[0]:
#             part = w1 in user_in
#         else:
#             part = part or w1 in user_in

#     return part

########################################################################
# Chat Functions #
########################################################################

def greeting():
    g = rand(0,len(salutaions)-1)

    if g == 0:
        after = getdaytime()
        greet = salutaions[g] + after.capitalize()
    else:
        greet = salutaions[g] 
    
    return greet
        

def question(): 
    fallback = "Please ask me something"
    used_arr = "questions"
    return randomize_phrases(questions, fallback, used_arr)

def make_joke():
    fallback = "I dont have more jokes. Please Ask me some thing"
    used_arr = "jokes"
    return randomize_phrases(jokes, fallback, used_arr)


def unclear_input():
    fallback = "Sorry I am not yet smart enough to understand you"
    used_arr = "unclear"
    return randomize_phrases(unclear_response, fallback, used_arr)

def goodbye():
    g = rand(0,len(adoption)-1)

    return adoption[g]

def check_for_joke(user_in):
    one = ["joke"]
    two = ["tell", "say", "give", "make"]
    
    return multi_word_AND_check(one,two,user_in)

# def check_for_greeting(user_in):
    
#     multi_word_check(salutaions, user_in)


########################################################################
# Main Loop #
########################################################################


def main(user_in):
    print(greeting())

    while user_in != "stop":

        user_in = str(input("Type here --> ")).lower()
        
        if user_in == "":
            print("You didn't write anything, try again")
        
        # elif check_for_greeting(user_in) == True:
        #     print(question())
            
        elif check_for_joke(user_in) is True:
            print(make_joke())
        
        elif user_in[len(user_in)-1] == "!" or user_in[len(user_in)-1] == "." or "question" in user_in and "ask" in user_in:
            print(question())

        elif user_in[len(user_in)-1] == "?":
            print(answer(user_in))

        elif "life, the universe and everything" in user_in:
            print(42)

        elif user_in == "stop":
            print(goodbye())

        else:
            print(unclear_input())



########################################################################
# Run #
########################################################################
if __name__ == "__main__":
    main(user_in)