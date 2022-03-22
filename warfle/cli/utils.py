import os
import json
from pathlib import Path
from termcolor import colored


def read_config_file():
  config_path = os.path.join(Path(__file__).parent, f"./config.json")
  with open(config_path, "r") as config_file:
    return json.loads(config_file.read())


def create_path(file: str) -> str:
  """Returns dynamic path of the file"""
  parent = Path(__file__).parent
  path = os.path.join(parent, file)

  return path
  

def read_warfle_text(path: str) -> str:
  """Returns text from *.warfle files"""
  try:
    with open(path, "r") as text:
      return text.read()

  except Exception as e:
    raise Exception(e)
  

def color_print(path: str, color = "white", attrs = []) -> None:
  """Prints colorized text on terminal"""

  colored_text = colored(
    text = read_warfle_text(path),
    color = color, 
    attrs = attrs
  )

  print(colored_text)
  return None

