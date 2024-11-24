import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem, Draw, Descriptors
import py3Dmol
import pandas as pd

# Function to convert SMILES to 3D XYZ format
def smiles_to_xyz(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    conf = mol.GetConformer()

    xyz = []
    num_atoms = mol.GetNumAtoms()
    xyz.append(f"{num_atoms}")
    xyz.append("Generated by RDKit")
    for i in range(num_atoms):
        atom = mol.GetAtomWithIdx(i)
        pos = conf.GetAtomPosition(i)
        xyz.append(f"{atom.GetSymbol()} {pos.x:.4f} {pos.y:.4f} {pos.z:.4f}")
    return "\n".join(xyz)

# Function to calculate molecular properties
def calculate_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    properties = {
        "Molecular Weight (g/mol)": round(Descriptors.MolWt(mol), 1),
        "Heavy Atoms": mol.GetNumHeavyAtoms(),
        "Rings": Chem.rdMolDescriptors.CalcNumRings(mol),
        "Rotatable Bonds": Chem.rdMolDescriptors.CalcNumRotatableBonds(mol),
        "HB Acceptors": Descriptors.NumHAcceptors(mol),
        "HB Donors": Descriptors.NumHDonors(mol),
        "Topo. Polar Surface Area (Å²)": round(Descriptors.TPSA(mol), 2),
        "Mol Refractivity": round(Descriptors.MolMR(mol), 2),
        "clogP": round(Descriptors.MolLogP(mol), 2),
    }
    return properties

# Initialize session state for SMILES and .xyz content
if "smiles" not in st.session_state:
    st.session_state["smiles"] = ""
if "xyz_content" not in st.session_state:
    st.session_state["xyz_content"] = None

# Streamlit App
st.title("SMILES Visualization")

# SMILES input box
smiles_input = st.text_input("Enter a SMILES string:", st.session_state["smiles"])

# Visualization style options
style_options = {
    'Ball and Stick': {'stick': {}, 'sphere': {'radius': 0.5}},
    'Stick': {'stick': {}},
    'Spacefill': {'sphere': {}}
}
selected_style = st.radio('Select visualization style', list(style_options.keys()))

# Button to process and visualize the SMILES
if st.button("Visualize"):
    mol = Chem.MolFromSmiles(smiles_input)
    if mol is None:
        st.error("Invalid SMILES string. Please try again.")
    else:
        st.session_state["smiles"] = smiles_input  # Save SMILES in session state
        st.session_state["xyz_content"] = smiles_to_xyz(smiles_input)  # Save .xyz content

# Only proceed if SMILES and .xyz content are valid
if st.session_state["smiles"] and st.session_state["xyz_content"]:
    mol = Chem.MolFromSmiles(st.session_state["smiles"])
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("2D Structure")
        img = Draw.MolToImage(mol, size=(300, 300))
        st.image(img, caption="2D Structure")

    with col2:
        st.subheader("3D Structure")
        xyz_content = st.session_state["xyz_content"]
        scale = 1
        width = int(320.0 * scale)
        height = int(300.0 * scale)

        # Visualize the 3D structure using py3Dmol
        xyzview = py3Dmol.view(width=width, height=height)
        xyzview.addModel(xyz_content, 'xyz')
        xyzview.setStyle(style_options[selected_style])  # Use selected visualization style
        xyzview.zoomTo()

        # Display the 3D visualization in Streamlit
        st.components.v1.html(xyzview._make_html(), width=width, height=height, scrolling=False)

    # Add the download button for the .xyz file
    st.download_button(
        label="Download .xyz file",
        data=xyz_content,
        file_name="molecule.xyz",
        mime="text/plain"
    )

    # Molecular Properties
    st.subheader("Molecular Properties")
    properties = calculate_properties(st.session_state["smiles"])
    if properties:
        df = pd.DataFrame(list(properties.items()), columns=["Property", "Value"])
        st.table(df)
    else:
        st.error("Failed to calculate molecular properties.")

