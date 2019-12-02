import time;import os;import string;import math;import random;import re;import json;import googletrans;import urllib;import requests;import datetime
from bot_ai import *

TOKEN = os.environ.get("chitti_ai_bot")
URL = f"https://api.telegram.org/bot{TOKEN}/"
translator = googletrans.Translator()
PatternType = type(re.compile(""))
debug_password = "".join(random.choice(string.ascii_lowercase) for i in range(4))
print("Debug password: " + debug_password)
last_update_id = None
py_wait_list = []
evaled = None

radios = {"8098":"http://c5.hostingcentar.com:8098/stream.ogg",'MusicPulse':'http://rfcmedia.streamguys1.com/MusicPulse.mp3','977hits':'http://19353.live.streamtheworld.com/977_HITS_SC'}


def get_url(url):
    response = requests.get(url)
    return response.content.decode("utf8")

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += f"&offset={offset}"
    return json.loads(get_url(url))


def get_last_update_id(updates):
    return max(int(update["update_id"])
              for update in updates["result"])


def echo(update):
    text = update["message"].get("text", "(No text sent)")
    chat = update["message"]["chat"]["id"]
    send_message(chat, text)


def respond(update):
    if "message" not in update or "text" not in update["message"]:
        return

    py_chat_id = update["message"]["chat"]["id"]

    if(py_chat_id in py_wait_list):
      evaled = exec(update["message"]["text"])
      send_message(chat_id,evaled)
      py_wait_list.remove(py_chat_id)

    text = update["message"]["text"].strip()

    if text.endswith("@chitti_ai_bot"):
        text = text[:-len("@chitti_ai_bot")]

    if text.startswith("/"):
        text_parts = text[1:].split(" ", 1)
        command = text_parts[0]
        param = text_parts[1] if len(text_parts) == 2 else ""
        respond_command(update["message"], command.lower(), param)
    else:
        respond_message(update["message"])


birth = datetime.date(day=20, month=2, year=2018)

def wait_for_py(chat_id):
  py_wait_list.append(chat_id)
  




def chuck_joke():
    data = json.loads(get_url("http://api.icndb.com/jokes/random1http://api.icndb.com/jokes/random"))
    if data["type"] == "success":
        joke = data["value"]["joke"].replace("&quot;", "\"")
        return joke.replace("Chuck Norris","Chitti")
    else:
        return "something went wrong"


def fact():
    new_fact = json.loads(get_url("http://randomuselessfact.appspot.com/random.json?language=en"))
    if(new_fact["language"] == 'de'):
      return random.choice(["Try again","fact lost","no facts now","go to hell"])
    else: 
      return new_fact['text']


def lower_fact():
    s = fact()
    s = s[0].lower() + s[1:]
    return s


def word_value(word):
    return sum(ord(c) for c in word)


def respond_command(msg, command, param):
    chat_id = msg["chat"]["id"]

    if command == "start":
        send_message(chat_id, START_MESSAGE)
    elif command == "help":
        send_message(chat_id, HELP_MESSAGE)
    elif command == "stop":
        if param.lower() == debug_password:
            send_message(chat_id, "Bye!")
            exit()
        else:
            send_message(chat_id, "Nice try!")
    elif command == "echo":
        send_message(chat_id, param)
    elif command in ("calculate", "calc", "eval", "python"):
      try:
        pass
            # if(command == "python"):
            #   send_message(chat_id,"send your code now")
        print("python block")
            #   wait_for_py(chat_id)
        evaled = eval(param, {"__builtins__": {}}, SAFE_FUNCTIONS)
      except Exception as e:
        send_message(chat_id, str(e))
            # send_message(chat_id, repr(evaled))
    elif command == "bot":
        respond_message(msg)
    elif command == "radio":
      try:
        for rad in radios: 
          send_message(chat_id,str(radios[rad]))
      except Exception as e:
        send_message(chat_id,e)
    elif command == "joke":
        send_message(chat_id, chuck_joke())
    elif command == "fact":
        send_message(chat_id, fact())
    elif command == "wiki":
      try:
        send_message(chat_id, wikipedia_definition(param))
      except:
        send_message(chat_id, "no query")
    else:
        send_message(chat_id, f"I'm sorry, I don't understand the command \"{command}\".")


