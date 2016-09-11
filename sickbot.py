from sickbot import config
from sickbot import cli
from sickbot import knowledge_base


def main():
    print config.welcome_msg

    while True:
        question = cli.read_question()
        if knowledge_base.is_command(question):
            knowledge_base.execute_command(question)
        else:
            answer = knowledge_base.get_answer(question)
            cli.write_answer(answer)
    return


if __name__ == "__main__":
    main()
