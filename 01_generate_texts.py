import pandas as pd
import datetime
import numpy as np
import csv

def convert_date_speeches(date):
    """
    Copied from open discourse
    """
    try:
        date = datetime.datetime.fromtimestamp(date)
        date = date.strftime("%Y-%m-%d %H:%M:%S")
        return date
    except (ValueError, TypeError) as e:
        print(e)
        return None

for legis in ["19", "20"]:
    speeches = pd.read_pickle("data/speeches_" + legis + ".pkl")
    speeches["date"] = speeches["date"].apply(convert_date_speeches)

    speeches = speeches.loc[speeches["faction_id"] != -1]

    faction_maping = {23: "SPD", 0: "AFD", 3: "Grüne", 4: "CDUCSU", 6: "linke", 13: "FDP"}

    for id, name in faction_maping.items():
        speeches.loc[speeches["faction_id"] == id, "speech_content"].str.replace("\n", ""). \
            str.replace("\t", "").str.replace('"', "").str.replace("\(\{[0-9]+\}\)", "", regex=True). \
        to_csv("data/faction/" + legis + "_" + name + ".txt", sep="|" ,header=None, index=None, quotechar="'",  escapechar="\\")
