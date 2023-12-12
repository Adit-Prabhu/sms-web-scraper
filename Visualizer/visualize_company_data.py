import re
import matplotlib.pyplot as plt
import numpy as np

def read_data(file_path, max_categories=60, exclude_categories=None):
    categories = []
    message_counts = []

    with open(file_path, 'r') as file:
        for line in file:
            match = re.search(r'([^:]+):\s*(\d+)', line)
            if match:
                category = match.group(1).strip()
                count = int(match.group(2).strip())

                # Exclude specified categories
                if exclude_categories is not None and category in exclude_categories:
                    continue

                categories.append(category)
                message_counts.append(count)

                # Stop reading after reaching the specified number of categories
                if len(categories) >= max_categories:
                    break

    return categories, message_counts

def plot_bubble_chart(categories, message_counts, output_file='message_distribution_bubble.png'):
    # Sorting categories based on message counts
    sorted_indices = np.argsort(message_counts)[::-1]
    categories = [categories[i] for i in sorted_indices]
    message_counts = [message_counts[i] for i in sorted_indices]

    # Use logarithmic scale for bubble sizes
    sizes = np.log(message_counts)

    # Set up color gradient
    colors = np.arange(len(categories))

    plt.figure(figsize=(12, 8))
    plt.scatter(message_counts, range(len(categories)), s=sizes*30, c=colors, cmap='viridis', alpha=0.7)

    for i, (category, count) in enumerate(zip(categories, message_counts)):
        # Horizontal labels centered on circle center
        plt.text(count, i, f'{category}: {count}', va='center', ha='center')

    plt.xlabel('Message Counts (log scale)')
    plt.title('Distribution of Messages Among Categories')
    plt.gca().invert_yaxis()  # To have the highest count at the top

    # Add colorbar for reference
    cbar = plt.colorbar()
    cbar.set_label('Color Gradient (for reference)')

    plt.axis('off')  # Turn off axis labels, ticks, and the square border
    plt.savefig(output_file)  # Save the plot as an image file
    plt.show()

def main():
    file_path = 'parsed_companies.txt'
    max_categories = 30
    exclude_categories = ["verification", "security", "secure", "payment", "confirmation", "this", "the", "Total Parsed Messages", "Unamed Chinese Company"]
    categories, message_counts = read_data(file_path, max_categories=max_categories, exclude_categories=exclude_categories)
    #print(categories)
    plot_bubble_chart(categories, message_counts)

if __name__ == "__main__":
    main()
