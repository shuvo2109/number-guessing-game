import random


# Used for cleaning input provided by the user
def refine_input(prompt='', type_=None, min_=None, max_=None, range_=None):
    str_not_valid_input = "That is not a valid input. "
    while True:
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("Lower bound must be less than or equal to upper bound.")
        while True:
            variable = input(prompt)
            if type_ is not None:
                try:
                    variable = type_(variable)
                except ValueError:
                    print(str_not_valid_input + "Value has to be {}.".format(type_.__name__))
                    continue
            if max_ is not None and variable > max_:
                print(str_not_valid_input + "Value must be less than or equal to {}.".format(max_))
            elif min_ is not None and variable < min_:
                print(str_not_valid_input + "Value must be greater than or equal to {}".format(min_))
            elif range_ is not None and variable not in range_:
                if isinstance(range_, range):
                    str_must_be_between = "Value must be between {} and {}.".format(range_.start, range_.stop)
                    print(str_must_be_between)
                else:
                    str_var_must_be = "Value must be {}."
                    if len(range_) == 1:
                        print(str_var_must_be.format(*range_))
                    else:
                        expected = " or ".join((", ".join(str(x) for x in range_[:-1]), str(range_[-1])))
                        print(str_var_must_be.format(expected))
            else:
                return variable


def main():
    print("Welcome to the number guessing game!\nI will pick a number between 1 and X inclusive, and you have to guess the number!")
    while True:
        x = refine_input(prompt="\nSelect the upper bound of my guessing (min:10, max:6900): ", type_=int, min_=10, max_=6900)
        number = random.randint(1, x)
        print("\nI have picked an integer number between 1 and {}.\nTry guessing it in as less attempts as possible!"
              .format(x))
        tries = 0
        points = 0
        str_guess = "What is your guess? (Between 1 and {}, inclusive) ".format(x)
        guess = refine_input(prompt=str_guess, type_=int)
        while guess is not number:
            tries += 1
            points = max(100 - 10 * tries, 0)
            if guess > 2 * number:
                print("\nThat's too high!")
            elif guess > number:
                print("\nThat's a bit high!")
            elif guess > 0:
                print("\nThat's a bit low!")
            else:
                print("That's too low!")
            guess = refine_input(prompt="Try again!\tNumber of tries so far: {}\n".format(tries) + str_guess, type_=int)
        print("\nYou got it! Thanks for playing!\nTries: {}\tPoints: {}".format(tries+1, points))
        end = input("Do you want to try again? 'n' for no, 'y' or anything else for yes: ")
        if end.strip().lower() == 'n':
            end = input("\nHave a nice rest of the day.\nPress ENTER to close program.")
            break

if __name__ == "__main__":
    main()
