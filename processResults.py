import pandas as pd
import string
import matplotlib.pyplot as plt


def process_results(trial_id):
    avg_balance = pd.read_csv("records/avg_balance.csv", header=None,
                              names=list(string.ascii_uppercase)[0:22],
                              index_col=False)

    avg_balance = avg_balance[avg_balance["A"] == trial_id]

    drop_list = ["None", " None", "N", " N"]
    avg_balance = avg_balance.loc[~avg_balance.C.isin(drop_list)]
    avg_balance = avg_balance.loc[~avg_balance.D.isin(drop_list)]

    avg_balance["C"] = avg_balance["C"].astype("float", errors="ignore")
    avg_balance["D"] = avg_balance["D"].astype("float", errors="ignore")

    new_names_agents = {"H": "GVWY", "L": "SHVR", "P": "ZIC", "T": "ZIP"}
    avg_balance.rename(columns=new_names_agents, inplace=True)
    avg_balance.plot(x="B", y=["GVWY", "SHVR", "ZIC", "ZIP"], kind="line")
    plt.show(block=True)

    new_names_bests = {"C": "Best Bid", "D": "Best Ask"}
    avg_balance.rename(columns=new_names_bests, inplace=True)
    avg_balance.plot(x="B", y=["Best Bid", "Best Ask"], kind="line")
    plt.show(block=True)
