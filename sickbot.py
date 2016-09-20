import threading
import time
import sys

from collections import deque

from sickbot import config
from sickbot import cli
from sickbot import knowledge_base


class ListenThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.daemon = True
        self.questionQueue = deque()

    def run(self):
        while True:
            question = cli.read_question()
            sys.stdout.write(config.user_prompt)
            sys.stdout.flush()
            if knowledge_base.is_command(question):
                knowledge_base.execute_command(question)
            else:
                self.questionQueue.append(question)


class Main(object):
    def __init__(self):
        self.kbResponse = 0

    def query(self, rspHandler):
        rspHandler(config.knowledge_base[""][self.kbResponse])
        self.kbResponse += 1
        if self.kbResponse >= len(config.knowledge_base[""]):
            self.kbResponse = 1

    def main(self):
        print config.welcome_msg
        sys.stdout.write(config.user_prompt)
        sys.stdout.flush()
        listenThread = ListenThread(1, "Thread-1", 1)
        listenThread.start()
        impatientResponses = [
            self.query
          , self.query
          , self.query
          , lambda rspHandler:
                rspHandler("Are you still there?")
          , lambda rspHandler:
                rspHandler("Hello?")
          , lambda rspHandler:
                rspHandler("Sigh...")
          , lambda rspHandler:
                rspHandler("I'm going to leave")
          , lambda rspHandler:
                rspHandler("Bye")
        ]
        lastResponseTime = time.time()
        impatienceLevel = 0

        while True:
            if not listenThread.isAlive():
                return
            if listenThread.questionQueue:
                question = listenThread.questionQueue.popleft()
                answer = knowledge_base.get_answer(question)
                cli.write_answer(answer)
                lastResponseTime = time.time()
                impatienceLevel = 0
                continue
            timeDiff = time.time() - lastResponseTime
            if timeDiff >= 10:
                impatientResponses[impatienceLevel](cli.write_answer)
                impatienceLevel += 1
                if len(impatientResponses) <= impatienceLevel:
                    time.sleep(1)
                    # exit with a somewhat cleaner CLI prompt
                    sys.stdout.write("\n")
                    sys.stdout.flush()
                    return
                lastResponseTime = time.time()
            time.sleep(1)
        return

if __name__ == "__main__":
    Main().main()
