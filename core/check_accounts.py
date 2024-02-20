import aiofiles
from loguru import logger

from custom_types.formatted_account import FormattedAccount
from utils import format_account
from .get_eligible_list import eligible_accounts_data


async def check_account(account_data: str) -> bool:
    formatted_account: FormattedAccount | None = format_account(account_data=account_data)

    if not formatted_account:
        return False

    drop_value: str | None = eligible_accounts_data.get(formatted_account.address.lower())

    if not drop_value:
        logger.error(f'{formatted_account.address} | Not Eligible')
        return False

    account_data_dict: dict = {
        'address': formatted_account.address,
        'private_key': formatted_account.private_key,
        'mnemonic': formatted_account.mnemonic
    }
    account_data_for_file: str = ' | '.join([current_value for current_value
                                             in account_data_dict.values()
                                             if current_value])

    async with aiofiles.open(file='eligible.txt',
                             mode='a',
                             encoding='utf-8-sig') as file:
        await file.write(f'{account_data_for_file} | {drop_value}\n')

    logger.success(f'{formatted_account.address} | Eliginle: {drop_value}')
