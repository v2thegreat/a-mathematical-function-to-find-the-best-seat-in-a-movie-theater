from find_best_seat_in_theater import find_best_seat


def main():
    width_of_screen = int(input('Enter the size of the screen in the number of seats infront of it: '))
    distance_between_screen_and_first_row = int(input('Enter the distance between the screen and the first row, also in the number of seats: '))

    best_seat = find_best_seat(width_of_screen,
                               distance_between_screen_and_first_row)

    print(f'Best Seat Position: {best_seat}th row')

if __name__ == '__main__':
    main()
