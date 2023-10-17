import os
import sys
import socket
import art
import internals

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
    execute(commands)
    print(commands)

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
    for command in commands:
        if command['command'] == 'exit':
            sys.exit()
        else:
            for command_class in internals.commands_list:
                if command['command'].casefold() == command_class.name.casefold():
                    command_class(command['arguments'], command['redirect']).execute()
                    break

if __name__ == "__main__":
    main()