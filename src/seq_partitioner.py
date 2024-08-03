
def partition_seq_length(seq_length):
    """
    Partition a given sequence length into sub-subregions for further analysis.

    Args:
    - seq_length (int): Length of sequence to partition.

    Returns:
    - subsubregions_0 (list): List of sub-subregions starting from index 0.
    - subsubregions_15 (list): List of sub-subregions starting from index 15.
    """
    
    if not isinstance(seq_length, int):
        raise ValueError(f"Error: Sequence length must be an integer. Received: {seq_length}")
    
    if seq_length < 45 or seq_length > 100000:
        raise ValueError(f"Error: Sequence length must be between 45 and 100000. You entered {seq_length}")

    # Initialize lists to store sub-subregions
    subsubregions_0 = []
    subsubregions_15 = []

    # Process for sub-subregions starting at index 0
    remaining_seq_length = seq_length
    start_index = 0
    subsubregion_number = 1
    while remaining_seq_length > 0:
        if remaining_seq_length <= 45:
            subsubregions_0.append([subsubregion_number, remaining_seq_length, start_index, start_index + remaining_seq_length - 1])
            break
        else:
            subsubregions_0.append([subsubregion_number, 30, start_index, start_index + 29])
            remaining_seq_length -= 30
            start_index += 30
            subsubregion_number += 1

    # Process for sub-subregions starting at index 15
    if seq_length <= 45:
        subsubregions_15.append([1, seq_length, 0, seq_length - 1])
    else:
        remaining_seq_length = seq_length - 30
        start_index = 15
        subsubregion_number = 1
        while remaining_seq_length > 0:
            if remaining_seq_length <= 45:
                subsubregions_15.append([subsubregion_number, remaining_seq_length, start_index, start_index + remaining_seq_length - 1])
                break
            else:
                subsubregions_15.append([subsubregion_number, 30, start_index, start_index + 29])
                remaining_seq_length -= 30
                start_index += 30
                subsubregion_number += 1
    # Return the partitioned sub-subregions

    return subsubregions_0, subsubregions_15