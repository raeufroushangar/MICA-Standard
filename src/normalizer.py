import numpy as np

def weighted_ave_normalization(total_impact_score, length):
    """
    Normalize the total impact score by the length of the subsubregion.

    Args:
    - total_impact_score (float): The total impact score for a subsubregion.
    - length (int): The length of the subsubregion.

    Returns:
    - float: The normalized value, with NaNs replaced by 0.
    """
    # Calculate the normalized impact score
    if length > 0:
        normalized_value = total_impact_score / length
    else:
        normalized_value = 0

    # Replace NaN values with 0
    return np.nan_to_num(normalized_value)
