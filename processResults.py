import string
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def process_results(trial_id, trial_balances, equilibrium_prices, is_last_trial,
                    is_figure1, is_figure2, is_figure3, is_figure4, is_figure5):

    avg_balance = pd.read_csv("records/avg_balance.csv", header=None,
                              names=list(string.ascii_uppercase)[0:26],
                              index_col=False)

    avg_balance = avg_balance[avg_balance["A"] == trial_id]

    drop_list = ["None", " None", "N", " N"]
    avg_balance = avg_balance.loc[~avg_balance.C.isin(drop_list)]
    avg_balance = avg_balance.loc[~avg_balance.D.isin(drop_list)]

    avg_balance["C"] = avg_balance["C"].astype("float", errors="ignore")
    avg_balance["D"] = avg_balance["D"].astype("float", errors="ignore")

    trial_balances.append(avg_balance["B"].values.tolist())
    trial_balances.append(avg_balance["H"].values.tolist())
    equilibrium_prices.append(avg_balance["C"].values.tolist()[-20::])
    equilibrium_prices.append(avg_balance["D"].values.tolist()[-20::])

    if is_figure1:
        new_names_agents = {"B": "Time", "H": "GVWY", "L": "INSD", "P": "SHVR", "T": "ZIC", "X": "ZIP"}
        avg_balance.rename(columns=new_names_agents, inplace=True)
        avg_balance.plot(x="Time", y=["GVWY", "INSD", "SHVR", "ZIC", "ZIP"], kind="line")
        plt.show(block=True)

    if is_figure2:
        new_names_bests = {"B": "Time", "C": "Best Bid", "D": "Best Ask"}
        avg_balance.rename(columns=new_names_bests, inplace=True)
        avg_balance.plot(x="Time", y=["Best Bid", "Best Ask"], kind="line")
        plt.show(block=True)

    if is_figure3:
        new_names_agents = {"B": "Time", "H": "GVWY"}
        avg_balance.rename(columns=new_names_agents, inplace=True)
        avg_balance["GVWY"] = avg_balance["GVWY"] / avg_balance["Time"]
        avg_balance.plot(x="Time", y="GVWY", kind="line")
        plt.show(block=True)

    if is_figure4 and is_last_trial:
        x1 = trial_balances[0]
        y1 = trial_balances[1]
        x2 = trial_balances[2]
        y2 = trial_balances[3]
        x3 = trial_balances[4]
        y3 = trial_balances[5]
        x4 = trial_balances[6]
        y4 = trial_balances[7]
        x5 = trial_balances[8]
        y5 = trial_balances[9]
        plt.xlabel("Time")
        plt.ylabel("Balance (Giveaway)")
        plt.plot(x1, y1, color='r', label='trial1')
        plt.plot(x2, y2, color='g', label='trial2')
        plt.plot(x3, y3, color='b', label='trial3')
        plt.plot(x4, y4, color='orange', label='trial4')
        plt.plot(x5, y5, color='purple', label='trial5')
        plt.legend()
        plt.show()

    if is_figure5 and is_last_trial:
        x1 = "trial1"
        x2 = "trial2"
        x3 = "trial3"
        x4 = "trial4"
        x5 = "trial5"
        y1 = (sum(equilibrium_prices[0]) + sum(equilibrium_prices[1])) / (
                len(equilibrium_prices[0]) + len(equilibrium_prices[1]))
        y2 = (sum(equilibrium_prices[2]) + sum(equilibrium_prices[3])) / (
                len(equilibrium_prices[2]) + len(equilibrium_prices[3]))
        y3 = (sum(equilibrium_prices[4]) + sum(equilibrium_prices[5])) / (
                len(equilibrium_prices[4]) + len(equilibrium_prices[5]))
        y4 = (sum(equilibrium_prices[6]) + sum(equilibrium_prices[7])) / (
                len(equilibrium_prices[6]) + len(equilibrium_prices[7]))
        y5 = (sum(equilibrium_prices[8]) + sum(equilibrium_prices[9])) / (
                len(equilibrium_prices[8]) + len(equilibrium_prices[9]))
        x = np.array([x1, x2, x3, x4, x5])
        y = np.array([y1, y2, y3, y4, y5])
        for a, b, i in zip(x, y, range(len(x))):
            plt.text(a, b + 0.5, "%.2f" % y[i], ha='center', fontsize=11)
        plt.ylim(80, 100)
        plt.ylabel("Estimated Equilibrium Price (Giveaway)")
        plt.bar(x, y, width=0.4, color=["r", "g", "b", "orange", "purple"])
        plt.show()
