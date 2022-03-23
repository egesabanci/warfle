<div align = "center" style = "width: 250px; height: auto;">
  <img src = "https://raw.githubusercontent.com/egesabanci/warfle/master/assets/warfle-logo.png?token=GHSAT0AAAAAABMKUTO2SAO7QKJK6OBB5EHGYSED6IA" />
</div>

<div style = "display: flex;">
  <img src = "https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
  <img src = "https://img.shields.io/badge/Solidity-e6e6e6?style=for-the-badge&logo=solidity&logoColor=black" />
</div>

# Overview
Warfle is an easy-to-use command-line interface for deploying smart contracts without any deep configurations.

### Important Note
In the current version, ``Warfle does not supports the public mainnet or testnet deployment`` but in the further versions, We will add this feature.

# Installation
Install from the with the ``setup`` file of the project:
```
>>> git clone https://www.github.com/egesabanci/warfle
```
```
>>> cd warfle/
>>> pip install .
```

# Example Usage
Let's say, we have a following smart contract:

```solidity
// Test.sol

pragma solidity >=5.0.1;

contract Test {
  string public greet;

  function setGreet(string memory text) public returns (bool) {
    greet = text;
    return true;
  }

  function greet() public view returns (string) {
    return greet;
  } 
}
```

###### Step 1:
Now, We want to deploy that contract with ``Warfle``. Firstly we need to initialize ``Warfle`` to the current working folder:

```
>>> warfle init
```
This command will create a ``.warfle`` configuration file to the current path. ``.warfle`` file contains:

```
{
	"rpc": "http://127.0.0.1:7545",
	"public": <YOUR WALLET PUBLIC KEY>
}
```

###### Step 2 (Optional):
If we want to update the configurations, We can simple use the ``warfle update`` command.

**Example usage:**
```
>>> warfle update KEY
```
``key`` argument must be ``rpc`` or ``public``. You can not add any other argument to the ``.warfle`` configuration file.

###### Step 3:
Then, We need to compile our smart contract with the ``warfle compile`` command. This command will create a new ``source`` folder to the current path. ``./source`` will contains 2 files: ``ABI of the contract (*.abi)`` and ``Bytecode of the contract (*.bin)``. In our case, ``./source`` will contains: ``Test.abi`` and ``Test.bin``:


**Example:**
```
>>> warfle compile Test.sol
```

###### Step 4:
Now, We are ready to deploy our contract with the ``warfle deploy`` command:
```
>>> warfle deploy <PATH TO ABI> <PATH TO BIN>
```
In our case:
```
>>> warfle deploy source/Test.abi source/Test.bin
```

# License
[MIT](https://github.com/egesabanci/warfle/blob/master/LICENSE.md) © Ege Sabanci egesabanci@outlook.com.tr