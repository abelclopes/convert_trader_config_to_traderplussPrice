import json

def parse_trader_config(file_path):
    categories = {}
    current_category = None

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()

            if not line or line.startswith('//') or line.startswith('<Currency'):
                continue

            if line.startswith('<Trader>'):
                continue

            if line.startswith('<Category>'):
                current_category = line.split()[1]
                categories[current_category] = []
                continue

            parts = line.split(',')
            if len(parts) >= 4:
                item_name = parts[0].strip()
                buy_price = parts[2].strip()
                sell_price = parts[3].strip()
                quantity = parts[1].strip()
                categories[current_category].append(f"{item_name},{quantity},-1,{buy_price},{quantity},{sell_price}")

    return categories

def convert_to_traderplus(categories, output_path):
    traderplus_data = {
        "Version": "2.5",
        "EnableAutoCalculation": 0,
        "EnableAutoDestockAtRestart": 0,
        "EnableDefaultTraderStock": 0,
        "TraderCategories": []
    }

    for category, items in categories.items():
        traderplus_data["TraderCategories"].append({
            "CategoryName": category,
            "Products": items
        })

    with open(output_path, 'w') as json_file:
        json.dump(traderplus_data, json_file, indent=4)

def main():
    input_path = 'TraderConfig.txt'
    output_path = 'TraderPlusPriceConfig.json'
    
    categories = parse_trader_config(input_path)
    convert_to_traderplus(categories, output_path)
    print(f'Conversão completa. JSON salvo em {output_path}')

if __name__ == "__main__":
    main()
