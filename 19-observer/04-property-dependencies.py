from typing import Any

# Dependencies between properties can be a problem
# if you have chained dependencies

class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()


class Person(PropertyObservable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age

    # We define a property that uses another, which
    # is notified. How can we send notifications
    # for this one? It is "read_only"...
    @property
    def can_vote(self):
        return self._age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        
        # We may think we the best place to call it
        # is in the age setter, since age modifies
        # can_vote. In order to do this,
        # we need to cache the old value, then
        # change the age, an compare afterwards.
        old_can_vote = self.can_vote
    
        self._age = value
        self.property_changed("age", value)

        if self.can_vote != old_can_vote:
            self.property_changed("can_vote", value)


if __name__ == "__main__":
    def person_changed(name, value):
        if name == "can_vote":
            print(f"Voting ability changed to {value}")

    p = Person()
    p.property_changed.append(
        person_changed
    )

    for age in range(16, 21):
        print(f"Changing age to {age}")
        p.age = age
