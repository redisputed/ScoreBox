"""Import box scores from Excel spreadsheet
    """
import scorebox.scoreimporter as sb
from pandas import ExcelFile


def test_get_sheets_returns_ExcelFile_object():
    folder: str = 'tests/data'
    filename: str = 'testsheet.xlsx'
    result = sb.get_sheets(folder, filename)
    assert isinstance(result, ExcelFile)


def test_verfiy_date_returns_for_mm_dd_yyyy_fmts():
    given: str = '03.11.2018'
    result = sb.verify_date(given)
    assert result
