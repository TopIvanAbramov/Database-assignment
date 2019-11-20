import random_data
import random
import datetime
import radar
import string


def insert_uses(a, b, c, d): #a:b - avaiable inventory id's c:d - avaiable trearment id's
    inserts = "INSERT INTO Uses (inventory_id, treatment_id) VALUES\n "

    l = min(min(b - a, d - c), 4)
    for k in range(l):
        inserts +=  "({}, {}),\n".format(a + k, c + k)

    inserts = inserts[:-2] + ';\n'
    return inserts

def randomString(stringLength=10):  #Generate a random string of fixed length
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))



def insert_chat(l, i, j, m, n): #l - number of prescribes, i:j - avaiable employee ssn, m:m - avaiable patient ssn
    inserts = "INSERT INTO Chat (message_id, time, employee_ssn, patient_ssn, text) VALUES\n "

    for k in range(l):
        inserts += "('{}', '{}', {}, {}, '{}'),\n".format(randomString(50),
                                                          radar.random_datetime(
                                                              start=datetime.datetime(year=2015,
                                                                                      month=5,
                                                                                      day=24),
                                                              stop=datetime.datetime(year=2019,
                                                                                     month=5,
                                                                                     day=24)
                                                          ),
                                                    random.randint(i, j - 1),
                                                    random.randint(m, n - 1),
                                                    "Random message"
                                                    )
    inserts = inserts[:-2] + ';\n'
    return inserts


def insert_attends(l, i, j, m, n): #l - number of prescribes, i:j - avaiable employee ssn, m:m - avaiable patient ssn
    inserts = "INSERT INTO Attends (employee_ssn, patient_ssn, cost, description, date) VALUES\n "

    for k in range(l):
        inserts += "({}, {}, {}, '{}', '{}'),\n".format(random.randint(i, j - 1),
                                                    random.randint(m, n - 1),
                                                    random.randint(1000, 50000),
                                                    "Attend description",
                                                    radar.random_date(
                                                        start=datetime.datetime(year=2015,
                                                                            month=5,
                                                                            day=24),
                                                        stop=datetime.datetime(year=2019,
                                                                           month=5,
                                                                           day=24)
                                                    )
                                                    )
    inserts = inserts[:-2] + ';\n'
    return inserts

def insert_prescribe(l, i, j, m, n): #l - number of prescribes, i:j - avaiable employee ssn, m:m - avaiable patient ssn
    inserts = "INSERT INTO Prescribe (employee_ssn, patient_ssn, description, date) VALUES\n "

    for k in range(l):
        inserts += "({}, {}, '{}', '{}'),\n".format(random.randint(i, j - 1),
                                                    random.randint(m, n - 1),
                                                    "Doctor attends patient",
                                                    radar.random_date(
                                                        start=datetime.date(year=2015,
                                                                            month=5,
                                                                            day=24),
                                                        stop=datetime.date(year=2019,
                                                                           month=5,
                                                                           day=24)
                                                    )
                                                    )
    inserts = inserts[:-2] + ';\n'
    return inserts


def insert_analysis_result(i, m, n):
    inserts = "INSERT INTO Analysis_result (id, patient_ssn, type, result, date) VALUES\n "

    for j in range(i):
        inserts += "({}, {}, '{}', '{}', '{}'),\n".format(j,
                                                   random.randint(m, n - 1),
                                                   random.choice(random_data.analysis_types),
                                                   'Medical result',
                                                   radar.random_date(
                                                       start=datetime.date(year=2015,
                                                                           month=5,
                                                                           day=24),
                                                       stop=datetime.date(year=2019,
                                                                          month=5,
                                                                          day=24)
                                                   ),
                                                   )
    inserts = inserts[:-2] + ';\n'
    return inserts

def insert_employee(i, j, type):
    inserts = "INSERT INTO Employee (ssn, name, surname, phone, specialization, salary, type) VALUES \n "
    for k in range(i, j):
        inserts += "({}, '{}', '{}', '+{}', '{}', {}, '{}'),\n".format(k, random.choice(random_data.names),
                                                                       random.choice(random_data.surnames),
                                                                       random.randint(10 ** 11, 10 ** 12 - 1),
                                                                       random.choice(random_data.specialization[type]),
                                                                       random.randint(20, 60) * 1000, type)

    inserts = inserts[:-2] + ';\n'
    return inserts


