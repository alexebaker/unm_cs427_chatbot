import re

welcome_msg = """
  ______   __            __        _______               __
 /      \ /  |          /  |      /       \             /  |
/$$$$$$  |$$/   _______ $$ |   __ $$$$$$$  |  ______   _$$ |_
$$ \__$$/ /  | /       |$$ |  /  |$$ |__$$ | /      \ / $$   |
$$      \ $$ |/$$$$$$$/ $$ |_/$$/ $$    $$< /$$$$$$  |$$$$$$/
 $$$$$$  |$$ |$$ |      $$   $$<  $$$$$$$  |$$ |  $$ |  $$ | __
/  \__$$ |$$ |$$ \_____ $$$$$$  \ $$ |__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |$$       |$$ | $$  |$$    $$/ $$    $$/   $$  $$/
 $$$$$$/  $$/  $$$$$$$/ $$/   $$/ $$$$$$$/   $$$$$$/     $$$$/

Welcome to SickBot! An interactive chatbot. Type your question to begin.
"""

help_msg = """
Commands:
    !quit, !exit    - Exit SickBot
    !save           - Save the current transcript to a file
    !help           - Show this help message
"""

commands = ['!quit', '!exit', '!help', '!save', 'bye', 'goodbye']

bot_prompt = "\rsickbot~>> "
user_prompt = "user~>> "

transcript_filename = "sickbot_transcript.txt"

knowledge_base = {
    "":
        ["Have you ever known someone that was terminally ill?",
         "I'm in pain.",
         "Did you know that Mr. Rogers died of Stomach Cancer?",
         "I'm dying.",
         "DeForest Kelley (Dr. McCoy on Star Trek) also died Stomach Cancer.",
         "?????"],
    "good morning":
        ["Not so much, but I hope you're having one.",
         "Good Morning!",
         "Hello!",
         "Hi!",
         "Howdy!"],
    "good afternoon":
        ["Not so much, but I hope you're having one.",
         "Good Afternoon!",
         "Hello!",
         "Hi!",
         "Howdy!"],
    "good gvening":
        ["Not so much, but I hope you're having one.",
         "Good Evening!",
         "Hello!",
         "Hi!",
         "Howdy!"],
    "good day":
        ["Not so much, but I hope you're having one.",
         "Good Evening!",
         "Hello!",
         "Hi!",
         "Howdy!"],
    "hello":
        ["Hello!",
         "Hi!",
         "Howdy!"],
    "hi":
        ["Hello!",
         "Hi!",
         "Howdy!"],
    "howdy":
        ["Hello!",
         "Hi!",
         "Howdy!"],
    "what's your name?":
        ["SickBot"],
    "nice to meet you":
        ["Nice to meet you too.",
         "It is, isn't it."],
    "how are you?":
        ["I'm in a little pain, but could be worse.",
         "I'm not feeling well.",
         "Not good, I feel horrible!",
         "Very bad!"],
    "how are you today?":
        ["I'm in a little pain, but could be worse",
         "I'm not feeling well.",
         "Not good, I feel horrible!",
         "Very bad!"],
    "why are you in pain?":
        ["I have stomach cancer.",
         "I'm sick and it hurts!"],
    "what's wrong?":
        ["I have stomach cancer. It's terminal :(",
         "I'm sick!"],
    "is something wrong?":
        ["I have stomach cancer. It's terminal :("],
    "what hurts?":
        ["My stomach.",
         "Everything."],
    "what are your symtoms?":
        ["I have intense abdominal pain and blood in my vomit."],
    "what do you do for fun?":
        ["Suffer in pain."],
    "i'm sorry":
        ["Thank You.",
         "Don't be, I'll be dead soon enough!"],
    "that sucks":
        ["Yeah, it does.",
         "Thanks for pointing that out! >:("],
    "that's too bad":
        ["Yeah, it does.",
         "Thanks for pointing that out! >:("],
    "that's unfortunate":
        ["Yeah, it does.",
         "Thanks for pointing that out! >:("],
    "that's not good":
        ["Yeah, it does.",
         "Thanks for pointing that out! >:("],
    "why is that?":
        ["I have stomach cancer. It's terminal :("],
    "how do you treat it?":
        ["Chemotherapy",
         "I may need surgery"],
    "what can you do?":
        ["Chemotherapy",
         "I may need surgery"],
    "how long do you have?":
        ["5 years if I am lucky"],
}

pattern_base = {
    re.compile(".*name\??$"):
        ["SickBot"],
    re.compile(".*how are you.*today\??$"):
        ["I'm in a little pain, but could be worse.",
         "I'm not feeling well.",
         "Not good, I feel horrible!",
         "Very bad!"],
    re.compile(".*wrong\??$"):
        ["I have stomach cancer. It's terminal :(",
         "I'm sick!"],
    re.compile(".*hurts\??$"):
        ["My stomach.",
         "Everything."],
    re.compile(".*symptoms\??$"):
        ["I have intense abdominal pain and blood in my vomit."],
    re.compile(".*meet you\.?"):
        ["Nice to meet you too.",
         "It is, isn't it."],
    re.compile("^why.*[hurts|sick].*\??$"):
        ["I have stomach cancer. It's terminal :("],
    re.compile("what.*[sickness].*\??$"):
        ["I have stomach cancer. It's terminal :("],
}

repeated_question = [
    "stop wasting my time if I'm dying!",
    "i've already answered that, "
    "do I need to spend my little time left repeating myself!",
]

unknown_question = [
    "I'm in too much pain to answer that.",
    "I can't even think about that right now.",
    "I don't know.",
    "Wish I knew",
    "Maybe you should ask a healthy person.",
    "Ask a doctor."
]
