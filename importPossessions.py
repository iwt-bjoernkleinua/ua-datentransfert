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

class Possession:
        extId_aws = None
        basementPossessions = None
        bathroomPossessions = None
        bedroomPossessions = None
        boxesPossessions = None
        commentsPossessions = None
        garagePossessions = None
        id_aws = None
        kitchenPossessions = None
        livingRoomPossessions = None
        miscPossessions = None
        nurseryPossessions = None
        possessionsListEditedByUser_aws = None
        possessionsListEditingActivated_aws = None
        studyPossessions = None
        totalVolume_aws = None
    
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
sql = "INSERT INTO `Possessions` (`extId_aws`,`basementPossessions`,`bathroomPossessions`,`bedroomPossessions`,`boxesPossessions`,`commentsPossessions`,`garagePossessions`,`id_aws`,`kitchenPossessions`,`livingRoomPossessions`,`miscPossessions`,`nurseryPossessions`,`possessionsListEditedByUser_aws`,`possessionsListEditingActivated_aws`,`studyPossessions`,`totalVolume_aws`) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

dynamodb = boto3.resource("dynamodb", config=my_config)
possessionTable = dynamodb.Table("ua-possession-backup")
dbQueryResponse = possessionTable.scan()
data = dbQueryResponse["Items"]

while "LastEvaluatedKey" in dbQueryResponse:
    dbQueryResponse = possessionTable.scan(
        ExclusiveStartKey=dbQueryResponse["LastEvaluatedKey"]
    )
    data += dbQueryResponse["Items"]


print("There are {} reccords".format(len(data)))

for item in data:
    possession = Possession()
    possession.extId_aws = item["extId_aws"]
    possession.id_aws = item["id_aws"]
    possession.basementPossessions = item["basementPossessions"]
    possession.bathroomPossessions = item["bathroomPossessions"]
    possession.bedroomPossessions = item["bedroomPossessions"]
    possession.boxesPossessions = item["boxesPossessions"]
    possession.commentsPossessions = item["commentsPossessions"]
    possession.garagePossessions = item["garagePossessions"]
    possession.kitchenPossessions = item["kitchenPossessions"]
    possession.livingRoomPossessions = item["livingRoomPossessions"]
    possession.miscPossessions = item["miscPossessions"]
    possession.nurseryPossessions = item["nurseryPossessions"]
    possession.possessionsListEditedByUser_aws = item["possessionsListEditedByUser_aws"]
    possession.possessionsListEditingActivated_aws = item["possessionsListEditingActivated_aws"]
    possession.studyPossessions = item["studyPossessions"]
    possession.totalVolume_aws = item["totalVolume_aws"]
    
    
    result = cursor.execute(sql,(possession.extId_aws,possession.basementPossessions,possession.bathroomPossessions,possession.bedroomPossessions,possession.boxesPossessions,possession.commentsPossessions,possession.garagePossessions,possession.id_aws, possession.kitchenPossessions,possession.livingRoomPossessions,possession.miscPossessions,possession.nurseryPossessions,possession.possessionsListEditedByUser_aws,possession.possessionsListEditingActivated_aws,possession.studyPossessions,possession.totalVolume_aws))
db.commit()