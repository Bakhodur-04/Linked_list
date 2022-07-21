from linkedList import LinkedList
from point2d import Point2d
import pygame as pg
import sys

FPS = 60
WHITE = (255, 255, 255)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLUE = (0, 0, 225)
INDIGO = (75, 0, 130)


def geometry_rect(screen, user_size, line_width):
    pos = pg.mouse.get_pos()

    point = Point2d(pos[0], pos[1])

    pg.draw.circle(screen, BLUE, (point.__sub__(user_size)), 8)
    pg.draw.circle(screen, BLUE, (point.__add_sub__(user_size)), 8)

    pg.draw.line(screen, RED, (point.__sub__(user_size)), (point.__add_sub__(user_size)), line_width)

    pg.draw.circle(screen, BLUE, (point.__add__(user_size)), 8)
    pg.draw.circle(screen, BLUE, (point.__sub_add__(user_size)), 8)

    pg.draw.line(screen, RED, (point.__add_sub__(user_size)), (point.__add__(user_size)), line_width)

    pg.draw.line(screen, RED, (point.__add__(user_size)), (point.__sub_add__(user_size)), line_width)

    pg.draw.line(screen, RED, (point.__sub_add__(user_size)), (point.__sub__(user_size)), line_width)


def main():
    linked_list = LinkedList()

    while True:
        print("\n1 LinkedList")
        print("2 PyGame")
        print("3 Exit")

        user_input_start = int(input("Введите число: "))

        if user_input_start == 1:
            while True:
                print("1-Append_to_end")
                print("2-Append_to_start")
                print("3-Insert_to_list")
                print("4-Remove_last")
                print("5-Remove_first")
                print("6-Remove_by_index")
                print("7-Get_Item")
                print("8-Print_list")
                print("9-Delete each -i element")
                print("0-Quit")

                user_input_list = int(input("Input number: "))

                if user_input_list == 1:
                    linked_list.append_to_end(int(input("Input number: ")))
                    print("Element added")

                elif user_input_list == 2:
                    linked_list.append_to_start(int(input("Input number: ")))
                    print("Element added")

                elif user_input_list == 3:
                    index = int(input("Input index: "))
                    elem = str(input("Input value: "))
                    linked_list.insert_to_list(elem, index)
                    print("Element added")

                elif user_input_list == 4:
                    linked_list.remove_last()
                    print("Last element removed")

                elif user_input_list == 5:
                    linked_list.remove_first()
                    print("First element removed")

                elif user_input_list == 6:
                    linked_list.remove_by_index(int(input("Input index: ")))

                elif user_input_list == 7:
                    user_index = int(input("Input index: "))
                    if linked_list.__getitem__(user_index):
                        print(f"Your element: {linked_list.__getitem__(user_index)}")
                    else:
                        print(f"Can't find element, try again! List length: {linked_list.__len__()}")

                elif user_input_list == 8:
                    print(f"Your list: {linked_list.print_list()}")

                elif user_input_list == 9:
                    linked_list.del_each_i_element(int(input()))

                elif user_input_list == 0:
                    print(linked_list)
                    print(f"Number of elements: {linked_list.__len__()}")
                    print("Iter: ", end="")
                    for x in linked_list:
                        print(x, end=" ")
                    break
                else:
                    print("Incorrect number! Try again!")
        elif user_input_start == 2:
            point = 0
            points = LinkedList()
            line_width = 4
            screen = pg.display.set_mode((1440, 900))
            screen.fill(WHITE)
            pg.display.update()
            clock = pg.time.Clock()
            pg.display.set_caption("Geometry primitive")
            print("Esc = exit")

            if linked_list:
                str_linked_list = linked_list.__str__()
                new_linked_list = str_linked_list.split()
                arrays = [int(x) for x in new_linked_list]
                if linked_list.__len__() % 2 == 0:
                    points_list = [arrays[i:i + 2] for i in range(0, len(arrays), 2)]
                    pg.draw.lines(screen, INDIGO, False, points_list, width=4)
                    for x in points_list:
                        pg.draw.circle(screen, RED, x, 8)
                else:
                    linked_list.append_to_end(0)
                    points_list = [arrays[i:i + 2] for i in range(0, len(arrays), 2)]
                    pg.draw.lines(screen, INDIGO, False, points_list, width=4)
                    for x in points_list:
                        pg.draw.circle(screen, RED, x, 8)

            run = True
            while run:
                clock.tick(FPS)
                for i in pg.event.get():
                    if i.type == pg.QUIT:
                        sys.exit()
                    if i.type == pg.MOUSEBUTTONDOWN:
                        if i.button == 1:
                            points.append_to_end((Point2d(i.pos[0], i.pos[1])))
                            if point != 0:
                                pg.draw.line(screen, RED, (points[point - 1].x, points[point - 1].y),
                                             (points[point].x, points[point].y), line_width)
                            pg.draw.circle(screen, BLUE, (points[point].x, points[point].y), 8)
                            point += 1
                    if i.type == pg.MOUSEWHEEL:
                        if pg.mouse.get_focused():
                            # pg.draw.rect(screen, GREEN, (pos[0] - 50, pos[1] - 50, 100, 100), 1) # Способ проще
                            geometry_rect(screen, 60, line_width)
                    if i.type == pg.KEYDOWN:
                        if i.key == pg.K_ESCAPE:
                            run = False
                pg.display.update()
                pg.display.flip()
                pg.time.delay(20)
        elif user_input_start == 3:
            break


if __name__ == '__main__':
    main()
