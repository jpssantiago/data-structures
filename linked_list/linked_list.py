class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def size(self):
        if self.head == None: 
            return 0

        count = 1
        current_node = self.head

        while current_node.next != None:
            count += 1
            current_node = current_node.next

        return count

    def add(self, value):
        if self.head == None:
            self.head = Node(value)
        else:
            if self.head.next == None:
                self.head.next = Node(value)
            else:
                current_node = self.head
                
                while current_node.next != None:
                    current_node = current_node.next

                current_node.next = Node(value)

    def get(self, value):
        if self.head == None:
            return None

        if self.head.value == value:
                return self.head
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

            if current_node.value == value:
                return current_node
            

    def search(self, value):
        if self.head == None:
            return False
        
        if self.head.value == value:
            return True
        
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next

            if current_node.value == value:
                return True
        
        return False

    def delete(self, value):
        if self.head == None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        current_node = self.head
        while current_node.next != None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return True
            
            current_node = current_node.next
        
        return False

    def to_array(self):
        if self.head == None:
            return []

        if self.head.next == None:
            return [self.head.value]

        current_node = self.head
        array = [self.head.value]

        while current_node.next != None:
            current_node = current_node.next

            array.append(current_node.value)
            
        return array

def main():
    list = LinkedList()
    print(f'Size: {list.size()}')
    print(f'Lista: {list.to_array()}')

    list.add(10)
    print(f'\nAdicionando 10: {list.to_array()}')

    print(f'\nDeletando 50 (não tem): {list.delete(50)}')
    print(f'Lista: {list.to_array()}')

    list.add(50)
    print(f'\nAdicionando 50: {list.to_array()}')

    print(f'\nDeletando 50 (tem): {list.delete(50)}')
    print(f'Lista: {list.to_array()}')

    print(f'\nProcurando 30 (não tem): {list.search(30)}')
    print(f'Lista: {list.to_array()}')

    list.add(30)
    print(f'\nAdicionando 30: {list.to_array()}')

    print(f'\nProcurando 30 (tem): {list.search(30)}')
    print(f'Lista: {list.to_array()}')

main()