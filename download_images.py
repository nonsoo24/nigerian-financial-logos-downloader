import requests
import os

image_data = [
    {
        "bankName": "Kuda.",
        "bankCode": "090267",
        "scCode": "50211",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/kuda.png"
    },
    {
        "bankName": "78 Finance Company Limited",
        "bankCode": "110072",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/78-Finance-Company.png"
    },
    {
        "bankName": "9 Payment Service Bank (9PSB)",
        "bankCode": "120001",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/9psb.png"
    },
    {
        "bankName": "9jaPay MFB",
        "bankCode": "090629",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Amegy-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/abbey_mortgage_bank.png",
        "bankCode": "070010",
        "scCode": "000",
        "bankName": "Abbey Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ABSU-MFB.png",
        "bankCode": "090640",
        "scCode": "000",
        "bankName": "ABSU MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Access Bank",
        "bankCode": "000014",
        "scCode": "044",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/access.png"
    },
    {
        "bankName": "Access Bank PLC (Diamond)",
        "bankCode": "000005",
        "scCode": "063",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/access.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/accion_mfb.png",
        "bankCode": "090134",
        "scCode": "000",
        "bankName": "ACCION MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ada-MFB.png",
        "bankCode": "090483",
        "scCode": "000",
        "bankName": "Ada MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Advancly MFB",
        "bankCode": "090759",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Advancly-MFB.png"
    },
    {
        "bankName": "Advans La Fayette MFB",
        "bankCode": "090155",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Advans-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Aella-MFB.png",
        "bankCode": "090614",
        "scCode": "000",
        "bankName": "Aella MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/AG-Mortgage-MFB.png",
        "bankCode": "100028",
        "scCode": "000",
        "bankName": "AG Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Akalabo MFB",
        "bankCode": "090698",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "AKSU MFB",
        "bankCode": "090756",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Aksu-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Akubank.png",
        "bankCode": "090531",
        "scCode": "000",
        "bankName": "Aku MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "AL-BARAKAH MFB",
        "bankCode": "090133",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Alert-MFB.png",
        "bankCode": "090297",
        "scCode": "000",
        "bankName": "Alert MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Alpha Morgan Bank",
        "bankCode": "000041",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Alpha-Morgan-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Alternative-Bank.png",
        "bankCode": "000037",
        "scCode": "000",
        "bankName": "Alternative Bank Limited",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Amac-MFB.png",
        "bankCode": "090394",
        "scCode": "000",
        "bankName": "AMAC MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ample MFB",
        "bankCode": "090770",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ample_mfb_480.png"
    },
    {
        "bankName": "ANIOMA MFB",
        "bankCode": "090751",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ANIOMA-MFB.png"
    },
    {
        "bankName": "Apex Trust MFB",
        "bankCode": "090737",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Apex-Trust-MFB.png"
    },
    {
        "bankName": "ARM MFB",
        "bankCode": "090816",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Asset-Matrix-MFB.png",
        "bankCode": "090287",
        "scCode": "000",
        "bankName": "Asset Matrix MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Assets-MFB.png",
        "bankCode": "090473",
        "scCode": "000",
        "bankName": "Asset MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Auchi Poly MFB",
        "bankCode": "090817",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Avuenegbe-MFB.png",
        "bankCode": "090478",
        "scCode": "000",
        "bankName": "Avuenegbe MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Awacash-MFB.png",
        "bankCode": "090633",
        "scCode": "000",
        "bankName": "Awacash MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090662",
        "scCode": "000",
        "bankName": "Awesome MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Aztec-MFB.png",
        "bankCode": "090540",
        "scCode": "000",
        "bankName": "Aztec MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Babcock MFB",
        "bankCode": "090729",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Baines Credit MFB",
        "bankCode": "090188",
        "scCode": "51229",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/bainescredit_mfb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/BAM-MFB.png",
        "bankCode": "090651",
        "scCode": "000",
        "bankName": "Bam MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Banc-Corp-MFB.png",
        "bankCode": "090581",
        "scCode": "000",
        "bankName": "Banc Corp MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Bankeasy MFB",
        "bankCode": "090789",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/BankEasy-MFB.png"
    },
    {
        "bankName": "Bankit MFB",
        "bankCode": "090275",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Bankly MFB",
        "bankCode": "090529",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bankly.png"
    },
    {
        "bankName": "Baobab MFB",
        "bankCode": "090136",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Baobab-MFB.png"
    },
    {
        "bankName": "Barnawa MFB",
        "bankCode": "090783",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Barnawa-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090672",
        "scCode": "000",
        "bankName": "Bellbank MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Benysta-MFB.png",
        "bankCode": "090413",
        "scCode": "000",
        "bankName": "Benysta Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Berahchah-MFB.png",
        "bankCode": "090618",
        "scCode": "000",
        "bankName": "Berachah MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Beststar MFB",
        "bankCode": "090615",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Best-Star-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090683",
        "scCode": "000",
        "bankName": "Bethel MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Blooms MFB",
        "bankCode": "090743",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Boctrust-MFB.png",
        "bankCode": "090117",
        "scCode": "000",
        "bankName": "Boctrust MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bokkos-MFB.png",
        "bankCode": "090703",
        "scCode": "000",
        "bankName": "Bokkos MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Bold MFB",
        "bankCode": "090753",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bold-MFB.png"
    },
    {
        "bankName": "Borgu MFB",
        "bankCode": "090395",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Boromu-MFB.png",
        "bankCode": "090501",
        "scCode": "000",
        "bankName": "Boromu MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Borstal-MFB.png",
        "bankCode": "090454",
        "scCode": "000",
        "bankName": "Borstal MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Bosak MFB",
        "bankCode": "090176",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bosak-MFB.png"
    },
    {
        "bankName": "Bowen MFB",
        "bankCode": "090148",
        "scCode": "50931",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/bowen_mfb.png"
    },
    {
        "bankName": "Branch International Finance Company Limited",
        "bankCode": "050006",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Branch.png"
    },
    {
        "bankName": "Build MFB",
        "bankCode": "090613",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Build-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bundi-MFB.png",
        "bankCode": "090661",
        "scCode": "000",
        "bankName": "Bundi MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090655",
        "scCode": "000",
        "bankName": "Bunkure MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "BuyPower MFB",
        "bankCode": "090682",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/BuyPower-MFB.png"
    },
    {
        "bankName": "Bway MFB",
        "bankCode": "090774",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Bway-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Canaan-MFB.png",
        "bankCode": "090647",
        "scCode": "000",
        "bankName": "Canaan MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Capitalmetriq Swift Microfinance Bank",
        "bankCode": "090509",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/CapitalMetriq-Swift-MFB-(1).png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Capstone-MFB.png",
        "bankCode": "090445",
        "scCode": "000",
        "bankName": "Capstone MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Carbon",
        "bankCode": "100026",
        "scCode": "565",
        "bankStatus": "active",
        "bankAvailability": "90%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/carbon.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Cardinalstone.png",
        "bankCode": "050017",
        "scCode": "000",
        "bankName": "Cardinalstone",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "CashConnect MFB",
        "bankCode": "090360",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/CashConnect-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/CashRite-MFB.png",
        "bankCode": "090649",
        "scCode": "000",
        "bankName": "CashRite MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "CENTRUM FINANCE",
        "bankCode": "050032",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Centrum-Finance.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Chanelle-MFB.png",
        "bankCode": "090397",
        "scCode": "000",
        "bankName": "Chanelle-MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Chase MFB",
        "bankCode": "090523",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/chase_mfb_480.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/citibank.png",
        "bankCode": "000009",
        "scCode": "023",
        "bankName": "Citi Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Citycode-Mortgage-Bank.png",
        "bankCode": "070027",
        "scCode": "000",
        "bankName": "Citycode Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Fedeth-MFB.png",
        "bankCode": "090482",
        "scCode": "000",
        "bankName": "Clearpay MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ConsistentTrust-MFB.png",
        "bankCode": "090553",
        "scCode": "000",
        "bankName": "Consistent Trust MFB (CTMFB)",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Consumer-MFB.png",
        "bankCode": "090130",
        "scCode": "000",
        "bankName": "Consumer MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "COOPFUND MFB",
        "bankCode": "090717",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/corestep_mfb.png",
        "bankCode": "090365",
        "scCode": "000",
        "bankName": "CoreStep MicroFinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/coronation.png",
        "bankCode": "060001",
        "scCode": "559",
        "bankName": "Coronation",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Country-Finance-MFB.png",
        "bankCode": "050001",
        "scCode": "000",
        "bankName": "County Finance",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Covenant MFB",
        "bankCode": "070006",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Covenant-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Credit-Direct.png",
        "bankCode": "110049",
        "scCode": "000",
        "bankName": "Credit Direct",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Creditville-MFB.png",
        "bankCode": "090611",
        "scCode": "000",
        "bankName": "Creditville MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Crystal Finance Company Limited",
        "bankCode": "050029",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Crystal-Finance-Company.png"
    },
    {
        "bankName": "Daily Trust MFB",
        "bankCode": "090705",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090596",
        "scCode": "000",
        "bankName": "Dal MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Davenport-1.png",
        "bankCode": "090673",
        "scCode": "000",
        "bankName": "Davenport MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Daylight Microfinance Bank",
        "bankCode": "090167",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/daylight_mfb_480.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DeltaTrust-Mortgage-Bank.png",
        "bankCode": "070023",
        "scCode": "000",
        "bankName": "Delta Trust Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Destiny MFB",
        "bankCode": "090723",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Destiny_MFB.png"
    },
    {
        "bankName": "Digitvant MFB",
        "bankCode": "090745",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Digitvant-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090404",
        "scCode": "000",
        "bankName": "Doje MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "DOT MFB",
        "bankCode": "090470",
        "scCode": "50162",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DOT_MFB.png"
    },
    {
        "bankName": "DSC Microfinance Bank",
        "bankCode": "090821",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DSC-MFB.png"
    },
    {
        "bankName": "DW MFB",
        "bankCode": "090721",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ebarcs_mfb.png",
        "bankCode": "090156",
        "scCode": "000",
        "bankName": "e-BARCs MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Earnwell-MFB.png",
        "bankCode": "090674",
        "scCode": "000",
        "bankName": "Earnwell MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ecobank Bank",
        "bankCode": "000010",
        "scCode": "050",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ecobank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ecobank.png",
        "bankCode": "100008",
        "scCode": "000",
        "bankName": "Ecobank Xpress Account",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090694",
        "scCode": "000",
        "bankName": "Ejindu MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ekondo_mfb.png",
        "bankCode": "090097",
        "scCode": "562",
        "bankName": "Ekondo MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Emaar MFB",
        "bankCode": "090712",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Emaar_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Entity-MFB.png",
        "bankCode": "090656",
        "scCode": "000",
        "bankName": "Entity MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Evib Finance",
        "bankCode": "050034",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Evib-Finance.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Excel-MFB.png",
        "bankCode": "090678",
        "scCode": "000",
        "bankName": "Excel Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Excellent-MFB.png",
        "bankCode": "090541",
        "scCode": "000",
        "bankName": "Excellent Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "FairMoney MFB",
        "bankCode": "090551",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Fairmoney.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Fast-Credit-Limited.png",
        "bankCode": "050009",
        "scCode": "000",
        "bankName": "Fast Credit Limited",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "FCMB",
        "bankCode": "000003",
        "scCode": "214",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/fcmb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/fcmb.png",
        "bankCode": "090409",
        "scCode": "000",
        "bankName": "FCMB MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Federal Polytechnic Nekede MFB",
        "bankCode": "090398",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/FedPoly-Nekede-MFB.png"
    },
    {
        "bankName": "FETS",
        "bankCode": "100001",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/FET.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Fewchore-Finance.png",
        "bankCode": "050003",
        "scCode": "000",
        "bankName": "Fewchore Finance",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ffs_mfb.png",
        "bankCode": "090153",
        "scCode": "000",
        "bankName": "FFS Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Fidelity Bank",
        "bankCode": "000007",
        "scCode": "070",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/fidelity.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Firmus-MFB.png",
        "bankCode": "090366",
        "scCode": "000",
        "bankName": "Firmus MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "First Bank of Nigeria",
        "bankCode": "000016",
        "scCode": "011",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/fbn-quest.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/First-Trust-Mortgage-Bank.png",
        "bankCode": "090107",
        "scCode": "000",
        "bankName": "First trust Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Firstmonie.png",
        "bankCode": "100014",
        "scCode": "000",
        "bankName": "Firstmonie Wallet",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "FOCUS MFB",
        "bankCode": "090709",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090521",
        "scCode": "000",
        "bankName": "Foresight Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Fortismobile",
        "bankCode": "100016",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Fortis-Mobile.png"
    },
    {
        "bankName": "FSDH Merchant Bank",
        "bankCode": "400001",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/fsdh-(1).png"
    },
    {
        "bankName": "FUD MFB",
        "bankCode": "090318",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/FUD-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Gabysn-MFB.png",
        "bankCode": "090591",
        "scCode": "000",
        "bankName": "Gabsyn MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Gadol Finance",
        "bankCode": "050033",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Gadol-Finance.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/GDL-Finance.png",
        "bankCode": "050026",
        "scCode": "000",
        "bankName": "GDL Finance",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Globus Bank",
        "bankCode": "000027",
        "scCode": "00103",
        "bankStatus": "active",
        "bankAvailability": "87%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/globus_bank.png"
    },
    {
        "bankName": "Goldman MFB",
        "bankCode": "090574",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/goldman_mfb_480.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090586",
        "scCode": "000",
        "bankName": "Gombe MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "GoMoney",
        "bankCode": "100022",
        "scCode": "100022",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/gomoney.png"
    },
    {
        "bankName": "Goodshepherd MFB",
        "bankCode": "090664",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Good-shepherd-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/GOSIFECHUKWU-MFB.png",
        "bankCode": "090687",
        "scCode": "000",
        "bankName": "Gosifechukwu MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Grants-MFB.png",
        "bankCode": "90335",
        "scCode": "000",
        "bankName": "Grants Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Greenacres-MFB.png",
        "bankCode": "090599",
        "scCode": "000",
        "bankName": "Greenacres MFB ",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Greenwich Merchant Bank",
        "bankCode": "060004",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Grooming-MFB.png",
        "bankCode": "090195",
        "scCode": "000",
        "bankName": "Grooming MFB ",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "GTBank Plc",
        "bankCode": "000013",
        "scCode": "058",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/gtb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/GTI.png",
        "bankCode": "090385",
        "scCode": "000",
        "bankName": "GTI MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Gwong-MFB.png",
        "bankCode": "090500",
        "scCode": "000",
        "bankName": "Gwong MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Haggai Mortgage Bank",
        "bankCode": "070017",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "95%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Haggai-Mortgage-Bank-(1).png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Halo-MFB.png",
        "bankCode": "090539",
        "scCode": "000",
        "bankName": "Halo MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "HILLPOST MFB",
        "bankCode": "090761",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Hillpost-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Hope-PSB.png",
        "bankCode": "120002",
        "scCode": "000",
        "bankName": "Hope PSB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "IBANK MFB",
        "bankCode": "090115",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Ibbu MFB",
        "bankCode": "090697",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/IBBU-MFB.png"
    },
    {
        "bankName": "Igbo- Ukwu MFB",
        "bankCode": "090803",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Ihiala MFB",
        "bankCode": "090725",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ihiala_MFB.png"
    },
    {
        "bankName": "Ijare MFB",
        "bankCode": "090730",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ijare-MFB.png"
    },
    {
        "bankName": "Ikere MFB",
        "bankCode": "090799",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ikere-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ikire-MFB.png",
        "bankCode": "090279",
        "scCode": "000",
        "bankName": "Ikire MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090681",
        "scCode": "000",
        "bankName": "Ikoyi ile MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ile Oluji MFB",
        "bankCode": "090710",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ile_Oluji_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090037",
        "scCode": "000",
        "bankName": "Ilishan MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ilora MFB",
        "bankCode": "090430",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ilora-MFB.png"
    },
    {
        "bankName": "Imowo MFB",
        "bankCode": "090417",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Imowo_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Imperial-Homes-Mortgage_Bank.png",
        "bankCode": "100024",
        "scCode": "000",
        "bankName": "Imperial Homes Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/IMSU-MFB.png",
        "bankCode": "090670",
        "scCode": "000",
        "bankName": "IMSU MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Indulge MFB",
        "bankCode": "090772",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Indulge-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Insight-MFB.png",
        "bankCode": "090434",
        "scCode": "000",
        "bankName": "Insight MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/IRL-MFB.png",
        "bankCode": "090149",
        "scCode": "000",
        "bankName": "Irl MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "ISUA MFB",
        "bankCode": "090701",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/ISUA_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090353",
        "scCode": "000",
        "bankName": "Isuofia Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "JAIZ Bank",
        "bankCode": "000006",
        "scCode": "301",
        "bankStatus": "active",
        "bankAvailability": "85%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/jaiz.png"
    },
    {
        "bankName": "Jigawa Savings and Loans Limited",
        "bankCode": "070029",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/JIGAWA-SAVINGS-AND-LOANS-LTD.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/jubilee_life.png",
        "bankCode": "090003",
        "scCode": "000",
        "bankName": "JubileeLife",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/KadPoly-MFB.png",
        "bankCode": "090320",
        "scCode": "000",
        "bankName": "KadPoly MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090669",
        "scCode": "000",
        "bankName": "Kadupe MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Kaizen MFB",
        "bankCode": "090800",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Kaizen-MFB.png"
    },
    {
        "bankName": "Katagum MFB",
        "bankCode": "090684",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Katsu MFB",
        "bankCode": "090749",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Katsu-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090667",
        "scCode": "000",
        "bankName": "Kayi MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/KayVee-MFB.png",
        "bankCode": "090554",
        "scCode": "000",
        "bankName": "KayVee MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/KC-MFB.png",
        "bankCode": "090549",
        "scCode": "000",
        "bankName": "KC MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/KCMB_MFB.png",
        "bankCode": "090191",
        "scCode": "000",
        "bankName": "KCMB MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/KEGOW_CHAMSMOBILE.png",
        "bankCode": "100036",
        "scCode": "000",
        "bankName": "KEGOW (ChamsMobile)",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Kenechukwu MFB",
        "bankCode": "090602",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Kenechukwu-MFB.png"
    },
    {
        "bankName": "Keystone Bank",
        "bankCode": "000002",
        "scCode": "082",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/keystone.png"
    },
    {
        "bankName": "Kolomoni MFB",
        "bankCode": "090480",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Kolomoni-MFB.png"
    },
    {
        "bankName": "Kredimoney Microfinance Bank",
        "bankCode": "090380",
        "scCode": "50200",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/kredimoney.png"
    },
    {
        "bankName": "Lawyers MFB",
        "bankCode": "090724",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Lawyers_mfb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/LeadCity-MFB.png",
        "bankCode": "090650",
        "scCode": "000",
        "bankName": "Leadcity MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Letshego MFB",
        "bankCode": "090420",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Letshego-MFB.png"
    },
    {
        "bankName": "Levite MFB",
        "bankCode": "090731",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Levite-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Life-Gate-MFB.png",
        "bankCode": "090557",
        "scCode": "000",
        "bankName": "LifeGate MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Lightway MFB",
        "bankCode": "090807",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/LightWay-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Links-MFB.png",
        "bankCode": "090435",
        "scCode": "000",
        "bankName": "Links MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Liquidcrest MFB",
        "bankCode": "090780",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Liquidcrest-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/living_trust_mortgage_bank.png",
        "bankCode": "07007",
        "scCode": "000",
        "bankName": "Living Trust Morgage Bank Plc",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Loma Bank",
        "bankCode": "090620",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Loma-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/lotus_bank.png",
        "bankCode": "000029",
        "scCode": "000",
        "bankName": "Lotus Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/M36-Bank.png",
        "bankCode": "100035",
        "scCode": "000",
        "bankName": "M36",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Maal MFB",
        "bankCode": "090764",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Maal-MFB.png"
    },
    {
        "bankName": "Madobi MFB",
        "bankCode": "090605",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Maestro MFB",
        "bankCode": "090746",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Maestro-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/mainstreet_mfb.png",
        "bankCode": "090171",
        "scCode": "000",
        "bankName": "Mainstreet MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/manny_mfb.png",
        "bankCode": "090383",
        "scCode": "51313",
        "bankName": "Manny Microfinance bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Mercury-Microfinance-bank.png",
        "bankCode": "090589",
        "scCode": "000",
        "bankName": "Mercury Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/MicroBiz-MFB.png",
        "bankCode": "090587",
        "scCode": "000",
        "bankName": "Microbiz MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Mint Microfinance Bank",
        "bankCode": "090763",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Mint.png",
        "bankCode": "090281",
        "scCode": "50304",
        "bankName": "Mint-Finex MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Mkobo_MFB.png",
        "bankCode": "090455",
        "scCode": "000",
        "bankName": "Mkobo Mfb",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Model MFB",
        "bankCode": "090775",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Momo PSB",
        "bankCode": "120003",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Momo-PSB.png"
    },
    {
        "bankName": "Moneyfield MFB",
        "bankCode": "090144",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Moneyfield-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/MONEYMASTER-PSB.png",
        "bankCode": "120005",
        "scCode": "000",
        "bankName": "Moneymaster PSB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Moniepoint",
        "bankCode": "090405",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "87%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/moniepoint.png"
    },
    {
        "bankName": "Moremonee MFB",
        "bankCode": "090685",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/M&M-MFB.png"
    },
    {
        "bankName": "MOUA MFB",
        "bankCode": "090659",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/MichaelOkparaUniagric-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Mutual-Alliance-MFB.png",
        "bankCode": "070028",
        "scCode": "000",
        "bankName": "Mutual Alliance Mortgage Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Mutual Benefits MFB",
        "bankCode": "090190",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Mutual-Benefits-MFB.png"
    },
    {
        "bankName": "NAF MFB",
        "bankCode": "090740",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Nasarawa MFB",
        "bankCode": "090349",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nasarawa_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/NDDC-MFB.png",
        "bankCode": "090679",
        "scCode": "000",
        "bankName": "NDDC MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Neptune MFB",
        "bankCode": "090329",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Neptune-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Net-MFB.png",
        "bankCode": "090675",
        "scCode": "000",
        "bankName": "Net MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/New-Dawn-MFB.png",
        "bankCode": "090205",
        "scCode": "000",
        "bankName": "New Dawn MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nexim-Bank.png",
        "bankCode": "030001",
        "scCode": "000",
        "bankName": "Nexim Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Nexton MFB",
        "bankCode": "090818",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nexton-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nigerian-Prisons-MFB.png",
        "bankCode": "090505",
        "scCode": "000",
        "bankName": "Nigerian Prisons MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Nomase MFB",
        "bankCode": "090736",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nomase-MFB.png"
    },
    {
        "bankName": "Nombank MFB",
        "bankCode": "090645",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Northquest Finance ",
        "bankCode": "050030",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Northquest-Finance.png"
    },
    {
        "bankName": "Noun MFB",
        "bankCode": "090822",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Nova Bank",
        "bankCode": "060003",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nova_Bank.png"
    },
    {
        "bankName": "Novus MFB",
        "bankCode": "090734",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Novus-MFB.png"
    },
    {
        "bankName": "NOWNOW DIGITAL SYSTEMS",
        "bankCode": "100032",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/contech_global.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nsuk-MFB.png",
        "bankCode": "090491",
        "scCode": "000",
        "bankName": "NSUK MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nuggets-MFB.png",
        "bankCode": "090676",
        "scCode": "000",
        "bankName": "Nuggets MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Nwannegadi-MFB.png",
        "bankCode": "090399",
        "scCode": "000",
        "bankName": "Nwannegadi MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "OBELEDU MFB",
        "bankCode": "090755",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Obollo MFB",
        "bankCode": "090810",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Oche MFB",
        "bankCode": "090333",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Oche-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Octopus-MFB.png",
        "bankCode": "090576",
        "scCode": "000",
        "bankName": "Octopus MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090654",
        "scCode": "000",
        "bankName": "Odoakpu MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "OGBERURU MFB",
        "bankCode": "090738",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Ogige MFB",
        "bankCode": "090739",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ogige-MFB.png"
    },
    {
        "bankName": "Ohha MFB",
        "bankCode": "090626",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ohha-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/OK-MFB.png",
        "bankCode": "090567",
        "scCode": "000",
        "bankName": "OK MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090646",
        "scCode": "000",
        "bankName": "Okengwe MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "OKO MFB",
        "bankCode": "090348",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Oko-MFB.png"
    },
    {
        "bankName": "OKWO-OHA MFB",
        "bankCode": "090752",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/OKWO-OHA-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Olive-MFB.png",
        "bankCode": "090696",
        "scCode": "000",
        "bankName": "Olive MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Omak-MFB.png",
        "bankCode": "090700",
        "scCode": "000",
        "bankName": "Omak MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Opay Digital Services Limited",
        "bankCode": "100004",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "87%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/OPAY.png"
    },
    {
        "bankName": "Optimus Bank",
        "bankCode": "000036",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "86%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Optimus-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090492",
        "scCode": "000",
        "bankName": "Oraukwu MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "OSANTA MFB",
        "bankCode": "090750",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/OSCOTECH-MFB.png",
        "bankCode": "090396",
        "scCode": "000",
        "bankName": "Oscotech Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Osomhe MFB",
        "bankCode": "090715",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Otech MFB",
        "bankCode": "090580",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Otech-MFB-(1).png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090542",
        "scCode": "000",
        "bankName": "Otuo MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ourpass MFB",
        "bankCode": "090767",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/OurPass-MFB.png"
    },
    {
        "bankName": "Ours MFB",
        "bankCode": "090346",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Paga",
        "bankCode": "100002",
        "scCode": "100002",
        "bankStatus": "active",
        "bankAvailability": "99%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/paga.png"
    },
    {
        "bankName": "PALMPAY",
        "bankCode": "100033",
        "scCode": "999991",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Palmpay.png"
    },
    {
        "bankName": "Parallex Bank",
        "bankCode": "000030",
        "description": "",
        "scCode": "526",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/parallex_bank.png"
    },
    {
        "bankName": "Parkway-ReadyCash",
        "bankCode": "100003",
        "scCode": "311",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/parkway_readycash.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Pathfinder-MFB.png",
        "bankCode": "090680",
        "scCode": "000",
        "bankName": "Pathfinder MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/PATRICKGOLD_MICROFINANCE_BANK.png",
        "bankCode": "090317",
        "scCode": "000",
        "bankName": "Patrickgold Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Paystack-Titan",
        "bankCode": "100039",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/titan_paystack.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Peace-MFB.png",
        "bankCode": "090402",
        "scCode": "000",
        "bankName": "Peace MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Pecan Trust Microfinance Bank",
        "bankCode": "090137",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/PecanTrust-MFB.png"
    },
    {
        "bankName": "Personal Trust MFB",
        "bankCode": "090135",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Personal-MFB-Ltd..png"
    },
    {
        "bankName": "Pettysave MFB",
        "bankCode": "090768",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Pettysave-MFB.png"
    },
    {
        "bankName": "PocketApp",
        "bankCode": "100042",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/PocketApp.png"
    },
    {
        "bankName": "Poder Finance",
        "bankCode": "050021",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/PFI-Finance.png"
    },
    {
        "bankName": "POINTONE MFB",
        "bankCode": "090754",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Pointone-MFB.png"
    },
    {
        "bankName": "POLARIS BANK",
        "bankCode": "000008",
        "scCode": "076",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/polaris.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Polyibadan-MFB.png",
        "bankCode": "090534",
        "scCode": "000",
        "bankName": "Polyibadan MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Premium Trust Bank",
        "bankCode": "000031",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Premium_trust_bank.png"
    },
    {
        "bankName": "Prestige MFB",
        "bankCode": "090274",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Prestige-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/PristineDivitis-MFB.png",
        "bankCode": "090499",
        "scCode": "000",
        "bankName": "Pristine Divitis MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Prodigy MFB",
        "bankCode": "090784",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Prodigy-MFB.png"
    },
    {
        "bankName": "Prospa Capital Microfinance Bank",
        "bankCode": "090495",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Goodnews_mfb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Prospects-MFB.png",
        "bankCode": "090689",
        "scCode": "000",
        "bankName": "Prospects MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Providus Bank",
        "bankCode": "000023",
        "scCode": "101",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/providus.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090690",
        "scCode": "000",
        "bankName": "Prudent Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Purplemoney-MFB.png",
        "bankCode": "090303",
        "scCode": "000",
        "bankName": "Purple Money MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Pyramid-MFB.png",
        "bankCode": "090657",
        "scCode": "000",
        "bankName": "Pyramid MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Qube-MFB.png",
        "bankCode": "090569",
        "scCode": "000",
        "bankName": "Qube MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Rand Merchant Bank",
        "bankCode": "000024",
        "scCode": "502",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/rand_merchant_bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Randalpha-MFB.png",
        "bankCode": "090496",
        "scCode": "000",
        "bankName": "Randalpha MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Rayyan MFB",
        "bankCode": "090616",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Rayyan_MFB.png"
    },
    {
        "bankName": "Rehoboth Microfinance Bank",
        "bankCode": "090463",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Rehoboth-MFB.png"
    },
    {
        "bankName": "Renmoney MFB",
        "bankCode": "090198",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Renmoney-MFB.png"
    },
    {
        "bankName": "Retrust MFB",
        "bankCode": "090766",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/retrust_mfb_480.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090666",
        "scCode": "000",
        "bankName": "Revelation MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Rex-MFB.png",
        "bankCode": "090449",
        "scCode": "000",
        "bankName": "Rex MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Ric MFB",
        "bankCode": "090720",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Rima Growth Pathway MFB",
        "bankCode": "090515",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Rima-Growth-Pathway-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Rockshield.png",
        "bankCode": "090547",
        "scCode": "000",
        "bankName": "Rockshield MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/RoyalBlue-MFB.png",
        "bankCode": "090622",
        "scCode": "000",
        "bankName": "Royal Blue MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Royal Exchange MFB",
        "bankCode": "090138",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Royal-Exchange-MFB-(1).png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/RSU-MFB.png",
        "bankCode": "090535",
        "scCode": "000",
        "bankName": "RSU MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Rubies",
        "bankCode": "090175",
        "scCode": "125",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/rubies.png"
    },
    {
        "bankName": "Run MFB",
        "bankCode": "090771",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Run-MFB.png"
    },
    {
        "bankName": "Sabi MFB",
        "bankCode": "090727",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Sabi-MFB.png"
    },
    {
        "bankName": "Safe Haven MFB",
        "bankCode": "090286",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/safe_haven_mfb.png"
    },
    {
        "bankName": "Sagamu MFB",
        "bankCode": "090140",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Sagamu-MFB.png"
    },
    {
        "bankName": "Sciart Finance",
        "bankCode": "050024",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/seedvest.png",
        "bankCode": "090369",
        "scCode": "000",
        "bankName": "Seedvest Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Shalom-MFB.png",
        "bankCode": "090502",
        "scCode": "000",
        "bankName": "Shalom MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Shepherd Trust MFB",
        "bankCode": "090401",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Shepherd_Trust_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Signature-Bank.png",
        "bankCode": "000034",
        "scCode": "000",
        "bankName": "Signature Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "110034",
        "scCode": "000",
        "bankName": "Simplify Energy",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Sincere MFB",
        "bankCode": "090339",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Sincere_MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/SolidAllianzeMFB.png",
        "bankCode": "090506",
        "scCode": "000",
        "bankName": "Solid Allianze MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Soroman MFB",
        "bankCode": "090769",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Soroman-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Source-MFB.png",
        "bankCode": "090641",
        "scCode": "000",
        "bankName": "Source MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Sparkle MFB",
        "bankCode": "090325",
        "scCode": "51310",
        "bankStatus": "active",
        "bankAvailability": "87%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/sparkle.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/spectrum_mfb.png",
        "bankCode": "090436",
        "scCode": "000",
        "bankName": "Spectrum MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Spring Sky Finance",
        "bankCode": "050036",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Spring-Sky-Finance.png"
    },
    {
        "bankName": "Springfield MFB",
        "bankCode": "090806",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Springfield-MFB.png"
    },
    {
        "bankName": "Stanbic IBTC Bank",
        "bankCode": "000012",
        "scCode": "221",
        "bankStatus": "active",
        "bankAvailability": "90%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/stanbic.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/stanbic.png",
        "bankCode": "100007",
        "scCode": "000",
        "bankName": "StanbicMobileMoney",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Standard Chartered",
        "bankCode": "000021",
        "scCode": "068",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/standard_chartered.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090162",
        "scCode": "000",
        "bankName": "Stanford MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Stellas.png",
        "bankCode": "090262",
        "scCode": "000",
        "bankName": "Stellas MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Sterling Bank",
        "bankCode": "000001",
        "scCode": "232",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/sterling.png"
    },
    {
        "bankName": "Sulspap MFB",
        "bankCode": "090305",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Sulspap-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Suntop-MFB.png",
        "bankCode": "090644",
        "scCode": "000",
        "bankName": "Suntop MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "SUNTRUST BANK",
        "bankCode": "000022",
        "scCode": "100",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/suntrust.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Support-MFB.png",
        "bankCode": "090446",
        "scCode": "000",
        "bankName": "Support MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Sure Anchor MFB",
        "bankCode": "090728",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "SWIFT TRUST MFB",
        "bankCode": "090757",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/SunTrust-MFB.png"
    },
    {
        "bankName": "TAJ Bank",
        "bankCode": "000026",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/taj_bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Taj-PinsPay.png",
        "bankCode": "080002",
        "scCode": "000",
        "bankName": "TAJ_Pinspay",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Tanadi.png",
        "bankCode": "090560",
        "scCode": "000",
        "bankName": "Tanadi MFB (CRUST)",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/tangerine_money.png",
        "bankCode": "090426",
        "scCode": "51269",
        "bankName": "Tangerine Money",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Tellerone MFB",
        "bankCode": "090788",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "TENN MFB",
        "bankCode": "090716",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "THE BROOK FINANCE LTD",
        "bankCode": "050031",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/The-Brook-Financw-Ltd.png"
    },
    {
        "bankName": "The Millennium MFB",
        "bankCode": "090711",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/The_Millennium_MFB.png"
    },
    {
        "bankName": "Titan Trust Bank",
        "bankCode": "000025",
        "scCode": "102",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/titan_trust_bank.png"
    },
    {
        "bankName": "TOFA MFB",
        "bankCode": "090714",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/DEFAULT-BANK.PNG"
    },
    {
        "bankName": "Toprate Microfinance Bank",
        "bankCode": "090801",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/TopRate-MFB.png"
    },
    {
        "bankName": "Transpay MFB",
        "bankCode": "090708",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/TransPayMFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Treasures-MFB.png",
        "bankCode": "090663",
        "scCode": "000",
        "bankName": "Treasures MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/U-C-MFB.png",
        "bankCode": "090315",
        "scCode": "000",
        "bankName": "U And C MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "UBA MONI",
        "bankCode": "000040",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UBAMoni.png"
    },
    {
        "bankName": "UBJ MFB",
        "bankCode": "090762",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UBJ-MFB.png"
    },
    {
        "bankName": "UCEE MFB",
        "bankCode": "090706",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UCEEMFB.PNG"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090403",
        "scCode": "000",
        "bankName": "UDA MICROFINANCE BANK",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Uga MFB",
        "bankCode": "090782",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Ultimate MFB",
        "bankCode": "090776",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ultimate-MFB.png"
    },
    {
        "bankName": "Ultraviolet MFB",
        "bankCode": "090781",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Ultraviolet-MFB.png"
    },
    {
        "bankName": "UMUCHINEMERE PROCREDIT MFB",
        "bankCode": "090514",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UMUCHINEMERE-PROCREDIT-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090652",
        "scCode": "000",
        "bankName": "Umuchukwu Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Umunnachi MFB",
        "bankCode": "090510",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UMUNNACHI-MFB.png"
    },
    {
        "bankName": "Umunri MFB",
        "bankCode": "090808",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Umunri-MFB.png"
    },
    {
        "bankName": "Umuoji MFB",
        "bankCode": "090814",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "bankName": "Uniabuja MFB",
        "bankCode": "090778",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Uniabuja-MFB.png"
    },
    {
        "bankName": "Union Bank",
        "bankCode": "000018",
        "scCode": "032",
        "bankStatus": "active",
        "bankAvailability": "97%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/union.png"
    },
    {
        "bankName": "United Bank for Africa",
        "bankCode": "000004",
        "scCode": "033",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/uba.png"
    },
    {
        "bankName": "Unity Bank",
        "bankCode": "000011",
        "scCode": "215",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/unity_bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Umuchinemere-Procredit-MFB.png",
        "bankCode": "090338",
        "scCode": "000",
        "bankName": "Uniuyo MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Unlimit Nigeria Limited",
        "bankCode": "110081",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/unlimit_nigeria_limited_480.png"
    },
    {
        "bankName": "Unubi MFB",
        "bankCode": "090719",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Unubi_mfb.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090619",
        "scCode": "000",
        "bankName": "URE MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "UVUOMA MFB",
        "bankCode": "090765",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/UZONDU_MICROFINANCE_BANK.png",
        "bankCode": "090453",
        "scCode": "000",
        "bankName": "Uzondu Microfinance Bank",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Vale Finance",
        "bankCode": "050020",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "81%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Vale-Finance.png"
    },
    {
        "bankName": "VFD MFB",
        "bankCode": "090110",
        "scCode": "566",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/VFD_MFB.png"
    },
    {
        "bankName": "Vista Microfinance Bank",
        "bankCode": "090787",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Vista-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/VTNETWORKS.png",
        "bankCode": "100012",
        "scCode": "000",
        "bankName": "VTNETWORKS",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Wallet MFB",
        "bankCode": "090805",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Wallet-MFB.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Waya-MFB.png",
        "bankCode": "090590",
        "scCode": "000",
        "bankName": "Waya MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Wema Bank",
        "bankCode": "000017",
        "scCode": "035",
        "bankStatus": "active",
        "bankAvailability": "94%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/wema.png"
    },
    {
        "bankName": "Weston-Charis MFB",
        "bankCode": "090741",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Weston-Charis-MFB.png"
    },
    {
        "bankName": "Whitecrust Finance",
        "bankCode": "050035",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Default-Bank.png",
        "bankCode": "090253",
        "scCode": "000",
        "bankName": "Wudil MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Xpress Wallet",
        "bankCode": "100040",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Xpress-Wallet.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Yes-MFB.png",
        "bankCode": "090142",
        "scCode": "000",
        "bankName": "Yes MFB",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Zedvance Finance Limited",
        "bankCode": "050019",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Zedvance_MFB.png"
    },
    {
        "bankName": "Zefa MFB ",
        "bankCode": "090747",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Zefa-MFB.png"
    },
    {
        "bankName": "ZENITH BANK PLC",
        "bankCode": "000015",
        "scCode": "057",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/zenith.png"
    },
    {
        "bankName": "Zenith Eazy Wallet",
        "bankCode": "100034",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/zenith.png"
    },
    {
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Konga_Pay.png",
        "bankCode": "100025",
        "scCode": "000",
        "bankName": "Zinternet - KongaPay",
        "bankStatus": "active",
        "bankAvailability": "100%"
    },
    {
        "bankName": "Zitra MFB",
        "bankCode": "090718",
        "description": "",
        "scCode": "000",
        "bankStatus": "active",
        "bankAvailability": "100%",
        "imageUrl": "https://d38v990enafbk6.cloudfront.net/Zitra_MFB.png"
    }
]

output_folder = "downloaded_bank_logos"
os.makedirs(output_folder, exist_ok=True)

for item in image_data:
    image_url = item.get("imageUrl")
    bank_name = item.get("bankName", "unknown_bank").replace(" ", "_").replace("/", "_")

    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status() # Raise an exception for bad status codes

            # Extract file extension from the URL
            file_extension = os.path.splitext(image_url)[1]
            if not file_extension: # Fallback if no extension in URL
                file_extension = ".png" # Assume PNG based on your data

            # Create a unique filename
            filename = f"{bank_name}_{item.get('bankCode')}{file_extension}"
            filepath = os.path.join(output_folder, filename)

            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded: {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {image_url}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred for {image_url}: {e}")

print("Download process complete.")