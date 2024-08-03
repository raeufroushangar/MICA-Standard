import os
import csv
import pandas as pd

def write_results_to_csv(file_path, data, headers):
    """
    Write data to a CSV file, creating a new directory each time.

    Args:
    - file_path (str): Path to the output file.
    - data (list): List of data to write.
    - headers (list): List of headers for the CSV file.
    """
    # Create directory, assuming it does not exist
    directory = os.path.dirname(file_path)
    os.makedirs(directory, exist_ok=True)

    # Write data to CSV
    df = pd.DataFrame(data, columns=headers)
    df.to_csv(file_path, index=False)

def write_processed_data(result_dir, positional_scores_0_data, positional_scores_15_data, combined_data_csv):
    """
    Write processed data to CSV files in the specified result directory.

    Args:
    - result_dir (str): Path to the directory where the results will be stored.
    - positional_scores_0_data (list): Data for positional scores starting at index 0.
    - positional_scores_15_data (list): Data for positional scores starting at index 15.
    - combined_data_csv (list): Combined and mapped sub-subregions data.
    """
    # Define file paths
    positional_scores_0_file = os.path.join(result_dir, "positional_scores_0.csv")
    positional_scores_15_file = os.path.join(result_dir, "positional_scores_15.csv")
    combined_data_file = os.path.join(result_dir, "combined_data.csv")

    # Write results to CSV files
    write_results_to_csv(positional_scores_0_file, positional_scores_0_data, ['Sub-subregion', 'Mutations', 'Positional Score'])
    write_results_to_csv(positional_scores_15_file, positional_scores_15_data, ['Sub-subregion', 'Mutations', 'Positional Score'])
    write_results_to_csv(combined_data_file, combined_data_csv, ['Interval', 'Mutations', 'Average Score'])

def write_region_data_to_csv(result_dir, region_details):
    """
    Write region details and region scores to CSV files in the specified result directory.

    Args:
    - result_dir (str): Path to the directory where the results will be stored.
    - region_details (list): List of region details to write.
    """
    # Define file paths for region details and region scores
    region_details_file = os.path.join(result_dir, "region_details.csv")
    region_scores_file = os.path.join(result_dir, "region_scores.csv")

    # Prepare the data for region details
    region_details_data = []
    for detail in region_details:
        region_number = detail['region_number']
        region_range = detail['region_range']
        region_score = detail['region_score']
        for subregion_detail in detail['subregions']:
            subregion_number = subregion_detail['subregion_number']
            subregion_range = subregion_detail['subregion_range']
            subregion_score = subregion_detail['subregion_score']
            for subsubregion_detail in subregion_detail['subsubregions']:
                subsubregion_number = subsubregion_detail['subsubregion_number']
                subsubregion_data = subsubregion_detail['subsubregion_data']
                subsubregion_range = subsubregion_detail['subsubregion_range']
                subsubregion_score = subsubregion_detail['subsubregion_score']
                region_details_data.append([
                    region_number, region_range, region_score,
                    subregion_number, subregion_range, subregion_score,
                    subsubregion_number, subsubregion_range, subsubregion_score
                ])
    
    # Write region details to CSV
    write_results_to_csv(region_details_file, region_details_data, [
        'Region Number', 
        'Region Range',
        'Region Score',
        'Subregion Number', 
        'Subregion Range',
        'Subregion Score',
        'Subsubregion Number',
        'Subsubregion Range',
        'Subsubregion Score'
    ])

    # Prepare the data for region scores
    region_scores_data = [
        [detail['region_number'], detail['region_range'], detail['region_score']]
        for detail in region_details
    ]
    
    # Write region scores to CSV
    write_results_to_csv(region_scores_file, region_scores_data, [
        'Region Number', 'Region Range', 'Region Score'
    ])
