import random
import numpy

def DoND():

	stay = 0

	switch = 0

	for i in range(10000):

		cases = []

		values = []

		for j in range (25):

			cases.append("Case " + str(j+1))

		values = [1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

		from numpy import random

		x = random.randint(len(cases))

		player_case = cases[x]
		
		player_value = values[x]

		#print("The player chooses " + player_case + " valued at $" + str(values[x]) + ".")

		cases.pop(x)

		values.pop(x)

		y = random.randint(len(cases))

		final_case = cases[y]

		final_value = values[y]

		#print("The final case is " + final_case + " valued at $" + str(values[y]) + ".")

		cases.pop(y)

		values.pop(y)

		offer = ((player_value + final_value) / 2) * 0.4

		#print("The banker's offer is $" + str(offer))

		if final_value > player_value:

			switch = switch + 1

		else:

			stay = stay + 1

	print("Number of switches: " + str(switch) + "." + " Player case is better: " + str(stay) + ".")


DoND()


