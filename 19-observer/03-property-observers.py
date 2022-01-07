from typing import Any

# Since python have the @property decorator, we can use it when
# defining observers to make better code

class Event(list):
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        for item in self:
            item(*args, **kwds)


# This is a class that you can inherit from for you to get
# a property_changed event
class PropertyObservable:
    def __init__(self) -> None:
        self.property_changed = Event()


# This is a person that has properties that you
# can observe (know when they change)
class Person(PropertyObservable):
    def __init__(self, age=0) -> None:
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        # In the setter, we verify that the value
        # has been changed and call an event.
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)

# A TrafficAuthoirity is an entity that is interested in
# knowing when a person has age to drive or not
class TrafficAuthority:
    def __init__(self, person: Person):
        self.person = person
        # In the begginning, the authority is always
        # interested in knowing
        person.property_changed.append(
            self.person_changed
        )

    def person_changed(self, name, value):
        if name == "age":
            if value < 16:
                print("Sorry, you still cannot drive")
            else:
                print("Okay, you can drive now")
                # When someone is able to drive,
                # the traffic authority isn't interested
                # anymore
                self.person.property_changed.remove(
                    self.person_changed
                )


if __name__ == "__main__":
    p = Person()
    ta = TrafficAuthority(p)
    for age in range(14, 20):
        print(f"Setting age = {age}")
        p.age = age
