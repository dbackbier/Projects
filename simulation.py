import random

# Team names for final output, will just use 1 and 2 in code
team_1_name = input("Enter home team: ").strip().upper()
team_2_name = input("Enter away team: ").strip().upper()

neutral = input("Neutral site? (y/n) ").strip()
if (neutral == "y"):
    adv = 1
else:
    adv = 1.5

# Variables
wins_1 = 0
wins_2 = 0
ties = 0

# Lists
# 65%
common_low = [10, 13, 14]
common_mid = [17, 20, 24, 27]
common_high = [28, 31, 34]

# 30%
uncommon_low = [3, 6, 7, 9]
uncommon_mid = [16, 21, 23, 26]
uncommon_high = [30, 35, 38, 41]

# 4.95%
rare_low = [0, 11, 12, 15]
rare_mid = [18, 22]
rare_high = [29, 33, 36, 37, 40, 42, 45]

# 0.05%
very_rare_low = [2, 5, 8]
very_rare_mid = [19, 25]
very_rare_high = [32, 39, 43, 44, 46, 47, 48, 49, 50, 51, 52]

# Find amount of times user wants to simulate
num_sim = int(input("How many times would you like to simulate the game(the more sims the more accurate the data)? "))

# Find rankings
team_1_off = int(input("Enter home team's offense ranking (1 through 32): "))
team_1_def = int(input("Enter home team's defense ranking (1 through 32): "))
team_2_off = int(input("Enter away team's offense ranking (1 through 32): "))
team_2_def = int(input("Enter away team's defense ranking (1 through 32): "))


def get_score_rarity():
    # Chances of the rarity of the scores, one for each team
    score_rarity_1 = random.randint(0, 10000)
    score_rarity_2 = random.randint(0, 10000)
    if 0 <= score_rarity_1 <= 6500:
        rarity_1 = "common"
    elif 6501 <= score_rarity_1 <= 9500:
        rarity_1 = "uncommon"
    elif 9501 <= score_rarity_1 <= 9994:
        rarity_1 = "rare"
    elif 9995 <= score_rarity_1 <= 10000:
        rarity_1 = "very rare"

    if 0 <= score_rarity_2 <= 6500:
        rarity_2 = "common"
    elif 6501 <= score_rarity_2 <= 9500:
        rarity_2 = "uncommon"
    elif 9501 <= score_rarity_2 <= 9994:
        rarity_2 = "rare"
    elif 9995 <= score_rarity_2 <= 10000:
        rarity_2 = "very rare"

    return rarity_1, rarity_2

