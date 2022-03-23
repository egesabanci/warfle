from fire import Fire
from .cli import commands


def main() -> None:
  Fire(dict(
    init = commands.init,
    compile = commands.compile,
    update = commands.update,
    deploy = commands.deploy
  ))
  
  return None