from http.client import responses
from chatbot import question
from randomizer import randomize_phrases
from json_parser import parse_to_var

file = "data.json"

done_phrases = parse_to_var(file, "done_phrases")
done_responses = done_phrases["responses"]

responses = parse_to_var(file, "responses")
fallbacks = responses["fallbacks"]

answers = responses["answers"]





def get_answer_from_json(uin):
    for a in answers:
        question = a["question"]
        answer = a["answer"]
        if uin == question:
            ret = answer

    

def choose_answer(answers_arr):
    answer = randomize_phrases(answers_arr, answers_arr[1], None)
    return answer

def answer(uin,response):
    i = uin
    print(response)
    if "who" and "build" and  "you" in uin:
        used_answer = responses["answers"]
        randomize_phrases(response["answer"],response["answer"][0],used_answer)
    else:
        used_fallback = done_responses["fallbacks"]
        return randomize_phrases(
                        fallbacks,
                        fallbacks[0],
                        used_fallback
                    )