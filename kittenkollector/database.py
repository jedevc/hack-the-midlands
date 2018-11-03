import sqlite3
import os

import random

IMAGE_DIR='/tmp/kittenkollector/images/' 

from robohash import Robohash

class Database:
    def __init__(self, dbfile, imgdir=IMAGE_DIR):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS kittens (id INTEGER PRIMARY KEY, name TEXT)')

        self.imgdir = imgdir
        if not os.path.exists(imgdir):
            os.makedirs(imgdir)

    def create(self, name):
        kid = random.randint(0, 16 ** 8)

        self.cursor.execute('INSERT INTO kittens(id, name) VALUES (?, ?)', (kid, name))
        self.conn.commit()

        code = Database._id_to_code(kid)
        return code

    def get(self, code):
        kid = Database._code_to_id(code)

        self.cursor.execute('SELECT name FROM kittens WHERE id=?', (kid,))
        result = self.cursor.fetchone()
        if not result:
            return None

        (name,) = result
        return name

    def getimage(self, code):
        kid = Database._code_to_id(code)

        self.cursor.execute('SELECT * FROM kittens WHERE id=?', (kid,))
        result = self.cursor.fetchone()
        if result:
            return self._find_image(code)

    def close(self):
        self.conn.close()

    def _code_to_id(code):
        code = code[:8]
        return int(code, 16)

    def _id_to_code(code):
        return "{0:08X}".format(code)

    def _find_image(self, code):
        path = os.path.join(self.imgdir, code + '.png')

        if not os.path.isfile(path):
            rh = Robohash(code)
            rh.assemble(roboset='set4')
            rh.img.save(path, 'png')

        return path
