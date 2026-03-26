# Lipinski Rule of Five App

A Cheminformatics web application built using Streamlit and RDKit to evaluate drug-likeness based on Lipinski’s Rule of Five.

This application calculates key molecular descriptors and determines whether a compound satisfies drug-likeness criteria commonly used in early-stage drug discovery.

---

##  What is Lipinski's Rule of Five?

Lipinski's Rule of Five is a rule of thumb used to evaluate whether a chemical compound with certain pharmacological or biological activity has properties that would make it a likely orally active drug in humans.

A compound is more likely to be drug-like if:

- Molecular weight < 500 Dalton
- LogP < 5
- Hydrogen bond donors < 5
- Hydrogen bond acceptors < 10

---

##  Features

- Accepts SMILES input
- Calculates:
  - Molecular Weight
  - LogP
  - Hydrogen Bond Donors
  - Hydrogen Bond Acceptors
- Displays Lipinski Rule evaluation
- Clean Streamlit UI
- Modular code structure

---

##  Tech Stack

- Python
- Streamlit
- RDKit
- Pandas

---

## Deployment
The application is deployed using GitHub and Streamlit Community Cloud.
Deployment Link:[Lipinski-rule-of-five-app](https://khushboo847-lipinski-rule-of-five-app-main-mwlxbv.streamlit.app/)

