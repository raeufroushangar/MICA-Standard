import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import pdist, squareform

def plot_region_heatmap(file_path, result_dir):
    data = pd.read_csv(file_path)

    # Filter out rows where Region Weight is zero
    data = data[data['Region Weight'] != 0]

    # Compute pairwise distances between region weights
    distances = pdist(data[['Region Weight']], metric='euclidean')

    # Perform hierarchical clustering
    linkage_matrix = linkage(distances, method='average')

    # Create a DataFrame with the distances in square form for seaborn clustermap
    distance_df = pd.DataFrame(squareform(distances), index=data['Region Number'], columns=data['Region Number'])

    # Create a clustermap with clustering only on the columns
    clustermap = sns.clustermap(distance_df, col_linkage=linkage_matrix, row_cluster=False, cmap='coolwarm', annot=True, figsize=(14, 10), annot_kws={"size": 8}, cbar_kws={"shrink": 0.5, "ticks": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]})

    # Add axis titles
    clustermap.ax_heatmap.set_xlabel('Region')
    clustermap.ax_heatmap.set_ylabel('Region')

    # Move the row labels to the left and rotate them by 90 degrees
    clustermap.ax_heatmap.yaxis.tick_left()
    clustermap.ax_heatmap.yaxis.set_label_position('left')
    clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), rotation=0)

    # Add title to the plot
    # clustermap.fig.suptitle('Regions Correlation Heatmap', y=1.05)

    # Save the plot
    plot_path = os.path.join(result_dir, 'region_correlation_heatmap.png')
    clustermap.savefig(plot_path)
    plt.close()

def plot_subregion_heatmap(file_path, result_dir):
    data = pd.read_csv(file_path)

    # Filter out rows where Subregion Weight is zero
    data = data[data['Subregion Weight'] != 0]

    # Combine region number and subregion number to form a unique identifier
    data['Subregion ID'] = data['Region Number'].astype(str) + '-' + data['Subregion Number'].astype(str)

    # Pivot the data to get subregions as columns
    subregion_weights = data.pivot_table(index='Subregion ID', values='Subregion Weight', aggfunc='mean')

    # Compute pairwise distances between subregion weights
    distances = pdist(subregion_weights, metric='euclidean')

    # Perform hierarchical clustering
    linkage_matrix = linkage(distances, method='average')

    # Create a DataFrame with the distances in square form for seaborn clustermap
    distance_df = pd.DataFrame(squareform(distances), index=subregion_weights.index, columns=subregion_weights.index)

    # Create a clustermap with clustering on the columns
    clustermap = sns.clustermap(distance_df, col_linkage=linkage_matrix, row_cluster=False, cmap='coolwarm', annot=True, figsize=(14, 10), annot_kws={"size": 8}, cbar_kws={"shrink": 0.5, "ticks": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]})

    # Add axis titles
    clustermap.ax_heatmap.set_xlabel('Region-Subregion')
    clustermap.ax_heatmap.set_ylabel('Region-Subregion')

    # Move the row labels to the left and rotate them by 0 degrees
    clustermap.ax_heatmap.yaxis.tick_left()
    clustermap.ax_heatmap.yaxis.set_label_position('left')
    clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), rotation=0)

    # Add title to the plot
    # clustermap.fig.suptitle('Subregions Correlation Heatmap', y=1.01)

    # Save the plot
    plot_path = os.path.join(result_dir, 'subregion_correlation_heatmap.png')
    clustermap.savefig(plot_path)
    plt.close()

def plot_subsubregion_heatmap(file_path, result_dir):
    data = pd.read_csv(file_path)

    # Filter out rows where Subsubregion Weight is zero
    data = data[data['Subsubregion Weight'] != 0]

    # Combine region number, subregion number, and subsubregion range to form a unique identifier
    data['Subsubregion ID'] = (data['Region Number'].astype(str) + '-' + 
                               data['Subregion Number'].astype(str) + '-' + 
                               data['Subsubregion Range'].astype(str))

    # Pivot the data to get subsubregions as columns
    subsubregion_weights = data.pivot_table(index='Subsubregion ID', values='Subsubregion Weight', aggfunc='mean')

    # Compute pairwise distances between subsubregion weights
    distances = pdist(subsubregion_weights, metric='euclidean')

    # Perform hierarchical clustering
    linkage_matrix = linkage(distances, method='average')

    # Create a DataFrame with the distances in square form for seaborn clustermap
    distance_df = pd.DataFrame(squareform(distances), index=subsubregion_weights.index, columns=subsubregion_weights.index)

    # Create a clustermap with clustering on the columns
    clustermap = sns.clustermap(distance_df, col_linkage=linkage_matrix, row_cluster=False, cmap='coolwarm', annot=True, figsize=(14, 10), annot_kws={"size": 8}, cbar_kws={"shrink": 0.5, "ticks": [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]})

    # Add axis titles
    clustermap.ax_heatmap.set_xlabel('Region-Subregion-Subsubregion')
    clustermap.ax_heatmap.set_ylabel('Region-Subregion-Subsubregion')

    # Move the row labels to the left and rotate them by 0 degrees
    clustermap.ax_heatmap.yaxis.tick_left()
    clustermap.ax_heatmap.yaxis.set_label_position('left')
    clustermap.ax_heatmap.set_yticklabels(clustermap.ax_heatmap.get_yticklabels(), rotation=0)

    # Add title to the plot
    # clustermap.fig.suptitle('Sub-subregions Correlation Heatmap', y=1.01)

    # Save the plot
    plot_path = os.path.join(result_dir, 'subsubregion_correlation_heatmap.png')
    clustermap.savefig(plot_path)
    plt.close()