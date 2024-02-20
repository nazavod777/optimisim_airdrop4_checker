import requests

r = requests.get(url='https://raw.githubusercontent.com/ethereum-optimism/op-analytics/main/reference_data/'
                     'address_lists/op_airdrop_4_simple_list.csv')
eligible_accounts_data: dict = {}

for current_account in (r.text.split('\n')):
    try:
        eligible_accounts_data[current_account.split(',')[0].lower()]: str = current_account.split(',')[1]

    except Exception:
        continue
