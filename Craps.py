import csv
import random
import matplotlib.pyplot as plt
import numpy as np

# Rules / starting values
START_CASH = 5000
MAX_BET = 1000
MIN_BET = 50
NUM_PLAYERS = 4
NUM_ROUNDS = 5
NUM_MATCHES = 10000
RETURNS = [2, 2, 2, 2, 2.8, 2.4, 2.17, 2.17, 2.4, 2.8, 1.5, 1.67, 1.83, 1.83, 1.67, 1.5, 2, 3]
# RETURNS = [2, 2, 2, 2, 2.4, 2.4, 2.17, 2.17, 2.4, 2.8, 2.5, 2.67, 2.83, 2.83, 2.67, 2.5, 2, 3]
DEFAULT_BET = [MIN_BET, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Must bet on pass / don't pass line

# Strategies:
    # [pass, no-pass, come, no-come, p4, p5, p6, p8, p9, p10,
    #        o4, o5, o6, o8, o9, o10, field (split into 2 for diff returns)]
    # Size: 17
    # Strategies work such that the first roll only considers first two
    # (pass, no-pass). On second roll, it applies all other bets. Field bets
    # go every roll.

# Simple strategies:
#    [1.4  1.3  1.4  1.3  6.7  4    1.5  1.5  4    6.7  0                             5.5
#    [p    np   c    nc   p4   p5   p6   p8   p9   p10  o4   o5   o6   o8   o9   o10  f]
s1 = [50 , 0  , 0  , 0  , 400, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
s2 = [50 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 400, 0  , 0  , 0  , 0  , 0]

# OTHER BETS
#    [1.4  1.3  1.4  1.3  6.7  4    1.5  1.5  4    6.7  0                             5.5
#    [p    np   c    nc   p4   p5   p6   p8   p9   p10  o4   o5   o6   o8   o9   o10  f]
P = [400, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
N = [0  , 400, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
P4 = [50 , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
P5 = [50 , 0  , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
P6 = [50 , 0  , 0  , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
O4 = [50 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0  , 0  , 0]
O5 = [50 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0  , 0]
O6 = [50 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 350, 0  , 0  , 0  , 0]
F = [50 , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 350]
# bbs = [P,N,P4,P5,P6,O4,O5,O6,F]

# PERCENTAGE OF STARTING MONEY bet (percentage of current money strat also?)
#    [1.4  1.3  1.4  1.3  6.7  4    1.5  1.5  4    6.7  0                             5.5
#    [p    np   c    nc   p4   p5   p6   p8   p9   p10  o4   o5   o6   o8   o9   o10  f]
m1 = [50, 0  , 0  , 0  , 4000  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m2 = [50, 0  , 0  , 0  , 4250  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m3 = [50, 0  , 0  , 0  , 4500  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m4 = [50, 0  , 0  , 0  , 4750  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m5 = [50, 0  , 0  , 0  , 4949  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m6 = [50, 0  , 0  , 0  , 4000  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m7 = [50, 0  , 0  , 0  , 4500  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m8 = [50, 0  , 0  , 0  , 4950  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m9 = [50, 0  , 0  , 0  , 850  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
m10 = [50, 0  , 0  , 0  , 950  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
bbs = [m1,m2,m3,m4,m5] # ,m6,m7,m8] #  m9,m10]

# TODO: THRESHOLD TO STOP BETTING.
#    [1.4                 6.7  4    1.5  1.5  4    6.7       0              0         5.5
#    [p    np   c    nc   p4   p5   p6   p8   p9   p10  o4   o5   o6   o8   o9   o10  f]
t1 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t2 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t3 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t4 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t5 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t6 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]
t7 = [100, 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0  , 0]

# TODO: Change strategy mid-way through a game

# SET PLAYER STRATS HERE
s = [m4, m4, m4, m4]


def main():
    # Strategies:
    # [pass, no-pass, come, no-come, p4, p5, p6, p8, p9, p10,
    #        o4, o5, o6, o8, o9, o10, field (split into 2 for diff returns)]
    # Size: 17
    # Strategies work such that the first roll only considers first two
    # (pass, no-pass). On second roll, it applies all other bets. Field bets
    # go every roll.

    players = [Player(t=70000), Player(t=70000), Player(t=70000), Player(t=70000)]
    players = strat_init(players)

    # Analyis / Data recording options!
    conv = False  # make sure NUM_MATCHES is correct
    hist = False
    test_run = False
    plots = False
    conf_int = True

    # print(avg_seq())
    if conf_int:
        data = []
        data2 = []
        for i in range(10):
            g = game(players)
            wins = g[0]
            data.append(wins[0])
            data2.append(wins[1])
        players = strat_init(players)
        print("-----")
        print(players[0].get_strat(), ": ", "("+str(np.min(data)*0.001)+", "+str(np.max(data)*0.001)+")")
        print(players[1].get_strat(), ": ", "("+str(np.min(data2)*0.001)+", "+str(np.max(data2)*0.001)+")")
    if conv:
        conv_data(players)
    if hist:
        hist_data(players)
    if test_run:
        g = game(players)
        wins = g[0]
        avgs = g[1]
        for i in range(NUM_PLAYERS):
            print("Player", i+1, ": ", wins[i], ", avg : ", avgs[i])
        print("Ties : ", wins[NUM_PLAYERS])
        print(g[2])
    if plots:
        with open("conv_data.csv", 'r') as f:
            csvr = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            for row in csvr:
                plt.plot(row[20:], linewidth=1)
            plt.show()
        with open("hist_data.csv", 'r') as f:
            csvr = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
            for row in csvr:
                plt.hist(row, bins=100)
            plt.show()


# [ Game simulation results ]

def conv_data(players):
    f = open("conv_data.csv", 'w', newline='')
    w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    for i in range(10):
        data = game(players, conv_data=True)
        w.writerow(data)
    f.close()


def hist_data(players):
    data = []
    for i in range(1000):
        wins = game(players)[0]
        w = np.argmax(wins)
        perc = (wins[w] * 1.) / (NUM_MATCHES * 1.)
        data.append(perc)
    f = open('hist_data.csv', 'w')
    w = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
    w.writerow(data)
    f.close()


def avg_seq():
    avg = 0
    for i in range(10000000):
        r_seq = round()
        avg += len(r_seq)
    return avg / 10000000


# [ Running of the game simulation ]

# Player object, tracks cash amount and strategy
class Player:
    def __init__(self, s=None, t=None):
        if s is None:
            s = DEFAULT_BET
        if t is None:
            t = 7000
        self.cash = START_CASH
        self.strategy = s
        self.playing = True
        self.threshold = t

    def update_cash(self, amount):
        self.cash += amount

    def reset_cash(self):
        self.cash = START_CASH

    def set_strat(self, s):
        self.strategy = s

    def set_playing(self, b):
        self.playing = b

    def get_cash(self):
        return self.cash

    def get_strat(self):
        return self.strategy

    def get_bet_amt(self):
        return np.sum(self.strategy)

    def get_playing(self):
        return self.playing

    def get_threshold(self):
        return self.threshold


# Initializes strategies, currently for 4 players, defaults for any player over 4.
# Specify player with 'n'
def strat_init(players, n=None):
    strats = s
    if n is None:
        for p in range(0, NUM_PLAYERS):
            player = players[p]
            if p < len(strats):
                players[p].set_strat(strats[p])
            else:
                player.set_strat(DEFAULT_BET)
    elif n <= len(strats):
        players[n-1].set_strat(strats[n-1])
    else:
        players[n-1].set_strat(DEFAULT_BET)
    return players


# Starts simulation of games (note: need to set strategies)
def game(players, conv_data=False):
    p_wins = []
    p_avg = []
    b_wins = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    count_seq_geq1 = 0
    if conv_data:
        conv_wins = []
    for i in range(NUM_PLAYERS):
        p_wins.append(0)
        p_avg.append(0)
    p_wins.append(0)  # +1 for ties
    for m in range(NUM_MATCHES):
        for i in range(NUM_PLAYERS):
            players[i].reset_cash()
            players[i].set_playing(True)
            players = strat_init(players)
        curr_winner = -1
        for n in range(NUM_ROUNDS):
            # r_seq = round()
            curr_scores = []
            for p in range(NUM_PLAYERS):
                r_seq = round()  # each player at their own table
                # print(r_seq)
                if len(r_seq) > 1:
                    count_seq_geq1 += 1
                player = players[p]
                wins = score(player, r_seq)
                bets = wins[1]
                b_wins += np.array(bets)
                if (p != curr_winner) & (player.get_playing()):  # if not winning reset to normal bet
                    players = strat_init(players, p+1)
                if (player.get_cash() >= player.get_threshold()) & (p == curr_winner):  # stop taking risks
                    player.set_strat(DEFAULT_BET)
                    sc = wins[0]  # score(player, r_seq)
                    player.update_cash(sc)
                if (player.get_playing()) & (player.get_cash() > player.get_bet_amt()):
                    sc = wins[0]  # score(player, r_seq)
                    player.update_cash(sc)
                elif player.get_playing():
                    player.set_strat([player.get_cash(), 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    sc = wins[0]  # score(player, r_seq)
                    player.update_cash(sc)
                    if sc < 0:
                        player.set_playing(False)
                curr_scores.append(player.get_cash())
            curr_winner = np.argmax(curr_scores)
        totals = []
        for i in range(NUM_PLAYERS):
            cash = players[i].get_cash()
            p_avg[i] += cash * 1.
            totals.append(cash)
        winner = np.argmax(totals)
        winner_cash = np.max(totals)
        count = 0
        for i in range(NUM_PLAYERS):
            if totals[i] == winner_cash:  # & (i == winner)
                p_wins[i] += 1
                count += 1
        if count >= 2:
            p_wins[NUM_PLAYERS] += 1
        if conv_data:
            conv_wins.append((p_wins[0] * 1.) / ((m+1) * 1.))
        # print(players[winner].get_cash())
        # print(totals)
    if conv_data:
        return conv_wins
    else:
        bruh = []
        for i in range(len(b_wins)):
            if i <= 1:
                num = b_wins[i]*1 / (NUM_PLAYERS*1.) / (NUM_ROUNDS*1.) / (NUM_MATCHES*1.)
            else:
                num = b_wins[i]*1 / (count_seq_geq1*1.)
            bruh.append(num)
        return [p_wins, np.array(p_avg)/NUM_MATCHES, bruh]


# Dice roll
def roll():
    r1 = random.randint(1, 6)
    r2 = random.randint(1, 6)
    return r1 + r2


# creates sequence THEN need to take sequence and decide which bets WON
# with array of 'won' bets calculate player totals
def round():
    r_seq = []
    r = roll()
    r_seq.append(r)
    count = 0
    if (r == 7) | (r == 11) | (r == 2) | (r == 3) | (r == 12):
        return r_seq
    else:
        while r != 7:
            r = roll()
            r_seq.append(r)
        return r_seq


# Takes sequence of rolls returns what bets won
def bet_wins(r_seq):
    # bool list tracking which nums have appeared yet (Size: 12)
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # bool list tracking which bets win (Size: 18)
    win = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    point = 0
    point_c = 0
    roll_num = 0
    for r in r_seq:
        roll_num += 1
        nums[r-1] += 1
        if roll_num == 1:  # pass/no-pass
            if (r == 7) | (r == 11):  # pass t=1
                win[0] = 1
            elif (r == 2) | (r == 3) | (r == 12):  # no-pass t=1
                win[1] = 1
            else:
                point = r
        if roll_num >= 2:  # roll_num >= 2
            if r == point:  # pass t>1
                win[0] = 1
                point = -1
            if roll_num == 2:
                if (r == 7) | (r == 11):  # come t=1
                    win[2] = 1
                elif (r == 2) | (r == 3) | (r == 12):  # no-come t=1
                    win[3] = 1
                else:
                    point_c = r
            else:
                if r == point_c:  # come t>1
                    win[2] = 1
                    point_c = -1
            if r == 7:  # end of roll sequence
                #    [p    np   c    nc   p4   p5   p6   p8   p9   p10  o4   o5   o6   o8   o9   o10  f]
                for i in range(4, 6+1):
                    if nums[i-1] == 0:
                        win[i+6] += 1
                    else:
                        win[i] += 1
                for i in range(8, 10+1):
                    if nums[i-1] == 0:
                        win[i+5] += 1
                    else:
                        win[i-1] += 1
                if point != -1:  # no-pass t>1
                    win[1] = 1
                if point_c != -1:  # no-come t>1
                    win[3] = 1
    for i in range(12):  # field bets
        n = nums[i]
        if (i+1 == 3) | (i+1 == 4) | (i+1 == 9) | (i+1 == 10) | (i+1 == 11):
            win[16] += n
        elif (i+1 == 2) | (i+1 == 12):
            win[17] += n
    return win


# Gets winnings from player strategy and roll sequence
def score(player, r_seq):
    strat = player.get_strat()
    wins = bet_wins(r_seq)
    net_gain = 0
    if len(r_seq) > 1:
        net_gain -= player.get_bet_amt()
        field_loss = len(r_seq) - wins[16] - wins[17]
        net_gain -= (field_loss * strat[16] * 1.)
        for i in range(len(wins)):
            if (i == 16) | (i == 17):
                net_gain += RETURNS[i] * strat[16] * wins[i] * 1.
            else:
                net_gain += RETURNS[i] * strat[i] * wins[i] * 1.
    else:
        net_gain -= strat[0] - strat[1]
        for i in range(2):
            net_gain += RETURNS[i] * strat[i] * wins[i] * 1.
    return [net_gain, wins]


for s1 in bbs:
    for s2 in bbs:
        s = [s1, s2, s2, s2]
        main()


#for i in range(0, 10):
#    t1 = i * 500 - 1500
 #   for j in range(0, 10):
 #       t2 = j * 500 - 1500
 #       p12 = [Player(t=8700+t1), Player(t=8700+t2), Player(t=8700+t2), Player(t=8700+t2)]
 #       main(p12)

#if __name__ == "__main__":
#     main()
