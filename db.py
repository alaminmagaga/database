import psycopg2
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',
    port=5432,
    user='postgres',
    password=env('DBPASS'),
    database=env('DATABASE')
)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the tasks table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS task
             (id SERIAL PRIMARY KEY,
             task TEXT NOT NULL,
             completed BOOLEAN,
             due_date DATE,
             completion_date DATE,
             priority INTEGER)''')

# Insert sample tasks into the tasks table
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Complete the web page design', True, '2023-05-01', '2023-05-03', 1))
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Create login and signup pages', True, '2023-05-03', '2023-05-05', 2))
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Product management', False, '2023-05-05', None, 3))
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Cart and wishlist creation', False, '2023-05-08', None, 4))
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Payment gateway integration', False, '2023-05-10', None, 5))
cursor.execute("INSERT INTO task (task, completed, due_date, completion_date, priority) VALUES (%s, %s, %s, %s, %s)",
               ('Order management', False, '2023-05-10', None, 6))

# Create the health table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS health
             (id SERIAL PRIMARY KEY,
             task TEXT NOT NULL,
             gender TEXT NOT NULL,
             status TEXT NOT NULL,
             positive BOOLEAN,
             due_date DATE,
             priority INTEGER)''')

# Insert sample health tasks into the health table
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Annual physical exam', 'Male', 'Completed', True, '2023-01-15', 1))
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Dental cleaning', 'Female', 'Completed', True, '2023-03-10', 2))
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Vision test', 'Male', 'Scheduled', False, '2023-06-20', 3))
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Blood pressure check', 'Female', 'Pending', False, '2023-05-10', 4))
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Cholesterol test', 'Male', 'Pending', False, '2023-05-25', 5))
cursor.execute("INSERT INTO health (task, gender, status, positive, due_date, priority) VALUES (%s, %s, %s, %s, %s, %s)",
               ('Flu shot', 'Female', 'Completed', True, '2022-10-01', 6))




# Create the ginger_exporters table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ginger_exporters (
        id SERIAL PRIMARY KEY,
        country TEXT NOT NULL,
        exporter TEXT NOT NULL,
        export_volume INTEGER,
        export_value INTEGER,
        production_area TEXT,
        key_markets TEXT
    )
''')

# Insert sample data into the ginger_exporters table
exporters_data = [
    ('China', 'Various', 530000, 649000000, 'Shandong, Guangxi, Guangdong', 'United States, Japan, European Union'),
    ('India', 'Various', 130000, 130000000, 'Kerala, Karnataka, Orissa', 'United States, European Union, Middle East'),
    ('Netherlands', 'Various', 60000, 127000000, 'Various', 'United States, Germany, United Kingdom'),
    ('Peru', 'Various', 54000, 88000000, 'Junín, Huancavelica, Ayacucho', 'United States, European Union, Japan'),
    ('Nigeria', 'Various', 45000, 73000000, 'Kaduna, Bauchi, Plateau', 'United States, United Kingdom, Netherlands'),
    ('Brazil', 'Various', 30000, 48000000, 'Pará, Bahia, São Paulo', 'United States, European Union, Argentina'),
    ('Thailand', 'Various', 25000, 38000000, 'Chiang Mai, Tak, Kamphaeng Phet', 'Various'),
    ('Vietnam', 'Various', 20000, 31000000, 'Hưng Yên, Phú Thọ, Thái Bình', 'United States, China, Japan'),
    ('Indonesia', 'Various', 18000, 28000000, 'Java, Sumatra, Sulawesi', 'United States, China, Singapore'),
    ('Bangladesh', 'Various', 15000, 23000000, 'Chittagong, Rangamati, Bandarban', 'United States, European Union, Middle East')
]

for exporter in exporters_data:
    cursor.execute('''
        INSERT INTO ginger_exporters (country, exporter, export_volume, export_value, production_area, key_markets)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', exporter)
# Commit the changes and close the connection
conn.commit()
conn.close()
