from typing import Any

# Lets suppose that you are a doctor and you
# want to be notified when people fall ill


# An event is a list of functions that must be
# invoked when an event happens.
class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class Person:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        # If this is an event, other classes, like a
        # Doctor class can subscribe to this event
        # an know when it happens
        self.falls_ill = Event()

    # When this method is called, an notification is
    # sent
    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


# We actually don't need a class, just a function to call
# a doctor
def call_doctor(name, address):
    print(f"{name} need a doctor at {address}")

# Now we must be sure that whenever a person falls ill, a
# doctor is called

if __name__ == "__main__":
    # We create a person
    person = Person("Sherlock", "221B Baker St")
    # We add the subscribers (callbacks) for the event 
    person.falls_ill.append(
        lambda name, address: print(f"{name} is ill")
    )
    person.falls_ill.append(call_doctor)

    # Lets see what happens when the person catches a cold
    person.catch_a_cold()

    # We can also remove the subscriptions
    person.falls_ill.remove(call_doctor)

    # Now we catch a cold again
    person.catch_a_cold()
