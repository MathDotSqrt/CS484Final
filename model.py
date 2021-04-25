import pandas as pd

INPUT_FILES = [
    './data/xaa',
    './data/xab',
    './data/xac',
    './data/xad',
    './data/xae',
    './data/xaf',
    './data/xag',
    './data/xah',
    './data/xai',
    './data/xaj',
    './data/xak',
    './data/xal',
    './data/xam',
]

input_dfs = [pd.read_csv(input) for input in INPUT_FILES]

train_df = pd.concat(input_dfs, ignore_index=True)
print(train_df)
