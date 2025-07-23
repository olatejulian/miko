from .entity import Entity


class World:
    def __init__(self):
        self.__entities: list[Entity] = []

    def create_entity(self) -> Entity:
        entity = Entity()

        self.__entities.append(entity)

        return entity

    def remove_entity(self, entity: Entity) -> None:
        if entity in self.__entities:
            self.__entities.remove(entity)

    def get_entities_with(self, *component_types: type) -> list[Entity]:
        return [entity for entity in self.__entities if entity.has(*component_types)]

    def get_entities(self) -> list[Entity]:
        return self.__entities

    def clear(self) -> None:
        self.__entities.clear()
