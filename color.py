# ANSI escape codes for colors
class TerminalColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default color

# Example usage
print(TerminalColors.RED + 'This text is in red color!' )
print(TerminalColors.GREEN + 'This text is in green color!')
print(TerminalColors.YELLOW + 'This text is in yellow color!')
print(TerminalColors.BLUE + 'This text is in blue color!')
print(TerminalColors.MAGENTA + 'This text is in magenta color!')
print(TerminalColors.CYAN + 'This text is in cyan color!' + TerminalColors.RESET)
