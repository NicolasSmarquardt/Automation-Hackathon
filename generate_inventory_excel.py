import pandas as pd
import json

def generate_inventory_excel(inventory_data_dict, excel_file_path):
    with pd.ExcelWriter(excel_file_path) as writer:
        for element_name, inventory_data in inventory_data_dict.items():
            equipment_list = []
            for item in inventory_data['data']:
                try:
                    installed_spec = item['attributes']['installedSpec']
                    part_number = installed_spec.get('partNumber', 'N/A')
                    equipment_type = installed_spec.get('type', 'N/A')
                    
                    # Localização
                    location = item['attributes']['locations'][0] if item['attributes']['locations'] else {}
                    location_info = f"Shelf: {location.get('shelf', 'N/A')}, Slot: {location.get('slot', 'N/A')}, NE Name: {location.get('neName', 'N/A')}"
                    
                    equipment_list.append({
                        'Part Number': part_number,
                        'Type': equipment_type,
                        'Location': location_info
                    })
                except KeyError:
                    continue  # Pular itens que não têm 'installedSpec' ou 'locations'
            
            # Criar um DataFrame e salvar na aba correspondente
            df = pd.DataFrame(equipment_list)
            df.to_excel(writer, sheet_name=element_name, index=False)