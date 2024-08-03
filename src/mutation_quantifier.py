from src.seq_partitioner import partition_seq_length
from src.mutation_and_weight_assignor import assign_mutations
from src.normalizer import weighted_ave_normalization

def quantify_significant_mutations(seq_length, mutations):
    """
    Quantify significant mutations by summing and normalizing impact scores for sub-subregions.

    Args:
    - seq_length (int): Length of the DNA sequence.
    - mutations (list of tuples): List of mutations, each represented as (position, mutation_data).

    Returns:
    - tuple: Two lists containing sub-subregions with their mutations and normalized impact scores for sub-subregions starting at index 0 and index 15.
    """
    # Partition the sequence into sub-subregions starting at index 0 and index 15
    subsubregions_0, subsubregions_15 = partition_seq_length(seq_length)
    
    # Process sub-subregions starting at index 0
    subsubregion_mutations_scores_0 = []
    assigned_mutations_0 = assign_mutations(subsubregions_0, mutations)
    for subsubregion, subsubregion_mutations in assigned_mutations_0:
        # Sum the impact scores of the mutations in the subsubregion
        total_impact_score = sum(mutation[1] for mutation in subsubregion_mutations)
        # Normalize by subsubregion length
        normalized_score = weighted_ave_normalization(total_impact_score, len(subsubregion))
        subsubregion_mutations_scores_0.append((subsubregion, subsubregion_mutations, normalized_score))

    # Process sub-subregions starting at index 15
    subsubregion_mutations_scores_15 = []
    assigned_mutations_15 = assign_mutations(subsubregions_15, mutations)
    for subsubregion, subsubregion_mutations in assigned_mutations_15:
        # Sum the impact scores of the mutations in the subsubregion
        total_impact_score = sum(mutation[1] for mutation in subsubregion_mutations)
        # Normalize by subsubregion length
        normalized_score = weighted_ave_normalization(total_impact_score, len(subsubregion))
        subsubregion_mutations_scores_15.append((subsubregion, subsubregion_mutations, normalized_score))

    return subsubregion_mutations_scores_0, subsubregion_mutations_scores_15
