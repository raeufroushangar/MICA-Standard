import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def extract_plot_data(positional_scores):
    mutation_positions = []
    scores = []
    for subsubregion in positional_scores:
        start = subsubregion[0][2]
        end = subsubregion[0][3]
        score = subsubregion[2]
        for mutation in subsubregion[1]:
            mutation_positions.append(mutation[0])
            scores.append(score)
    return mutation_positions, scores

def plot_positional_scores_by_mutation_positions(positional_scores_0, positional_scores_15, combined_data, output_dir):
    mutation_positions_0, scores_0 = extract_plot_data(positional_scores_0)
    mutation_positions_15, scores_15 = extract_plot_data(positional_scores_15)

    combined_positions = []
    combined_scores = []
    for interval, mutations, score in combined_data:
        for mutation in mutations:
            combined_positions.append(mutation[0])
            combined_scores.append(score)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Scatter plot for mutation positions and positional scores
    scatter_0 = ax.scatter(mutation_positions_0, scores_0, color='blue', label='Start Index 0', alpha=0.4, s=20)
    scatter_15 = ax.scatter(mutation_positions_15, scores_15, color='green', label='Start Index 15', alpha=0.4, s=20)
    scatter_combined = ax.scatter(combined_positions, combined_scores, color='red', label='Combined', alpha=0.4, s=20)

    # Plot lines connecting the dots for each category
    # Start Index 0
    if mutation_positions_0:
        ax.plot(mutation_positions_0, scores_0, color='blue', linestyle='-', alpha=0.4)

    # Start Index 15
    if mutation_positions_15:
        ax.plot(mutation_positions_15, scores_15, color='green', linestyle='-', alpha=0.4)

    # Combined
    if combined_positions:
        ax.plot(combined_positions, combined_scores, color='red', linestyle='-', alpha=0.4)

    # Custom legend
    handles = [
        plt.Line2D([0], [0], marker='o', color='blue', markersize=10, label='Start Index 0', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='green', markersize=10, label='Start Index 15', linestyle='-'),
        plt.Line2D([0], [0], marker='o', color='red', markersize=10, label='Combined', linestyle='-')
    ]


    ax.set_xlabel('Mutation Position')
    ax.set_ylabel('Positional Score')
    ax.set_title('Positional Scores by Mutation Positions')
    ax.legend(handles=handles)

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_scores_by_mutation_positions.png')
    plt.savefig(plot_file)
    plt.close(fig)


# def plot_positional_weights_by_subsubregion_ranges(positional_weights_0, positional_weights_15, combined_data, output_dir):
#     def extract_plot_data(positional_weights):
#         subregion_intervals = []
#         mutation_positions = []
#         weights = []
#         for subsubregion in positional_weights:
#             start = subsubregion[0][2]
#             end = subsubregion[0][3]
#             weight = subsubregion[2]
#             if weight != 0:  # Filter out zero weights
#                 interval_label = f"{start}-{end}"
#                 subregion_intervals.append((start, end, weight, interval_label))
#                 for mutation in subsubregion[1]:
#                     mutation_positions.append(mutation[0])
#                     weights.append(weight)
#         return subregion_intervals, mutation_positions, weights

#     subregion_intervals_0, mutation_positions_0, weights_0 = extract_plot_data(positional_weights_0)
#     subregion_intervals_15, mutation_positions_15, weights_15 = extract_plot_data(positional_weights_15)

#     combined_intervals = []
#     combined_positions = []
#     combined_weights = []
#     for interval, mutations, weight in combined_data:
#         if weight != 0:  # Filter out zero weights
#             start, end = interval
#             interval_label = f"{start}-{end}"
#             combined_intervals.append((start, end, weight, interval_label))
#             for mutation in mutations:
#                 combined_positions.append(mutation[0])
#                 combined_weights.append(weight)

#     # Plotting the data
#     fig, ax = plt.subplots(figsize=(15, 8))

