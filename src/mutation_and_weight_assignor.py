def assign_mutations(subsubregions, mutations):
    """
    Assign mutations to their respective sub-subregions.

    Args:
    - subsubregions (list of lists): [subsubregion_number, length, start_index, end_index].
    - mutations (list of tuples): (position, mutation_data).

    Returns:
    - list of tuples: Each tuple contains a sub-subregion and its assigned mutations.
    """
    assigned = []
    
    for subsubregion in subsubregions:
        subsubregion_mutations = []
        for mutation in mutations:
            # Check if mutation position is within the sub-subregion range
            if subsubregion[2] <= mutation[0] <= subsubregion[3]:
                subsubregion_mutations.append(mutation)
        
        # Append sub-subregion and its mutations to the result list
        assigned.append((subsubregion, subsubregion_mutations))
    
    return assigned
