from gofree.gofree import app
from os import getenv

if __name__ == '__main__':
    port_env = getenv('GOFREE_PORT')
    port = int(port_env) if port_env else 8080

    app.run('0.0.0.0', port)
