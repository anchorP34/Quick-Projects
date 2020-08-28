# How Likely was the Giolito no hitter?
# Using the assumptions that the player's batting averages heading
# into the game were their "true" batting averages, we can use
# probabilities to show how likely it was for each batter to get out
# for each plate appearance

lineup = {
    1: .273 #Gonzales, walked in the 
    , 2: .200 # Frazier 
    , 3: .220 # Reynolds
    , 4: .205 # Bell
    , 5: .151 # Polanco
    , 6: .200 # Riddle
    , 7: .244 # Tucker
    , 8: .167 # Dyson
    , 9: .182 # Murphy 2 at bats
}

# Probability that will be multiplied
final_prob = 1

batter_walk = 10 # Tenth batter was a walk so ignore it
pinch_hitter = 27 # The 27th batter was the pinch hitter

# There was 28 plate appearances due to 1 walk
plate_appearance = 1
keep_going = True

while keep_going:
    for player in lineup:
        # If it was a walk, skip the plate appearance
        if plate_appearance == batter_walk:
            plate_appearance += 1
            continue

        elif plate_appearance == pinch_hitter:
            lineup[player] = .133 # Osuna 1 at bat in place for Murphy. Osuna hit .133
            final_prob *= (1-lineup[player])
            
        elif plate_appearance > 28:
            keep_going = False
            break

        # Final probability multiplied by the probability of getting out
        else:
            final_prob *= (1-lineup[player])  

        # Add 1 to plate appearance
        print('Plate Appearance: {}\t Player Chance of Getting Out: {}\t New Probability: {}'.format(plate_appearance,1- lineup[player], final_prob))
        plate_appearance += 1

    # Show what the final probability was
print('Final Likelihood of No Hitter: {}'.format(final_prob))