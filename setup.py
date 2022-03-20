import os
from typing import List
from setuptools import find_packages, setup


class PackageInfo:
  @staticmethod
  def get_readme() -> str:
    """Returns README text if it is exists in given path"""
    if "README.md" in os.listdir(os.path.abspath("./")):
      with open(os.path.abspath("./README.md"), "r") as readme:
        return readme.read()

    return ""


  @staticmethod
  def get_dependencies() -> List[str]:
    """Returns dependency list if it is exists in given path"""
    return [""]


  @staticmethod
  def get_console_scripts() -> List[str]:
    """Returns console scripts from ./console.scripts"""
    with open("./console.scripts", "r") as commands:
      scripts = commands.readlines()
      return list(map(lambda x: x.replace("\n", ""), scripts))


  @classmethod
  def get_package(cls):
    cls.author = "Ege Sabanci"
    cls.author_email = "egesabanci@outlook.com.tr"
    cls.description = "Easy to use command line deployer for smart contracts."
    cls.long_description = cls.get_readme()
    cls.licence = "MIT"
    cls.name = "warfle"
    cls.version = "0.0.1"
    cls.packages = find_packages() + cls.get_dependencies()
    cls.entry_points = dict(console_scripts = cls.get_console_scripts())

    return cls


if __name__ == "__main__":
  package = PackageInfo.get_package()

  setup(
    name = package.name,
    version = package.version,
    packages = package.packages
  )