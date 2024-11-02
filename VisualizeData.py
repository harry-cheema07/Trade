import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd

data=gd.getData('MSFT')

plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.plot((data['Close'].index), (data['Close']), marker='o')  # Line plot
plt.title('Line Graph Title')  # Title of the graph
plt.xlabel('Date')  # X-axis label
plt.ylabel('Closed Price')  # Y-axis label
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)  # Add grid lines for better visibility
plt.tight_layout()  # Adjust layout to avoid clipping
plt.show()  # Display the plot