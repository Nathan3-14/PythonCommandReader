# PythonCommandReader

### [Wiki](https://github.com/Nathan3-14/PythonCommandReader/wiki)

## Contents
- [Installation](#installation)
- [Usage](#usage)
- [Code Snippets](#code-snippets)


## Installation
- Clone this repo into your project folder
- Rename it to 'command'
- Inside that folder, create a json file and name it whatever you like (recommended is 'help.json')
- Copy [default.json](https://github.com/Nathan3-14/PythonCommandReader/blob/main/default.json) into your new file
- Add any function you wish to add following the template


## Usage
- Import the module ([1](../../wiki/code-snippets/#import)) at the top of your script
- Add a 'command_dict' dictionary to store all your functions ([2](../../wiki/code-snippets/#command-dictionary))
- Create your command interpreter by assigning a variable with the CommandReader class ([3](../../wiki/code-snippets/#interpreter-variable))
- To run a command, use the run command, built in to the class ([4](../../wiki/code-snippets/#run-command))


## Code snippets

### Import
```python
import command.command
```

### Command Dictionary
```python
# ...

def foo(args: list):
    print("Foo")
    return True
def bar(args: list):
    print("Bar")
    return True

command_dict = {
    "foo": foo,
    "bar": bar
}
# Remember to not call () the functions, just type their names #

# ...
```

### Interpreter Variable
```python
command_base = command.CommandReader("./command/help.json", command_dict)
# replace with the path to your help file  ^^^^^
```

### Run Command
```python
command_base.run("command_name", args)
# Args must be a list containing all arguments for the function
```

### Function Template
```python
def func_name(args: list): # Arguments must be (args: list) and nothing else
    if len(args) != 0: # If input args are incorrect
        return False # Used by the interpreter in order to show syntax errors
    do_stuff()
    return True # Is needed at the end of functions
```
