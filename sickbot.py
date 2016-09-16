from sickbot import config
from sickbot import cli
from sickbot import knowledge_base
import thread
import threading
import time
import sys

class ListenThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.daemon = True
        self.lastResponseTime = time.time()
    def run(self):
        while True:
            question = cli.read_question()
            self.lastResponseTime = time.time()
            if knowledge_base.is_command(question):
                knowledge_base.execute_command(question)
            else:
                answer = knowledge_base.get_answer(question)
                cli.write_answer(answer)

def main():
    print config.welcome_msg
    listenThread = ListenThread(1, "Thread-1", 1)
    listenThread.start()

    while True:
        timeDiff = time.time() - listenThread.lastResponseTime
        if timeDiff >= 121:
            return
        if timeDiff >= 120:
            cli.write_answer("Bye")
            time.sleep(121 - timeDiff)
            continue
        if timeDiff >= 105:
            cli.write_answer("I'm going to leave")
            time.sleep(120 - timeDiff)
            continue
        if timeDiff >= 90:
            cli.write_answer("Sigh...")
            time.sleep(105 - timeDiff)
            continue
        if timeDiff >= 75:
            cli.write_answer("Hello?")
            time.sleep(90 - timeDiff)
            continue
        if timeDiff >= 60:
            cli.write_answer("Are you still there?")
            time.sleep(75 - timeDiff)
            continue
        if timeDiff >= 45:
            cli.write_answer(config.knowledge_base[""][2])
            time.sleep(60 - timeDiff)
            continue
        if timeDiff >= 30:
            cli.write_answer(config.knowledge_base[""][1])
            time.sleep(45 - timeDiff)
            continue
        if timeDiff >= 15:
            cli.write_answer(config.knowledge_base[""][0])
            time.sleep(30 - timeDiff)
            continue
        time.sleep(15 - timeDiff)
    return


if __name__ == "__main__":
    main()
