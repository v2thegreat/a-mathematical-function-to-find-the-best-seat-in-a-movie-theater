from math import cos, sin, ceil


peripheral_view = 114


def find_best_seat(width_of_screen, distance_between_screen_and_first_row):

    distance_from_screen = cot(peripheral_view) * width_of_screen/2
    best_possible_seat = distance_from_screen -
                            distance_between_screen_and_first_row
    return ceil(best_possible_seat)


def cot(angle):

    return cos(angle)/sin(angle)


def main():
    width_of_screen = 14
    distance_between_screen_and_first_row = 1

    best_seat = find_best_seat(width_of_screen,
                               distance_between_screen_and_first_row)

    print(f'Best Seat Position: {best_seat}')


if __name__ == '__main__':
    main()
