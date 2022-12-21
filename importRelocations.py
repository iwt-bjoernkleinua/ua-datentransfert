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


class Relocation:
    extId_aws = None
    bidLowerLimit = None
    bidUpperLimit = None
    distance_aws = None
    emailComanditer_aws = None
    enabledForAuctionIndex = None
    enabledForAuction_aws = None
    id_aws = None
    loadingAddressHasElevator_aws = None
    loadingAppartment_aws = None
    loadingCarryingDistance_aws = None
    loadingCity_aws = None
    loadingComment_aws = None
    loadingCountry_aws = None
    loadingFloor_aws = None
    loadingLatitude_aws = None
    loadingLongitude_aws = None
    loadingNoParkingZone_aws = None
    loadingPersons_aws = None
    loadingPostalCode_aws = None
    loadingRegion_aws = None
    loadingRooms_aws = None
    loadingStaircaseWidth_aws = None
    loadingState_aws = None
    loadingVolume_aws = None
    lowestOffer = None
    averageOffer = None
    numberOfBids = None
    mountingComment_aws = None
    mounting_aws = None
    numOfBids_aws = None
    ownerId_aws = None
    packingWorks_aws = None
    relocationAuctionEndDate_aws = None
    relocationDateEarliest_aws = None
    relocationDateLatest_aws = None
    relocationDateType_aws = None
    relocationShortId_aws = None
    services_aws = None
    setup_boxesPack_aws = None
    setup_boxesUnpack_aws = None
    setup_furnitureAssemble_aws = None
    setup_furnitureDisassemble_aws = None
    setup_kitchenAssemble_aws = None
    setup_kitchenDisassemble_aws = None
    status_aws = None
    unloadingAddressHasElevator_aws = None
    unloadingAddressNotKnownYet_aws = None
    unloadingAppartment_aws = None
    unloadingCarryingDistance_aws = None
    unloadingCity_aws = None
    unloadingComment_aws = None
    unloadingCountry_aws = None
    unloadingFloor_aws = None
    unloadingLatitude_aws = None
    unloadingLongitude_aws = None
    unloadingNoParkingZone_aws = None
    unloadingPostalCode_aws = None
    unloadingRegion_aws = None
    unloadingStaircaseWidth_aws = None
    unloadingState_aws = None
    volume_aws = None


print("HALLO")

my_config=Config(
    region_name="eu-central-1"
)



dynamodb = boto3.resource("dynamodb", config=my_config)
print("Noch da")
relocationTable = dynamodb.Table("ua-relocation")
print("immer noch da")
dbQueryResponse = relocationTable.query(
        IndexName="enabledForAuctionIndex",
        KeyConditionExpression=Key("enabledForAuctionIndex").eq("True")
    )
