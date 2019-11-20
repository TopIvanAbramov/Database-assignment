import os
import psycopg2
import generate_inserts

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')

cur = conn.cursor()

counter = 0

while(counter <= 50):

    cur.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")

    try:
        cur.execute("""CREATE TABLE Employee(
        ssn INTEGER  PRIMARY KEY,
        name VARCHAR (50),
        surname VARCHAR (50),
        phone VARCHAR(20),
        specialization VARCHAR (50),
        salary INTEGER,
        type VARCHAR (15)
        );
    
        CREATE TABLE Room(
        id INTEGER PRIMARY KEY,
        type VARCHAR (20) NOT NULL,
        quantity_of_beds INTEGER NOT NULL
        );
    
        CREATE TABLE Patient(
        ssn INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR (50) NOT NULL,
        surname VARCHAR (50) NOT NULL,
        gender VARCHAR (25) NOT NULL,
        weight INTEGER,
        birth_date DATE,
        height INTEGER,
        blood_type VARCHAR(20),
        phone VARCHAR(20),
        country VARCHAR(50),
        city VARCHAR(50),
        street VARCHAR(50),
        building VARCHAR(20),
        room_id INTEGER REFERENCES Room(id)
        );
    
    
        CREATE TABLE Log(
        id INTEGER  PRIMARY KEY  NOT NULL,
        name VARCHAR (50) NOT NULL,
        type VARCHAR (50) NOT NULL,
        time TIMESTAMP NOT NULL
        );
    
        CREATE TABLE Inventory_item(
        id INTEGER PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        quantity INTEGER NOT NULL,
        type VARCHAR (50) NOT NULL,
        supplier VARCHAR (50) NOT NULL,
        cost INTEGER NOT NULL
        );
    
        CREATE TABLE Analysis_result(
        id INTEGER NOT NULL,
        patient_ssn INTEGER NOT NULL,
        type VARCHAR(50) NOT NULL,
        result VARCHAR(2000) NOT NULL,
        date DATE NOT NULL,
        PRIMARY KEY(id, patient_ssn)
        );
    
    
        CREATE TABLE Treatment_plan(
        id INTEGER PRIMARY KEY,
        doctor_ssn INTEGER REFERENCES Employee(ssn) NOT NULL,
        patient_ssn INTEGER REFERENCES Patient(ssn) NOT NULL,
        discharge_date DATE,
        hospitalization_date DATE,
        diagnoses VARCHAR (50) NOT NULL,
        procedures VARCHAR (500) NOT NULL
        );
    
        CREATE TABLE Attends(
        employee_ssn INTEGER REFERENCES Employee(ssn) NOT NULL,
        patient_ssn INTEGER REFERENCES Patient(ssn) NOT NULL,
        cost INTEGER,
        description VARCHAR(500),
        date TIMESTAMP,
        PRIMARY KEY(date, employee_ssn, patient_ssn)
        );
    
        CREATE TABLE Prescribe(
        employee_ssn INTEGER REFERENCES Employee(ssn) NOT NULL,
        patient_ssn INTEGER REFERENCES Patient(ssn) NOT NULL,
        description VARCHAR(500),
        date TIMESTAMP,
        PRIMARY KEY(date, employee_ssn, patient_ssn)
        );
    
        CREATE TABLE Chat(
        message_id VARCHAR(50) NOT NULL,
        time TIMESTAMP NOT NULL,
        employee_ssn INTEGER REFERENCES Employee(ssn) NOT NULL,
        patient_ssn INTEGER REFERENCES Patient(ssn) NOT NULL,
        text VARCHAR(500),
        PRIMARY KEY(message_id, employee_ssn, patient_ssn)
        );
        
        CREATE TABLE Uses(
        inventory_id INTEGER NOT NULL,
        treatment_id INTEGER NOT NULL,
        FOREIGN KEY (inventory_id) REFERENCES Inventory_item(id),
        FOREIGN KEY (treatment_id) REFERENCES Treatment_plan(id),
        PRIMARY KEY(inventory_id, treatment_id)
        );
    
       """)
    except:
        print("Tables already exist")


    try:
        rooms = generate_inserts.insert_room(1, 5)
        patients = generate_inserts.insert_patient(101, 105, 1, 5)
        doctors = generate_inserts.insert_employee(1, 5, "doctor")
        nurses = generate_inserts.insert_employee(5, 10, "nurse")
        prescribe = generate_inserts.insert_prescribe(3, 1, 5, 101, 105)
        analysis_report = generate_inserts.insert_analysis_result(5, 101, 105)
        attends = generate_inserts.insert_attends(3, 1, 5, 101, 105)
        chat = generate_inserts.insert_chat(3, 1, 5, 101, 105)
        inventory = generate_inserts.insert_inventory(3)
        treatment_plan = generate_inserts.insert_treatment_plan(3, 1, 5, 101, 105)
        uses = generate_inserts.insert_uses(0, 3, 0, 3)

        cur.execute(rooms)
        cur.execute(patients)
        cur.execute(doctors)
        cur.execute(nurses)
        cur.execute(prescribe)
        cur.execute(analysis_report)
        cur.execute(attends)
        cur.execute(chat)
        cur.execute(inventory)
        cur.execute(treatment_plan)
        cur.execute(uses)
    except:
        print(rooms, patients, doctors, nurses, prescribe, analysis_report, attends, chat, inventory, treatment_plan, uses, sep="\n")
        break
        #print("Information already inserted")


    conn.commit()
    #conn.close()

    counter+=1