import datetime

now = datetime.datetime.now()
time = now.strftime("%I:%M:%S")


def log_start():
    print(f'Log Started at {time} \n')


def create_log(keyword):
    print(f'{keyword} at {time} \n')


def close_log():
    print(f'Closed Log at {time} \n')
