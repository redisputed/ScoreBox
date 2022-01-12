import os
import re
import pandas as pd

date_fmt = re.compile(r'(\d{2})[/.-](\d{2})[/.-](\d{4})')


def get_sheets(path: str, filename: str) -> pd.DataFrame:
    ef = pd.ExcelFile(os.path.join(path, filename))
    return ef


def verify_date(datestring: str) -> bool:
    match = date_fmt.match(datestring)
    return bool(match)
