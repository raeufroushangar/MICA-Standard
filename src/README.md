# Source Directory

This directory contains the source code files for the MICA project. Each file is organized by specific actions and functionalities.

## Overview

The sequence is partitioned into two sets of sub-subregions: one starting from index 0 and the other from index 15. Functions then assign mutations, scores, distances, and normalization values to each partition. Finally, `subsubregion_combiner.py` combines both sets of sub-subregions.

## File Descriptions

- **seq_partitioner.py**
  - `partition_seq_length`: Partitions a given sequence into sub-subregions of length 30-45. It generates two lists of sub-subregions: one starting from index 0 and the other from index 15.

- **mutation_and_weight_assignor.py**
  - Functions to assign mutations and scores:
  - `assign_mutations`: Assigns mutations to their respective sub-subregions.
  - `assign_positional_score`: Calculates positional scores based on distance.

- **normalizer.py**
  - `weighted_ave_normalization`: Normalizes the weighted impact values by calculating their average.

- **weight_calculator.py**
  - Functions to calculate scores:
  - `calculate_subsubregion_scores`: Calculates the scores for a sub-subregion by aggregating the weighted impact of the mutations within the sub-subregion.
  - `calculate_subregion_scores`: Calculates the scores for a subregion by aggregating the scores of its sub-subregions.
  - `calculate_region_scores`: Calculates the scores for a region by aggregating the scores of its subregions.

- **mutation_quantifier.py**
  - `quantify_significant_mutations`: Quantifies significant mutations by calculating positional scores for sub-subregions using the `partition_seq_length`, `assign_mutations`, and `calculate_subsubregion_scores` functions.

- **subsubregion_combiner.py**
  - Functions to combine and map scores and mutations from both sets of sub-subregions:
    - `extract_boundaries`: Extracts the boundaries of sub-subregions for combination.
    - `create_combined_intervals`: Creates combined intervals from the boundaries of both sets of sub-subregions.
    - `map_subsubregions_to_intervals`: Maps the sub-subregions to the created combined intervals.
    - `calculate_overlap_and_combine`: Calculates the overlap between sub-subregions and combines their scores and mutations.
    - `combine_and_map_scores_and_mutations`: Combines and maps the scores and mutations from both sets of sub-subregions to the final intervals.

- **mutation_file_reader.py**
  - `read_mutation_data`: Reads mutation positions and impact scores from a CSV file and returns a list of tuples or an error message.

- **data_processor.py**
  - Functions for processing data:
    - `process_mutation_data`: Processes mutation data and returns positional scores and combined data.
    - `process_region_details`: Extracts details for each region, including scores and subregion information.

- **result_writer.py**
  - Functions for writing results:
    - `write_results_to_csv`: Writes data to a CSV file.
    - `write_processed_data`: Writes processed data to CSV files.
    - `write_region_data_to_csv`: Writes region details and region scores to separate CSV files.

- **data_bucketer.py**
  - Functions for grouping data:
    - `bucket_subsubregions_to_subregions`: Groups sub-subregions into subregions.
    - `bucket_subregions_to_regions`: Groups subregions into regions.

- **plotter.py**
  - Functions for generating and saving plots:
    - `plot_positional_scores_by_mutation_positions`: Generates a scatter plot of positional scores by mutation positions.
    - `plot_positional_scores_by_subsubregion_ranges`: Generates a scatter plot of positional scores by sub-subregion ranges.
    - `plot_density_for_positional_scores`: Generates a density plot for positional scores.
    - `plot_positional_scores`: Generates a plot of positional scores for regions, subregions, and sub-subregions.
    - `generate_plots`: Generates and saves all plots to the MICA_result output directory.

- **heatmapper.py**
  - Functions for generating correlation heatmaps:
    - `plot_region_heatmap`: Generates a heatmap of correlations between regions based on their positional scores.
    - `plot_subregion_heatmap`: Generates a heatmap of correlations between subregions based on their positional scores.
    - `plot_subsubregion_heatmap`: Generates a heatmap of correlations between sub-subregions based on their positional scores.
