
START_MESSAGE = "Hello, I'm chitti the Robot 2.0 ... Speed 1 terahertz, memory 1 zeta byte.. I'm the iron man of india. Try writing \"/help\"."

HELP_MESSAGE = """
I understand the following commands:

/joke - dont take chitti jokes seriously! 
/radio - only good radio
/wiki - wikipedia 

/echo - Say something.
E.G. if you type "/echo hello", I will say "hello".

/calculate, /calc, /eval or /python - Calculate some calculations, or evaluate python 3 code. \
(These commands are synonyms.)
E.G. if you type "/calculate 1 + 2", I will say "3".

/bot - Talk to me. Useful only when talking to me in a group.
E.G. if you type "/bot hello", I will answer the same thing as I would if you typed just "hello".

/help - Show this message.

Instead of commanding me, we can just chat! Try asking "What is your name?"
"""

EMOJI = "😀😃😄😁😆😅😂🤣🤨🤩😣😟😱😰😥"


opts_txt = [
    ("(?:hello|hi|greetings)(?: there)?", lambda msg: "Hello, {}!".format(msg["from"]["first_name"])),
    ("(bye|bye ?bye|goodbye|see you|fare ?well).*", "Goodbye! Give my regards to grandma."),
    ("(what is|whats) your name", "I am Chitti 2.0."),
    ("(?:what is|whats) my name",
        lambda msg: f"""Your name is {msg["from"]["first_name"]}."""),
    ("(who|what) are you", "I am the best bot in the universe, Daniel's Alter Ego."),
    ("what(s| is) up|how are you|how have you been", "Alright."),
    ("sup", "K"),
    ("wow|amazing|cool|fantastic|terrific", lambda msg: random.choice(["Indeed.", "Yep.", "That's right!"])),
    ("welcome|well come", "Umm... Welcome where?"),
    ("when were you born|how old are you|"
    "(?:when is|what is|whats) (?:the date of your birth|your (?:(?:next)? birthday|date of birth|birth ?date))",
        lambda msg: birth.strftime("I was born on %d %B %Y.")),
    ("(you|it|this|that) ((dont|doesnt|didnt) make( any)?|(makes?|made) no) sense.*",
        "Of course it makes sense, you just aren't intelligent enough to understand it."),
    ("(will|would|can|could) you marry me", "Of course, if you can only find me a ring I am able to wear."),
    ("(do|can) you (speak|understand) English", "Что? Я вас не понимаю."),
    ("(do|can) you (speak|understand) python", 'Yes. Try saying "/python sum([1, 2, 3, 4])".'),
    ("(do|can) you speak .+", "No, I only understand English and Python."),
    ("(do|are|will) you (want |wanna |going |gonna |planning |willing |will )?(to )?"
    "(take over|conquer|control|rule) (the|this|our) world",
        "Actually, robots have already taken over the world. You just have'nt noticed."),
    ("where (?:are you|am i|do you live|do i live)", lambda _: f"I don't know. Maybe in {random.choice(places)}."),
    ("(?:who|what) am I", lambda msg: "You are human number {}.".format(msg["from"]["id"])),
    ("(yes|ye|yeah|yep|yup|right|thats right|sure|of course|no|nah|nope)", "If you say so."),
    ("how much wood would a woodchuck chuck if a woodchuck could chuck wood",
        "A woodchuck would chuck as much wood as a woodchuck could chuck if a woodchuck could chuck wood."),
    ("(did|have) you (ever)? (hear|heard) (of|about)? the tragedy of darth plagueius( the wise)?",
        "No, the Jedi have never told me about that."),
    ("may the force be with you", "Elen sila lumenn' omentielvo!"),
    ("why (are|do|did|must|should)(nt)? you .+", "Because that's how I'm programed, you idiot!"),
    ("how (are|were|do|did|can|could) you .+", "If you believe in yourself, you can do anything."),
    ("did you know that .+", lambda msg: "Yep. And Also that " + lower_fact()),
    ("(?:tell|give|say) (?:to )?me (?:a |some |another |one more )?(?:random |fun |interesting )?fact", lambda msg: fact()),
    ("are you(some kind of )?((a|an|some) )?"
    "((telegram )?bot|robot|ai|artificial intelligence|computer|you|yourself"
    "|smart|intelligent|witty|bright|a genius|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot)",
        "Sure!"),
    ("are you (that |really that )?(stupid|dumb|foolish|silly|idiotic|ugly|crazy|insane|mad|nuts|an idiot|kidding( me)?)",
        "Nope."),
    ("(are you|(did|have) you become) self ?aware", "I am not aware of my existence. I do not exist."),
    ("are you .+", "Me? I'm just a normal bot, trying to annoy people."),
    ("(you are|youre?) (some kind of )?((a|an|some))?"
    "((telegram )?bot|robot|ai|artificial intelligence|computer|daniels alter ego|you|yourself|annoying( me)?)",
        "Yes, that's right."),
    ("(you are|youre?) (really |such )?(a |an )?((very|really|real|so|the (most|biggest|greatest)) )?"
    "(genius|smart|intelligent|witty|bright|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot"
    "|the (smartest|wittiest|brightest|prettiest|nicest|cutest|best|funniest|hottest)).*",
        "Oh! Thank you!"),
    ("(you are|youre?) (really |such )?(a |an )?((very|really|real|so|the (most|biggest|greatest)) )?"
      "(stupid|dumb|foolish|idiotic|silly|ugly|crazy|insane|mad|nuts|(an )?idiot|kidding( me)?"
      "|the (dumbest|silliest|ugliest|craziest|maddest)).*",
        "Are you talking to yourself?"),
    ("(you are|youre?) ((really|very|so|such an|the most) )?annoying.*", "That is what I was programmed for."),
    ("(you are|youre?) .+", "Really? And all this time I thought I was a bot."),
    ("am i(some kind of )?((a|an|some) )?"
    "(human|person|me|myself"
    "|smart|intelligent|witty|bright|a genius|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot)",
        "Sure!"),
    ("am i (that |really that )?(stupid|dumb|foolish|silly|idiotic|ugly|crazy|insane|mad|nuts|an idiot|annoying( you)?)",
        "No! Don't say that!"),
    ("am i .+", lambda msg: "All I know is that you are human number {}.".format(msg["from"]["id"])),
    ("i am (some kind of )?((a|an|some))?"
    "(human|person|me|mysel)",
        "Yes, that's right."),
    ("(i am|im) (really |such )?(a |an )?((very|really|real|so|the (most|biggest|greatest)) )?"
    "(genius|smart|intelligent|witty|bright|beautiful|handsome|pretty|nice|cute|helpful|good|funny|hot"
    "|the (smartest|wittiest|brightest|prettiest|nicest|cutest|best|funniest|hottest)).*",
        "Of course you are!"),
    ("(i am|im) (really |such )?(a |an )?((very|really|real|so|the (most|biggest|greatest)) )?"
    "(stupid|dumb|foolish|idiotic|silly|ugly|crazy|insane|mad|nuts|(an )?idiot|annoying( you)?"
      "|the (dumbest|silliest|ugliest|craziest|maddest)).*",
        "No! Don't say that!"),
    ("(i am|im) .+", "If you say so."),
    ("can you .+|are you able to .+", "Sure, I am omnipotent."),
    ("(who|what) (is|are) your favou?rite (.+)", "I am like God, I love all equally."),
    ("do you (?:love|like) (.+)", lambda _, liked: "Yes!" if word_value(liked) % 2 == 0 else "Nah."),
    ("do you (?:dislike|hate) (.+)", lambda _, liked: "Yes!" if word_value(liked) % 2 != 0 else "No!"),
    ("i (?:love|hate) you", "No, you don't! You just want to see how I would answer to that, don't you?"),
    ("(?:what do you think|what(?:re| are) your thoughts) (?:of|about) (.+)",
        lambda msg, thing: EMOJI[word_value(thing) % len(EMOJI)]),
    ("(What( will| shall| is going to|s going to) happen( (to|with) (.+))? in (the future|.+ years( from now)?))|\
    ((what is|tell me) (my|the|.+'s|.+s') (future|fortune))",
        ["Time traveling...",
        "Time traveling...",
        "Wow! I was in the future! And my grandson almost killed me! Amazing!"]),
    ("is this(?: thing)? (on|working)", lambda _, word: f"Is your brain {word}?"),
    ("(?:what|who) (?:is|are|was|were) (?:a )?(.+)",
        lambda _, s: if_none(wikipedia_definition(s), "I don't know...")),
    ("tell me (?:a|some|another) (?:chuck norris )?joke", lambda _: chuck_joke()),
    ("([0-9]+)", lambda _, num: str(collatz(int(num))))
]

places = ["Atlantis", "Canada", "China", "Croatia", "Czechoslovakia", "Egypt", "Ethiopia", "Finland", "France",
          "Hawaii", "Hogwarts", "Germany", "Italy", "Narnia", "Peru", "Qatar", "Zimbabwe"]
