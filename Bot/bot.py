from asyncore import dispatcher
from imaplib import Commands
import time
import logging

from aiogram import Bot, Dispatcher, executor, types


TOKEN = "5785394868:AAGAby1o-g9x5RTrOZi3pLkxiaS5o1ChDTY"
MASSAGE = "DID YOU TAKE MONEY, {} from someone?"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands = ['/start'])
async def start_hendler(message: types.Message):
	id = message.from_user.id
	first_name = message.from_user.first_name
	user_full_name = message.from_user.full_name
	logging.info(f'{id} {user_full_name}')
	await message.reply(f"Hello, {user_full_name}!")

	for i in range(10):
		time.sleep(2)
		await bot.massage(id, MASSAGE.format(first_name))
		
if __name__ == '__main__':
	executor.start_polling(dp)