def get_score_chance(off1, def1, off2, def2):
    diff_1 = off1 - def2
    diff_2 = off2 - def1
    if -31 <= diff_1 <= -23:
        off1_high_chance = 0.4
        off1_mid_chance = 0.6
        off1_low_chance = 0.0
    elif -22 <= diff_1 <= -14:
        off1_high_chance = 0.35
        off1_mid_chance = 0.6
        off1_low_chance = 0.05
    elif -13 <= diff_1 <= -5:
        off1_high_chance = 0.3
        off1_mid_chance = 0.6
        off1_low_chance = 0.1
    elif -4 <= diff_1 <= 4:
        off1_high_chance = 0.25
        off1_mid_chance = 0.5
        off1_low_chance = 0.25
    elif 5 <= diff_1 <= 13:
        off1_high_chance = 0.2
        off1_mid_chance = 0.5
        off1_low_chance = 0.3
    elif 14 <= diff_1 <= 22:
        off1_high_chance = 0.15
        off1_mid_chance = 0.5
        off1_low_chance = 0.35
    elif 23 <= diff_1 <= 31:
        off1_high_chance = 0.0
        off1_mid_chance = 0.5
        off1_low_chance = 0.5

    if -31 <= diff_2 <= -23:
        off2_high_chance = 0.4
        off2_mid_chance = 0.6
        off2_low_chance = 0.0
    elif -22 <= diff_2 <= -14:
        off2_high_chance = 0.35
        off2_mid_chance = 0.6
        off2_low_chance = 0.05
    elif -13 <= diff_2 <= -5:
        off2_high_chance = 0.3
        off2_mid_chance = 0.6
        off2_low_chance = 0.1
    elif -4 <= diff_2 <= 4:
        off2_high_chance = 0.25
        off2_mid_chance = 0.5
        off2_low_chance = 0.25
    elif 5 <= diff_2 <= 13:
        off2_high_chance = 0.2
        off2_mid_chance = 0.5
        off2_low_chance = 0.3
    elif 14 <= diff_2 <= 22:
        off2_high_chance = 0.15
        off2_mid_chance = 0.5
        off2_low_chance = 0.35
    elif 23 <= diff_2 <= 31:
        off2_high_chance = 0.0
        off2_mid_chance = 0.5
        off2_low_chance = 0.5

    if off1_high_chance == 0.4:
        off1_high_lb = 0
        off1_high_hb = 40
        off1_mid_lb = 41
        off1_mid_hb = 100
        off1_low_lb = 0
        off1_low_hb = 0
    elif off1_high_chance == 0.35:
        off1_high_lb = 0
        off1_high_hb = 35
        off1_mid_lb = 36
        off1_mid_hb = 95
        off1_low_lb = 96
        off1_low_hb = 100
    elif off1_high_chance == 0.3:
        off1_high_lb = 0
        off1_high_hb = 30
        off1_mid_lb = 31
        off1_mid_hb = 90
        off1_low_lb = 91
        off1_low_hb = 100
    elif off1_high_chance == 0.25:
        off1_high_lb = 0
        off1_high_hb = 25
        off1_mid_lb = 26
        off1_mid_hb = 75
        off1_low_lb = 76
        off1_low_hb = 100
    elif off1_high_chance == 0.2:
        off1_high_lb = 0
        off1_high_hb = 20
        off1_mid_lb = 21
        off1_mid_hb = 70
        off1_low_lb = 71
        off1_low_hb = 100
    elif off1_high_chance == 0.15:
        off1_high_lb = 0
        off1_high_hb = 15
        off1_mid_lb = 16
        off1_mid_hb = 65
        off1_low_lb = 66
        off1_low_hb = 100
    elif off1_high_chance == 0.0:
        off1_high_lb = 0
        off1_high_hb = 0
        off1_mid_lb = 0
        off1_mid_hb = 50
        off1_low_lb = 51
        off1_low_hb = 100

    if off2_high_chance == 0.4:
        off2_high_lb = 0
        off2_high_hb = 40
        off2_mid_lb = 41
        off2_mid_hb = 100
        off2_low_lb = 0
        off2_low_hb = 0
    elif off2_high_chance == 0.35:
        off2_high_lb = 0
        off2_high_hb = 35
        off2_mid_lb = 36
        off2_mid_hb = 95
        off2_low_lb = 96
        off2_low_hb = 100
    elif off2_high_chance == 0.3:
        off2_high_lb = 0
        off2_high_hb = 30
        off2_mid_lb = 31
        off2_mid_hb = 90
        off2_low_lb = 91
        off2_low_hb = 100
    elif off2_high_chance == 0.25:
        off2_high_lb = 0
        off2_high_hb = 25
        off2_mid_lb = 26
        off2_mid_hb = 75
        off2_low_lb = 76
        off2_low_hb = 100
    elif off2_high_chance == 0.2:
        off2_high_lb = 0
        off2_high_hb = 20
        off2_mid_lb = 21
        off2_mid_hb = 70
        off2_low_lb = 71
        off2_low_hb = 100
    elif off2_high_chance == 0.15:
        off2_high_lb = 0
        off2_high_hb = 15
        off2_mid_lb = 16
        off2_mid_hb = 65
        off2_low_lb = 66
        off2_low_hb = 100
    elif off2_high_chance == 0.0:
        off2_high_lb = 0
        off2_high_hb = 0
        off2_mid_lb = 0
        off2_mid_hb = 50
        off2_low_lb = 51
        off2_low_hb = 100

    return off1_low_lb, off1_low_hb, off1_mid_lb, off1_mid_hb, off1_high_lb, off1_high_hb, off2_low_lb, off2_low_hb, off2_mid_lb, off2_mid_hb, off2_high_lb, off2_high_hb

