import numpy as np

# Load Text For Training
def load_text(filename):
    with open(filename, encoding='utf-8') as f:
        return f.read().lower()

print(load_text('data.txt'))

