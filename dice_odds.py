
def pct_format(num):
	return str(round(num * 100)) + "%"


def lowest_is_6(num_dice):
	# Odds that all dice are 6
	return (1 / 6) ** num_dice

def lowest_is_45(num_dice):
	# Odds that all dice are 4/5/6, with the odds that they're all 6 subtracted
	return (3 / 6) ** num_dice - lowest_is_6(num_dice)

def lowest_is_123(num_dice):
	odds = 0
	for i in range(num_dice):
		odds += (1 - odds) * (3 / 6)
	return odds

def highest_is_123(num_dice):
	return (3 / 6) ** num_dice

def highest_is_45(num_dice):
	# Odds that all dice are between 1-5, with the odds that they're all 1/2/3 subtracted
	return (5 / 6) ** num_dice - highest_is_123(num_dice)

def highest_is_6(num_dice):
	odds = 0
	for i in range(num_dice):
		odds += (1 - odds) * (1 / 6)
	return odds

def one_6(num_dice):
	return (1 / 6) * (5 / 6) ** (num_dice - 1) * num_dice

def two_plus_6(num_dice):
	return highest_is_6(num_dice) - one_6(num_dice)


def get_all_odds(num_dice):
	if num_dice == 0:
		return [lowest_is_123(2), lowest_is_45(2), lowest_is_6(2), 0]
	else:
		return [highest_is_123(num_dice), highest_is_45(num_dice), one_6(num_dice), two_plus_6(num_dice)]


if __name__ == "__main__":
	print("0, failure: " + pct_format(lowest_is_123(2)))
	print("0, partial success: " + pct_format(lowest_is_45(2)))
	print("0, full success: " + pct_format(lowest_is_6(2)))
	print("0, critical success: " + pct_format(0))
	print()

	for i in range(1, 5):
		print(str(i) + ", failure: " + pct_format(highest_is_123(i)))
		print(str(i) + ", partial success: " + pct_format(highest_is_45(i)))
		# print(str(i) + ", full/crit success: " + pct_format(highest_is_6(i)))
		print(str(i) + ", full success: " + pct_format(one_6(i)))
		print(str(i) + ", critical success: " + pct_format(two_plus_6(i)))
		print()