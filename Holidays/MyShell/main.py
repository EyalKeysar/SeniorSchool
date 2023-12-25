import os
import sys
import socket
import art
import internals
import subprocess

def main():
    print("Welcome to Keysar Shell!\n" + art.text2art("KEYSAR\nSHELL"))
    main_loop()

def main_loop():
    while True:
        username = os.getenv("USERNAME")
        prompt = f"{username}@{socket.gethostname()}" + ":" + f"{os.getcwd()}$ "
        print(prompt, end="")
        user_input = input()
        handle_input(user_input)

def handle_input(user_input):
    tokens = tokenize(user_input)
    commands = parse(tokens)
    print(commands)
    execute(commands)

def tokenize(user_input):
    """
    Tokenizes the user input into a list of tokens
    """
    tokens = []
    current_token = ""
    in_quotes = False

    for char in user_input:
        if char == ' ' and not in_quotes:
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char == '"':
            in_quotes = not in_quotes
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)

    return tokens

def parse(tokens):
    """
    Parses the tokens into a command and an argument
    """
    commands = []
    current_command = {'command': None, 'arguments': [], 'redirect': None}
    for token in tokens:
        if token == '|':
            commands.append(current_command)
            current_command = {'command': None, 'arguments': [], 'redirect': None}
        elif token == '>':
            current_command['redirect'] = tokens[tokens.index(token) + 1]
            break
        elif current_command['command'] is None:
            current_command['command'] = token
        else:
            current_command['arguments'].append(token)
    commands.append(current_command)
    return commands

def execute(commands):
    """
    Executes the commands
    """

    piped_arguments = []

    i = -1
    for command in commands:
        i += 1

        if(command['command'].casefold() == "help"):
            internals.help.HelpCommand(command['arguments'], command['redirect']).execute()
            continue

        for command_class in internals.commands.commands_list:
            if command['command'].casefold() == command_class.name.casefold():
                try:
                    command_class(command['arguments'], command['redirect']).execute()
                    return
                except Exception as e:
                    print("execute error" + str(e))
                    return
                
        # execute external commands
        paths = os.environ["PATH"].split(os.pathsep)
        for path in paths:
            try:
                files = os.listdir(path)
                for file in files:
                    base_name, extension = os.path.splitext(file)
                    if base_name == command['command'] and os.access(os.path.join(path, file), os.X_OK):
                        executable_path = os.path.join(path, file)

                        # use popen to execute the command
                        if command['redirect'] is not None:
                            with open(command['redirect'], 'w') as f:
                                print("redirecting to " + command['redirect'])
                                subprocess.Popen([executable_path] + command['arguments'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                                proc.wait()
                                print(proc.returncode)
                                print()
                        else:
                            print("not redirecting")
                            proc = subprocess.Popen([executable_path] + command['arguments'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                            proc.wait()
                            with command['redirect'] as f:
                                f.write(proc.stdout)
                        return
            except OSError as e:
                print("execute error" + str(e))
                continue

    print("Command not found.")
    

        

if __name__ == "__main__":
    main()