from src.mutation_file_reader import read_mutation_data
from src.mutation_quantifier import quantify_significant_mutations
from src.subsubregion_combiner import combine_and_map_mutations

def process_mutation_data(mutation_file_path, seq_length):
    """
    Process mutation data and return partitioned (starting at index 0 and index 15) and combined data.

    Args:
    - mutation_file_path (str): Path to the input mutation data file.
    - seq_length (int): Length of the sequence.

    Returns:
    - tuple: (positional_scores_0_data, positional_scores_15_data, combined_data)
    """
    # Read mutation data file
    mutations = read_mutation_data(mutation_file_path)

    if isinstance(mutations, list):
        # Quantify significant mutations
        positional_scores_0, positional_scores_15 = quantify_significant_mutations(seq_length, mutations)
        
        # Prepare data for returning
        positional_scores_0_data = [
            [subsubregion[0], subsubregion[1], subsubregion[2]] for subsubregion in positional_scores_0
        ]
        positional_scores_15_data = [
            [subsubregion[0], subsubregion[1], subsubregion[2]] for subsubregion in positional_scores_15
        ]
        combined_data = combine_and_map_mutations(positional_scores_0, positional_scores_15)
        combined_data_csv = [
            [interval, mutations, score] for interval, mutations, score in combined_data
        ]

        return positional_scores_0_data, positional_scores_15_data, combined_data_csv
    else:
        raise ValueError(mutations)
    
def process_region_details(regions):
    """
    Extract details for each region, subregion, and sub-subregion.

    Args:
    - regions (list): List of regions, where each region is a list of subregions.

    Returns:
    - list: List of dictionaries containing details for each region.
    """
    region_details = []

    for i, region in enumerate(regions, start=1):
        if not region:
            continue
        start = region[0][0][0][0]
        end = region[-1][-1][0][1]

        region_scores = []
        subregions_details = []

        for j, subregion in enumerate(region, start=1):
            sub_start = subregion[0][0][0]
            sub_end = subregion[-1][0][1]

            subregion_scores = []
            subsubregions_details = []

            for k, subsubregion in enumerate(subregion, start=1):
                subsub_start, subsub_end = subsubregion[0][0], subsubregion[0][1]
                subsubregion_score = subsubregion[2]
                subsubregions_details.append({
                    'subsubregion_number': k,
                    'subsubregion_range': (subsub_start, subsub_end),
                    'subsubregion_score': subsubregion_score,
                    'subsubregion_data': subsubregion  # Ensure this key is included
                })
                subregion_scores.append(subsubregion_score)

            subregion_score = sum(subregion_scores) / len(subregion_scores) if subregion_scores else 0
            region_scores.append(subregion_score)
            subregions_details.append({
                'subregion_number': j,
                'subregion_range': (sub_start, sub_end),
                'subregion_score': subregion_score,
                'subsubregions': subsubregions_details
            })

        region_score = sum(region_scores) / len(region_scores) if region_scores else 0
        region_detail = {
            'region_number': i,
            'region_range': (start, end),
            'region_score': region_score,
            'subregions': subregions_details
        }
        region_details.append(region_detail)

    return region_details