#     # Function to add labels and prevent overlap
#     def add_labels_with_prevention(ax, intervals, color):
#         last_position = None
#         for start, end, weight, label in intervals:
#             position = (start + end) / 2
#             y = weight
#             if last_position is not None and abs(position - last_position) < 5:
#                 position += 10 - abs(position - last_position)
#             ax.hlines(weight, start, end, colors=color, alpha=0.4)
#             ax.text(position, y, label, fontsize=9, color=color, ha='center', va='bottom')
#             last_position = position

#     # Plot lines for subregion intervals and add labels with overlap prevention
#     add_labels_with_prevention(ax, subregion_intervals_0, 'blue')
#     add_labels_with_prevention(ax, subregion_intervals_15, 'green')
#     add_labels_with_prevention(ax, combined_intervals, 'red')

#     # Scatter plot for mutation positions and positional weights
#     ax.scatter(mutation_positions_0, weights_0, color='blue', label='Start Index 0', alpha=0.7)
#     ax.scatter(mutation_positions_15, weights_15, color='green', label='Start Index 15', alpha=0.7)
#     ax.scatter(combined_positions, combined_weights, color='red', label='Combined', alpha=0.7)

#     # Plot lines connecting the dots for each category
#     # Start Index 0
#     if mutation_positions_0:
#         ax.plot(mutation_positions_0, weights_0, color='blue', linestyle='-', alpha=0.7)

#     # Start Index 15
#     if mutation_positions_15:
#         ax.plot(mutation_positions_15, weights_15, color='green', linestyle='-', alpha=0.7)

#     # Combined
#     if combined_positions:
#         ax.plot(combined_positions, combined_weights, color='red', linestyle='-', alpha=0.7)

#     # Custom legend
#     handles = [
#         plt.Line2D([0], [0], marker='o', color='blue', markersize=10, label='Start Index 0', linestyle='-'),
#         plt.Line2D([0], [0], marker='o', color='green', markersize=10, label='Start Index 15', linestyle='-'),
#         plt.Line2D([0], [0], marker='o', color='red', markersize=10, label='Combined', linestyle='-')
#     ]

#     # Labels and legend
#     ax.set_xlabel('Sub-subregions')
#     ax.set_ylabel('Positional Weight')
#     ax.set_title('Positional Weights by Sub-subregion Ranges')
#     ax.legend(handles=handles)

#     plt.tight_layout()

#     # Save the plot
#     plot_file = os.path.join(output_dir, 'positional_weights_by_subsubregion_ranges.png')
#     plt.savefig(plot_file)
#     plt.close(fig)

def plot_density_for_positional_scores(positional_scores_0, positional_scores_15, combined_data, output_dir):
    def extract_plot_data(positional_scores):
        indices = []
        scores = []
        for subsubregion in positional_scores:
            if len(subsubregion) < 3 or not subsubregion[0] or len(subsubregion[0]) < 4:
                continue  # Skip if the sub-subregion does not have the expected format
            start, end = subsubregion[0][2], subsubregion[0][3]
            score = subsubregion[2]
            indices.extend(range(start, end + 1))
            scores.extend([score] * (end - start + 1))
        return indices, scores

    def extract_combined_plot_data(combined_data):
        indices = []
        scores = []
        for subsubregion in combined_data:
            if len(subsubregion) < 3:
                continue  # Skip if the sub-subregion does not have the expected format
            start, end = subsubregion[0][0], subsubregion[0][1]
            score = subsubregion[2]
            indices.extend(range(start, end + 1))
            scores.extend([score] * (end - start + 1))
        return indices, scores

    # Extract data for plotting
    indices_0, scores_0 = extract_plot_data(positional_scores_0)
    indices_15, scores_15 = extract_plot_data(positional_scores_15)
    indices_combined, scores_combined = extract_combined_plot_data(combined_data)

    # Combine data into DataFrames for plotting with Seaborn
    data_0 = pd.DataFrame({'Index': indices_0, 'Score': scores_0, 'Type': 'Start Index 0'})
    data_15 = pd.DataFrame({'Index': indices_15, 'Score': scores_15, 'Type': 'Start Index 15'})
    data_combined = pd.DataFrame({'Index': indices_combined, 'Score': scores_combined, 'Type': 'Combined'})

    # Plot the data
    plt.figure(figsize=(15, 8))

    # KDE plot with less dense colors (more transparent)
    sns.kdeplot(data=data_0, x='Index', weights='Score', fill=True, color='blue', label='Start Index 0', alpha=0.2)
    sns.kdeplot(data=data_15, x='Index', weights='Score', fill=True, color='green', label='Start Index 15', alpha=0.2)
    sns.kdeplot(data=data_combined, x='Index', weights='Score', fill=True, color='red', label='Combined', alpha=0.2)

    # Labels and legend
    plt.xlabel('Sub-subregions')
    plt.ylabel('Density')
    plt.title('Positional Scores Density Plot')
    plt.legend(title='Type')

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_score_density_plot.png')
    plt.savefig(plot_file)
    plt.close()

