import os
import json

class CommandReader:
    def __init__(self, command_path: str, command_dict: list):
        with open(command_path, "r") as f:
            self.command_help = json.load(f)
            self.commands = command_dict.copy()
            self.commands["help"] = self.command_help

    def run(self, command_name: str, args: list):
        self.commands[command_name](args)
        #self.commands[command_name](args)

    def help(self, help_dict: list):
        if "main" in help_dict.keys():
            help_main = help_dict["main"]
            for command in help_main:
                help_command = help_main[command]
                print(f"{command}:\n  Description: {help_command['description']}\n  Usage: '{help_command['usage']}'\n")
        else:
            help_command = help_dict
            print(f"{help_name}:\n  Description: {help_command['description']}\n  Usage: '{help_command['usage']}'\n")

    def command_help(self, args: list):
        self.help(self.command_help)
