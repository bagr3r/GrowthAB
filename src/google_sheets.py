import gspread

from google.oauth2.service_account import Credentials


def update_google_sheet(results):

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    credentials = Credentials.from_service_account_file(
        "growthab-498518-571f44151b75.json",
        scopes=scopes
    )

    client = gspread.authorize(
        credentials
    )

    spreadsheet = client.open(
        "GrowthAB - testes"
    )

    worksheet = spreadsheet.sheet1

    for result in results:

        worksheet.append_row([
            result["test_name"],
            result["partner"],
            result["winner"],
            float(result["profit"]),
            round(float(result["roi"]), 2),
            result["decision"]
        ])