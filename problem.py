# Part A
# Really simple way of implementation, using basic dice config, show
# the combos you can make, then show the combinations you can make in the shape of the matrix. 
# Then print the distribution of getting each of these rolls. 
# This implementation will be used more to show each of the implementation of the doomed dice to show
# that they have the exact same distributions. 
from itertools import permutations

print("\n\n\nPart A:")
die_A = [1, 2, 3, 4, 5, 6]
die_B = [1, 2, 3, 4, 5, 6]
sides_A = len(die_A)
sides_B = len(die_B)
total_combo = sides_A * sides_B
print("Total combo is: " + str(total_combo))
num_arr = []
s = {}
for x in die_A:
    for j in die_B:
        num_arr.append(x+j)
        print(x + j, end='')
        print(" ", end='')
    print("\n")
s = set(num_arr)
for x in s:
    print(str(x) + " " + str(num_arr.count(x)) + "/36")
    
# Part B
# Can brute force, checking every possibility through 6 nested loops,
# but that would take a long time and not be very efficient, as shown here.  ->
print("\n\n\nPart B BRUTE FORCE\n")

# Function to calculate the probability distribution for a given die configuration
def calculate_distribution(die1, die2):
    distribution = {}
    for i in range(2, 13):
        distribution[i] = 0

    # Calculate the distribution
    for d1 in die1:
        for d2 in die2:
            sum_val = d1 + d2
            distribution[sum_val] += 1

    # Calculate the total number of rolls
    total_rolls = 0
    for count in distribution.values():
        total_rolls += count

    # Calculate the final distribution percentages
    final_distribution = {}
    for sum_val, count in distribution.items():
        final_distribution[sum_val] = count / total_rolls

    return final_distribution

def undoom_dice_brute_force():
    # Original probability distribution
    original_probabilities = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
                              8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}


    # Brute force through all combinations for Die A
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                for d in range(1, 5):
                    for e in range(1, 5):
                        for f in range(1, 5):
                            new_die_a = [a, b, c, d, e, f]
                            # Generate unique combinations for Die B
                            for new_die_b in permutations(range(1, 9), 6):
                                new_distribution = calculate_distribution(new_die_a, new_die_b)
                                if new_distribution == original_probabilities:
                                    return new_die_a, list(new_die_b)
    return None

print()
print()
undoomed_dice = undoom_dice_brute_force()
print(undoomed_dice)

# Printing to show solution, same as Part A
die_A = undoomed_dice[0]
die_B = undoomed_dice[1]
sides_A = len(die_A)
sides_B = len(die_B)

num_arr = []
s = {}
for x in die_A:
    for j in die_B:
        num_arr.append(x+j)
        print(x + j, end='')
        print(" ", end='')
    print("\n")
s = set(num_arr)
for x in s:
    print(str(x) + " " + str(num_arr.count(x)) + "/36")
    
    
# This function spits out the right answer, but takes quite long to complete. 
# Since Dice B can have as many spots as needed, this means that we need constraints.
# Since we need combinations that give us 2 and 12, the low and top end of the combos given by the 
# dice, this means that both dice need to have 1. But since Dice A can only get up to 4, this leads
# to the conclusion that Dice B would have a max of 8, which is shown in the brute force as well.
# 
# Logic: 
# Find all possibilities of each dice recursively using the conditions.
# From here, we can compare distributions and see if there's a match, then return accordingly.
#
# Implementation:

die_A = [1,2,3,4,5,6]
die_B = [1,2,3,4,5,6]



def undoom_v2(die_A, die_B):
    original_probabilities = {2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36, 7: 6/36,
                              8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36}
    spots_A = [1, 2, 3, 4]
    # This is the base list fed into the functions because the dice need both min and max to have the 
    # same distributions. 
    base_A = [1, 4]
    sides_left = 4
    all_poss_A = []
    # Calculates all possibilities for Dice A recursively with replacement. 
    def poss_A(spots, left, all_poss, base):
        # Base case, if you fill up all 6 spots, then add the possibility to the list
        # and continue. 
        if (left == 0):
            all_poss.append(list(base))
            return all_poss
        for spot in spots:
            poss_A(spots, left - 1, all_poss, base + [spot])
        return all_poss
    spots_B = [1, 2, 3, 4, 5, 6, 7, 8]
    base_B = [1, 8]
    all_poss_B = []
    sides_left = 4
    # Calculates all possibilities for Dice B without replacement.
    
    def poss_B(spots, left, index, all_poss, base):
        if (left == 0):
            all_poss.append(list(base))
            return all_poss
        for i in range(index,len(spots)):
            poss_B(spots, left - 1, i+1, all_poss, base + [spots[i]])
        return all_poss



    die_A_result = poss_A(spots_A, sides_left, all_poss_A, base_A)
    die_B_result = poss_B(spots_B, sides_left, 0, all_poss_B, base_B)
    
    # Check for each dice in both possible lists, compare distributions and if they are
    # equal to the target distribution, then return
    for die in die_A_result:
        for die_2 in die_B_result:
            new_possibilities = calculate_distribution(die, die_2)
            if (original_probabilities == new_possibilities):
                return sorted(die), sorted(die_2)
print()
print()
print("Part B RECURSIVE SOLUTION")

dice = undoom_v2(die_A, die_B)


# Printing to show solution, same as Part A

die_A = dice[0]
die_B = dice[1]
print(die_A)
print(die_B)
print()
sides_A = len(die_A)
sides_B = len(die_B)

num_arr = []
s = {}
for x in die_A:
    for j in die_B:
        num_arr.append(x+j)
        print(x + j, end='')
        print(" ", end='')
    print("\n")
s = set(num_arr)
for x in s:
    print(str(x) + " " + str(num_arr.count(x)) + "/36")


    
        
            
    



