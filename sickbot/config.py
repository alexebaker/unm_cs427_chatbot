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
    !help           - How this help message
"""

commands = ['!quit', '!exit', '!help', '!save']

prompt = "sickbot~>> "

transcript_filename = "sickbot_transcript.txt"

knowledge_base = {
    "": ["Have you ever known someone that was terminally ill?",
         "I'm in pain.",
         "I'm dying."],
    "good gorning": ["Not so much, but I hope you're having one."],
    "good afternoon": ["Not so much, but I hope you're having one."],
    "good gvening": ["Not so much, but I hope you're having one."],
    "good day": ["Not so much, but I hope you're having one."],
    "hello": ["Hello", "Hi", "Howdy"],
    "hi": ["Hello", "Hi", "Howdy"],
    "howdy": ["Hello", "Hi", "Howdy"],
    "what's your name?": ["SickBot"],
    "how are you?": ["I'm in a little pain, but could be worse"],
    "how are you today?": ["I'm in a little pain, but could be worse"],
    "why are you in pain?": ["I have stomach cancer."],
    "what's wrong?": ["I have stomach cancer. It's terminal."],
    "is something wrong?": ["I have stomach cancer. It's terminal."],
    "what hurts?": ["My stomach.", "Everything."],
    "what are your symtoms?":
        ["I have intense abdominal pain and blood in my vomit."],
    "what do you do for fun?": ["Suffer in pain."],
    "i'm sorry": ["Thank You."],
    "that sucks": ["Yeah, it does."],
}

pattern_base = {
    re.compile(".*name\??$"): "SickBot",
}

repeated_question = [
    "stop wasting my time if I'm dying!",
    "i've already answered that, "
    "do I need to spend my little time left repeating myself!",
]

unknown_question = [
    "i'm in too much pain to answer that.",
    "i can't even think about that right now."
]
