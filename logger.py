import datetime

now = datetime.datetime.now()


def log_start():
    print(f'Log Started at {now.strftime("%I:%M:%S")} \n')


def create_log(keyword):
    print(f'{keyword} at {now.strftime("%I:%M:%S")} \n')


def close_log():
    print(f'Closed Log at {now.strftime("%I:%M:%S")} \n')
