<div style = "width: 100vw; display: flex; align-items: center; justify-content: center;">
  <img src = "https://raw.githubusercontent.com/egesabanci/warfle/master/assets/warfle-logo.png?token=GHSAT0AAAAAABMKUTO3VF6MWN2URV45XEX2YSEBSDA">
</div>

# Overview
Warfle is an easy-to-use command-line interface for deploying smart contracts without any deep configurations.

### Important Note
In the current version, `Warfle does not supports the public mainnet or testnet deployment` but in the further versions, We will add this feature.

# Installation
###### Option 1:
Install directly from the PYPI (recommended):
```
>>> pip install warfle
```
###### Option 2:
Install from the with the `setup` file of the project:
```
>>> git clone github.com/egesabanci/warfle
```
```
>>> cd warfle/
>>> pip install .
```

# Example Usage
Let's say, we have a following smart contract:
```sol
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
Now, We want to deploy that contract with `Warfle`. Firstly we need to initialize `Warfle` to the current working folder:
```
>>> warfle init
```
This command will create a `.warfle` configuration file to the current path. `.warfle` file contains:
```json
{
	"rpc": "http://127.0.0.1:7545",
	"public": <YOUR WALLET PUBLIC KEY>
}
```

###### Step 2 (Optional):
If we want to update the configurations, We can simple use the `warfle update` command.

**Example usage:**
```
>>> warfle update KEY VALUE
```
`key` argument must be `rpc` or `public`. You can not add any other argument to the `.warfle` configuration file.

###### Step 3:
Then, We need to compile our smart contract with the `warfle compile` command. This command will create a new `source` folder to the current path. `./source` will contains 2 files: `ABI of the contract (*.abi)` and `Bytecode of the contract (*.bin)`. In our case, `./source` will contains: `Test.abi` and `Test.bin`:
**Example usage:**
```
>>> warfle compile Test.sol
```

###### Step 4:
Now, We are ready to deploy our contract with the `warfle deploy` command:
```
>>> warfle deploy <PATH TO ABI> <PATH TO BIN>
```
In our case:
```
>>> warfle deploy source/Test.abi source/Test.bin
```

# LICENSE
[MIT](https://github.com/egesabanci/warfle/blob/master/LICENSE.md) © Ege Sabanci egesabanci@outlook.com.tr