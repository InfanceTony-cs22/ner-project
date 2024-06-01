Overview
This repository contains a Python implementation of a Named Entity Recognition (NER) system using Finite Automata. The project demonstrates how to identify specific patterns corresponding to named entities (e.g., names of people, organizations, locations) within text data.

Features
Finite Automata Implementation: Utilizes a finite automaton model to recognize named entities based on predefined patterns.
Customizable Entities: Users can define and add their own named entities for recognition.
Text Input: Accepts user-provided text for identifying named entities.
Output: Provides feedback on recognized named entities within the input text.
Components
State Class (state.py)
Represents a state in the finite automaton.

name: Name of the state (optional).
transitions: Dictionary mapping input characters to next states.
is_final: Indicates if the state is a final state where a named entity has been recognized.
Automaton Class (automaton.py)
Manages the finite automaton for recognizing named entities.

start_state: Initial state of the automaton.
states: Set of states within the automaton.
current_state: Tracks the current state during entity recognition.
Main Script (main.py)
Entry point of the application.

Handles user interaction and integrates the Automaton class for named entity recognition.
Allows users to define named entities and input text for recognition.
Usage
Setup: Clone the repository and ensure Python 3.x is installed.

bash
Copy code
git clone https://github.com/your-username/ner-finite-automata.git
cd ner-finite-automata
Define Named Entities: Edit main.py to add named entities using the add_entity(entity) method.

python
Copy code
automaton.add_entity("Infance Tony")
automaton.add_entity("Stella Marys College of Engineering")
Run the Program: Execute main.py and input text to recognize named entities.

css
Copy code
python main.py
Output: The program will display recognized named entities found in the input text.

Dependencies
Python 3.x
No external libraries beyond standard Python libraries are required.
Future Enhancements
Support for more complex patterns and entity types.
Integration with larger NLP pipelines.
Improved error handling and input validation.
License
This project is licensed under the MIT License.

Contributors
Infance Tony (@InfanceTony-cs22)