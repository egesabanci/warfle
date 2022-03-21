from fire import Fire
from warfle.cli.commands import *


def main() -> None:
  Fire(dict(
    init = init
  ))
  
  return None