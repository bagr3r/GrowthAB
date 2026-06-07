import gspread

from google.oauth2.service_account import Credentials

#Registra os resultados dos experimentos na planilha no google sheets
def update_google_sheet(results):

    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    #Autentica utilizando uma conta de serviço configurada no Google Cloud Plataform
    credentials = Credentials.from_service_account_file(
        "growthab-498518-571f44151b75.json",
        scopes=scopes
    )

    client = gspread.authorize(
        credentials
    )

    #abre a planilha de acompanhamento dos testes
    spreadsheet = client.open(
        "GrowthAB - testes"
    )

    worksheet = spreadsheet.sheet1

    for result in results:

        worksheet.append_row([
            result["test_name"],
            result["period"],
            result["description"],
            result["result"],
            result["decision"],
            result["partner"],
            result["winner"],
            round(result["profit"], 2),
            round(result["roi"], 2)
        ])