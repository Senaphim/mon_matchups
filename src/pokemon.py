import pandas as pd
import numpy as np

class Pokemon():
    def __init__(self, src_csv="./data/pokemon.csv"):
        data_types = {
                "ID": np.int32,
                "Name": str,
                "Form": str,
                "Type1": str,
                "Type2": str,
                "Total": np.int32,
                "HP": np.int32,
                "Attack": np.int32,
                "Defense": np.int32,
                "Sp. Atk": np.int32,
                "sp. Def": np.int32,
                "Speed": np.int32,
                "Generation": np.int32
                }
        self.dataset = pd.read_csv(src_csv, header=0, dtype=data_types)
        self._init_ok = 1
