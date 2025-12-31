"""
clean_pdb.py

Clean PepFold-generated PDB files for UCSF ChimeraX by removing
non-standard and invalid PDB records (e.g., REMARK lines).

Author: YOUR NAME
License: MIT
"""

import os

# ===================== USER INPUT =====================
input_pdb = r"PEPFOLD-model1.pdb"
# =====================================================

# Strict set of PDB records accepted by ChimeraX
VALID_RECORDS = {
    "ATOM",
    "HETATM",
    "TER",
    "CONECT",
    "MODEL",
    "ENDMDL"
}

def clean_pdb(input_pdb):
    """
    Remove non-standard PDB records and produce a ChimeraX-compatible file.
    """
    base, _ = os.path.splitext(input_pdb)
    output_pdb = base + "_clean.pdb"

    with open(input_pdb, "r") as fin, open(output_pdb, "w") as fout:
        for line in fin:
            record = line[:6].strip()
            if record in VALID_RECORDS:
                fout.write(line)

        fout.write("END\n")

    print("PDB cleaned successfully.")
    print("Output:", output_pdb)

if __name__ == "__main__":
    clean_pdb(input_pdb)
