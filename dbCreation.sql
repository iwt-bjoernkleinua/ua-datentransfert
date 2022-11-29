CREATE TABLE Relocations (
    extId_aws varchar(255),
    bidLowerLimit varchar(255),
    bidUpperLimit varchar(255),
    distance_aws varchar(255),
    emailComanditer_aws varchar(255),
    enabledForAuctionIndex varchar(255),
    enabledForAuction_aws varchar(255),
    id_aws varchar(255),
    loadingAddressHasElevator_aws varchar(255),
    loadingAppartment_aws varchar(255),
    loadingCarryingDistance_aws varchar(255),
    loadingCity_aws varchar(255),
    loadingComment_aws varchar(255),
    loadingCountry_aws varchar(255),
    loadingFloor_aws varchar(255),
    loadingLatitude_aws varchar(255),
    loadingLongitude_aws varchar(255),
    loadingNoParkingZone_aws varchar(255),
    loadingPersons_aws varchar(255),
    loadingPostalCode_aws varchar(255),
    loadingRegion_aws varchar(255),
    loadingRooms_aws varchar(255),
    loadingStaircaseWidth_aws varchar(255),
    loadingState_aws varchar(255),
    loadingVolume_aws varchar(255),
    lowestOffer varchar(15),
    averageOffer varchar(15),
    numberOfBids varchar(10),
    mountingComment_aws varchar(255),
    mounting_aws varchar(255),
    numOfBids_aws varchar(255),
    ownerId_aws varchar(255),
    packingWorks_aws varchar(255),
    relocationAuctionEndDate_aws varchar(255),
    relocationDateEarliest_aws varchar(255),
    relocationDateLatest_aws varchar(255),
    relocationDateType_aws varchar(255),
    relocationShortId_aws varchar(255),
    services_aws varchar(255),
    setup_boxesPack_aws varchar(255),
    setup_boxesUnpack_aws varchar(255),
    setup_furnitureAssemble_aws varchar(255),
    setup_furnitureDisassemble_aws varchar(255),
    setup_kitchenAssemble_aws varchar(255),
    setup_kitchenDisassemble_aws varchar(255),
    status_aws varchar(255),
    unloadingAddressHasElevator_aws varchar(255),
    unloadingAddressNotKnownYet_aws varchar(255),
    unloadingAppartment_aws varchar(255),
    unloadingCarryingDistance_aws varchar(255),
    unloadingCity_aws varchar(255),
    unloadingComment_aws varchar(255),
    unloadingCountry_aws varchar(255),
    unloadingFloor_aws varchar(255),
    unloadingLatitude_aws varchar(255),
    unloadingLongitude_aws varchar(255),
    unloadingNoParkingZone_aws varchar(255),
    unloadingPostalCode_aws varchar(255),
    unloadingRegion_aws varchar(255),
    unloadingStaircaseWidth_aws varchar(255),
    unloadingState_aws varchar(255),
    volume_aws varchar(255),
    INDEX (enabledForAuctionIndex),
    PRIMARY KEY (extId_aws)
);
    

Create Table Bids(
    account_aws varchar(255),
    appointementText_aws varchar(255),
    bidId_aws varchar(255),
    bidName_aws varchar(255),
    bidNumber_aws int,
    bidPrice_aws DECIMAL(6,2),
    createdDate_aws varchar(255),
    extId_aws varchar(255),
    id_aws varchar(255),
    recomendation_aws varchar(255),
    sortOrder_aws varchar(255),
    status_aws varchar(255),
    topRecomendation_aws varchar(255),
    startDate_aws varchar(255),
    endDate_aws varchar(255),
    relocationId_aws varchar(255),
    incId int auto_increment,
    INDEX (account_aws),
    INDEX(bidId_aws),
    PRIMARY KEY (incId)
);

Create Table Possessions(
    extId_aws varchar(40),
    basementPossessions varchar(1000),
    bathroomPossessions varchar(1000),
    bedroomPossessions varchar(1000),
    boxesPossessions varchar(1000),
    commentsPossessions varchar(1000),
    garagePossessions varchar(1000),
    id_aws varchar(40),
    kitchenPossessions varchar(1000),
    livingRoomPossessions varchar(1000),
    miscPossessions varchar(1000),
    nurseryPossessions varchar(1000),
    possessionsListEditedByUser_aws TINYINT,
    possessionsListEditingActivated_aws TINYINT,
    studyPossessions varchar(1000),
    totalVolume_aws varchar(10),
    INDEX (id_aws),
    Primary Key (extId_aws)    
);

CREATE TABLE Favorites(
    accountId varchar(40),
    relocation varchar(40),
    INDEX (accountId)
);


CREATE TABLE Test(
    test1 varchar(40),
    test2 varchar(40),
    incId int auto_increment,
    Primary Key (incId)
);

CREATE TABLE Employees(
    id_aws varchar(40),
    backOffice INTEGER,
    email_aws varchar(255),
    mobilePhone_aws varchar(255),
    name_aws varchar(255),
    phone_aws varchar(255),
    photo_aws varchar(255),
    position varchar(100),
    salutation_aws varchar(20),
    Primary Key(id_aws)

)

alter table Test AUTO_INCREMENT=1001;