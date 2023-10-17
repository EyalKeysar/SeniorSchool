def handle_stdout(redirect, stdout):
    if redirect:
        try:
            with open(redirect, "w") as f:
                f.write(stdout)
                stdout = ""
        except FileNotFoundError:
            stdout = f"cd: {redirect}: No such file or directory"
        except PermissionError:
            stdout = f"cd: {redirect}: Permission denied"
        except Exception as e:
            stdout = f"cd: {redirect}: {e}"
    print(stdout)