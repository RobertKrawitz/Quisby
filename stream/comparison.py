from itertools import groupby

import config
from sheetapi import sheet
from sheet_util import create_spreadsheet, append_to_sheet, read_sheet
from util import combine_two_array_alternating
from graph import graph_stream_data


def compare_stream_results(spreadsheets):
    values = []
    results = []
    spreadsheet_name
    test_name = 'stream'

    for spreadsheetId in spreadsheets:
        values.append(read_sheet(spreadsheetId, range='stream'))
        spreadsheet_name.append(get_sheet(spreadsheetId, range=[])[
                                'properties']['title'])

    spreadsheet_name = " vs ".join(spreadsheet_name)

    for index, value in enumerate(values):
        values[index] = (list(g) for k, g in groupby(
            value, key=lambda x: x != []) if k)

    for value, ele in zip(values[0], values[1]):
        results.append([""])

        if value[0][0] == 'Max Througput':
            results = combine_two_array_alternating(results, value, ele)

        elif value[1][0] == ele[1][0]:
            results.append(value[0])
            results = combine_two_array_alternating(
                results, value[1:], ele[1:])

    spreadsheetId = create_spreadsheet(spreadsheet_name, test_name)
    append_to_sheet(spreadsheetId, results, test_name)
    graph_stream_data(spreadsheetId, test_name)

    print(f'https://docs.google.com/spreadsheets/d/{spreadsheetId}')

    return results


spreadsheets = ['1ucUesKesu91NfnDvpnbsEf2SluL4_NaCHLQbIf3CH9c',
                '1GofU4KegjkniGFhZInZGoBSSUP67aaCq4Jc77MEIBEE']


compare_stream_results(spreadsheets)