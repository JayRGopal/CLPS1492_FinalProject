import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects

def plot_epoch_vs_pcterr(csv_file, line_color='blue', title_font_size=20, 
                         label_font_size=30, ticks_font_size=15, plot_title='Epoch vs Percent Error'):
    """
    Plots Percent Error vs Epoch from a CSV file.

    :param csv_file: Path to the CSV file.
    :param line_color: Color of the plot line.
    :param title_font_size: Font size of the plot title.
    :param label_font_size: Font size of the x and y axis labels.
    :param ticks_font_size: Font size of the x and y axis ticks.
    :param plot_title: Title of the plot.
    """
    # Load CSV
    data = pd.read_csv(csv_file)

    # Plotting
    plt.figure(figsize=(12, 9))
    plt.plot(data['|Epoch'], data['#PctErr'], color=line_color)
    plt.title(plot_title, fontsize=title_font_size)
    plt.fill_between(data['|Epoch'], data['#PctErr'], color=line_color, alpha=0.3)  # Shadow effect
    plt.xlabel('Epoch', fontsize=label_font_size)
    plt.ylabel('Percent Error', fontsize=label_font_size)
    plt.xticks(fontsize=ticks_font_size)
    plt.yticks(fontsize=ticks_font_size)

    # Adding shadow effect
    # plt.gca().get_lines()[0].set_path_effects([
    #     PathEffects.withStroke(linewidth=5, foreground=line_color, alpha=0.3)
    # ])

    # Save the plot
    plt.savefig(f'{plot_title}.png')

# Example usage
plot_epoch_vs_pcterr('topdown_and_latent.csv', line_color='gray', title_font_size=34, 
                     label_font_size=35, ticks_font_size=25, plot_title='Training Plot for Hybrid Network')

