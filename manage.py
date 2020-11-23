from flask_cors import CORS
from demo.app import create_app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand


app = create_app()
CORS(app)
manager = Manager(app)


if __name__ == '__main__':
    manager.add_command('server', Server())
    manager.add_command('db', MigrateCommand)
    manager.run()
