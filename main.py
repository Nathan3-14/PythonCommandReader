import command
import funcs


command_dict = {
    "this": funcs.this,
    "that": funcs.that
}

command_base = command.CommandReader("./help.json", command_dict)
command_base.run("this", ["test"])
command_base.run("foo", ["bar"])
command_base.run("quit", [])
command_base.run("help", ["help"])
