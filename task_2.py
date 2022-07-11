


data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_date = [data[num] for num in range(1,len(data)) if data[num] > data[num-1]]

print(new_date)
        
