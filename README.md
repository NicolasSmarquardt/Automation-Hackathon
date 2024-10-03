# Automation-Hackathon

## Project Overview

This project was developed during the Automattion Hackthon H2 2024, and automates the process of creating hardware inventories of telecommunications network elements using RESTCONF API and Python to send requests to CIENA's management software (NAVIGATOR NCS) and retrieve information about equipments that makes up the sites of a network.

After retrieving the data, it is stored in a JSON file. The information is then processed and saved into an Excel file, with each site having its own dedicated sheet.

## Motivation

The telecommunications environment is complex, comprising a wide array of interconnected equipment. Efficient management of these assets is crucial to the operational success of any service provider. This project was motivated by the need to automate and streamline the process of generating comprehensive inventory reports for network equipment.

Accurate reports are essential for better resource allocation and investment planning. Furthermore, having an organized and up-to-date equipment inventory facilitates internal and external audits, ensuring compliance and operational transparency. A detailed overview of the existing infrastructure is also critical for planning network expansions or future upgrades, allowing for informed decisions that enhance network performance and scalability.

## Usage

To use the scripts you must specify some informations hardcoding. And these informations are:

MCP_SERVER = "https://<IP ADRESS>"

MCP_USERNAME = "USER"

MCP_PASSWORD = "USERPASSWORD"

network_constr_ids = {

    'NE1': 'network_constr_id',
    
    'NE2': 'network_constr_id',
    
    'NE3': 'network_constr_id',
    
    'NE4': 'network_constr_id',
    
    'NE5': 'network_constr_id',
    
    'NEX': 'network_constr_id'
    
}

With that you will be able to run the scripts.

## Future upgrades:

Upgrade this scripts auttomating also the process of getting the network_constr_ids using this API:

​/nsi​/api​/networkConstructs

