import requests
import os
from dotenv import load_dotenv

load_dotenv()

# PROTOTIPO!!!!

# --- Definindo variáveis de ambiente ---


api_key = os.environ.get("MAILGUN_API_KEY")

domain = "sandboxc84a38ff79c943018c7f83303837c85e.mailgun.org"
email_destinatario = "patrickgougeoncouto@gmail.com"

disciplina = "Pensamento Computacional"
aprovado = False



# --- Autenticando email destinatário ---


# response = requests.post(
#     "https://api.mailgun.net/v5/sandbox/auth_recipients?email={}".format(
#         email_destinatario
#     ),
#     auth=("api", api_key),
# )

# print(f"Status: {response.status_code}")


# --- Enviando primeiro email ---

response = requests.post(
    "https://api.mailgun.net/v3/{}/messages".format(domain),
    auth=("api", api_key),
    data={
        "from": "Test <postmaster@{}>".format(domain),
        "to": email_destinatario,
        "subject": "Monitoria - Resultado da Análise",
        "text": "Você foi {} na disciplina de {}.".format(
            "aprovado" if aprovado else "reprovado", disciplina
        ),
    }
)
print(f"Status: {response.status_code}")
