import sqlite3

def animal_select(res):
    if res is None:
        return None
    
    return{
        "id": res[0],
        "name" : res[1],
        "species" : res[2],
        "breed" : res[3],
        "age" : res[4],
        "description" : res[5],
        "email" : res[6],
        "address" : res[7],
        "city" : res[8],
        "post_code" : res[9]

        }
    

class Database:
    """
    A simple SQLite database handler for managing the 'Animaux' table.
    
    Attributes:
        db_path (str): Path to the SQLite database file.
        conn (sqlite3.Connection): Connection object to the SQLite database.
        cur (sqlite3.Cursor): Cursor object for executing SQL queries.
    """
    
    def __init__(self, db_path='db/animaux.db'):
        """
        Initialize the Database instance.
        Args:
            db_path (str, optional): Path to the SQLite database file.
            Defaults to 'animaux.db'.
        """
        self.db_path = db_path
        self.conn = None
        self.cur = None

    
    def connect(self):
        """
        Establish a connection to the SQLite database and create a cursor.
        If a connection already exists, reuse it.
        """
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
            self.cur = self.conn.cursor()
    
    
    def close(self):
        """
        Close the connection to the database and reset the 
        connection and cursor attributes.
        """
        if self.conn:
            self.conn.close()
            self.conn = None
            self.cur = None

    
    def add_table_animaux(self):
        """
        Create the 'Animaux' table if it does not exist.
        
        """
        self.connect()
        query = ("""CREATE TABLE IF NOT EXISTS Animaux 
            (id_animal INTEGER PRIMARY KEY AUTOINCREMENT, 
            nom VARCHAR(25), 
            espece VARCHAR(25), 
            race VARCHAR(25), 
            age INTEGER,
            description VARCHAR(500),
            courriel VARCHAR(100),
            adresse VARCHAR(100),
            ville VARCHAR (50),
            code_postal VARCHAR(7));""")
        
        self.cur.execute(query)
        self.conn.commit()
        self.close()

    
    def get_all_animaux(self):
        """
        Retrieve all records from the 'Animaux' table.
        
        Returns:
            list of dictionary: Each dictionary represents one animal record.
        """
        self.connect()
        query = ("""SELECT * FROM Animaux""")

        res = self.cur.execute(query)
        animaux = res.fetchall()
        self.close()
        return [animal_select(animal) for animal in animaux]
    
    
    def add_animal(self, nom, espece, race, age, description, courriel, 
                   adresse, ville, code_postal):
        """
        Insert a new animal record into the 'Animaux' table.
        Returns:
            int: The inserted animal.
        """
        self.connect()
        query = ("""INSERT INTO Animaux(nom, espece, race, age, 
            description, courriel, adresse, ville, code_postal) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        
        self.cur.execute(query, (nom, espece, race, age, description, 
                                 courriel, adresse, ville, code_postal))
        
        self.conn.commit()
        res = self.cur.execute("SELECT LAST_INSERT_ROWID()")
        new_id = res.fetchone()[0]
        self.close()

        return self.get_animal(new_id)
    
    
    def get_animal(self, id_animal):
        """
        Retrieve a single animal record by its ID.
        Args:
            id_animal (int): The ID of the animal to retrieve.
        Returns:
            dictionary or None: The animal record as a dictionary, 
            or None if not found.
        """
        self.connect()
        query = ("""SELECT * FROM Animaux 
                 WHERE id_animal = ?""")
        res = self.cur.execute(query, (id_animal,))
        line = res.fetchone()
        self.close()
        
        if line is None:
            return None
        
        animal_chosen = animal_select(line)
        return animal_chosen
    
    
    def get_entry(self, entry):
        """
        Search for animals matching the entry in nom, espece, race, 
        description, or ville.
            Args:
        entry (str): The search keyword.
            Returns:
        list of dictionary: All matching animals.
        """
        self.connect()
        
        query = ("""SELECT * FROM Animaux 
                      WHERE nom LIKE ? OR espece LIKE ? OR race LIKE ? 
                      OR description LIKE ? OR ville LIKE ?""")
        
        params = tuple(['%' + entry + '%'] * 5)
        
        res = self.cur.execute(query,params)
        animaux = res.fetchall()
        self.close()
        return [animal_select(a) for a in animaux]

 
    