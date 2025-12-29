from src.featurization import featurize
from src.similarity import compute_similarity
from src.prioritization import rank_candidates
import pandas as pd

# Load example compounds
df = pd.read_csv("data/example_compounds.csv")

# Featurize compounds
X = featurize(df["smiles"])

# Compute similarity matrices
chem_sim, bio_sim = compute_similarity(X)

# Rank candidates
ranked = rank_candidates(df, chem_sim, bio_sim)

# Save outputs
ranked.to_csv("results/ranked_hits.csv", index=False)

print("Demo complete. Ranked candidates saved.")
