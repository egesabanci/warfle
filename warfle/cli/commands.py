from warfle.cli.utils import color_print, create_path


def init() -> None:
  """Creates .warfle file for store configurations"""

  # TODO: create the configuration file
  path = create_path("./texts/init.warfle")
  color_print(path, color = "green", attrs = ["reverse"])

  return None