import sqlite3
import os

import random

import string

IMAGE_DIR='/tmp/kittenkollector/images/' 
NUMERALS = string.digits + string.ascii_lowercase
KODE_LENGTH = 6

from robohash import Robohash

class Database:
    def __init__(self, dbfile, imgdir=IMAGE_DIR):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()

        self.cursor.execute('CREATE TABLE IF NOT EXISTS kittens (id INTEGER PRIMARY KEY, name TEXT, location TEXT)')

        self.imgdir = imgdir
        if not os.path.exists(imgdir):
            os.makedirs(imgdir)

    def create(self, name, location):
        kid = random.randint(0, len(NUMERALS) ** KODE_LENGTH)

        self.cursor.execute('INSERT INTO kittens(id, name, location) VALUES (?, ?, ?)', (kid, name, location))
        self.conn.commit()

        kode = Database._id_to_kode(kid)
        return kode

    def get(self, kode):
        kid = Database._kode_to_id(kode)

        self.cursor.execute('SELECT name, location FROM kittens WHERE id=?', (kid,))
        result = self.cursor.fetchone()
        if not result:
            return None

        name, location = result
        return name, location

    def getimage(self, kode):
        kid = Database._kode_to_id(kode)

        self.cursor.execute('SELECT * FROM kittens WHERE id=?', (kid,))
        result = self.cursor.fetchone()
        if result:
            return self._find_image(kode)

    def close(self):
        self.conn.close()

    def _find_image(self, kode):
        path = os.path.join(self.imgdir, kode + '.png')

        if not os.path.isfile(path):
            rh = Robohash(kode)
            rh.assemble(roboset='set4')
            rh.img.save(path, 'png')

        return path

    def _kode_to_id(kode):
        return int(kode, len(NUMERALS))

    def _id_to_kode(kid):
        digits = []
        while kid != 0:
            rem = kid % len(NUMERALS)
            kid = kid // len(NUMERALS)
            digits.append(NUMERALS[rem])

        return ''.join(reversed(digits))
