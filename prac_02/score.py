def main():
    score = int(input("Your score? "))
    result = classify_scores(score)
    print(f"{score} is {result}")


def classify_scores(score):
    """identify the level of score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score > 90:
        result = "Excellent"
    elif score > 50:
        result = "Passable"
    else:
        result = "bad"
    return result


main()
