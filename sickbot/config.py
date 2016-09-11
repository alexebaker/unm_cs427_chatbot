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
    "Good Morning": ["Not so much, but I hope you're having one."],
    "Good Afternoon": ["Not so much, but I hope you're having one."],
    "Good Evening": ["Not so much, but I hope you're having one."],
    "Good Day": ["Not so much, but I hope you're having one."],
    "Hello": ["Hello", "Hi", "Howdy"],
    "Hi": ["Hello", "Hi", "Howdy"],
    "Howdy": ["Hello", "Hi", "Howdy"],
    "What's your name?": ["SickBot"],
    "How are you?": ["I'm in a little pain, but could be worse"],
    "How are you today?": ["I'm in a little pain, but could be worse"],
    "Why are you in pain?": ["I have stomach cancer."],
    "What's wrong?": ["I have stomach cancer. It's terminal."],
    "Is something wrong?": ["I have stomach cancer. It's terminal."],
    "What hurts?": ["My stomach.", "Everything."],
    "What are your symtoms?":
        ["I have intense abdominal pain and blood in my vomit."],
    "What do you do for fun?": ["Suffer in pain."],
}

repeated_question = [
    "Stop wasting my time if I'm dying!",
    "I've already answered that, \
    do I need to spend my little time left repeating myself!",
]

unknown_question = [
    "I'm in too much pain to answer that.",
    "I cna't even think about that right now."
]
