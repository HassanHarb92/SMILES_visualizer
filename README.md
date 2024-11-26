# SMILES Visualizer

**SMILES Visualizer** is a simple and interactive web application for molecular visualization and analysis. It allows users to input a **SMILES string** to generate 2D and 3D visualizations of the molecule and calculate important molecular properties such as molecular weight, rotatable bonds, and hydrogen bond donors/acceptors. The app is built using **Streamlit** and the **RDKit** library for cheminformatics.

## Features

- **2D Visualization**: Displays a 2D structure of the molecule based on the input SMILES string.
- **3D Visualization**: Interactive 3D visualization of the molecule using py3Dmol.
- **Molecular Properties**:
  - Molecular weight
  - Number of heavy atoms
  - Number of rings
  - Rotatable bonds
  - Hydrogen bond acceptors and donors
  - Topological polar surface area
  - LogP and molar refractivity

## Usage

1. Open the [SMILES Visualizer App](https://smiles-visualizer.streamlit.app/).
2. Enter a valid **SMILES string** in the input box (e.g., `Oc1ccccc1` for phenol).
3. Click the **"Visualize"** button to generate the 2D and 3D structures and calculate molecular properties.

## Example

### Input
SMILES: `Oc1ccccc1` (Phenol)

### Output
- **2D Visualization**: A 2D depiction of phenol.
- **3D Visualization**: Interactive 3D model of phenol.
- **Molecular Properties**:
  - Molecular weight: `94.1 g/mol`
  - Hydrogen bond donors: `1`
  - Hydrogen bond acceptors: `1`
  - Rotatable bonds: `0`
  - Topological polar surface area: `20.23 Å²`

## Built With

- [Streamlit](https://streamlit.io/) - Framework for creating interactive web apps.
- [RDKit](https://www.rdkit.org/) - Toolkit for cheminformatics.
- [py3Dmol](https://3dmol.csb.pitt.edu/) - Library for 3D molecular visualization.

## Acknowledgments

- [RDKit](https://www.rdkit.org/)
- [Streamlit](https://streamlit.io/)
- [py3Dmol](https://3dmol.csb.pitt.edu/)

---

**Try it now**: [SMILES Visualizer](https://smiles-visualizer.streamlit.app/)

