import random

MINIMUM_SCORE = 0
PASS_SCORE = 50
HIGH_SCORE = 90
MAXIMUM_SCORE = 100


def main():
    number_of_score = int(input("Number of score: "))
    for score in range(number_of_score):
        score = get_random_score()
        print(classify_scores(score))


def get_random_score():
    """using the random method to get the random score"""
    return random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)


def classify_scores(score):
    """identified the level of score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score > HIGH_SCORE:
        return f" {score} is Excellent"
    elif score > PASS_SCORE:
        return f" {score} is Passable"
    else:
        return f" {score} is bad"


main()
