import pandas as pd
import numpy as np

from pTypes import str_type_to_enum

class Moves():
    def __init__(self, src_csv="./data/moves.csv"):
        data_types = {
                "#": np.int32,
                "Name": str,
                "Type": str,
                "Category": str,
                "PP": np.int32,
                "Power": "Int64",
                "Accuracy": "Int64",
                "Gen": np.int32
                }
        self.dataset = pd.read_csv(src_csv, header=0, dtype=data_types)
        self._init_ok = 1

    def move_type(self, move, mv_type = ""):
        if mv_type == "":
            row = self.dataset[self.dataset["Name"] == move]
            if row.empty:
                return None
            category = str(row["Category"].values[0])
            if category == "Status":
                return None
            mv_type = str(row["Type"].values[0])
        mv_type = str_type_to_enum(mv_type)
        return mv_type