def get_score_value(llb1, lhb1, mlb1, mhb1, hlb1, hhb1, llb2, lhb2, mlb2, mhb2, hlb2, hhb2):
    # Chances of the value of score (high, mid, low)
    rad_score_value_1 = random.randint(0, 100)
    rad_score_value_2 = random.randint(0, 100)
    if lhb1 == 0.0:
        if hlb1 <= rad_score_value_1 <= hhb1:
            score_value_1 = "high"
        elif mlb1 <= rad_score_value_1 <= mhb1:
            score_value_1 = "mid"
    else:
        if hlb1 <= rad_score_value_1 <= hhb1:
            score_value_1 = "high"
        elif mlb1 <= rad_score_value_1 <= mhb1:
            score_value_1 = "mid"
        elif llb1 <= rad_score_value_1 <= lhb1:
            score_value_1 = "low"

    if lhb2 == 0.0:
        if hlb2 <= rad_score_value_2 <= hhb2:
            score_value_2 = "high"
        elif mlb2 <= rad_score_value_2 <= mhb2:
            score_value_2 = "mid"
    else:
        if hlb2 <= rad_score_value_2 <= hhb2:
            score_value_2 = "high"
        elif mlb2 <= rad_score_value_2 <= mhb2:
            score_value_2 = "mid"
        elif llb2 <= rad_score_value_2 <= lhb2:
            score_value_2 = "low"

    return score_value_1, score_value_2

def get_final_score(r1, v1, r2, v2):
    if v1 == "low":
        if r1 == "common":
            s1 = common_low[random.randint(0, len(common_low)-1)]
        elif r1 == "uncommon":
            s1 = uncommon_low[random.randint(0, len(uncommon_low)-1)]
        elif r1 == "rare":
            s1 = rare_low[random.randint(0, len(rare_low)-1)]
        elif r1 == "very rare":
            s1 = very_rare_low[random.randint(0, len(very_rare_low)-1)]
    elif v1 == "mid":
        if r1 == "common":
            s1 = common_mid[random.randint(0, len(common_mid)-1)]
        elif r1 == "uncommon":
            s1 = uncommon_mid[random.randint(0, len(uncommon_mid)-1)]
        elif r1 == "rare":
            s1 = rare_mid[random.randint(0, len(rare_mid)-1)]
        elif r1 == "very rare":
            s1 = very_rare_mid[random.randint(0, len(very_rare_mid)-1)]
    elif v1 == "high":
        if r1 == "common":
            s1 = common_high[random.randint(0, len(common_high)-1)]
        elif r1 == "uncommon":
            s1 = uncommon_high[random.randint(0, len(uncommon_high)-1)]
        elif r1 == "rare":
            s1 = rare_high[random.randint(0, len(rare_high)-1)]
        elif r1 == "very rare":
            s1 = very_rare_high[random.randint(0, len(very_rare_high)-1)]

    if v2 == "low":
        if r2 == "common":
            s2 = common_low[random.randint(0, int((len(common_low) - 1)/adv))]
        elif r2 == "uncommon":
            s2 = uncommon_low[random.randint(0, int((len(uncommon_low) - 1)/adv))]
        elif r2 == "rare":
            s2 = rare_low[random.randint(0, int((len(rare_low) - 1)/adv))]
        elif r2 == "very rare":
            s2 = very_rare_low[random.randint(0, int((len(very_rare_low) - 1)/adv))]
    elif v2 == "mid":
        if r2 == "common":
            s2 = common_mid[random.randint(0, int((len(common_mid) - 1)/adv))]
        elif r2 == "uncommon":
            s2 = uncommon_mid[random.randint(0, int((len(uncommon_mid) - 1)/adv))]
        elif r2 == "rare":
            s2 = rare_mid[random.randint(0, int((len(rare_mid) - 1)/adv))]
        elif r2 == "very rare":
            s2 = very_rare_mid[random.randint(0, int((len(very_rare_mid) - 1)/adv))]
    elif v2 == "high":
        if r2 == "common":
            s2 = common_high[random.randint(0, int((len(common_high) - 1)/adv))]
        elif r2 == "uncommon":
            s2 = uncommon_high[random.randint(0, int((len(uncommon_high) - 1)/adv))]
        elif r2 == "rare":
            s2 = rare_high[random.randint(0, int((len(rare_high) - 1)/adv))]
        elif r2 == "very rare":
            s2 = very_rare_high[random.randint(0, int((len(very_rare_high) - 1)/adv))]

    return s1, s2

