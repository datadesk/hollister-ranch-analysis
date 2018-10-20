"""
Settings common to all notebooks.
"""
import os

# Set shared folders
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_dir = os.path.join(base_dir, 'input')
output_dir = os.path.join(base_dir, 'output')

# Make sure they exist
os.path.exists(input_dir) or os.mkdir(input_dir)
os.path.exists(output_dir) or os.mkdir(output_dir)