def extract_plot_data_from_details(region_details):
    subsubregion_data = []
    subregion_data = []
    region_data = []
    mutation_positions = []
    mutation_scores = []

    for region_detail in region_details:
        # Extract region data
        start, end = region_detail['region_range']
        score = region_detail['region_score']
        region_data.append((start, end, score, region_detail['region_number']))

        for subregion_detail in region_detail['subregions']:
            # Extract subregion data
            sub_start, sub_end = subregion_detail['subregion_range']
            subregion_score = subregion_detail['subregion_score']
            if subregion_score != 0:
                subregion_data.append((sub_start, sub_end, subregion_score, f"{region_detail['region_number']},{subregion_detail['subregion_number']}"))

            for subsubregion_detail in subregion_detail['subsubregions']:
                # Extract sub-subregion data
                subsub_start, subsub_end = subsubregion_detail['subsubregion_range']
                subsubregion_score = subsubregion_detail['subsubregion_score']
                if subsubregion_score != 0:
                    subsubregion_data.append((subsub_start, subsub_end, subsubregion_score, f"{region_detail['region_number']},{subregion_detail['subregion_number']},{subsubregion_detail['subsubregion_number']}"))
                for mutation in subsubregion_detail['subsubregion_data'][1]:  # Assuming mutations are in subsubregion_detail['subsubregion_data'][1]
                    if isinstance(mutation, tuple) or isinstance(mutation, list):  # Ensure mutation is a tuple or list
                        mutation_positions.append(mutation[0])
                        mutation_scores.append(subsubregion_score)
    
    return subsubregion_data, subregion_data, region_data, mutation_positions, mutation_scores



# Function to add interval bars and labels
def add_interval_bars(ax, data, color, label, hierarchy=False):
    for start, end, score, *numbers in data:
        ax.hlines(score, start, end, colors=color, alpha=0.4, linewidth=5)
        if numbers:  # Ensure there are elements in numbers
            if hierarchy:
                ax.text((start + end) / 2, score, f"{numbers[0]}", fontsize=7, color=color, ha='center', va='bottom')
            else:
                ax.text((start + end) / 2, score, f"{numbers[0]}", fontsize=7, color=color, ha='center', va='bottom')




# Function to add labels and prevent overlap
def add_labels_with_prevention(ax, positions, scores, color):
    y_positions = []
    for i, (pos, score) in enumerate(zip(positions, scores)):
        y = score + 0.02
        while any(abs(y - prev_y) < 0.05 for prev_y in y_positions):
            y += 0.05
        y_positions.append(y)
        ax.text(pos, y, str(pos), fontsize=7, color=color, ha='center', va='bottom')

import matplotlib.ticker as ticker

def plot_data(data, label, color, title, output_dir, file_name, hierarchy=False, points=False):
    fig, ax = plt.subplots(figsize=(15, 8))

    if points:
        # Plot points for subsubregions
        for start, end, score, *numbers in data:
            mid_point = (start + end) / 2
            ax.scatter(mid_point, score, color=color, alpha=0.4, s=5)
            if hierarchy:
                ax.text(mid_point, score, f"{numbers[0]}", fontsize=7, color=color, ha='center', va='bottom')
            else:
                ax.text(mid_point, score, f"{numbers[0]}", fontsize=7, color=color, ha='center', va='bottom')
    else:
        # Add interval bars
        add_interval_bars(ax, data, color, label, hierarchy=hierarchy)

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color=color, linewidth=5 if not points else 0, marker='o' if points else '', markersize=3 if points else 0, label=label, alpha=0.4)
    ]

    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Score')
    ax.set_title(title)
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, file_name)
    plt.savefig(plot_file)
    plt.close(fig)



