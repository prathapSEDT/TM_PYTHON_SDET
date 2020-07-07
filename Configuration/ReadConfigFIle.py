from configparser import ConfigParser

configur=ConfigParser()

configur.read("ApplicationDetails.cnf")

# to get the data from the config file

print(configur.get("ENVIRONMENT",'EXE'))

print(configur.get("DB_DETAILS",'DB_USERNAME'))
