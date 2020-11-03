from itertools import groupby

import quisby.config as config
from quisby.sheet.sheet_util import (
    create_spreadsheet,
    append_to_sheet,
    read_sheet,
    get_sheet,
)
from quisby.util import combine_two_array_alternating
from quisby.benchmarks.hammerdb.graph import graph_hammerdb_data


def compare_hammerdb_results(spreadsheets, test_name):
    spreadsheet_name = []
    values = []
    results = []

    for spreadsheetId in spreadsheets:
        values.append(read_sheet(spreadsheetId, range=test_name))
        spreadsheet_name.append(
            get_sheet(spreadsheetId, range=[])["properties"]["title"]
        )

    spreadsheet_name = " vs ".join(spreadsheet_name)

    for index, value in enumerate(values):
        values[index] = (list(g) for k, g in groupby(value, key=lambda x: x != []) if k)

    for value, ele in zip(values[0], values[1]):
        results.append([""])
        # Make sure it's same system family
        # TODO: Maybe check for whole type instead of family
        if value[0][1].split(".")[0] == ele[0][1].split(".")[0]:
            results = combine_two_array_alternating(results, value, ele)

    spreadsheetId = create_spreadsheet(spreadsheet_name, test_name)
    append_to_sheet(spreadsheetId, results, test_name)
    graph_hammerdb_data(spreadsheetId, test_name)

    print(f"https://docs.google.com/spreadsheets/d/{spreadsheetId}")

    return results
