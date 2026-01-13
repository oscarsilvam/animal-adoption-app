import sqlite3

def animal_select(res):
    if res is None:
        return None
    
    return{
        "id": res[0],
        "photo" : res[1],
        "name" : res[2],
        "species" : res[3],
        "breed" : res[4],
        "age" : res[5],
        "description" : res[6],
        "email" : res[7],
        "address" : res[8],
        "city" : res[9],
        "post_code" : res[10]

        }
    

class Database:
    """
    A simple SQLite database handler for managing the 'Animals' table.
    
    Attributes:
        db_path (str): Path to the SQLite database file.
        conn (sqlite3.Connection): Connection object to the SQLite database.
        cur (sqlite3.Cursor): Cursor object for executing SQL queries.
    """
    
    def __init__(self, db_path='db/animals.db'):
        """
        Initialize the Database instance.
        Args:
            db_path (str, optional): Path to the SQLite database file.
            Defaults to 'animals.db'.
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

    
    def add_table_animals(self):
        """
        Create the 'Animals' table if it does not exist.
        
        """
        self.connect()
        query = ("""CREATE TABLE IF NOT EXISTS Animals 
            (id_animal INTEGER PRIMARY KEY AUTOINCREMENT, 
            photo TEXT,     
            name VARCHAR(25), 
            species VARCHAR(25), 
            race VARCHAR(25), 
            age INTEGER,
            description VARCHAR(500),
            email VARCHAR(100),
            address VARCHAR(100),
            city VARCHAR (50),
            post_code VARCHAR(7));""")
        
        self.cur.execute(query)
        self.conn.commit()
        self.close()

    
    def get_all_animals(self):
        """
        Retrieve all records from the 'Animals' table.
        
        Returns:
            list of dictionary: Each dictionary represents one animal record.
        """
        self.connect()
        query = ("""SELECT * FROM Animals""")

        res = self.cur.execute(query)
        animals = res.fetchall()
        self.close()
        return [animal_select(animal) for animal in animals]
    
    
    def add_animal(self, photo, name, species, race, age, description, email, 
                   address, city, post_code):
        """
        Insert a new animal record into the 'Animals' table.
        Returns:
            int: The inserted animal.
        """
        self.connect()
        query = ("""INSERT INTO Animals(photo, name, species, race, age, 
            description, email, address, city, post_code) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
        
        self.cur.execute(query, (photo, name, species, race, age, description, 
                                 email, address, city, post_code))
        
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
        query = ("""SELECT * FROM Animals 
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
        Search for animals matching the entry in name, espece, race, 
        description, or city.
            Args:
        entry (str): The search keyword.
            Returns:
        list of dictionary: All matching animals.
        """
        self.connect()
        
        query = ("""SELECT * FROM Animals 
                      WHERE name LIKE ? OR species LIKE ? OR race LIKE ? 
                      OR description LIKE ? OR city LIKE ?""")
        
        params = tuple(['%' + entry + '%'] * 5)
        
        res = self.cur.execute(query,params)
        animals = res.fetchall()
        self.close()
        return [animal_select(a) for a in animals]

 
    