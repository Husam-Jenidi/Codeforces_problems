# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
N = int ( input ( ) )
colors = input ( )
take = 0
for i in range ( N-1 ):
    if colors [ i ]== colors [ i+1 ]:
        take += 1
print(take)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
