import pandas as pd
import string
import matplotlib.pyplot as plt


def process_results(trial_id, trial_balances, is_last_trial, is_figure1, is_figure2, is_figure3, is_figure4):
    avg_balance = pd.read_csv("records/avg_balance.csv", header=None,
                              names=list(string.ascii_uppercase)[0:26],
                              index_col=False)

    avg_balance = avg_balance[avg_balance["A"] == trial_id]

    trial_balances.append(avg_balance["B"].values.tolist())
    trial_balances.append(avg_balance["H"].values.tolist())

    drop_list = ["None", " None", "N", " N"]
    avg_balance = avg_balance.loc[~avg_balance.C.isin(drop_list)]
    avg_balance = avg_balance.loc[~avg_balance.D.isin(drop_list)]

    avg_balance["C"] = avg_balance["C"].astype("float", errors="ignore")
    avg_balance["D"] = avg_balance["D"].astype("float", errors="ignore")

    if is_figure1:
        new_names_agents = {"B": "Time", "H": "GVWY", "L": "INSD", "P": "SHVR", "T": "ZIC", "X": "ZIP"}
        avg_balance.rename(columns=new_names_agents, inplace=True)
        avg_balance.plot(x="Time", y=["GVWY", "INSD",  "SHVR", "ZIC", "ZIP"], kind="line")
        plt.show(block=True)

    if is_figure2:
        new_names_bests = {"B": "Time", "C": "Best Bid", "D": "Best Ask"}
        avg_balance.rename(columns=new_names_bests, inplace=True)
        avg_balance.plot(x="Time", y=["Best Bid", "Best Ask"], kind="line")
        plt.show(block=True)

    if is_figure3:
        new_names_agents = {"B": "Time", "H": "GVWY"}
        avg_balance.rename(columns=new_names_agents, inplace=True)
        avg_balance.plot(x="Time", y="GVWY", kind="line")
        plt.show(block=True)

    if is_figure4 and is_last_trial:
        x1 = trial_balances[0]
        y1 = trial_balances[1]
        x2 = trial_balances[2]
        y2 = trial_balances[3]
        x3 = trial_balances[4]
        y3 = trial_balances[5]
        plt.xlabel("Time")
        plt.ylabel("Balance")
        plt.plot(x1, y1, color='r', label='trial1')
        plt.plot(x2, y2, color='g', label='trial2')
        plt.plot(x3, y3, color='b', label='trial3')
        plt.legend()
        plt.show()
