import os
import json

from warfle.cli.utils import (
  color_print,
  create_path,
  read_config_file
)


def init() -> None:
  """Creates .warfle file for store configurations"""

  try:
    save_name = ".warfle"
    target_path = os.path.join(os.getcwd(), save_name)

    config_file = read_config_file()
    public_key = input("Enter your public key: ")
    config_file["public"] = public_key

    with open(target_path, "a") as config:
      config.write(json.dumps(config_file))
      
    stdout = create_path("./texts/init.warfle")
    color_print(stdout, color = "green", attrs = ["reverse"])

  except Exception as e:
    raise Exception(e)
    
  return None