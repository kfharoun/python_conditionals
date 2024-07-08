def check_letter(letta):
    letter = letta.lower()
    vowels = "aeiou"
    if letter in vowels:
        return f"The letter {letta} is a vowel"
    else:
        return f"the letter {letta} is a consonant"
print(check_letter("A"))

def check_voting_eligibility():
    voting_age=18
    print("Please enter your age")
    x = input()
    y=int(x)
    if y < voting_age: 
        print("you cant vote!")
    if y>= voting_age: 
        print("you can vote!")
check_voting_eligibility()