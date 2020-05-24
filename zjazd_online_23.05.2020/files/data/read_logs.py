import sys

try:
    f_path = sys.argv[1]
except IndexError:
    f_path = "data/logs.txt"

    with open("logs.txt") as f:
        last_login = {}
        last_logout = {}
        user_total_time = {}
        for line in f:
            login,action,time = line.split(";")
            time = int(time)

            if action == "LOGIN":
                last_login[login] = time

            elif action == "LOGOUT":

                user_total_time[login] = user_total_time.get(login, 0) + time - last_login[login]

print("Czas przebywania w systemie:")
for key,value in sorted(user_total_time.items(),key=lambda x: x[1]):
    print(f"- {key}: {value}s")






