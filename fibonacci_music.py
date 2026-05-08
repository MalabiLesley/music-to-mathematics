# Music to Mathematics – Fibonacci Melody Generator

**University of Eastern Africa, Baraton** | MATH 499 | April 2023  
**Team:** Eddah Jeptum, Malabi Lesley (me), Lenox Ondieki, Titame Jack  
**Supervisor:** Dr. Robert Okong'o

## 🎯 What This Project Does
Translates pure mathematics (Fibonacci sequence, Golden Ratio, modular arithmetic) into musical melodies using a Python algorithm. The same systematic **rule → output → validation** workflow is identical to the data transformation and quality checks I perform on real datasets.

## 🧠 Why It Matters for Data & QA Roles
- **Algorithmic mapping:** Just like mapping raw logs to structured JSON/CSV, this project maps abstract numbers to musical notes via clear, reproducible rules.
- **Validation:** The script programmatically verifies that the generated note sequences are periodic—mirroring how I would flag a dataset for impossible patterns or data leakage.
- **Documentation:** Every step (modulo choice, note mapping, rhythm derivation) is fully documented, similar to a **data lineage log**.

## 🛠️ How It Works
1. Generate the Fibonacci sequence up to *n* terms.
2. Apply **modulo *m*** (where *m* = number of notes in the chosen scale) to each Fibonacci number.
3. Map the resulting numbers 0–(*m*-1) to musical notes in the scale.
4. The sequence becomes periodic, as proven using group theory and the division algorithm.
5. A rhythm is optionally added by interpreting Fibonacci numbers as note durations.

## 📊 Scales Explored
- C Major Pentatonic (mod 5)
- E Minor Pentatonic (mod 5)
- A Minor Blues (mod 6)
- C Major (mod 7)
- Harmonic A Minor (mod 8)
- Full Chromatic (mod 12)

Each scale produces a unique, repeatable melody.

## 🧰 Tech Stack
- **Python** – core logic, modulo mapping, period detection
- **Score Creator** – used to render final melodies with rhythm (see project PDF)

## 📁 Repository Structure