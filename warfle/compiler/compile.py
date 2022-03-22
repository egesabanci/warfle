import os
import json

from solcx import compile_source


def compile_solidity(filepath: str):
  """Compiles source code (Solidity)"""

  try:
    with open(filepath, "r") as sol_file:
      source = sol_file.read()
      compiled_source = compile_source(
        source,
        output_values = ["abi", "bin"]
      )

      return compiled_source

  except Exception as e:
    raise Exception(e)
  

def save_compiled_source(filepath: str) -> None:
  """Compiles source code (Solidity) and save it to the ./source folder"""

  try:
    filename = os.path.split(filepath)[-1].split(".")[0]

    compiled_source = compile_solidity(filepath)
    id, interface = compiled_source.popitem()
    
    bytecode = interface["bin"]
    abi = json.dumps(interface["abi"])

    if "source" not in os.listdir("./"):
      os.system("mkdir ./source")

    # save bytecode to the ./source folder
    with open(f"./source/{filename}.bin", "w") as file:
      file.write(bytecode)

    # save abi to the ./source folder
    with open(f"./source/{filename}.abi", "w") as file:
      file.write(abi)

    return None

  except Exception as e:
    raise Exception(e)