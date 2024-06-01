import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk
from tkinter.constants import END

class State:
    def __init__(self, name):
        self.name = name
        self.transitions = {}
        self.is_final = False

    def add_transition(self, input_char, next_state):
        self.transitions[input_char] = next_state

    def get_next_state(self, input_char):
        return self.transitions.get(input_char, None)


class Automaton:
    def __init__(self):
        self.start_state = State("start")
        self.states = {self.start_state}
        self.current_state = self.start_state

    def add_named_entity(self, named_entity):
        current_state = self.start_state
        for char in named_entity:
            if char in current_state.transitions:
                current_state = current_state.transitions[char]
            else:
                new_state = State(named_entity)
                current_state.add_transition(char, new_state)
                self.states.add(new_state)
                current_state = new_state
        current_state.is_final = True

    def recognize(self, text):
        named_entities = []
        words = text.split()
        for word in words:
            self.current_state = self.start_state
            for char in word:
                if char in self.current_state.transitions:
                    self.current_state = self.current_state.transitions[char]
                else:
                    break
            if self.current_state.is_final:
                named_entities.append(self.current_state.name)
        return named_entities


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Named Entity Recognition")
        self.automaton = Automaton()

        self.create_widgets()

    def create_widgets(self):
        # Frame for named entities
        self.entity_frame = ttk.Frame(self.root, padding="10")
        self.entity_frame.pack()

        ttk.Label(self.entity_frame, text="Named Entities:").grid(row=0, column=0, padx=5, pady=5)
        self.entities_text = scrolledtext.ScrolledText(self.entity_frame, height=10, width=40)
        self.entities_text.grid(row=1, column=0, padx=5, pady=5)

        # Frame for text input and recognition
        self.recognition_frame = ttk.Frame(self.root, padding="10")
        self.recognition_frame.pack()

        ttk.Label(self.recognition_frame, text="Text to Recognize:").grid(row=0, column=0, padx=5, pady=5)
        self.text_entry = ttk.Entry(self.recognition_frame, width=50)
        self.text_entry.grid(row=1, column=0, padx=5, pady=5)

        self.recognize_button = ttk.Button(self.recognition_frame, text="Recognize", command=self.recognize_text)
        self.recognize_button.grid(row=1, column=1, padx=5, pady=5)

        # Output frame
        self.output_frame = ttk.Frame(self.root, padding="10")
        self.output_frame.pack()

        ttk.Label(self.output_frame, text="Output:").grid(row=0, column=0, padx=5, pady=5)
        self.output_text = scrolledtext.ScrolledText(self.output_frame, height=5, width=50)
        self.output_text.grid(row=1, column=0, padx=5, pady=5)

    def recognize_text(self):
        self.output_text.delete('1.0', END)
        
        # Clear previous entities
        self.automaton = Automaton()
        
        # Retrieve named entities from text box
        entities_input = self.entities_text.get('1.0', END).strip().split('\n')
        for entity in entities_input:
            if entity.strip():
                self.automaton.add_named_entity(entity.strip())

        # Recognize named entities in input text
        text_to_recognize = self.text_entry.get().strip()
        recognized_entities = self.automaton.recognize(text_to_recognize)

        if recognized_entities:
            self.output_text.insert(END, f"Named entities found: {recognized_entities}\n")
        else:
            self.output_text.insert(END, "No named entities found in the input text\n")


def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
