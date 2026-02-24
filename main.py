import streamlit as st
from rdkit.Chem import Draw
from utils.calculations import compute_properties, lipinski_violations

st.set_page_config(page_title="Lipinski Filter", layout="centered")

st.title("🧪 Lipinski Rule of Five Filter")

st.markdown("Evaluate drug-likeness from a SMILES string.")

smiles = st.text_input("Enter SMILES:")

if smiles:
    props = compute_properties(smiles)

    if props:
        st.subheader("📊 Molecular Properties")

        col1, col2 = st.columns(2)
        col1.metric("Molecular Weight", f"{props['MW']:.2f}")
        col2.metric("LogP", f"{props['LogP']:.2f}")

        col3, col4 = st.columns(2)
        col3.metric("H-bond Donors", props["HBD"])
        col4.metric("H-bond Acceptors", props["HBA"])

        st.subheader("🧬 Structure")
        st.image(Draw.MolToImage(props["Mol"]))

        violations = lipinski_violations(props)

        st.subheader("✅ Lipinski Evaluation")

        if not violations:
            st.success("Passes Lipinski Rule of Five 🎉")
        else:
            st.error("Violations detected:")
            for v in violations:
                st.write(f"❌ {v}")

    else:
        st.error("Invalid SMILES")
