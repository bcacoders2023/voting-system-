import tkinter as tk
from tkinter import messagebox

class VotingMachine:
    def __init__(self, root):
        self.root = root
        self.root.title("Voting Machine")

        # Dictionary to store candidates and their votes
        self.candidates = {}

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Label for instructions
        self.label = tk.Label(self.root, text="Enter Candidate Name:")
        self.label.pack(pady=10)

        # Entry field for entering candidate names
        self.candidate_entry = tk.Entry(self.root)
        self.candidate_entry.pack(pady=10)

        # Button to add candidates
        self.add_button = tk.Button(self.root, text="Add Candidate", command=self.add_candidate)
        self.add_button.pack(pady=5)

        # Button to vote
        self.vote_button = tk.Button(self.root, text="Vote for Candidate", command=self.vote_for_candidate)
        self.vote_button.pack(pady=5)

        # Button to show results
        self.results_button = tk.Button(self.root, text="Show Results", command=self.show_results)
        self.results_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def add_candidate(self):
        name = self.candidate_entry.get().strip()
        if name:
            if name not in self.candidates:
                self.candidates[name] = 0
                messagebox.showinfo("Success", f"Candidate {name} added.")
            else:
                messagebox.showwarning("Duplicate", f"Candidate {name} is already added.")
        else:
            messagebox.showwarning("Input Error", "Candidate name cannot be empty!")
        self.candidate_entry.delete(0, tk.END)

    def vote_for_candidate(self):
        name = self.candidate_entry.get().strip()
        if name in self.candidates:
            self.candidates[name] += 1
            messagebox.showinfo("Vote Casted", f"Vote casted for {name}.")
        else:
            messagebox.showwarning("Not Found", f"Candidate {name} not found.")
        self.candidate_entry.delete(0, tk.END)

    def show_results(self):
        if self.candidates:
            results = "\n".join([f"{name}: {votes} votes" for name, votes in self.candidates.items()])
            messagebox.showinfo("Voting Results", results)
        else:
            messagebox.showwarning("No Candidates", "No candidates added yet.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VotingMachine(root)
    root.geometry("300x300")  # Set window size
    root.mainloop()
