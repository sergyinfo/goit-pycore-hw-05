"""
Task 2: Write a function that takes a string as input 
and returns a generator that yields all real numbers in the string.
"""

def generator_numbers(text: str):
    """
    Return generator that yields all real numbers in the text.

    :param text: str
    :return: generator
    """
    for word in text.split():
        try:
            yield float(word)
        except ValueError:
            pass

def sum_profit(text: str, func: callable) -> float:
    """
    Return sum of all real numbers in the text.

    :param text: str
    :param func: callable
    :return: float
    """

    return sum(func(text))


if __name__ == "__main__":
    text_to_test = """Загальний дохід працівника складається з декількох частин:
      1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
    total_income = sum_profit(text_to_test, generator_numbers)
    print(f"Загальний дохід: {total_income}") # 1351.46
