import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

def generate_heatmap(csv_path, output_png_path):
    '''
    Makes a heatmap to find ideal hyperparams (minimizing First Zero) for our simulation!
    '''

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Extract relevant columns (for Jay's Top Down network)
    x = df['#AssocToOut2']
    y = df['#OutToAssoc']
    z = df['#FirstZero']

    # Create grid coordinates for interpolation
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate
    zi = griddata((x, y), z, (xi, yi), method='cubic') 
    #zi = griddata((x, y), z, (xi, yi), method='linear')
    #zi = griddata((x, y), z, (xi, yi), method='nearest')

    # Find the minimum value of z (FirstZero) and its coordinates
    min_idx = np.argmin(zi)
    min_x_idx, min_y_idx = np.unravel_index(min_idx, zi.shape)
    min_x = xi[min_x_idx, min_y_idx]
    min_y = yi[min_x_idx, min_y_idx]
    min_zi = zi[min_x_idx, min_y_idx]

    # Create the plot with enhancements
    plt.figure(figsize=(14, 11))
    contour_plot = plt.contourf(xi, yi, zi, levels=15, cmap='viridis')
    cbar = plt.colorbar(contour_plot, label='First Zero')
    cbar.set_label('First Zero', size=25)
    cbar.ax.tick_params(labelsize=25)
    plt.scatter(x, y, c=z, cmap='viridis', edgecolor='black', s=80)  # Larger black X's
    plt.xlabel('AssocToOut2', fontsize=25)
    plt.ylabel('OutToAssoc', fontsize=25)
    plt.title('Hyperparameter Search: Top Down Network', fontsize=30)
    plt.xticks(fontsize=20)  # Larger tickmarks
    plt.yticks(fontsize=20)

    # Save the plot as a PNG file
    plt.savefig(output_png_path, format='png')

    # Return the minimum values
    return min_x, min_y, min_zi


minx, miny, minz = generate_heatmap('topdown_hyperparams.csv', 'topdown_hyperparams_plot.png')

print(f'AssocToOut2={minx}, OutToAssoc={miny}, FirstZero={minz}')