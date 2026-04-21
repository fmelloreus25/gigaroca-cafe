from fastapi import FastAPI

# Inicializa o aplicativo FastAPI com as informações do nosso projeto
app = FastAPI(
    title="API - GigaRoça & Café",
    description="Sistema de Gestão, Estoque e PDV para produtos mineiros",
    version="1.0.0"
)

# Cria a nossa primeira Rota (Endpoint) de teste
@app.get("/")
def mensagem_de_boas_vindas():
    return {
        "mensagem": "Bem-vindo ao servidor do GigaRoça & Café!",
        "status": "O servidor está online e funcionando perfeitamente.",
        "proximo_passo": "Vamos configurar o banco de dados!"
    }