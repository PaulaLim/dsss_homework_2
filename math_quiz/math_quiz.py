import random, math


def createRandomNumber(min, max):
    """
    Create a random integer number between a given min and max value.

    Args:
        min (int): The lower border of the interval to choose a random integer from.
        max (int): The upper border of the interval to choose a random integer from.

    Returns:
        int: The randomly chosen number out of the provided interval.

    Raises:
        ValueError: If min is greater than max.

    Examples:
        >>> createRandomNumber(0,10)
        1
        >>> createRandomNumber(75,100)
        95
    """
    try:
        # Round min up if it’s a decimal, round max down if it’s a decimal.
        min = math.ceil(min) if isinstance(min, float) else min
        max = math.floor(max) if isinstance(max, float) else max

        # Check if min is greater than max.
        if min > max:
            raise ValueError("The 'min' value cannot be greater than the 'max' value.")

        # Create a random integer number between given min and max value.
        return random.randint(min, max)
    
    except ValueError as e:
        # Handle the ValueError exception.
        print(e)


def chooseRandomOperation():
    """
    Choose a mathematical operator out of +, - or *.

    Args: 
        This function does not take any arguments.

    Returns:
        string: The randomly chosen mathematical operation.

    Raises:
        This function does not raise any errors.

    Examples:
        >>> chooseRandomOperator()
        '*'
        >>> chooseRandomOperator()
        '-'
    """
    # Randomly choose one of the three given mathematical operations.
    return random.choice(['+', '-', '*'])


def performOperation(number1, number2, operation):
    """
    Perform the mathematical operation consisting of two numbers and an operator.

    Args: 
        number1 (int): First given number for the operation.
        number2 (int): Second given number for the operation.
        operation (string): Given operator that defines the type of calculation.

    Returns:
        string: The composed mathematical problem.
        int: The result of the performed calculation.

    Raises:
        This function does not raise any errors.

    Examples:
        >>> performOperation(2, 4, '*')
        '2 * 4 8'
        >>> performOperation(10, 9, '-')
        '10 - 9 1'
    """
    # Compose the problem out of the two given numbers and the operation.
    problem = f"{number1} {operation} {number2}"
    # Check given operation and perform calculation
    if operation == '+': answer = number1 + number2
    elif operation == '-': answer = number1 - number2
    else: answer = number1 * number2
    # Return the composed problem and the associated solution.
    return problem, answer

def math_quiz():
    """
    Presenting a mathematical quiz with several rounds, during which the player is intended to give answers that create a final score.

    Args: 
        This function does not take any arguments.

    Returns:
        This function does not return anything.

    Raises:
        This function does not raise any errors.

    Examples:
        >>> chooseRandomOperator()
        '*'
        >>> chooseRandomOperator()
        '-'
    """
    # Counts correct answers.
    score = 0
    # Defines the number of rounds.
    rounds = 3

    # Welcome the player and explain the game.
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Iterates through the number of rounds.
    for _ in range(rounds):
        # In each round: create random numbers and associated operation.
        number1 = createRandomNumber(1, 10); 
        number2 = createRandomNumber(1, 5.5); 
        operation = chooseRandomOperation()
        
        # Formulate the problem and calculate right answer.
        PROBLEM, ANSWER = performOperation(number1, number2, operation)
        # Show the problem to the player.
        print(f"\nQuestion: {PROBLEM}")
        # Ask the player to input an answer.
        useranswer = input("Your answer: ")
        # Convert string into integer.
        useranswer = int(useranswer)

        # Check correctness of the given answer.
        if useranswer == ANSWER:
            # Let the player know that the given answer was correct.
            print("Correct! You earned a point.")
            # Add one point to the existing score.
            score += 1
        else:
            # Let the player know that the given answer was incorrect.
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    # If all rounds were played, let the player know that the game is over and tell the final score.
    print(f"\nGame over! Your score is: {score}")

if __name__ == "__main__":
    math_quiz()
