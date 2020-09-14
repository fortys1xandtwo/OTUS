import asyncio
from asyncpg import DataError
from asyncpgsa import pg
from sqlalchemy import MetaData, Table, Column, Integer, String
from lesson9_async_DB.request_json import make_requests

metadata = MetaData()

USERS = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(32), unique=True),
    Column("username", String(32), unique=True),
    Column("email", String(50), unique=True)
)

POSTS = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("title", String(256), nullable=False),
    Column("body", String(256), nullable=False)
)


def print_results(results):
    for index, row in enumerate(results):
        if index == 0:
            print(" | ".join([str(name).ljust(15) for name in row.keys()]))
        print(" | ".join([str(value).ljust(15) for value in row.values()]))


async def test_select():
    u = await pg.query(USERS.select().where(USERS.c.id == 3))
    q = await pg.query(POSTS.select().where(POSTS.c.user_id == dict(u[0])['id']))
    print("Query executed", dict(u[0]), "\n", dict(q[0]))


async def main():
    await pg.init("postgresql://postgres:password@localhost/homework")
    print("Connection established")

    try:
        # for res in api_res[0]:
        #     query = USERS.insert().values(id=res['id'],
        #                           name=res['name'],
        #                           username=res['username'],
        #                           email=res['email'],
        #                           )
        #     await pg.query(query)
        # for res in api_res[1]:
        #     query = POSTS.insert().values(id=res['id'],
        #                                   user_id=res['userId'],
        #                                   title=res['title'],
        #                                   body=res['body'],
        #                                   )
        #     await pg.query(query)
        await test_select()
        all_users = await pg.query(USERS.select())
        all_posts = await pg.query(POSTS.select())
        print(f"Collected {len(all_users)} rows for users, "
              f"{len(all_posts)} rows for posts")

    except DataError as e:
        print("Something went wrong with the data:", e)


if __name__ == '__main__':
    api_res = asyncio.run(make_requests())
    asyncio.run(main())
