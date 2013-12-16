from app import app, manager
from flask.ext.migrate import MigrateCommand

manager.add_command('db', MigrateCommand)

<<<<<<< HEAD
app.debug = False
manager.run()
=======
app.debug = True
manager.run()
>>>>>>> d9607955825599cd1317c450f6b1bd3c007c6123
