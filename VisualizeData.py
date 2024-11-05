import pandas as pd
import matplotlib.pyplot as plt
import GetData as gd
ticker='AAPL'
data=gd.getData(ticker)

y1=data['Close']
y2=data['Volume']
x1=data['Close'].index
BarColor = []

Price=0
for y in y1:
    if y >= Price:
        BarColor.append('green')
        Price = y
    else:
        BarColor.append('red')
        Price = y
print(BarColor)

fig, ax1 = plt.subplots(figsize=(10, 6))


# Plotting the line chart
ax1.plot(x1, y1, color='blue', marker='o', label='Sine Wave')
ax1.set_title('Price Chart of '+ticker)
ax1.set_ylabel('Close Price', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

for i, txt in enumerate(y1):
    ax1.text(x1[i], y1[i], f"{y1[i]:.2f}", ha='center', va='bottom', color='blue', fontsize=10)



# Create a second y-axis for the bar chart
ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
bars=ax2.bar(x1, y2, color=BarColor, alpha=0.6, label='Random Values')
for bar in bars:
    yval = bar.get_height()  # Get the height of each bar
    ax2.text(bar.get_x(), yval/2, str(yval), ha='center', va='center',rotation=90)  # Annotate the bar



ax2.set_ylabel('Volume', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Show plot
plt.show()