def calc_winner(s1, s2):
    if s1 > s2:
        # wins_1 = wins_1 + 1
        print(f"{team_1_name} win {s1}-{s2}")
    elif s2 > s1:
        #wins_2 = wins_2 + 1
        print(f"{team_2_name} win {s2}-{s1}")
    elif s1 == s2:
        #ties = ties + 1
        print(f"Tie {s1}-{s2}")

def print_results(w1, w2, t, t1, t2):
    print(f"\n{team_1_name} win percentage is {round(((w1+(ties/2)/num_sim) / 100), 1)} \n")
    print(f"{team_2_name} win percentage is {round(((w2+(ties/2)/num_sim) / 100), 1)} \n")

    print(f"{team_1_name} record against {team_2_name} is {w1}-{((num_sim-w1)-t)}-{t} \n")
    print(f"{team_2_name} record against {team_1_name} is {w2}-{((num_sim - w2) - t)}-{t} \n")

    if (t1/num_sim) > (t2/num_sim):
        print(f"{team_1_name} win {round((t1/num_sim))}-{round((t2/num_sim))} \n")
    elif (t2/num_sim) > (t1/num_sim):
        print(f"{team_2_name} win {round((t2 / num_sim))}-{round((t1 / num_sim))} \n")
    else:
        print(f"The teams tie {round((t1 / num_sim))}-{round((t2 / num_sim))} \n")
def main():
    wins_1 = 0
    wins_2 = 0
    ties = 0
    s1t = 0
    s2t = 0
    for i in range(num_sim):
        get_score_rarity()
        get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)
        get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])
        get_final_score(get_score_rarity()[0], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[0], get_score_rarity()[1], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[1])
        s1 = get_final_score(get_score_rarity()[0], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[0], get_score_rarity()[1], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[1])[0]
        s2 = get_final_score(get_score_rarity()[0], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[0], get_score_rarity()[1], get_score_value(get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[0], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[1], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[2], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[3], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[4], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[5], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[6], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[7], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[8], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[9], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[10], get_score_chance(team_1_off, team_1_def, team_2_off, team_2_def)[11])[1])[1]
        if s1 > s2:
            wins_1 = wins_1 + 1
            print(f"{team_1_name} win {round(s1)}-{round(s2)}")
        elif s2 > s1:
            wins_2 = wins_2 + 1
            print(f"{team_2_name} win {round(s2)}-{round(s1)}")
        elif s1 == s2:
            ties = ties + 1
            print(f"Tie {round(s1)}-{(s2)}")
        s1t += s1
        s2t += s2

    print_results(wins_1, wins_2, ties, s1t, s2t)

if __name__ == "__main__":
    main()
    #9-8