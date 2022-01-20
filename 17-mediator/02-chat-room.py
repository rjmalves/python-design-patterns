# Vamos implementar um esquema de sala de chat

from unicodedata import name


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        self.chat_log.append(s)
        print(f"[{self.name}'s chat] {s}")

    def say(self, message):
        self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        self.room.direct_message(self.name, who, message)


class ChatRoom:
    def __init__(self):
        self.people = []

    def join(self, person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def direct_message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == "__main__":
    # Neste caso o objeto room é o mediator
    room = ChatRoom()

    john = Person("John")
    jane = Person("Jane")

    room.join(john)
    room.join(jane)

    john.say("hi room!")
    jane.say("oh, hey john")

    simon = Person("Simon")
    room.join(simon)
    simon.say("hi everyone")

    jane.private_message("Simon", "glad you could join us!")
