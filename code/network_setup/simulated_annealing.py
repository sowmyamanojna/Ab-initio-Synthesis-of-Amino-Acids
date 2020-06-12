#Simulated Annealing

# Variables -
# Gi_1 = calculated G of initial compound 1
# Gi_2 = calculated G of initial compound 2
# Gf = calculated G of final compound if edge formation occurs.

# Number of cycles
n = 50
# Number of trials per cycle
m = 50
# Number of accepted solutions
na = 0.0
# Probability of accepting worse solution at the start
p1 = 0.7
# Probability of accepting worse solution at the end
p50 = 0.001
# Initial temperature
t1 = -1.0/math.log(p1)
# Final temperature
t50 = -1.0/math.log(p50)
# Fractional reduction every cycle
frac = (t50/t1)**(1.0/(n-1.0))

for i in range(n):
    print('Cycle: ' + str(i) + ' with Temperature: ' + str(t))
    for j in range(m):
        # Generate new trial points
        # iterate over the list of connected components and find a new trial compound that can be combined - find 2.
        initial_diff_G = Gf - (Gi_1 + Gi_2)
        
        if (initial_diff_G<0):
            # Initialize DeltaE_avg if a worse solution was found
            #   on the first iteration
            if (i==0 and j==0):
                diff_G = initial_diff_G
            # objective function is worse
            # generate probability of acceptance
            p = math.exp(-initial_diff_G/(diff_G * t))
            # determine whether to accept worse point
            if (random.random()<p):
                # accept the worse solution
                accept = True
            else:
                # don't accept the worse solution
                accept = False
        else:
            # objective function is lower, automatically accept
            accept = True
        if (accept==True):
            #create an edge between the 2 elements. (should satisfy valency and that should be checked earlier)
            # increment number of accepted solutions
            na = na + 1.0
            # update DeltaE_avg
            diff_G = (diff_G * (na-1.0) +  initial_diff_G) / na
    # Record the lowest G values at the end of every cycle (this was a part of the original code. we need not do this)
    # Lower the temperature for next cycle
    t = frac * t