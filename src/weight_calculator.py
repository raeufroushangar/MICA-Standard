import numpy as np
from src.mutation_and_weight_assignor import assign_positional_weight
from src.normalizer import weighted_ave_normalization 

def calculate_subsubregion_weights(subsubregion, subsubregion_mutations):
    """
    Calculate the weighted impact for a sub-subregion based on mutations.

    Args:
    - subsubregion (list): A sub-subregion represented as [subsubregion_number, length, start_index, end_index].
    - subsubregion_mutations (list of tuples): Mutations within the sub-subregion, each represented as (position, impact).

    Returns:
    - float: The normalized weighted impact for the sub-subregion.
    """
    total_positional_weighted_impact = 0

    # Return 0 if no mutations are found in the subsubregion
    if not subsubregion_mutations:
        return 0

    for pos, impact in subsubregion_mutations:
        # Calculate the distance from the mutation position to each position in the sub-subregion
        distance = np.abs(np.arange(subsubregion[2], subsubregion[3] + 1) - pos)
        # Calculate positional weights based on the distance
        positional_weights = assign_positional_weight(distance)
        # Calculate the positional weighted impact
        positional_weighted_impact = positional_weights * impact
        # Accumulate the total positional weighted impact
        total_positional_weighted_impact += positional_weighted_impact

    # Normalize the total positional weighted impact
    subsubregion_normalized_weighted_impact = weighted_ave_normalization(total_positional_weighted_impact)
    return subsubregion_normalized_weighted_impact


def calculate_subregion_weights(subregion):
    """
    Calculate the weights for a subregion.

    Args:
    - subregion (list): A list of sub-subregions within a subregion.

    Returns:
    - float: The normalized weighted impact for the subregion.
    """
    subregion_size = len(subregion)
    total_positional_weighted_impact = np.zeros(subregion_size)
    
    if not subregion:
        return 0  # Return 0 if no sub-subregions found in the subregion

    for i, (interval, combined_mutations, weight) in enumerate(subregion):
        if weight == 0:
            continue

        distance = np.abs(np.arange(subregion_size) - i)
        positional_weights = assign_positional_weight(distance)
        positional_weighted_impact = positional_weights * weight
        total_positional_weighted_impact += positional_weighted_impact
        
    subregion_normalized_weighted_impact = weighted_ave_normalization(total_positional_weighted_impact)
    return subregion_normalized_weighted_impact


def calculate_region_weights(region):
    """
    Calculate the weights for a region.

    Args:
    - region (list): A list of subregions within a region.

    Returns:
    - float: The normalized weighted impact for the region.
    """
    region_size = len(region)
    total_positional_weighted_impact = np.zeros(region_size)
    
    if not region:
        return 0  # Return 0 if no subregions found in the region

    for i, subregion in enumerate(region):
        subregion_weight = calculate_subregion_weights(subregion)
        if subregion_weight == 0:
            continue
        distance = np.abs(np.arange(region_size) - i)
        positional_weights = assign_positional_weight(distance)
        positional_weighted_impact = positional_weights * subregion_weight
        total_positional_weighted_impact += positional_weighted_impact

    region_normalized_weighted_impact = weighted_ave_normalization(total_positional_weighted_impact)

    return region_normalized_weighted_impact