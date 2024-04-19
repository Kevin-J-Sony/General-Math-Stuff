'''
price_list = []

def ten_day_moving_average_list(p_list):
    ten_day_list = [p_list[0]]
    for i in range(1, 10):
        ten_day_list.append((i * ten_day_list[-1] + p_list[i]) / (i+1))
    
    for i in range(10, len(p_list)):
        ten_day_list.append((10 * ten_day_list[-1] + p_list[i] - ten_day_list[-10]) / 10)
        
    return ten_day_list

def diff_day_moving_averages(p_list, n_days):
    n_day_list = [p_list[0]]
    for i in range(1, n_days):
        n_day_list.append((i * n_day_list[-1] + p_list[i]) / (i+1))
    
    for i in range(n_days, len(p_list)):
        n_day_list.append((n_days * n_day_list[-1] + p_list[i] - n_day_list[-n_days]) / n_days)
        
    return n_day_list


price_list = [i for i in range(1, 101)]
print(price_list)
print(ten_day_moving_average_list(price_list))
print(diff_day_moving_averages(price_list, 50))
'''

x = 0.5
y1 = x/(1-x**2)
y2 = 0
for i in range(50):
    y2 = y2 + x**(2*i + 1)


print(y1)
print(y2)
print(y1 - y2)