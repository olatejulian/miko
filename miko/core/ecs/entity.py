from typing import Type, TypeVar, cast

T = TypeVar("T")


class Entity:
    __id_counter = 0

    def __init__(self):
        self.id = Entity.__id_counter

        Entity.__id_counter += 1

        self.__components: dict[Type, object] = {}

    def add(self, component: object) -> None:
        self.__components[type(component)] = component

    def get(self, component_type: Type[T]) -> T | None:
        return cast(T | None, self.__components.get(component_type, None))

    def remove(self, component_type: Type[T]) -> None:
        if component_type in self.__components:
            del self.__components[component_type]

    def has(self, *component_types: Type) -> bool:
        return all(
            component_type in self.__components for component_type in component_types
        )

    def components(self) -> dict[Type, object]:
        return self.__components.copy()