SAFE_FUNCTIONS = {
    "abs": abs, "round": round, "pos": pow, "divmod": divmod,
    "int": int, "float": float, "complex": complex, "bool": bool, "slice": slice,
    "str": str, "repr": repr, "ascii": ascii, "format": format, "bytes": bytes, "bytearray": bytearray,
    "list": list, "dict": dict, "set": set, "frozenset": frozenset, "tuple": tuple, "range": range,
    "map": map, "filter": filter, "sorted": sorted, "iter": iter,
    "next": next, "reversed": reversed, "enumerate": enumerate,
    "sum": sum, "min": min, "max": max, "all": all, "any": any, "len": len,
    "ord": ord, "chr": chr, "bin": bin, "oct": oct, "hex": hex,
    "globals": globals, "locals": locals, "vars": vars,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "pi": math.pi, "e": math.e, "tau": math.tau, "degrees": math.degrees, "radians": math.radians
}

GOOD_CHARS = string.ascii_letters + string.digits + " "


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n*3 + 1


def wikipedia_definition(s):
  s = s.replace(" ", "_")
  site_text = requests.get("https://en.wikipedia.org/w/api.php?action=opensearch&limit=1&search=" + s).text
  json_list = json.loads(site_text)
  if json_list[3] == []:
    return None
  else:
    return json_list[3][0]


def if_none(x, when_none):
  if x is None:
    return when_none
  else:
    return x

opts = [(re.compile(reg, re.IGNORECASE), ans) for (reg, ans) in opts_txt]

def respond_message(msg):
    line = msg["text"].strip()
    if line.startswith("/bot "):
        line = line[len("/bot "):]
    if line.endswith("@chitti_ai_bot"):
        line = line[:len("@chitti_ai_bot")]

    line_words = "".join(i for i in line if i in GOOD_CHARS)
    chat_id = msg["chat"]["id"]

    for cond, answer in opts:
        m = cond.fullmatch(line_words)
        if m:
            if isinstance(answer, (str, tuple, list)):
                send_messages(chat_id, answer)
            elif callable(answer):
                send_messages(chat_id, answer(msg, *m.groups()))
            break
    else:
        default_response(msg)


def default_response(msg):
    line = msg["text"].strip()
    if line.startswith("/bot "):
        line = line[len("/bot "):]
    if line.endswith("@daniel_alter_bot"):
        line = line[:len("@daniel_alter_bot")]
    chat_id = msg["chat"]["id"]

    rnd_response_num = random.randrange(5)
    if rnd_response_num == 0:
        send_message(chat_id, f'You have just said: "{line}".')
    elif rnd_response_num == 1:
        try:
            trans = translator.translate(line, dest="zh-TW").text
        except AttributeError:
            default_response(msg)
        else:
            send_message(chat_id, f'In Chinese that would be "{trans}".')
    elif rnd_response_num == 2:
        send_message(chat_id, "Wow! I didn't understand anything!")
    elif rnd_response_num == 3:
        num = random.choice(("Two", "Three", "Four", "Five", "Six", "Seven"))
        send_message(chat_id, f"Yes! I mean no! Ummm... {num}?")
    elif rnd_response_num == 4:
        send_message(chat_id, f"What?")


def send_message(chat_id, text):
    print(chat_id,"<<",text)
    try:
      pass
    except:
      print("log failed")
    text = urllib.parse.quote_plus(text)
    url = URL + f"sendMessage?text={text}&chat_id={chat_id}"
    get_url(url)


def send_messages(chat_id, texts):
    if isinstance(texts, str):
        send_message(chat_id, texts)
    elif isinstance(texts, (tuple, list)):
        for text in texts:
            send_message(chat_id, text)



def main():
  last_update_id = None
  evaled = None
  while True:
      new_updates = get_updates(last_update_id)
      if len(new_updates["result"]) > 0:
          last_update_id = get_last_update_id(new_updates) + 1
          for upd in new_updates["result"]:
              
              try:
                print(upd["message"]["from"]["username"],">>",upd["message"]["text"])
              except:
                print("update: ", upd)
              respond(upd)
      time.sleep(0.5)