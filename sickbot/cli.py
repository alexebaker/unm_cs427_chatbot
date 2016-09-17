import time

from config import bot_prompt, user_prompt
from sickbot import knowledge_base

def read_question():
    """Reads input from the command line.

    Does no processing of the question.

    :rtype: string
    :returns: Question read from the command line.
    """
    question = raw_input(user_prompt)
    return question


def write_answer(answer):
    """Writes an answer to the command line.

    :type answer: string
    :param answer: String to write to the command line.
    """
    time.sleep(len(answer)/10)
    print bot_prompt + answer
    knowledge_base.transcript.append(answer)
    return
