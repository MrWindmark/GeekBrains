import json

firm_dict = {}
avg_profit = 0
with open('Task7.txt', 'r') as file:
    for line in file:
        data = line.strip()
        tmp = data.split(' ')
        firm_profit = int(tmp[2]) - int(tmp[3])
        if firm_profit > 0:
            firm_dict[tmp[0]] = firm_profit
            avg_profit += firm_profit

average_profit = {'average_profit': avg_profit / len(firm_dict)}

with open("Task7.json", "w") as f:
    json.dump([firm_dict, average_profit], f)