from quart import Quart, redirect
from quart_cors import cors
from markupsafe import escape
from os import getenv
from asyncpg.pool import Pool
from asyncpg.exceptions import UniqueViolationError
import asyncpg

app = Quart(__name__)
cors(app)

pool: Pool

SCHEMA_VERSION = 1


# For some reason, asyncpg doesn't type this. This is here for autocomplete
async def get_con() -> asyncpg.Connection:
    return await pool.acquire()


@app.before_first_request
async def prepare():
    global pool

    # postgres://user:password@host:port/database
    pool = await asyncpg.create_pool(dsn=getenv('GOFREE_PG_DSN'))
    con = await get_con()

    try:
        await con.execute(
            'CREATE TABLE IF NOT EXISTS links (name text unique, destination text)'
        )
        await con.execute(
            'CREATE TABLE IF NOT EXISTS schema_version (version int, hello text unique)'
        )
        await con.execute(
            'INSERT INTO schema_version VALUES ($1, $2) ON CONFLICT DO NOTHING',
            SCHEMA_VERSION,
            'hello'
        )
    finally:
        await pool.release(con)


@app.route('/add <path:parts>')
async def add(parts):
    parts = parts.split(' ')
    name = escape(parts[0])
    where = escape(parts[1])
    con = await get_con()

    try:
        await con.execute(
            'INSERT INTO links (name, destination) VALUES ($1, $2)',
            name, where
        )
    except UniqueViolationError:
        return 'Link already exists!'
    finally:
        await pool.release(con)

    return f'Added {name}: {where}'


@app.route('/<name>')
async def link(name):
    con = await get_con()

    try:
        dest = await con.fetchval(
                'SELECT destination FROM links WHERE name = $1', escape(name)
            )
        res = redirect(dest) if dest else 'Not found'
    finally:
        await pool.release(con)

    return res
