# Named Entity Recognition using Finite Automata

## Overview

This repository contains a Python implementation of a Named Entity Recognition (NER) system using Finite Automata. The project demonstrates how to identify specific patterns corresponding to named entities (e.g., names of people, organizations, locations) within text data.

## Features

- **Finite Automata Implementation**: Utilizes a finite automaton model to recognize named entities based on predefined patterns.
- **Customizable Entities**: Users can define and add their own named entities for recognition.
- **Text Input**: Accepts user-provided text for identifying named entities.
- **Output**: Provides feedback on recognized named entities within the input text.

## Components

### State Class (`state.py`)

Represents a state in the finite automaton.

- `name`: Name of the state (optional).
- `transitions`: Dictionary mapping input characters to next states.
- `is_final`: Indicates if the state is a final state where a named entity has been recognized.

### Automaton Class (`automaton.py`)

Manages the finite automaton for recognizing named entities.

- `start_state`: Initial state of the automaton.
- `states`: Set of states within the automaton.
- `current_state`: Tracks the current state during entity recognition.

### Main Script (`main.py`)

Entry point of the application.

- Handles user interaction and integrates the Automaton class for named entity recognition.
- Allows users to define named entities and input text for recognition.

## Usage

1. **Setup**: Clone the repository and ensure Python 3.x is installed.

  ## Dependencies

- Python 3.x
- No external libraries beyond standard Python libraries are required.

## Future Enhancements

- Support for more complex patterns and entity types.
- Integration with larger NLP pipelines.
- Improved error handling and input validation.

## Contributors

- Infance Tony ([@InfanceTony-cs22](https://github.com/InfanceTony-cs22))

