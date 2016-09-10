from config import prompt


def read_question():
    """Reads input from the command line.

    Does no processing of the question.

    :rtype: string
    :returns: Question read from the command line.
    """
    question = raw_input(prompt)
    return question


def write_answer(answer):
    """Writes an answer to the command line.

    :type answer: string
    :param answer: String to write to the command line.
    """
    print prompt + answer
    return
