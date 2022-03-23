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
    
    if "requirements.txt" in os.listdir():
      with open("./requirements.txt", "r") as dep:
        dependency_list = dep.readlines()
        all_dependencies = list(map(lambda x: x.replace("\n", ""), dependency_list))
        return all_dependencies
        
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
    cls.url = "https://www.github.com/egesabanci/warfle"
    cls.description = "Easy to use command line deployer for smart contracts."
    cls.long_description = cls.get_readme()
    cls.long_description_content_type = "text/markdown"
    cls.license = "MIT"
    cls.name = "warfle-deploy-cli"
    cls.version = "1.0.0"
    cls.packages = find_packages()
    cls.install_requires = cls.get_dependencies()
    cls.include_package_data = True
    cls.package_data = {"texts": ["*"]}
    cls.entry_points = dict(console_scripts = cls.get_console_scripts())
    cls.classifiers = [
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.8",
    ]

    return cls


if __name__ == "__main__":
  package = PackageInfo.get_package()
   
  setup(
    author = package.author,
    author_email = package.author_email,
    url = package.url,
    description = package.description,
    long_description_content_type = package.long_description_content_type,
    long_description = package.long_description,
    license = package.license,
    name = package.name,
    version = package.version,
    packages = package.packages,
    install_requires = package.install_requires,
    entry_points = package.entry_points,
    classifiers = package.classifiers,
    include_package_data = package.include_package_data,
    package_data = package.package_data
  )