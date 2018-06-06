class animal_stack():
    class stack_node():
        def __init__(self, animal_obj, id_tag):
            self.amimal_obj = animal_obj
            self.id_tag = id_tag

    def __init__(self):
        self.cats = []
        self.dogs = []
        self.id = 0

    def enqueue(self,animal_obj):
        self.id +=1
        if isinstance(Dog, animal_obj):
            self.dogs.append(stack_node(animal_obj,self.id))
        else:
            self.cats.append(stack_node(animal_obj,self.id))

    def dequeue_any(self):
        if self.dogs[-1].id_tag <= self.cats[-1].id_tag:
            return self.dogs.pop()
        else:
            return self.cats.pop()

    def dequeue_cat(self):
        return self.cats.pop()

    def dequeue_dog(self):
        return self.dogs.pop()
