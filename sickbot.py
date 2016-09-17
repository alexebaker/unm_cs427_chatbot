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
            if knowledge_base.is_command(question):
                knowledge_base.execute_command(question)
            else:
                answer = knowledge_base.get_answer(question)
                knowledge_base.transcript.append(question)
                cli.write_answer(answer)
                self.lastResponseTime = time.time()

def main():
    print config.welcome_msg
    listenThread = ListenThread(1, "Thread-1", 1)
    listenThread.start()
    kbResponse = 0;

    while True:
        if not listenThread.isAlive():
            return
        timeDiff = time.time() - listenThread.lastResponseTime
        if timeDiff >= 121:
            return
        if timeDiff >= 120:
            answer = "Bye"
            nextResponseIn = 121
        elif timeDiff >= 105:
            answer = "I'm going to leave"
            nextResponseIn = 120
        elif timeDiff >= 90:
            answer = "Sigh..."
            nextResponseIn = 105
        elif timeDiff >= 75:
            answer = "Hello?"
            nextResponseIn = 90
        elif timeDiff >= 60:
            answer = "Are you still there?"
            nextResponseIn = 75
        elif timeDiff >= 45:
            answer = config.knowledge_base[""][kbResponse]
            kbResponse += 1
            if kbResponse >= len(config.knowledge_base[""]):
                kbResponse = 0
            nextResponseIn = 60
        elif timeDiff >= 30:
            answer = config.knowledge_base[""][kbResponse]
            kbResponse += 1
            if kbResponse >= len(config.knowledge_base[""]):
                kbResponse = 0
            nextResponseIn = 45
        elif timeDiff >= 15:
            answer = config.knowledge_base[""][kbResponse]
            kbResponse += 1
            if kbResponse >= len(config.knowledge_base[""]):
                kbResponse = 0
            nextResponseIn = 30
        else:
            time.sleep(15 - timeDiff)
            continue
        cli.write_answer(answer)
        time.sleep(nextResponseIn - timeDiff)
    return


if __name__ == "__main__":
    main()
