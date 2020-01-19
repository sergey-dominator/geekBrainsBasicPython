from sys import argv

worked_hours, rate_per_hour, bonus = argv[1:]

try:
    worker_salary = (int(worked_hours) * int(rate_per_hour)) + int(bonus)
    print(f'The worker earned {worker_salary}$')
except ValueError:
    print('Wrong input parameters')
