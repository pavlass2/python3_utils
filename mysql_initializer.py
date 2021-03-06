# Python3
# Generates sql script that creates database and user with rights for that database.

# Parameters.
client_ip = ""
db_ip = ""
db_name = ""
db_user_name = ""
db_user_password = ""

# Check parameters.
if client_ip == "":
    client_ip = input("client_ip: ")
if db_ip == "":
    db_ip = input("db_ip: ")
if db_name == "":
    db_name = input("db_name: ")
if db_user_name == "":
    db_user_name = input("db_user_name: ")
if db_user_password == "":
    db_user_password = input("db_user_password: ")

# Generate script.
script = [
    "-- This script was generated by mysql_initializer using following parameters:\n",
    "-- client_ip: {0}\n".format(client_ip),
    "-- db_ip: {0}\n".format(db_ip),
    "-- db_name: {0}\n".format(db_name),
    "-- db_name: {0}\n".format(db_user_name),
    "\n",
    "-- 1) Create database.\n",
    "CREATE DATABASE IF NOT EXISTS '{0}';\n".format(db_name),
    "\n",
    "-- 2) Create user.\n",
    "CREATE USER IF NOT EXISTS '{0}'@'{1}' IDENTIFIED BY '{2}';\n".format(db_user_name, client_ip, db_user_password),
    "\n",
    "-- 3) Grant user rights.\n"
    "GRANT CREATE, ALTER, ALTER ROUTINE, DROP, DELETE, INSERT, SELECT, UPDATE, REFERENCES, INDEX ON '{0}'.* TO '{1}'@'{2}';\n".format(
        db_name, db_user_name, client_ip),
    "FLUSH PRIVILEGES;\n"
]
print("Writing script:")
for line in script:
    print(line)

# Save to a file.
with open(db_name + '.sql', "w") as file:
    file.writelines(script)
