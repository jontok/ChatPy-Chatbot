from http.client import responses
from randomizer import randomize_phrases
from json_parser import parse_to_var

file = "data.json"

done_phrases = parse_to_var(file, "done_phrases")
responses = done_phrases["responses"]

responses = parse_to_var(file, "responses")
fallbacks = responses["fallbacks"]



# def get_answer_from_json(uin):
    
#     return

def answer(uin,response):
    i = uin
    print(response)
    if "who" and "build" and  "you" in uin:
        used_answer = responses["answers"]
        randomize_phrases(response["answer"],response["answer"][0],used_answer)
    else:
        used_fallback = responses["fallbacks"]
        return randomize_phrases(
                        fallbacks,
                        fallbacks[0],
                        used_fallback
                    )