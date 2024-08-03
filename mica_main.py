import warnings
warnings.filterwarnings("ignore", category=UserWarning, message="Unable to import Axes3D")

import os
import argparse
from src.data_processor import process_mutation_data, process_region_details
from src.result_writer import write_processed_data, write_region_data_to_csv
from src.data_bucketer import bucket_subsubregions_to_subregions, bucket_subregions_to_regions
from src.plotter import generate_plots
# from src.heatmapper import plot_region_heatmap, plot_subregion_heatmap, plot_subsubregion_heatmap

def run_ecmpia_analysis(mutation_file_path, result_dir, seq_length, plot=False):
    """
    Run the ECMPIA analysis using the specified mutations_data.csv file and result directory.

    Args:
    - mutation_file_path (str): Path to the mutations_data.csv file.
    - result_dir (str): Path to the directory where the results will be stored.
    - seq_length (int): Length of the DNA sequence.
    - plot (bool): Whether to plot the data or not.
    """

    try:
        # Process mutation data
        positional_scores_0_data, positional_scores_15_data, combined_data_csv = process_mutation_data(mutation_file_path, seq_length)

        # Write processed data to CSV files if processing was successful
        if positional_scores_0_data is not None and positional_scores_15_data is not None and combined_data_csv is not None:
            write_processed_data(result_dir, positional_scores_0_data, positional_scores_15_data, combined_data_csv)
            
            # Call the bucket_subsubregions_to_subregions function
            subregions = bucket_subsubregions_to_subregions(combined_data_csv)

            # Call the bucket_subregions_to_regions function
            regions = bucket_subregions_to_regions(subregions)
            
            # Process region details
            region_details = process_region_details(regions)

            # Write region details to CSV
            write_region_data_to_csv(result_dir, region_details)

            # Generate and save plots if the plot argument is True
            if plot:
                generate_plots(positional_scores_0_data, positional_scores_15_data, combined_data_csv, region_details, result_dir)
                # plot_region_heatmap(region_weights_file_path, result_dir)
                # plot_subregion_heatmap(region_details_file_path, result_dir)
                # plot_subsubregion_heatmap(region_details_file_path, result_dir)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run ECMPIA analysis on mutation data.")
    parser.add_argument('-f', '--file', type=str, required=True, help="Path to the mutations_data.csv file")
    parser.add_argument('-r', '--result_dir', type=str, required=True, help="Path to the ECMPIA result directory")
    parser.add_argument('-l', '--length', type=int, required=True, help="Length of the DNA sequence")
    parser.add_argument('--plot', action='store_true', help="Option to plot the data")
    args = parser.parse_args()

    run_ecmpia_analysis(args.file, args.result_dir, args.length, args.plot)
