import sys
import random

import config
import cli


transcript = []


def is_command(cmd):
    """Check is the given command is valid.

    :type cmd: string
    :param cmd: command to check for

    :rtype: bool
    :returns: True if the command is valid, False otherwise
    """
    return cmd in config.commands


def execute_command(cmd):
    """Executes the given command.

    :type cmd: string
    :param cmd: command to execute
    """
    if cmd in ['!quit', '!exit']:
        sys.exit(0)
    elif cmd in ['bye', 'goodbye']:
        cli.write_answer('Goodbye!')
        sys.exit(0)
    elif cmd in ['!help']:
        print config.help_msg
    elif cmd in ['!save']:
        save_transcript()
    return


def get_answer(question):
    """Gets an answer to a question.

    :type question: string
    :param question: Question to retriecve an answer for.

    :rtype: string
    :returns: An answer to the given question
    """
    answer = ""
    question = question.lower()
    botResponse = None
    for response in reversed(transcript):
        if response.startswith(config.bot_prompt):
            botResponse = response[len(config.bot_prompt):]
            break
    if botResponse == config.knowledge_base[""][0]:
        if question.startswith("no"):
            return "Then you should consider yourself lucky."
        if question.startswith("yes"):
            return "Then I'm sorry.  You know it's not pleasant."
    elif question in transcript:
        return random.choice(config.repeated_question)
    elif question in config.knowledge_base:
        return random.choice(config.knowledge_base[question])
    elif is_pattern(question):
        return pattern_answer(question)
    else:
        return random.choice(config.unknown_question)


def is_pattern(question):
    """Checks to see if there is a pattern matching the question.

    :type question: string
    :param question: Question to check for a matching pattern

    :rtype: bool
    :returns: True if the question matches a pattern, False otherwise
    """
    for regex, _ in config.pattern_base.iteritems():
        if regex.match(question):
            return True
    return False


def pattern_answer(question):
    """Get the answer to the pattern the question matches.

    :type question: string
    :param question: Question to check for a matching pattern

    :rtype: string
    :returns: Answer to the question
    """
    for regex, answers in config.pattern_base.iteritems():
        if regex.match(question):
            return random.choice(answers)
    return ""


def save_transcript():
    """Saves the current transcript to a file."""
    with open(config.transcript_filename, 'w') as f:
        for line in transcript:
            f.write("%s\n" % (line))
    return
