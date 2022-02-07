from random import randint as rand
from json_parser import parse_to_var

file = "data.json"
done_phrases = parse_to_var(file, "done_phrases")


########################################################################
# Main Module #
########################################################################

def randomize_phrases(phrases, fallback, arr_name):
    p_num = 0
    x = 0
    while p_num < len(phrases):
        p_num = rand(0,len(phrases)-1)
        if arr_name != None:
            if p_num in done_phrases[arr_name]:
                x = x + 1
                if x ==  len(phrases):
                    return fallback
            else:
                done_phrases[arr_name].append(p_num)
                return phrases[p_num]
        else:
            return phrases[p_num]