print("und immer noch")
data = dbQueryResponse["Items"]
credentials = getDbUserNameAndPassword()
print("Crdentials are {}".format(credentials))
dbUserName = credentials["username"]
dbPassword = credentials["password"]
dbName = credentials["dbname"]
dbHost = credentials["host"]
db = pymysql.connect(host=dbHost, user=dbUserName, passwd=dbPassword, database=dbName)
cursor = db.cursor()
#sql = "INSERT INTO `Relocation` (`bidLowerLimit`,`bidUpperLimit`,`distance_aws`,`emailComanditer_aws`,`enabledForAuctionIndex`,`enabledForAuction_aws`,`id_aws`,`loadingAddressHasElevator_aws`,`loadingAppartment_aws`,`loadingCarryingDistance_aws`,`loadingCity_aws`,`loadingComment_aws`,`loadingCountry_aws`,`loadingFloor_aws`,`loadingLatitude_aws`,`loadingLongitude_aws`,`loadingNoParkingZone_aws`,`loadingPersons_aws`,`loadingPostalCode_aws`,`loadingRegion_aws`,`loadingRooms_aws`,`loadingStaircaseWidth_aws`,`loadingState_aws`,`loadingVolume_aws`,`mountingComment_aws`,`mounting_aws`,`numOfBids_aws`,`ownerId_aws`,`packingWorks_aws`,`relocationAuctionEndDate_aws`,`relocationDateEarliest_aws`,`relocationDateLatest_aws`,`relocationDateType_aws`,`relocationShortId_aws`,`services_aws`,`setup_boxesPack_aws`,`setup_boxesUnpack_aws`,`setup_furnitureAssemble_aws`,`setup_furnitureDisassemble_aws`,`setup_kitchenAssemble_aws`,`setup_kitchenDisassemble_aws`,`status_aws`,`unloadingAddressHasElevator_aws`,`unloadingAddressNotKnownYet_aws`,`unloadingAppartment_aws`,`unloadingCarryingDistance_aws`,`unloadingCity_aws`,`unloadingComment_aws`,`unloadingCountry_aws`,`unloadingFloor_aws`,`unloadingLatitude_aws`,`unloadingLongitude_aws`,`unloadingNoParkingZone_aws`,`unloadingPostalCode_aws`,`unloadingRegion_aws`,`unloadingStaircaseWidth_aws`,`unloadingState_aws`,`volume_aws`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"
sql = "INSERT INTO `Relocations` (`extId_aws`,`bidLowerLimit`,`bidUpperLimit`,`distance_aws`,`emailComanditer_aws`,`enabledForAuctionIndex`,`enabledForAuction_aws`,`id_aws`,`loadingAddressHasElevator_aws`,`loadingAppartment_aws`,`loadingCarryingDistance_aws`,`loadingCity_aws`,`loadingComment_aws`,`loadingCountry_aws`,`loadingFloor_aws`,`loadingLatitude_aws`,`loadingLongitude_aws`,`loadingNoParkingZone_aws`,`loadingPersons_aws`,`loadingPostalCode_aws`,`loadingRegion_aws`,`loadingRooms_aws`,`loadingStaircaseWidth_aws`,`loadingState_aws`,`loadingVolume_aws`,`lowestOffer`,`mountingComment_aws`,`mounting_aws`,`numOfBids_aws`,`ownerId_aws`,`packingWorks_aws`,`relocationAuctionEndDate_aws`,`relocationDateEarliest_aws`,`relocationDateLatest_aws`,`relocationDateType_aws`,`relocationShortId_aws`,`services_aws`,`setup_boxesPack_aws`,`setup_boxesUnpack_aws`,`setup_furnitureAssemble_aws`,`setup_furnitureDisassemble_aws`,`setup_kitchenAssemble_aws`,`setup_kitchenDisassemble_aws`,`status_aws`,`unloadingAddressHasElevator_aws`,`unloadingAddressNotKnownYet_aws`,`unloadingAppartment_aws`,`unloadingCarryingDistance_aws`,`unloadingCity_aws`,`unloadingComment_aws`,`unloadingCountry_aws`,`unloadingFloor_aws`,`unloadingLatitude_aws`,`unloadingLongitude_aws`,`unloadingNoParkingZone_aws`,`unloadingPostalCode_aws`,`unloadingRegion_aws`,`unloadingStaircaseWidth_aws`,`unloadingState_aws`,`volume_aws`,`averageOffer`, `numberOfBids`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
for item in data:
    relocation = Relocation()
    relocation.extId_aws=item["extId_aws"]
    relocation.bidLowerLimit=item["bidLowerLimit"]
    relocation.bidUpperLimit=item["bidUpperLimit"]
    relocation.distance_aws=item["distance_aws"]
    relocation.emailComanditer_aws=item["emailComanditer_aws"]
    relocation.enabledForAuctionIndex=item["enabledForAuctionIndex"]
    relocation.enabledForAuction_aws=item["enabledForAuction_aws"]
    relocation.id_aws=item["id_aws"]
    relocation.loadingAddressHasElevator_aws=item["loadingAddressHasElevator_aws"]
    relocation.loadingAppartment_aws=item["loadingAppartment_aws"]
    relocation.loadingCarryingDistance_aws=item["loadingCarryingDistance_aws"]
    relocation.loadingCity_aws=item["loadingCity_aws"]
    relocation.loadingComment_aws=item["loadingComment_aws"]
    relocation.loadingCountry_aws=item["loadingCountry_aws"]
    relocation.loadingFloor_aws=item["loadingFloor_aws"]
    relocation.loadingLatitude_aws=item["loadingLatitude_aws"]
    relocation.loadingLongitude_aws=item["loadingLongitude_aws"]
    relocation.loadingNoParkingZone_aws=item["loadingNoParkingZone_aws"]
    relocation.loadingPersons_aws=item["loadingPersons_aws"]
    relocation.loadingPostalCode_aws=item["loadingPostalCode_aws"]
    relocation.loadingRegion_aws=item["loadingRegion_aws"]
    relocation.loadingRooms_aws=item["loadingRooms_aws"]
    relocation.loadingStaircaseWidth_aws=item["loadingStaircaseWidth_aws"]
    relocation.loadingState_aws=item["loadingState_aws"]
    relocation.loadingVolume_aws=item["loadingVolume_aws"]
    relocation.lowestOffer = "0"
    relocation.mountingComment_aws=item["mountingComment_aws"]
    relocation.mounting_aws=item["mounting_aws"]
    relocation.numOfBids_aws=item["numOfBids_aws"]
    relocation.ownerId_aws=item["ownerId_aws"]
    relocation.packingWorks_aws=item["packingWorks_aws"]
    relocation.relocationAuctionEndDate_aws=item["relocationAuctionEndDate_aws"]
    relocation.relocationDateEarliest_aws=item["relocationDateEarliest_aws"]
    relocation.relocationDateLatest_aws=item["relocationDateLatest_aws"]
    relocation.relocationDateType_aws=item["relocationDateType_aws"]
    relocation.relocationShortId_aws=item["relocationShortId_aws"]
    relocation.services_aws=item["services_aws"]
    relocation.setup_boxesPack_aws=item["setup_boxesPack_aws"]
    relocation.setup_boxesUnpack_aws=item["setup_boxesUnpack_aws"]
    relocation.setup_furnitureAssemble_aws=item["setup_furnitureAssemble_aws"]
    relocation.setup_furnitureDisassemble_aws=item["setup_furnitureDisassemble_aws"]
    relocation.setup_kitchenAssemble_aws=item["setup_kitchenAssemble_aws"]
    relocation.setup_kitchenDisassemble_aws=item["setup_kitchenDisassemble_aws"]
    relocation.status_aws=item["status_aws"]
    relocation.unloadingAddressHasElevator_aws=item["unloadingAddressHasElevator_aws"]
    relocation.unloadingAddressNotKnownYet_aws=item["unloadingAddressNotKnownYet_aws"]
    relocation.unloadingAppartment_aws=item["unloadingAppartment_aws"]
    relocation.unloadingCarryingDistance_aws=item["unloadingCarryingDistance_aws"]
    relocation.unloadingCity_aws=item["unloadingCity_aws"]
    relocation.unloadingComment_aws=item["unloadingComment_aws"]
    relocation.unloadingCountry_aws=item["unloadingCountry_aws"]
    relocation.unloadingFloor_aws=item["unloadingFloor_aws"]
    relocation.unloadingLatitude_aws=item["unloadingLatitude_aws"]
    relocation.unloadingLongitude_aws=item["unloadingLongitude_aws"]
    relocation.unloadingNoParkingZone_aws=item["unloadingNoParkingZone_aws"]
    relocation.unloadingPostalCode_aws=item["unloadingPostalCode_aws"]
    relocation.unloadingRegion_aws=item["unloadingRegion_aws"]
    relocation.unloadingStaircaseWidth_aws=item["unloadingStaircaseWidth_aws"]
    relocation.unloadingState_aws=item["unloadingState_aws"]
    relocation.volume_aws=item["volume_aws"]
    relocation.averageOffer = "0"
    relocation.numberOfBids = "0"                                                                                                                                                                                                                                
    #result = cursor.execute(sql, (relocation.bidLowerLimit,relocation.bidUpperLimit,relocation.distance_aws,relocation.emailComanditer_aws,relocation.enabledForAuctionIndex,relocation.enabledForAuction_aws,relocation.id_aws,relocation.loadingAddressHasElevator_aws,relocation.loadingAppartment_aws,relocation.loadingCarryingDistance_aws,relocation.loadingCity_aws,relocation.loadingComment_aws,relocation.loadingCountry_aws,relocation.loadingFloor_aws,relocation.loadingLatitude_aws,relocation.loadingLongitude_aws,relocation.loadingNoParkingZone_aws,relocation.loadingPersons_aws,relocation.loadingPostalCode_aws,relocation.loadingRegion_aws,relocation.loadingRooms_aws,relocation.loadingStaircaseWidth_aws,relocation.loadingState_aws,relocation.loadingVolume_aws,relocation.mountingComment_aws,relocation.mounting_aws,relocation.numOfBids_aws,relocation.ownerId_aws,relocation.packingWorks_aws,relocation.relocationAuctionEndDate_aws,relocation.relocationDateEarliest_aws,relocation.relocationDateLatest_aws,relocation.relocationDateType_aws,relocation.relocationShortId_aws,relocation.services_aws,relocation.setup_boxesPack_aws,relocation.setup_boxesUnpack_aws,relocation.setup_furnitureAssemble_aws,relocation.setup_furnitureDisassemble_aws,relocation.setup_kitchenAssemble_aws,relocation.setup_kitchenDisassemble_aws,relocation.status_aws,relocation.unloadingAddressHasElevator_aws,relocation.unloadingAddressNotKnownYet_aws,relocation.unloadingAppartment_aws,relocation.unloadingCarryingDistance_aws,relocation.unloadingCity_aws,relocation.unloadingComment_aws,relocation.unloadingCountry_aws,relocation.unloadingFloor_aws,relocation.unloadingLatitude_aws,relocation.unloadingLongitude_aws,relocation.unloadingNoParkingZone_aws,relocation.unloadingPostalCode_aws,relocation.unloadingRegion_aws,relocation.unloadingStaircaseWidth_aws,relocation.unloadingState_aws,relocation.volume_aws))
    result = cursor.execute(sql, (relocation.extId_aws,relocation.bidLowerLimit,relocation.bidUpperLimit,relocation.distance_aws,relocation.emailComanditer_aws,relocation.enabledForAuctionIndex,relocation.enabledForAuction_aws,relocation.id_aws,relocation.loadingAddressHasElevator_aws,relocation.loadingAppartment_aws,relocation.loadingCarryingDistance_aws,relocation.loadingCity_aws,relocation.loadingComment_aws,relocation.loadingCountry_aws,relocation.loadingFloor_aws,relocation.loadingLatitude_aws,relocation.loadingLongitude_aws,relocation.loadingNoParkingZone_aws,relocation.loadingPersons_aws,relocation.loadingPostalCode_aws,relocation.loadingRegion_aws,relocation.loadingRooms_aws,relocation.loadingStaircaseWidth_aws,relocation.loadingState_aws,relocation.loadingVolume_aws,relocation.lowestOffer,relocation.mountingComment_aws,relocation.mounting_aws,relocation.numOfBids_aws,relocation.ownerId_aws,relocation.packingWorks_aws,relocation.relocationAuctionEndDate_aws,relocation.relocationDateEarliest_aws,relocation.relocationDateLatest_aws,relocation.relocationDateType_aws,relocation.relocationShortId_aws,relocation.services_aws,relocation.setup_boxesPack_aws,relocation.setup_boxesUnpack_aws,relocation.setup_furnitureAssemble_aws,relocation.setup_furnitureDisassemble_aws,relocation.setup_kitchenAssemble_aws,relocation.setup_kitchenDisassemble_aws,relocation.status_aws,relocation.unloadingAddressHasElevator_aws,relocation.unloadingAddressNotKnownYet_aws,relocation.unloadingAppartment_aws,relocation.unloadingCarryingDistance_aws,relocation.unloadingCity_aws,relocation.unloadingComment_aws,relocation.unloadingCountry_aws,relocation.unloadingFloor_aws,relocation.unloadingLatitude_aws,relocation.unloadingLongitude_aws,relocation.unloadingNoParkingZone_aws,relocation.unloadingPostalCode_aws,relocation.unloadingRegion_aws,relocation.unloadingStaircaseWidth_aws,relocation.unloadingState_aws,relocation.volume_aws, relocation.averageOffer, relocation.numberOfBids))
db.commit()