# PDB Cleaner for ChimeraX

This script cleans PepFold-generated PDB files by removing invalid
and non-standard PDB records (e.g., REMARK lines) that cause warnings
in UCSF ChimeraX.

## Features
- Removes invalid PDB records
- Produces ChimeraX-compatible PDB files
- Simple and beginner-friendly
- No external dependencies

## Usage

1. Place `clean_pdb.py` in the same folder as your PDB file
2. Edit the input filename inside the script
3. Run in Spyder or with Python:

```bash
python clean_pdb.py
