import requests
import json

# Função para obter os dados de inventário
def get_inventory(token, network_construct_id, mcp_server, limit=30):
    url = f'{mcp_server}/nsi/api/equipment'
    
    headers = {
        'accept': 'application/json',
        'Authorization': f'Bearer {token}',  # Usa o token passado como parâmetro
    }
    
    params = {
        'networkConstruct.id': network_construct_id,
        'limit': str(limit),  # Limite de resultados, convertido para string
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, verify=False)  # verify=False ignora certificados SSL
        if response.status_code == 200:
            inventory_data = response.json()
            return inventory_data
        else:
            raise Exception(f"Unexpected status code: {response.status_code}, {response.text}")
    
    except requests.exceptions.RequestException as e:
        raise Exception(f"Inventory request failed: {e}")