from rdkit import Chem 
from rdkit.Chem import Descriptors, Crippen, Lipinski

def compute_properties(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if not mol:
        return None

    return {
        "MW": Descriptors.MolWt(mol),
        "LogP": Crippen.MolLogP(mol),
        "HBD": Lipinski.NumHDonors(mol),
        "HBA": Lipinski.NumHAcceptors(mol),
        "Mol": mol
    }

def lipinski_violations(props):

    violations = []

    if props["MW"] > 500:
        violations.append("Molecular Weight > 500")
    if props["LogP"] > 5:
        violations.append("LogP > 5")
    if props["HBD"] > 5:
        violations.append("HBD >5")
    if props["HBA"] > 10:
        violations.append("HBA > 10")

    return violations



    


