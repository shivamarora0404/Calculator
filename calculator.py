"""
🎨 SUPER COOL FUN CALCULATOR 🎨
A colorful, interactive calculator with multiple modes!
"""

import math
import time
import sys
from datetime import datetime

# ANSI color codes for terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_banner():
    """Display awesome ASCII art banner"""
    banner = f"""
{Colors.CYAN}{Colors.BOLD}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗        ║
║    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║        ║
║    ██║     ███████║██║     ██║     ██║   ██║        ║
║    ██║     ██╔══██║██║     ██║     ██║   ██║        ║
║    ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝        ║
║     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝         ║
║                                                       ║
║          🌟 The Most Fun Calculator Ever! 🌟          ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
{Colors.END}
    """
    print(banner)

def typing_effect(text, delay=0.03):
    """Print text with typing animation"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def calculate_basic(num1, operator, num2):
    """Perform basic arithmetic operations"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "Error: Division by zero!",
        '^': lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else "Error: Modulo by zero!"
    }
    
    if operator in operations:
        return operations[operator](num1, num2)
    return "Invalid operator!"

def scientific_mode():
    """Scientific calculator functions"""
    print(f"\n{Colors.GREEN}🔬 SCIENTIFIC MODE 🔬{Colors.END}")
    print(f"{Colors.YELLOW}Available functions:{Colors.END}")
    print("1. sin(x)  2. cos(x)  3. tan(x)")
    print("4. sqrt(x) 5. log(x)  6. ln(x)")
    print("7. factorial(x) 8. Back to main")
    
    choice = input(f"\n{Colors.CYAN}Choose function (1-8): {Colors.END}")
    
    if choice == '8':
        return
    
    try:
        x = float(input(f"{Colors.CYAN}Enter value: {Colors.END}"))
        
        results = {
            '1': ('sin', math.sin(math.radians(x))),
            '2': ('cos', math.cos(math.radians(x))),
            '3': ('tan', math.tan(math.radians(x))),
            '4': ('sqrt', math.sqrt(x) if x >= 0 else "Error: Negative number!"),
            '5': ('log', math.log10(x) if x > 0 else "Error: Non-positive number!"),
            '6': ('ln', math.log(x) if x > 0 else "Error: Non-positive number!"),
            '7': ('factorial', math.factorial(int(x)) if x >= 0 and x == int(x) else "Error: Non-negative integer required!")
        }
        
        if choice in results:
            func_name, result = results[choice]
            print(f"\n{Colors.GREEN}✨ {func_name}({x}) = {result}{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.END}")

def conversion_mode():
    """Unit conversion calculator"""
    print(f"\n{Colors.BLUE}🔄 CONVERSION MODE 🔄{Colors.END}")
    print(f"{Colors.YELLOW}Available conversions:{Colors.END}")
    print("1. Celsius ↔ Fahrenheit")
    print("2. Kilometers ↔ Miles")
    print("3. Kilograms ↔ Pounds")
    print("4. Back to main")
    
    choice = input(f"\n{Colors.CYAN}Choose conversion (1-4): {Colors.END}")
    
    if choice == '4':
        return
    
    try:
        value = float(input(f"{Colors.CYAN}Enter value: {Colors.END}"))
        
        if choice == '1':
            f = (value * 9/5) + 32
            c = (value - 32) * 5/9
            print(f"\n{Colors.GREEN}🌡️  {value}°C = {f:.2f}°F{Colors.END}")
            print(f"{Colors.GREEN}🌡️  {value}°F = {c:.2f}°C{Colors.END}")
        elif choice == '2':
            miles = value * 0.621371
            km = value * 1.60934
            print(f"\n{Colors.GREEN}🛣️  {value} km = {miles:.2f} miles{Colors.END}")
            print(f"{Colors.GREEN}🛣️  {value} miles = {km:.2f} km{Colors.END}")
        elif choice == '3':
            lbs = value * 2.20462
            kg = value * 0.453592
            print(f"\n{Colors.GREEN}⚖️  {value} kg = {lbs:.2f} lbs{Colors.END}")
            print(f"{Colors.GREEN}⚖️  {value} lbs = {kg:.2f} kg{Colors.END}")
        else:
            print(f"{Colors.RED}Invalid choice!{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.END}")