def insert_patient(i, j, m, n): #i:j - avaiable ssn's m:n - avaiable room_id's
    inserts = "INSERT INTO Patient (ssn, name, surname, gender, weight, birth_date, height, blood_type, phone, country, city, street, building, room_id) VALUES \n"
    for k in range(i, j):
        inserts += "({}, '{}', '{}', '{}', {}, '{}', {}, '{}', '+{}', '{}', '{}', '{}', {}, {}),\n".format(k, random.choice(random_data.names),
                                                                                random.choice(random_data.surnames),
                                                                                random.choice(random_data.genders),
                                                                                random.randint(45, 100),
                                                                                radar.random_date(
                                                                                    start=datetime.date(year=1960,
                                                                                                        month=5,
                                                                                                        day=24),
                                                                                    stop=datetime.date(year=2013,
                                                                                                       month=5,
                                                                                                       day=24)
                                                                                ),
                                                                                random.randint(80, 220),
                                                                                random.choice(random_data.blood_type),
                                                                                random.randint(10 ** 11, 10 ** 12 - 1),
                                                                                random.choice(random_data.countries),
                                                                                random.choice(random_data.cities),
                                                                                random.choice(random_data.street),
                                                                                random.randint(1, 10),
                                                                                random.randint(m, n - 1)
                                                                                )

    inserts = inserts[:-2] + ';\n'
    return inserts


def insert_room(i, j):
    inserts = "INSERT INTO Room (id, type, quantity_of_beds) VALUES \n"
    for k in range(i, j):
        inserts += "({}, '{}', {}),\n".format(k, random.choice(random_data.room_type), random.randint(2, 10))

    inserts = inserts[:-2] + ';\n'
    return inserts


def insert_log(i):
    lgs = list(open('logs.txt'))
    print("INSERT INTO Log VALUES")
    for i in range(i - 1):
        shit, time, type, name = random.choice(lgs).split(sep=" ", maxsplit=3)
        print("({}, '{}', '{}', '{}'),".format(i, name, type, time))
    shit, time, type, name = random.choice(lgs).split(sep=" ", maxsplit=3)
    print("({}, '{}', '{}', '{}');".format(i + 1, name, type, time))


def insert_inventory(i): #i - number of id's
    inserts = "INSERT INTO Inventory_item (id, name, quantity, type, supplier, cost) VALUES \n"
    for k in range(i):
        inserts += "({}, '{}', {}, '{}', '{}', {}),\n".format(k,
                                              random.choice(random_data.inventory),
                                              random.randint(2, 10),
                                              'medicine',
                                              random.choice(random_data.suppliers),
                                              random.randint(10, 50) * 500
                                              )

    inserts = inserts[:-2] + ';\n'
    return inserts



def insert_treatment_plan(n, doc_ssn1, doc_snn_2, pat_snn1, pat_snn_2):
    inserts = "INSERT INTO Treatment_plan (id, doctor_ssn, patient_ssn, discharge_date, hospitalization_date, diagnoses, procedures) VALUES \n"
    for k in range(n):
        diagnoses = random.choice(list(random_data.treatments.keys()))
        inserts += "({}, {}, {}, '{}', '{}', '{}', '{}'),\n".format(k,
                                            random.randint(doc_ssn1, doc_snn_2 - 1),
                                            random.randint(pat_snn1, pat_snn_2 - 1),
                                            radar.random_date(
                                                start=datetime.date(year=2014,
                                                                    month=5,
                                                                    day=24),
                                                stop=datetime.date(year=2015,
                                                                   month=5,
                                                                   day=24)
                                            ),
                                            radar.random_date(
                                                start=datetime.date(year=2012,
                                                                    month=5,
                                                                    day=24),
                                                stop=datetime.date(year=2013,
                                                                   month=5,
                                                                   day=24)
                                            ),
                                            diagnoses,
                                            random.choice(random_data.treatments[diagnoses]))

    inserts = inserts[:-2] + ';\n'
    return inserts


def generate_inserts():
    print(insert_room(1, 5))
    print(insert_patient(101, 105, 1, 5))
    print(insert_employee(1, 5, "doctor"))
    print(insert_employee(5, 10, "nurse"))
    print(insert_analysis_result(5, 101, 105))
    print(insert_prescribe(3, 1, 5, 101, 105))
    print(insert_attends(3, 1, 5, 101, 105))
    print(insert_chat(3, 1, 5, 101, 105))
    print(insert_uses(3, 0, 3, 0, 3))
    print(insert_treatment_plan(3, 1, 5, 101, 105))
    print(insert_inventory(3))

#generate_inserts()
