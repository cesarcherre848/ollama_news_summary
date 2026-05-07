import requests
import json

def procesar_reporte_8k(ticker, texto_reporte):
    url = "http://localhost:11434/api/generate"
    
    # Agregamos un pequeño prefijo para contextualizar al modelo
    prompt_completo = f"Analiza el siguiente reporte 8-K de la empresa con ticker {ticker}:\n\n{texto_reporte}"
    
    payload = {
        "model": "news_summary", # El modelo que automatizamos en Docker
        "prompt": prompt_completo,
        "stream": False,
        "options": {
            "temperature": 0.2 # Reforzamos que sea determinista y analítico
        }
    }
    
    print(f"📡 Enviando Form 8-K de {ticker} al modelo local...")
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        resultado = response.json()
        print("\n" + "="*60)
        print(f"📊 SÍNTESIS BURSÁTIL: {ticker} (Form 8-K)")
        print("="*60)
        print(resultado["response"])
        print("="*60 + "\n")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión con el contenedor de Ollama: {e}")

# Texto simulado de un Form 8-K real (En inglés)
texto_edgar_8k = """
UNITED STATES SECURITIES AND EXCHANGE COMMISSION
Form 8-K
Current Report Pursuant to Section 13 or 15(d) of the Securities Exchange Act of 1934

Date of Report: May 7, 2026
Company: Global Steel Dynamics Inc. (Ticker: GSD)

Item 8.01 Other Events.
On May 7, 2026, Global Steel Dynamics Inc. (the "Company") announced the successful deployment of a new Mixed-Integer Linear Programming (MILP) model across its primary Electric Arc Furnace (EAF) facilities. The optimization framework dynamically adjusts scrap metal charge balances and chemical mass in real-time. Preliminary Q2 data indicates this deployment will reduce overall energy consumption by approximately 12.5% per ton of steel produced.

Despite these operational efficiencies, the Company's management notes potential near-term headwinds. Forward-looking guidance has been slightly revised due to unexpected volatility in the international scrap metal supply chain and rising grid electricity tariffs in regional markets, which may offset up to 4.5% of the projected margin improvements for the fiscal year 2026. No immediate changes to dividend policies were announced.
"""

if __name__ == "__main__":
    procesar_reporte_8k("GSD", texto_edgar_8k)