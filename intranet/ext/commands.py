from intranet.ext.database import db
from intranet.models import Vln, Act
from datetime import datetime


def createdb():
    """Create database"""
    db.create_all()

def dropdb():
    """Clean database"""
    db.drop_all()

def insertdb():
    """Insert database"""
    db.session.bulk_save_objects([
        Vln(olt='',tfc='',vln='')
    ])
    db.session.commit()

def updatedb():
    """Update database"""
    db.session.bulk_update_mappings(Act, [
        {'id':'','req':''},
    ])
    db.session.commit()

def init_app(app):
    # add multiple commands in a bulk
    for command in [createdb, dropdb, insertdb, updatedb]:
        app.cli.add_command(app.cli.command()(command))
