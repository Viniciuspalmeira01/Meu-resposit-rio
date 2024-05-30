import requests

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and 'rates' in data:
        return data['rates'].get(target_currency, None)
    else:
        raise Exception("Error fetching exchange rates")

def get_crypto_price(crypto_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data.get(crypto_id, {}).get('usd', None)
    else:
        raise Exception("Error fetching cryptocurrency price")
def cotações():
    try:
        # Cotações de moedas fiduciárias
        dolar_rate = get_exchange_rate("YOUR_API_KEY", "USD", "BRL")
        euro_rate = get_exchange_rate("YOUR_API_KEY", "EUR", "BRL")
        
        # Cotação de Bitcoin
        bitcoin_price = get_crypto_price("bitcoin")
        
        dollar = (f"Cotação do Dólar: {dolar_rate} BRL")
        euro = (f"Cotação do Euro: {euro_rate} BRL")
        bitcoin = (f"Cotação do Bitcoin: {bitcoin_price} USD")
        
    except Exception as e:
        print(f"Erro ao obter cotações: {e}")

    money = [dollar , euro , bitcoin]
    return money
cotações()