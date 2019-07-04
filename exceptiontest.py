data= [0 for i in range(0,5)] 
'''
try:
    for i in range(1,10):
        print(data[i])
except IndexError as e:
    print('error')
'''
for i in range(1,10):
    try:
        print(data[i])
    except IndexError as e:
        print('error')