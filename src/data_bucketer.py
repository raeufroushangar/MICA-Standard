def bucket_subsubregions_to_subregions(combined_data, subsubregions_per_subregion=20):
    """
    Groups sub-subregions into subregions.

    Args:
    - combined_data (list): List of combined sub-subregions data.
    - subsubregions_per_subregion (int, optional): Number of sub-subregions per subregion. Default is 20.

    Returns:
    - list: List of subregions, each containing a specified number of sub-subregions.
    """
    subregions = [
        combined_data[i:i + subsubregions_per_subregion]
        for i in range(0, len(combined_data), subsubregions_per_subregion)
    ]
    return subregions

def bucket_subregions_to_regions(subregions, subregions_per_region=10):
    """
    Groups subregions into regions.

    Args:
    - subregions (list): List of subregions data.
    - subregions_per_region (int, optional): Number of subregions per region. Default is 10.

    Returns:
    - list: List of regions, each containing a specified number of subregions.
    """
    num_subregions_per_region = len(subregions) // subregions_per_region
    if len(subregions) % subregions_per_region != 0:
        num_subregions_per_region += 1
    
    regions = [subregions[i:i + num_subregions_per_region] for i in range(0, len(subregions), num_subregions_per_region)]
    return regions
