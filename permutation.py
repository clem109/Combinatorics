# __author__ = 'clementvenard'
#
#
# # Method to calculate the factorial of a number and hence the number of permutations as well as generate an initial
# # list of the permutations
#
number = (int(input("Enter number to calculate the number of permutations: ")))
initial_number = number
permutation_list = list(range(1, number + 1))

for x in range(1, number):
    number = number * x

print("The number of permutations is: ", number)

print("Lexographical order:", 1, "-- Value:", permutation_list)

for y in range(1, number):
    n = initial_number-1
    for z in range(1, initial_number):
        if permutation_list[n] > permutation_list[n-1]:
            suffix = permutation_list[n:]
            prefix = permutation_list[:n]
            s = 0
            newone = []
            x = 0
            for x in suffix:
                if suffix[s] > permutation_list[n-1]:
                    newone.append(suffix[s])
                    s = s + 1
                    x = x + 1
                    newone.sort()

                else:
                    x = x + 1
                    s = s + 1

            prefix[-1], newone[0] = newone[0], prefix[-1]

            in_first = set(newone)
            in_second = set(suffix)

            in_second_but_not_in_first = in_first - in_second

            result = suffix + list(in_second_but_not_in_first)

            final = list(set(result) - set(prefix))
            final.sort()

            final_value = prefix + final

        else:
            n = n - 1
            x = 0

    print("Lexographical order:", y + 1, "-- Value:", final_value)
    permutation_list = final_value


