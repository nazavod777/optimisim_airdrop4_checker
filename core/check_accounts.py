import aiofiles
from loguru import logger

from custom_types.formatted_account import FormattedAccount
from .get_eligible_list import eligible_accounts_data


async def check_account(account_data: FormattedAccount) -> bool:
    drop_value: str | None = eligible_accounts_data.get(account_data.address.lower())

    if not drop_value:
        logger.error(f'{account_data.address} | Not Eligible')
        return False

    account_data_dict: dict = {
        'address': account_data.address,
        'private_key': account_data.private_key,
        'mnemonic': account_data.mnemonic
    }
    account_data_for_file: str = ' | '.join([current_value for current_value
                                             in account_data_dict.values()
                                             if current_value])

    async with aiofiles.open(file='eligible.txt',
                             mode='a',
                             encoding='utf-8-sig') as file:
        await file.write(f'{account_data_for_file} | {drop_value}\n')

    logger.success(f'{account_data.address} | Eliginle: {drop_value}')
