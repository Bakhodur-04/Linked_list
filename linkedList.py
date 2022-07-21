class LinkedList:
    class Node:
        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        if not node:
            return ""

        result = str(node.element)
        while node.next_node:
            node = node.next_node
            result += " " + str(node.element)

        return result

    def __len__(self):
        if not self.head:
            return 0
        i = 1

        node = self.head
        while node.next_node:
            i += 1
            node = node.next_node
        return i

    def __iter__(self):
        self.current_node = self.head
        return self

    def __next__(self):
        if self.current_node:
            res = self.current_node.element
            self.current_node = self.current_node.next_node
            return res
        else:
            self.current_node = self.head
            raise StopIteration

    def __getitem__(self, index):
        if self.head is None:
            print("Item are missing")
        i = 0
        k = 0
        node = self.head
        length_list = self.__len__()
        if (index >= 0) and (index <= length_list):
            while node is not None:
                if i >= index:
                    return node.element
                node = node.next_node
                i += 1
            return False
        elif (index < 0) and (index*(-1) <= length_list):
            index *= -1
            while node is not None:
                if k == length_list - index:
                    return node.element
                node = node.next_node
                k += 1
            return False
        else:
            print(f"Index out of range, try again! Length list {self.__len__()}")

    def append_to_end(self, element):
        if not self.head:
            self.head = self.Node(element)
            return

        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)

    def append_to_start(self, element):
        if not self.head:
            self.head = self.Node(element)
            return

        node = self.head
        self.head = self.Node(element, next_node=node)

    def insert_to_list(self, element, index):
        try:
            if not self.head:
                self.head = self.Node(element)
                return

            i = 0
            node = self.head
            prev_node = 0
            if index == 0:
                self.append_to_start(element)
            else:
                while i < index:
                    prev_node = node
                    node = node.next_node
                    i += 1

                prev_node.next_node = self.Node(element, next_node=node)

        except AttributeError:
            print(f"Your index out of list, try again! List length = {self.__len__()}")
        except TypeError:
            print("Input your index and try again!")

    def remove_last(self):
        node = self.head
        prev_node = 0
        while node.next_node:
            prev_node = node
            node = node.next_node

        prev_node.next_node = None

    def remove_first(self):
        node = self.head
        self.head = node.next_node

    def remove_by_index(self, index):
        node = self.head
        prev = None
        curr = 0
        if index <= self.__len__():
            while node:
                if curr == index:
                    if prev:
                        prev.next_node = node.next_node
                    else:
                        self.head = node.next_node
                        return

                prev = node
                node = node.next_node
                curr += 1
            print("Your element removed")
        else:
            print(f"Your index out of list, try again! List length = {self.__len__()}")

    def print_list(self):
        print(self.__str__())

    def del_each_i_element(self, index):
        count = 0
        if index == 0:
            print(f"Your index out of range")
        elif index <= self.__len__():
            while count < self.__len__():
                count += index - 1
                self.remove_by_index(count)
            print(self.__str__())
        else:
            print(f"Your index out of range, list length: {self.__len__()}")
