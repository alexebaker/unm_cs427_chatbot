import time
import sys

import config
import knowledge_base


def read_question():
    """Reads input from the command line.

    Does no processing of the question.

    :rtype: string
    :returns: Question read from the command line.
    """
    question = raw_input()
    knowledge_base.transcript.append(config.user_prompt + question)
    return question


def write_answer(answer):
    """Writes an answer to the command line.

    :type answer: string
    :param answer: String to write to the command line.
    """
    time.sleep(len(answer)/10 + 1)
    print config.bot_prompt + answer
    sys.stdout.write(config.user_prompt)
    sys.stdout.flush()
    knowledge_base.transcript.append(config.bot_prompt + answer)
    return
