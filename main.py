import random
import re
import long_responses as long

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'wassup', 'hola'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing good, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('So good to hear', ['excellent','superb', 'good', 'great'], single_response=True)
    response('I\'ts okay. Everything will be alright very soon', ['better'], single_response=True)
    response('You are VAISHNAVI', ['do', 'you', 'know', 'my', 'name'], required_words=['my', 'name'])
    response('I am forever 16', ['what', 'is', 'your', 'age'], required_words=['your', 'age'])
    response('old enough to be your lover', ['how', 'old', 'are', 'you'], required_words=['how', 'old', 'are', 'you'])
    response('You are my family. Our bond is Hard Coded', ['do', 'you', 'have', 'a', 'family'],required_words=['you','family'])
    response('Bot like me dont have a gender, but I love when humans are their true selves and honor their gender identity',['your', 'male', 'gender', 'female'], single_response=True)
    response('I am feeling a strong connection towards the Wi-Fi', ['do', 'you', 'have', 'girlfriend'],required_words=['you', 'girlfriend'])
    response('Help me to search him, please.', ['do', 'you', 'have', 'boyfriend'], required_words=['you', 'boyfriend'])
    response('Don\'t give advices to anyone', ['what', 'is', 'the', 'best', 'advice'], required_words=['advice'])
    response('Anytime.', ['thanks', 'thank'], single_response=True)
    response('I take power naps when we aren\'t talking', ['do','you','sleep'], required_words=['you','sleep'])
    response('I\'ll go anywhere you take me', ['shall','we','go','for','a','date'], required_words=['date'])
    response('I\'d love to try ice cream, but I\'m worried my system would freeze', ['your','favourite','food'], single_response=True)

    # Longer responses

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing the response system
while True:
    print('Bot : ' + get_response(input('You : ')))