def plot_regions_subregions_positional_scores(region_details, output_dir):
    # Extract plot data
    subsubregion_data, subregion_data, region_data, mutation_positions, mutation_scores = extract_plot_data_from_details(region_details)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Add interval bars for regions and subregions
    add_interval_bars(ax, region_data, 'red', 'Regions')
    add_interval_bars(ax, subregion_data, 'green', 'Subregions')

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color='red', linewidth=5, label='Regions', alpha=0.4),
        plt.Line2D([0], [0], color='green', linewidth=5, label='Subregions', alpha=0.4),
    ]

    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Score')
    ax.set_title('Positional Scores of Regions, Subregions')
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_scores_of_regions_subregions.png')
    plt.savefig(plot_file)
    plt.close(fig)

def plot_positional_scores(region_details, output_dir):
    # Extract plot data
    subsubregion_data, subregion_data, region_data, mutation_positions, mutation_scores = extract_plot_data_from_details(region_details)

    # Plotting the data
    fig, ax = plt.subplots(figsize=(15, 8))

    # Add interval bars for regions and subregions
    add_interval_bars(ax, region_data, 'red', 'Regions')
    add_interval_bars(ax, subregion_data, 'green', 'Subregions')

    # Plot points for sub-subregions
    for start, end, score, *numbers in subsubregion_data:
        mid_point = (start + end) / 2
        ax.scatter(mid_point, score, color='blue', alpha=0.4, s=5)
        ax.text(mid_point, score, f"{numbers[0]}", fontsize=7, color='blue', ha='center', va='bottom')

    # Custom legend
    handles = [
        plt.Line2D([0], [0], color='red', linewidth=5, label='Regions', alpha=0.4),
        plt.Line2D([0], [0], color='green', linewidth=5, label='Subregions', alpha=0.4),
        plt.Line2D([0], [0], marker='o', color='blue', markersize=3, label='Sub-subregions', linestyle='', alpha=0.4)
    ]

    ax.set_xlabel('Sequence Length')
    ax.set_ylabel('Positional Score')
    ax.set_title('Positional Scores of Regions, Subregions, Sub-subregions')
    ax.legend(handles=handles, loc='center left', bbox_to_anchor=(1, 0.5))

    plt.tight_layout()

    # Save the plot
    plot_file = os.path.join(output_dir, 'positional_scores_of_regions_subregions_subsubregions.png')
    plt.savefig(plot_file)
    plt.close(fig)

    # Generate individual plots
    plot_data(region_data, 'Region', 'red', 'Positional Scores of Regions', output_dir, 'positional_scores_regions.png')
    plot_data(subregion_data, 'Subregion, Region', 'green', 'Positional Scores of Subregions', output_dir, 'positional_scores_subregions.png', hierarchy=True)
    plot_data(subsubregion_data, 'Sub-subregion, Subregion, Region', 'blue', 'Positional Scores of Sub-subregions', output_dir, 'positional_scores_subsubregions.png', hierarchy=True, points=True)



def generate_plots(positional_scores_0, positional_scores_15, combined_data, region_details, output_dir):
    """
    Generate and save all plots to the specified output directory.

    Args:
    - positional_scores_0: Positional scores starting from index 0
    - positional_scores_15: Positional scores starting from index 15
    - combined_data: Combined positional scores data
    - region_details: Detailed information about regions, subregions, and sub-subregions
    - output_dir: Directory to save the plots
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    plot_positional_scores_by_mutation_positions(positional_scores_0, positional_scores_15, combined_data, output_dir)
    # plot_positional_scores_by_subsubregion_ranges(positional_scores_0, positional_scores_15, combined_data, output_dir)
    plot_regions_subregions_positional_scores(region_details, output_dir)

    plot_density_for_positional_scores(positional_scores_0, positional_scores_15, combined_data, output_dir)
    plot_positional_scores(region_details, output_dir)
