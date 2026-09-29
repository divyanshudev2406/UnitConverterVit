Unit Converter

A simple command-line unit converter written in Python. It runs in the terminal and needs no extra libraries.

Features
Length: meter to kilometer, kilometer to meter
Temperature: Celsius to Fahrenheit, Fahrenheit to Celsius
Requirements
Python 3.6 or higher
Git (only needed if you want to clone the repository)
No extra libraries or packages are needed
Setup
1. Check that Python is installed

Open a terminal (Command Prompt or PowerShell on Windows, Terminal on Mac or Linux) and run:

python --version

If you see a version number like Python 3.x.x, you are ready. On some Mac/Linux systems you may need to use python3 instead of python.

If Python is not installed, download it from https://www.python.org/downloads/ and install it. On Windows, tick "Add Python to PATH" during installation.

2. Get the project

Clone the repository:

git clone https://github.com/divyanshudev2406/UnitConverterVit.git
cd UnitConverterVit

Or download the ZIP from the GitHub page (Code > Download ZIP), extract it, and open a terminal inside the extracted folder.

3. Install dependencies

There are none. The program only uses built-in Python features, so you can skip this step.

4. Configuration

No configuration is needed.

How to Run

In the project folder, run:

python unit_converter.py

(Use python3 unit_converter.py if python does not work on your system.)

How to Use
Choose the type of conversion: 1 for Length or 2 for Temperature.
Choose the specific conversion from the menu.
Type the number you want to convert.
The answer is printed and the program ends.
Example
Welcome to the Unit Converter!
Select the type of conversion:
1) Length
2) Temperature
Enter your choice (1/2): 2
1) Celsius to Fahrenheit
2) Fahrenheit to Celsius
Enter your choice (1/2): 1
Enter Celsius: 100
Answer: 212.0 F
Formulas Used
Conversion	Formula
Meter to Kilometer	km = m / 1000
Kilometer to Meter	m = km * 1000
Celsius to Fahrenheit	F = C * 9/5 + 32
Fahrenheit to Celsius	C = (F - 32) * 5/9
Known Limitations
The program converts one value and then stops. Run it again for another conversion.
Entering text instead of a number when asked for a value will cause an error.
Project Structure
UnitConverterVit/
├── unit_converter.py
└── README.md
Author

Divyanshu
