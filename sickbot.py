from sickbot import config
from sickbot import cli
from sickbot import knowledge_base
from collections import deque
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
        self.resetImpatience()
        self.questionQueue = deque()
    def run(self):
        while True:
            question = cli.read_question()
            if knowledge_base.is_command(question):
                knowledge_base.execute_command(question)
            else:
                self.questionQueue.append(question)
    def resetImpatience(self):
        self.lastResponseTime = time.time()
        self.impatienceLevel = 0

class Main:
    def __init__(self):
        self.kbResponse = 0

    def query(self, rspHandler):
        rspHandler(config.knowledge_base[""][self.kbResponse])
        self.kbResponse += 1
        if self.kbResponse >= len(config.knowledge_base[""]):
            self.kbResponse = 0

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

        while True:
            if not listenThread.isAlive():
                return
            if listenThread.questionQueue:
                question = listenThread.questionQueue.popleft()
                answer = knowledge_base.get_answer(question)
                cli.write_answer(answer)
                listenThread.resetImpatience()
                continue
            timeDiff = time.time() - listenThread.lastResponseTime
            if timeDiff / 10 > len(impatientResponses) + 1:
                return
            if timeDiff / 10 > listenThread.impatienceLevel + 1:
                impatientResponses[listenThread.impatienceLevel](cli.write_answer)
                listenThread.impatienceLevel += 1
            time.sleep(1)
        return

if __name__ == "__main__":
    Main().main()
