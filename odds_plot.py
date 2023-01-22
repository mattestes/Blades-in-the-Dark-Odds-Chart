from matplotlib import pyplot as plt
import numpy as np

# https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
# https://www.geeksforgeeks.org/create-a-stacked-bar-plot-in-matplotlib/

import dice_odds

plt.figure(figsize=(10,6))

max_dice = 4

num_dice = []
failure_odds = []
partial_success_odds = []
full_success_odds = []
critical_success_odds = []

for i in range(max_dice, -1, -1):
	num_dice.append(str(i))
	odds = dice_odds.get_all_odds(i)
	failure_odds.append(odds[0] * 100)
	partial_success_odds.append(odds[1] * 100)
	full_success_odds.append(odds[2] * 100)
	critical_success_odds.append(odds[3] * 100)

failure_odds = np.array(failure_odds)
partial_success_odds = np.array(partial_success_odds)
full_success_odds = np.array(full_success_odds)
critical_success_odds = np.array(critical_success_odds)

red_color = "#F2575F"
failure_bar = plt.barh(num_dice, failure_odds, color=red_color)
yellow_color = "#FFD135"
partial_success_bar = plt.barh(num_dice, partial_success_odds, left=failure_odds, color=yellow_color)
green_color = "#59DF82"
full_success_bar = plt.barh(num_dice, full_success_odds, left=partial_success_odds + failure_odds, color=green_color)
blue_color = "#6FD3FF"
critical_success_bar = plt.barh(num_dice, critical_success_odds, left=full_success_odds + partial_success_odds + failure_odds, color=blue_color)


# gca() stands for Get Current Axes; this returns the axes object
# https://www.statology.org/matplotlib-hide-axis/
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# https://www.geeksforgeeks.org/how-to-remove-ticks-from-matplotlib-plots/
plt.tick_params(left = False)

plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Dice Rolled", size=15)
plt.xlabel("% Chance", size=15)
plt.title("Blades in the Dark Success Odds", size=15)

plt.legend((failure_bar[0], partial_success_bar[0], full_success_bar[0], critical_success_bar[0]), 
	("Failure", "Partial Success", "Full Success", "Critical Success"),
	framealpha=0.9)

# This sets up the % labels on each of the sections
for bar in ax.patches:
	pct_display = str(round(bar.get_width())) + "%" if bar.get_width() > 0 else ""
	x_center = bar.get_x() + bar.get_width() / 2 if bar.get_width() > 5 else bar.get_x() + bar.get_width() + 3
	ax.text(x_center, bar.get_y() + bar.get_height() / 2, pct_display, ha='center', va='center', size=15)

plt.show()