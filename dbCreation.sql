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
    lowestOffer varchar(255),
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
    INDEX (enabledForAuctionIndex)
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
    INDEX (account_aws)
);

Create Table Possessions(
    extId_aws varchar(255),
    basementPossessions varchar(255),
    bathroomPossessions varchar(255),
    bedroomPossessions varchar(255),
    boxesPossessions varchar(255),
    commentsPossessions varchar(255),
    garagePossessions varchar(255),
    id_aws varchar(255),
    kitchenPossessions varchar(255),
    livingRoomPossessions varchar(255),
    miscPossessions varchar(255),
    nurseryPossessions varchar(255),
    possessionsListEditedByUser_aws TINYINT,
    possessionsListEditingActivated_aws TINYINT,
    studyPossessions varchar(255),
    totalVolume_aws varchar(255),
    INDEX (extId_aws)    
)