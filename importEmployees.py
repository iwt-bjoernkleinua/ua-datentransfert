import boto3
from botocore.config import Config
from boto3.dynamodb.conditions import Key
import pymysql
import botocore.exceptions
import simplejson as json

def getDbUserNameAndPassword():
    print("in begining")
    secret_name = "rds-portal-credentials-name"
    region_name = "eu-central-1"
    session = boto3.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=region_name
    )
    secretResponse = None
    credentials = None
    try:
        secretResponse = client.get_secret_value(
            SecretId=secret_name
        )
    except botocore.exceptions.ClientError as e:
        print("ERROR {}".format(e))
    print("SecretResponse is {}".format(secretResponse))
    if "SecretString" in secretResponse:
        credentials = secretResponse["SecretString"]
    return json.loads(credentials)

class Employee:
    id = None
    backOffice = None
    email = None
    mobilePhone = None
    name = None
    phone = None
    photo = None
    position = None
    salutation = None
    
    
my_config=Config(
    region_name="eu-central-1"
)

credentials = getDbUserNameAndPassword()
dbUserName = credentials["username"]
dbPassword = credentials["password"]
dbName = credentials["dbname"]
dbHost = credentials["host"]
db = pymysql.connect(host=dbHost, user=dbUserName, passwd=dbPassword, database=dbName)
cursor = db.cursor()
sql = """REPLACE INTO Employees (id_aws, backOffice, email_aws, mobilePhone_aws, name_aws, phone_aws, photo_aws, position, salutation_aws)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

dynamodb = boto3.resource("dynamodb", config=my_config)
employeeTable = dynamodb.Table("ua-employee-backup")
dbQueryResponse = employeeTable.scan()
data = dbQueryResponse["Items"]

while "LastEvaluatedKey" in dbQueryResponse:
    dbQueryResponse = employeeTable.scan(
        ExclusiveStartKey=dbQueryResponse["LastEvaluatedKey"]
    )
    data += dbQueryResponse["Items"]



print("There are {} reccords".format(len(data)))

for item in data:
    employee = Employee()
    if "backOffice" in item:
        if item["backOffice"] == True:
            employee.backOffice = 1
        else:
            employee.backOffice = 0
    else:
        employee.backOffice = None

    employee.id = item["id_aws"] 
    employee.email = item["email_aws"]
    employee.mobilePhone = item["mobilePhone_aws"]
    employee.name = item["name_aws"]
    employee.phone = item ["phone_aws"]
    employee.photo = item["photo_aws"]
    employee.position = item["position"]
    employee.salutation = item["salutation_aws"]

    
    result = cursor.execute(sql,(employee.id, employee.backOffice, employee.email, employee.mobilePhone, employee.name, employee.phone, employee.photo, employee.position, employee.salutation))
db.commit()