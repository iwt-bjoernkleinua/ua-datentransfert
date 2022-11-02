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

class Bid:
    account_aws = None
    appointementText_aws = None
    bidId_aws = None
    bidName_aws = None
    bidNumber_aws = None
    bidPrice_aws = None
    createdDate_aws = None
    extId_aws = None
    id_aws = None
    recomendation_aws = None
    sortOrder_aws = None
    status_aws = None
    topRecomendation_aws = None
    
    
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
sql = "INSERT INTO `Bids` (`account_aws`,`appointementText_aws`,`bidId_aws`,`bidName_aws`,`bidNumber_aws`,`bidPrice_aws`,`createdDate_aws`,`extId_aws`,`id_aws`,`recomendation_aws`,`sortOrder_aws`,`status_aws`,`topRecomendation_aws`) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

dynamodb = boto3.resource("dynamodb", config=my_config)
bidTable = dynamodb.Table("ua-bid-backup")
dbQueryResponse = bidTable.scan()
data = dbQueryResponse["Items"]

while "LastEvaluatedKey" in dbQueryResponse:
    dbQueryResponse = bidTable.scan(
        ExclusiveStartKey=dbQueryResponse["lastEvaluatedKey"]
    )
    data += dbQueryResponse["Items"]



print("There are {} reccords".format(len(data)))

for item in data:
    bid = Bid()
    bid.account_aws = item["account_aws"]
    bid.appointementText_aws = item["appointementText_aws"]
    bid.bidId_aws = item["bidId_aws"]
    bid.bidName_aws = item["bidName_aws"]
    bid.bidNumber_aws = item["bidNumber_aws"]
    bid.bidPrice_aws = item["bidPrice_aws"]
    bid.createdDate_aws = item["createdDate_aws"]
    bid.extId_aws = item ["extId_aws"]
    bid.id_aws = item["id_aws"]
    bid.recomendation_aws = item["recomendation_aws"]
    bid.sortOrder_aws = item["sortOrder_aws"]
    bid.status_aws = item["status_aws"]
    bid.topRecomendation_aws = item["topRecomendation_aws"]
    
    result = cursor.execute(sql,(bid.account_aws, bid.appointementText_aws, bid.bidId_aws, bid.bidName_aws, bid.bidNumber_aws, bid.bidPrice_aws, bid.createdDate_aws, bid.extId_aws, bid.id_aws, bid.recomendation_aws, bid.sortOrder_aws, bid.status_aws, bid.topRecomendation_aws))
db.commit()
    