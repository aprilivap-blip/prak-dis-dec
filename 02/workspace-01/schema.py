import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return [
            Book(
                title="Indahnya Senja Sore",
                author="Indah Purwati",
            ),
            Book(
                title="Aku Berkelana",
                author="Ainka Lana",
            ),
        ]


schema = strawberry.Schema(query=Query)
app = GraphQL(schema)