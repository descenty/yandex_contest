notation = ('A', 'B', 'C', 'D', 'E', 'F')


def main():
    n = int(input())
    seats = []
    for i in range(n):
        seats.append([list(x) for x in input().split('_')])
    print(seats)
    n = int(input())
    for i in range(n):
        num, side, position = input().split()
        num = int(num)
        flag = False
        for row in range(len(seats)):
            target_seats = seats[row][0 if side == 'left' else 1]
            if side == 'left' and position == 'window':
                target_seats = target_seats[:num]
            elif side == 'left' and position == 'aisle':
                target_seats = target_seats[-num - 1:]
            elif side == 'right' and position == 'window':
                target_seats = target_seats[-num - 1:]
            elif side == 'right' and position == 'aisle':
                target_seats = target_seats[:num]
            print(target_seats)
            if all(x == '.' for x in target_seats):
                flag = True
                if side == 'left' and position == 'window':
                    for index in range(num):
                        seats[row][0][index] = 'X'
                    break
                elif side == 'left' and position == 'aisle':
                    for index in range(num):
                        seats[row][0][-index - 1] = 'X'
                    break
                elif side == 'right' and position == 'window':
                    for index in range(num):
                        seats[row][1][-index - 1] = 'X'
                    break
                elif side == 'right' and position == 'aisle':
                    for index in range(num):
                        seats[row][1][index] = 'X'
                    break
        if not flag:
            print('Cannot fulfill passengers requirements')
        print(seats)


main()
