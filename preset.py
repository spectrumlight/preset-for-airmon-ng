import subprocess

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output, error

# List of commands to be executed
commands = [
    "sudo airmon-ng start wlan0",
    "sudo airmon-ng check kill",
    # Add more commands as needed
]

for command in commands:
    print(f"Executing command: {command}")
    output, error = run_command(command)

    if error:
        print(f"Error while executing command: {error}")
        break

    print(f"Command output: {output}")

print("Script has completed.")
