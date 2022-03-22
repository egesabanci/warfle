from fire import Fire
from warfle.cli.commands import *


def main() -> None:
  Fire(dict(
    init = init,
    compile = compile,
    update = update,
    deploy = deploy
  ))
  
  return None