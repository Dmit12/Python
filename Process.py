# "диспетчер задач"
# Консольная программа, которая управляется текстовыми командами, выполняющими
# следующие действия.
# Показ запущенных процессов, и количество выделенной им памяти
# Остановка и возобновление процесса
# Изменение приоритета выбранного процесса.

import psutil
from parse import *

def user_help():
	print('ДОКУМЕНТАЦИЯ\n'
		  'pp #показать процессы\n'
		  's PID #остановить процесс\n'
		  'r PID #возобновить процесс\n'
		  'chp PID#сменить приоритет')

user_help()
while True:
	user_command = input('\n')
	if 'pp' in user_command:
		print("\n\n\n%-5s %-30s %-10s" % ('PID', 'NAME', 'MEMORY'))
		for proc in psutil.process_iter():
			pinfo = proc.as_dict(attrs=['pid', 'name'])
			print("%-5s %-30s %-10d" % (pinfo["pid"], pinfo["name"], (proc.memory_info()[1] / 1024)))

	if 's' in user_command:
		result = parse("s {pid}", user_command)['pid']
		psutil.Process(int(result)).suspend()
		pname = psutil.Process(int(result)).as_dict(attrs=['pid', 'name'])['name']
		print(f'\nПроцесс {pname} остановлен\n')

	if 'r' in user_command:
		result = parse("r {pid}", user_command)['pid']
		psutil.Process(int(result)).resume()
		pname = psutil.Process(int(result)).as_dict(attrs=['pid', 'name'])['name']
		print(f'\nПроцесс {pname} возобновлен')

	if 'chp' in user_command:
		result = parse("chp {pid}", user_command)['pid']
		psutil.Process(int(result)).nice(psutil.HIGH_PRIORITY_CLASS)
		print('\nПриоритет повышен')

	if 'help' in user_command:
		user_help()
