#!/bin/bash/env python3

import csv
import glob
import re

file_name = glob.glob("*.csv")[0]
with open(file_name, "r") as file:
    reader = csv.DictReader(file)
    # fieldnames = next(reader)
    # print(fieldnames)

    results = {}

    for row in reader:
        if not row["COL_2"] in results:
            if row["COL_3"] == "開始" or row["COL_3"] == "終了" or row["COL_3"] == "正常":
                results[row["COL_2"]] = {row["COL_3"]: row["COL_1"]}
            # elif row["COL_3"] == "終了":
            #     results[row["COL_2"]] = {row["COL_3"]: row["COL_1"]}
            # elif row["COL_3"] == "正常":
            #     results[row["COL_2"]] = {row["COL_3"]: row["COL_1"]}
            elif "コマンド" in row["COL_3"]:
                res = re.match("(^コマンド\([0-9]*2).*\)", row["COL_3"])
                if res:
                    results[row["COL_2"]] = {row["COL_3"]: row["COL_1"]}
            else:
                raise ValueError(f"unknown COL_3: {row['COL_3']}")
        else:
            if (row["COL_3"] == "開始" or row["COL_3"] == "終了" or row["COL_3"] == "正常") and row["COL_2"] in results:
                id = row["COL_2"]
                results[id][row["COL_3"]] = row["COL_1"]
            # elif row["COL_3"] == "終了" and row["COL_2"] in results:
            #     id = row["COL_2"]
            #     results[row["COL_2"]][row["COL_3"]] = row["COL_1"]
            # elif row["COL_3"] == "正常" and row["COL_2"] not in results:
            #     id = row["COL_2"]
            #     results[id] = {row["COL_3"]: row["COL_1"]}
            elif row["COL_2"] in results:
                id = row["COL_2"]
                res = re.match("(^コマンド\([0-9]*2).*\)", row["COL_3"])
                if res:
                    results[id][row["COL_3"]] = row["COL_1"]
            else:
                raise ValueError(f"unknown COL_2: {row['COL_2']}")
    print(results)
