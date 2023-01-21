# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

N = int(input())
police_list = list(map(int, input().strip().split()))[:N]
police_man = 0
crime = 0
for i in range(N):
    if police_list[i] > 0:
        police_man += police_list[i]
    if police_man > 0 > police_list[i]:
        police_man -= 1
        crime -= 1
    if police_list[i] < 0:
        crime += 1
print(crime)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
