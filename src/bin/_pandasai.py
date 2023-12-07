import os
from dotenv import load_dotenv

load_dotenv('../../local.env')

import pandas as pd
from src.packages.constants.path_constants import PathConstants

dataset_path = PathConstants().CDB_DATASET_PATH

battles_dataset_name = os.path.join(dataset_path, 'battles.csv')

battles_df = pd.read_csv(battles_dataset_name)

from src.packages.llms.zephyr import Zephyr
from pandasai import SmartDataframe

llm = Zephyr.construct_llm()

dd = SmartDataframe(battles_df, config={"llm": llm})
print(dd.chat("Number of wars in poland"))
