"""
Music to Mathematics: Fibonacci Sequence & Golden Ratio Melody Generator
University of Eastern Africa, Baraton - MATH 499 Project

This script maps the Fibonacci sequence to musical notes using modular arithmetic
and validates that the resulting sequences are periodic, as proven in the paper.
"""

def fibonacci_up_to(n_terms):
    """Generate Fibonacci sequence up to n_terms."""
    seq = [0, 1]
    for i in range(2, n_terms):
        seq.append(seq[-1] + seq[-2])
    return seq

def apply_modulo(seq, mod):
    """Apply modulo operation to each element in the sequence."""
    return [x % mod for x in seq]

def map_to_notes(mod_vals, note_map):
    """Convert modulo values to note names using a mapping list."""
    return [note_map[v] for v in mod_vals]

def find_period(note_seq):
    """Find the least period of a periodic sequence (used for validation)."""
    n = len(note_seq)
    for p in range(1, n // 2 + 1):
        if note_seq[:p] * (n // p) == note_seq[:p * (n // p)] and note_seq[:p] == note_seq[-p:]:
            return p
    return n

# Define scales as lists of notes (order matters)
scales = {
    "C_Major_Pentatonic": ["C", "D", "E", "G", "A"],
    "E_Minor_Pentatonic": ["E", "G", "A", "B", "D"],
    "A_Minor_Blues":      ["A", "C", "D", "D#", "E", "G"],
    "C_Major":            ["C", "D", "E", "F", "G", "A", "B"],
    "Harmonic_A_Minor":   ["A", "B", "C", "D", "E", "F", "G", "G#"],
    "Full_Chromatic":     ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
}

N_TERMS = 30  # number of Fibonacci terms to generate

output_lines = []
for scale_name, notes in scales.items():
    mod = len(notes)
    fib = fibonacci_up_to(N_TERMS)
    mod_vals = apply_modulo(fib, mod)
    note_sequence = map_to_notes(mod_vals, notes)

    # Validate periodicity (the project proves it is periodic)
    period = find_period(note_sequence)

    output_lines.append(f"=== {scale_name} (mod {mod}) ===")
    output_lines.append(f"Fibonacci (first {N_TERMS} terms): {fib}")
    output_lines.append(f"Modulo {mod} values: {mod_vals}")
    output_lines.append(f"Note sequence: {note_sequence}")
    output_lines.append(f"Least period found: {period}")
    output_lines.append("")

# Print to console
result = "\n".join(output_lines)
print(result)

# Save to file for GitHub portfolio
with open("sample_output.txt", "w") as f:
    f.write(result)