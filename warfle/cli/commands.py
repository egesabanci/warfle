import os
import json

from warfle.cli.utils import (
  color_print,
  create_path,
  read_config_file
)

from warfle.compiler.compile import save_compiled_source


def init() -> None:
  """Creates .warfle file for store configurations"""

  try:
    save_name = ".warfle"
    target_path = os.path.join(os.getcwd(), save_name)

    config_file = read_config_file()
    public_key = input("Enter your public key: ")
    config_file["public"] = public_key

    with open(target_path, "w") as config:
      config.write(json.dumps(config_file))
      
    info = create_path("./texts/init.warfle")
    color_print(info, color = "green", attrs = ["reverse"])
    return None

  except Exception as e:
    raise Exception(e)
    


def compile(file: str) -> None:
  """Compiles and saves the source code to the ./source"""

  save_compiled_source(file)
  return None


def update(key: str, value: str) -> None:
  try:
    if ".warfle" not in os.listdir("./"):
      err = create_path("./texts/no-warfle.warfle")
      color_print(err, color = "red")
      return None

    with open("./.warfle", "r") as config_file:
      config = json.loads(config_file.read())

    if not key in list(config.keys()):
      err = create_path("./texts/no-key.warfle")
      color_print(err, color = "red")
      return None
      
    config[key] = value

    with open("./.warfle", "w") as config_file:
      config_file.write(json.dumps(config))  
     
    info = create_path("./texts/config-update-success.warfle")
    color_print(info, color = "green", attrs = ["reverse"])

    return None

  except Exception as e:
    raise Exception(e)