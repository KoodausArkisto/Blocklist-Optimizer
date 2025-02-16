# Blocklist Optimizer

Blocklist Optimizer is a simple GUI application that helps users split large host lists into smaller parts. The program allows users to input IP addresses or domain names, which are divided into multiple files based on a specified maximum number of entries per file.

## Motivation

The motivation for creating Blocklist Optimizer stems from the limitations of certain firewall and network management tools, such as pfSense, which restrict the number of entries in alias lists to 5000. This application allows users to efficiently manage and split larger host lists into manageable sizes, ensuring compatibility with such systems.


## Features

- Input IP addresses or domain names, each on a new line.
- Load an existing .txt file containing a host list.
- Specify the maximum number of items per file.
- Provide a base name for the output files.
- Create a folder where all generated files will be saved.

## Usage Instructions

1. **Input Hosts**: Type or paste the IP addresses or domain names into the input field. Ensure that each address is on a new line.
2. **Load File**: You can load a pre-existing host list by clicking the "Load a blocklist file" button. Select the desired .txt file.
3. **Set Maximum Items**: Enter the maximum number of items you want in each generated file in the "Maximum items in row" field.
4. **Provide Base Name**: Enter your desired base name in the "Save as" field, which will be used to name the output files.
5. **Generate Lists**: Click the "Generate List" button. The program will create the files and save them in a new folder named after your base name + "_Aliases".

## Example

If you input the following IP addresses:

192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4

And set the maximum number to 2, the program will create a folder named "YourBaseName_Aliases" containing the following files:

- YourBaseNamePart1.txt (contains 192.168.1.1 and 192.168.1.2)
- YourBaseNamePart2.txt (contains 192.168.1.3 and 192.168.1.4)

## Requirements

- Python 3.x
- Tkinter (usually included with Python installation)

## Installation

1. Ensure you have Python 3.x installed.
2. Download or clone this project.
3. Run the `blocklist_optimizer.py` file using Python.

## Additional Information

If you have any questions or suggestions, feel free to contact the developer.