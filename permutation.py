# __author__ = 'clement venard'
#
#
#
#

# Prompt for user input
number = (int(input("Enter number to calculate the number of permutations: ")))
initial_number = number
# Create a list of numbers from 1 to number to be permutated
permutation_list = list(range(1, number + 1))

# Method to determine the number of permutations
for x in range(1, number):
    number = number * x

print("The number of permutations is: ", number)
print("Lexographical order:", 1, "-- Value:", permutation_list)

# Method to display each permutation using a lexographical order
for y in range(1, number):
    n = initial_number-1
    for z in range(1, initial_number):

        # If the last value in the order is greater than the one after it, add this to the suffix, iterate through
        # until you have a list of suffix's
        if permutation_list[n] > permutation_list[n-1]:
            suffix = permutation_list[n:]
            prefix = permutation_list[:n]
            s = 0
            newone = []
            x = 0
            for x in suffix:
                # Check if the suffix value is greater than the last value of the prefix and create a new list with these
                # values, this will be used to check which suffix value to swap with the last value of the prefix
                if suffix[s] > permutation_list[n-1]:
                    newone.append(suffix[s])
                    s = s + 1
                    x = x + 1
                    newone.sort()

                else:
                    x = x + 1
                    s = s + 1

            # Swap the last value of the prefix with the first of the new list of possible prefix's
            prefix[-1], newone[0] = newone[0], prefix[-1]

            # Create sets to be able to add and replace missing and duplicate values in the suffix.
            in_first = set(newone)
            in_second = set(suffix)

            in_second_but_not_in_first = in_first - in_second

            result = suffix + list(in_second_but_not_in_first)

            final_suffix = list(set(result) - set(prefix))
            final_suffix.sort()

            # Store this new list as a permutation_list by concatenating the prefix with the final_suffix
            final_value = prefix + final_suffix


        else:
            n = n - 1
            x = 0

    print("Lexographical order:", y + 1, "-- Value:", final_value)
    permutation_list = final_value


