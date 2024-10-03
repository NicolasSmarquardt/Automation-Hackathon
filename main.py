import json
from auth import token_request
from spectral import get_spectral_data
from inventory import get_inventory
from generate_inventory_excel import generate_inventory_excel

import warnings
from urllib3.exceptions import InsecureRequestWarning

# Importa a função do arquivo report_generator.py
from report_generator import generate_spectral_report

# Defina o caminho do arquivo JSON e onde deseja salvar o relatório
json_file_path = 'spectral_data.json'
report_file_path = 'spectral_report.txt'

# Suprimir avisos de SSL não verificados
warnings.simplefilter('ignore', InsecureRequestWarning)

MCP_SERVER = "https://10.183.205.152"
MCP_USERNAME = "admin"
MCP_PASSWORD = "adminpw"
network_constr_ids = {
    'NE1': 'c465bba4-c689-3bd0-85c9-281b3188b050',
    'NE2': 'd120cf03-03cc-3d1b-b617-0c5acb237929',
    'NE3': 'caea76c6-ce8a-33c2-b368-4fd471fbbd9f',
    'NE4': '48258af3-51b6-39c4-9b5e-21aa2fcd45d2',
    'NE5': '55b304c5-f4fd-3a49-8a2a-7a0840552e4f'
}

fre_ids = '55b304c5-f4fd-3a49-8a2a-7a0840552e4f::TPE_55b304c5-f4fd-3a49-8a2a-7a0840552e4f::EQPT_1_6-1-CTPServerToClient-cef01d9b-a846-4fef-80c4-e92445ad3fdc-OTSi_c465bba4-c689-3bd0-85c9-281b3188b050::TPE_c465bba4-c689-3bd0-85c9-281b3188b050::EQPT_1_6-2-CTPServerToClient-cef01d9b-a846-4fef-80c4-e92445ad3fdc-OTSi'

def main():
    try:
        # Autenticação e obtenção do token
        token = token_request(MCP_SERVER, MCP_USERNAME, MCP_PASSWORD)
        print(token)
        
        inventory_data_dict = {}

        for element_name, network_id in network_constr_ids.items():
            inventory_data = get_inventory(token, network_id, MCP_SERVER, limit=40)
            inventory_data_dict[element_name] = inventory_data

        # Save each inventory to a separate JSON file
        with open(f'inventory_data_{element_name}.json', 'w') as json_file:
            json.dump(inventory_data, json_file, indent=4)
        print(f"Inventory for {element_name} saved in 'inventory_data_{element_name}.json'")

        # Generate the Excel file from the inventory data, with tabs for each element
        excel_file_path = 'inventory_equipment_all_elements_test2.xlsx'
        generate_inventory_excel(inventory_data_dict, excel_file_path)
        print("Excel file with all elements generated successfully!")
        
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    
