from randomizer import randomize_phrases
from json_parser import parse_to_var

file = "data.json"

done_phrases = parse_to_var(file, "done_phrases")
done_responses = done_phrases["responses"]

responses = parse_to_var(file, "responses")
fallbacks = responses["fallbacks"]

answers = responses["answers"]

########################################################################
# Supporting Functions #
########################################################################

def get_answer_from_json(uin):
    for a in answers:
        question = answers[a]["question"]
        answer = answers[a]["answer"]
        for q in question:
            if uin == q:
                return answer
                break
        
def choose_answer(answers_arr):
    answer = randomize_phrases(answers_arr, answers_arr[1], None)
    return answer

########################################################################
# Main Module #
########################################################################

def answer(uin):
    answer_arr = get_answer_from_json(uin)
    if answer_arr != None:
        return choose_answer(answer_arr)
    else:
        used_fallback = done_responses["fallbacks"]
        return randomize_phrases(
                    fallbacks,
                    fallbacks[0],
                    None
                )