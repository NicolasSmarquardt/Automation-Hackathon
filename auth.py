import requests

# Função para solicitar o token usando as credenciais
def token_request(mcp_server, username, password):
    url = f'{mcp_server}/tron/api/v2/tokens'
    
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    
    data = {
        'username': username,
        'password': password,
    }
    
    try:
        response = requests.post(url, headers=headers, data=data, verify=False)  # verify=False ignora certificados SSL
        if response.status_code in [200, 201]:  # 200 OK ou 201 Created
            response_data = response.json()
            return response_data.get('token')  # Extrai e retorna o valor do token
        else:
            raise Exception(f"Unexpected status code: {response.status_code}, {response.text}")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Token request failed: {e}")