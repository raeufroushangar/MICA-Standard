from collections import defaultdict
from src.mutation_and_weight_assignor import assign_mutations

def extract_boundaries(subsubregions):
    """
    Extract unique boundaries from sub-subregions.

    Args:
    - subsubregions (list): List of sub-subregions.

    Returns:
    - list: Sorted list of unique boundaries.
    """
    boundaries = set()
    for sub in subsubregions:
        boundaries.add(sub[0][2])  # start
        boundaries.add(sub[0][3] + 1)  # end
    return sorted(boundaries)

def create_combined_intervals(sorted_boundaries):
    """
    Create combined intervals from sorted boundaries.

    Args:
    - sorted_boundaries (list): Sorted list of boundaries.

    Returns:
    - list: List of combined intervals.
    """
    combined_intervals = []
    for i in range(len(sorted_boundaries) - 1):
        start = sorted_boundaries[i]
        end = sorted_boundaries[i + 1] - 1
        combined_intervals.append([start, end])
    return combined_intervals

def map_subsubregions_to_intervals(subsubregions):
    """
    Map sub-subregions to intervals.

    Args:
    - subsubregions (list): List of sub-subregions.

    Returns:
    - dict: Dictionary mapping intervals to sub-subregions.
    """
    interval_dict = defaultdict(list)
    for sub in subsubregions:
        sub_start = sub[0][2]
        sub_end = sub[0][3]
        interval_dict[(sub_start, sub_end)].append(sub)
    return interval_dict

def calculate_overlap_and_combine(interval, interval_dict):
    """
    Calculate overlap and combine mutations and impact scores for an interval.

    Args:
    - interval (tuple): Interval represented as (start, end).
    - interval_dict (dict): Dictionary mapping intervals to sub-subregions.

    Returns:
    - tuple: Combined interval data including mutations and normalized impact scores.
    """
    start, end = interval
    total_impact_score = 0
    total_length = 0
    combined_mutations = []

    for (sub_start, sub_end), subs in interval_dict.items():
        if sub_end >= start and sub_start <= end:
            for sub in subs:
                overlap_start = max(start, sub_start)
                overlap_end = min(end, sub_end)
                overlap_length = overlap_end - overlap_start + 1
                impact_score = sum(mutation[1] for mutation in sub[1])
                total_impact_score += impact_score * overlap_length
                total_length += overlap_length
                for mutation in sub[1]:
                    if overlap_start <= mutation[0] <= overlap_end:
                        if mutation not in combined_mutations:
                            combined_mutations.append(mutation)

    if total_length > 0:
        normalized_impact_score = total_impact_score / total_length
    else:
        normalized_impact_score = 0

    return (interval, combined_mutations, normalized_impact_score)

def combine_and_map_mutations(subsubregions1, subsubregions2):
    """
    Combine and map mutations and impact scores for two sets of sub-subregions.

    Args:
    - subsubregions1 (list): First list of sub-subregions.
    - subsubregions2 (list): Second list of sub-subregions.

    Returns:
    - list: Combined and mapped data for the sub-subregions.
    """
    # Extract and sort boundaries
    boundaries1 = extract_boundaries(subsubregions1)
    boundaries2 = extract_boundaries(subsubregions2)
    sorted_boundaries = sorted(set(boundaries1 + boundaries2))

    # Create combined intervals
    combined_intervals = create_combined_intervals(sorted_boundaries)

    # Map subsubregions to intervals
    subsubregions = subsubregions1 + subsubregions2
    interval_dict = map_subsubregions_to_intervals(subsubregions)

    # Calculate overlap and combine mutations for each interval
    mapped_data = []
    for interval in combined_intervals:
        mapped_data.append(calculate_overlap_and_combine(interval, interval_dict))

    return mapped_data
