import pandas as pd
import numpy as np

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

