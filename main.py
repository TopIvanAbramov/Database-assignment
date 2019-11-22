import os
import psycopg2
import generate_inserts

conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')

cur = conn.cursor()

cur.execute("DROP SCHEMA public CASCADE; CREATE SCHEMA public;")

queries = open('queries.txt').read()

#print(queries)

cur.execute(queries)


rooms = generate_inserts.insert_room(1, 5)
patients = generate_inserts.insert_patient(101, 105, 1, 5)
doctors = generate_inserts.insert_employee(1, 5, "doctor")
nurses = generate_inserts.insert_employee(5, 10, "nurse")
prescribe = generate_inserts.insert_prescribe(3, 1, 5, 101, 105)
analysis_report = generate_inserts.insert_analysis_result(5, 101, 105)
attends = generate_inserts.insert_attends(100, 1, 5, 101, 105)
chat = generate_inserts.insert_chat(3, 1, 5, 101, 105)
inventory = generate_inserts.insert_inventory(3)
treatment_plan = generate_inserts.insert_treatment_plan(3, 1, 5, 101, 105)
uses = generate_inserts.insert_uses(0, 3, 0, 3)
logs = generate_inserts.insert_log(3)

print(treatment_plan)

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
cur.execute(logs)


print(rooms, patients, doctors, nurses, prescribe, analysis_report, attends, chat, inventory, treatment_plan, uses, logs, sep="\n")

conn.commit()
#conn.close()