def fun_facts():
    """Display random math fun facts"""
    facts = [
        "🎲 The number 1 is not considered prime!",
        "🎯 Pi (π) has been calculated to over 31 trillion digits!",
        "🌟 Zero is the only number that can't be represented in Roman numerals!",
        "🎨 The Golden Ratio (φ) ≈ 1.618 appears frequently in nature!",
        "🔢 111,111,111 × 111,111,111 = 12,345,678,987,654,321",
        "🎪 A googol is 1 followed by 100 zeros!",
        "🌈 Euler's identity: e^(iπ) + 1 = 0 (called the most beautiful equation!)",
        "🎭 The probability of shuffling a deck into perfect order is 1 in 8×10^67!"
    ]
    import random
    print(f"\n{Colors.YELLOW}💡 Math Fun Fact:{Colors.END}")
    typing_effect(f"{Colors.CYAN}{random.choice(facts)}{Colors.END}", 0.02)

def basic_calculator():
    """Main basic calculator mode"""
    print(f"\n{Colors.GREEN}➕ BASIC CALCULATOR ➕{Colors.END}")
    print(f"{Colors.YELLOW}Operators: + - * / ^ (power) % (modulo){Colors.END}")
    
    try:
        num1 = float(input(f"{Colors.CYAN}Enter first number: {Colors.END}"))
        operator = input(f"{Colors.CYAN}Enter operator: {Colors.END}").strip()
        num2 = float(input(f"{Colors.CYAN}Enter second number: {Colors.END}"))
        
        result = calculate_basic(num1, operator, num2)
        
        # Animated result display
        print(f"\n{Colors.YELLOW}Calculating", end="")
        for _ in range(3):
            time.sleep(0.3)
            print(".", end="", flush=True)
        print()
        
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 RESULT: {num1} {operator} {num2} = {result}{Colors.END}")
        
    except ValueError:
        print(f"{Colors.RED}Error: Please enter valid numbers!{Colors.END}")
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.END}")

def history_log(calculation):
    """Save calculation to history file"""
    try:
        with open('calculator_history.txt', 'a') as f:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f"[{timestamp}] {calculation}\n")
    except:
        pass

def main():
    """Main program loop"""
    print_banner()
    typing_effect(f"{Colors.YELLOW}Welcome to the most awesome calculator you'll ever use!{Colors.END}")
    
    while True:
        print(f"\n{Colors.BOLD}{'='*55}{Colors.END}")
        print(f"{Colors.CYAN}🎮 CHOOSE YOUR MODE:{Colors.END}")
        print(f"{Colors.YELLOW}1.{Colors.END} ➕ Basic Calculator")
        print(f"{Colors.YELLOW}2.{Colors.END} 🔬 Scientific Mode")
        print(f"{Colors.YELLOW}3.{Colors.END} 🔄 Conversion Mode")
        print(f"{Colors.YELLOW}4.{Colors.END} 💡 Math Fun Fact")
        print(f"{Colors.YELLOW}5.{Colors.END} 👋 Exit")
        print(f"{Colors.BOLD}{'='*55}{Colors.END}")
        
        choice = input(f"\n{Colors.GREEN}Enter your choice (1-5): {Colors.END}").strip()
        
        if choice == '1':
            basic_calculator()
        elif choice == '2':
            scientific_mode()
        elif choice == '3':
            conversion_mode()
        elif choice == '4':
            fun_facts()
        elif choice == '5':
            print(f"\n{Colors.CYAN}{'='*55}{Colors.END}")
            typing_effect(f"{Colors.YELLOW}Thanks for using Super Cool Calculator! 🎉{Colors.END}")
            typing_effect(f"{Colors.CYAN}Keep calculating and stay awesome! ✨{Colors.END}")
            print(f"{Colors.CYAN}{'='*55}{Colors.END}\n")
            break
        else:
            print(f"{Colors.RED}❌ Invalid choice! Please select 1-5.{Colors.END}")
        
        input(f"\n{Colors.YELLOW}Press Enter to continue...{Colors.END}")
        print("\n" * 2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Calculator interrupted. Goodbye! 👋{Colors.END}\n")