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
    if "requirements.txt" in os.listdir(os.path.abspath("./")):
      with open(os.path.abspath("./requirements.txt"), "r") as dep:
        dependency_list = dep.readlines()
        all_dependencies = list(map(lambda x: x.replace("\n", ""), dependency_list))
        return list(map(lambda x: x[:x.index("=")], all_dependencies)).append("warfle")
        
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
    cls.license = "MIT"
    cls.name = "warfle"
    cls.version = "0.0.1"
    cls.packages = find_packages()
    cls.install_requires = cls.get_dependencies()
    cls.entry_points = dict(console_scripts = cls.get_console_scripts())

    return cls


if __name__ == "__main__":
  package = PackageInfo.get_package()
   
  setup(
    author = package.author,
    author_email = package.author_email,
    description = package.description,
    long_description = package.long_description,
    license = package.license,
    name = package.name,
    version = package.version,
    packages = package.packages,
    install_requires = package.install_requires,
    entry_points = package.entry_points,
  )