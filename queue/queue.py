class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self, first = None):
        self.first = first

    def is_empty(self):
        return self.first == None

    def peek(self):
        return self.first

    def size(self):
        current_node = self.first
        i = 0

        while current_node != None:
            i += 1
            current_node = current_node.next
        
        return i

    def enqueue(self, value):
        if self.is_empty():
            self.first = Node(value)
        else:
            current_node = self.first

            while current_node.next != None:
                current_node = current_node.next
            
            current_node.next = Node(value)

    def dequeue(self):
        if self.first != None:
            removed = self.first
            self.first = self.first.next
            return removed

    def to_string(self):
        current_node = self.first
        arr = []

        while current_node != None:
            arr.append(current_node.value)
            current_node = current_node.next
        
        return str(arr).replace(',', ' <-')


def tests():
    print('Queue => Operação: valor_recebido |> valor_esperado\n')
    queue = Queue()

    print(f'1. Está vazia: {queue.is_empty()} |> True')
    print(f'2. Tamanho: {queue.size()} |> 0')
    print(f'3. Pegar o primeiro elemento: {queue.peek()} |> None')
    print(f'4. Adicionar "50": {queue.enqueue(50)} |> None')
    print(f'5. Mostrando lista: {queue.to_string()} |> [50]')
    print(f'6. Está vazia: {queue.is_empty()} |> False')
    print(f'7. Tamanho: {queue.size()} |> 1')
    print(f'8. Pegar o primeiro elemento: {queue.peek().value} |> 50')
    print(f'9. Adicionar "13": {queue.enqueue(13)} |> None')
    print(f'10. Mostrando lista: {queue.to_string()} |> [50 <- 13]')
    print(f'11. Está vazia: {queue.is_empty()} |> False')
    print(f'12. Tamanho: {queue.size()} |> 2')
    print(f'13. Removendo "50": {queue.dequeue().value} |> 50')
    print(f'14. Mostrando lista: {queue.to_string()} |> [13]')
    print(f'15. Está vazia: {queue.is_empty()} |> False')
    print(f'16. Tamanho: {queue.size()} |> 1')
    print(f'17. Pegar o primeiro elemento: {queue.peek().value} |> 13')

def main():
    queue = Queue()

    for i in range(10):
        queue.enqueue(i)
    
    print(queue.to_string())

tests()