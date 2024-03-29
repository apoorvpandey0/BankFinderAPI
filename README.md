# BankFinderAPI
Live version : https://bankfinderapi.herokuapp.com/
This is an RESTful API for finding banks using their IFSC code or any properties such as Name,Branch,State,Bank_id and City
you can visit the Admin Panel at https://bankfinderapi.herokuapp.com/admin and use "admin" as both username and password to gain access.

## REST API examples
### Get bank by IFSC code or any other property 
1. https://bankfinderapi.herokuapp.com/?ifsc=ABHY0065001
2. https://bankfinderapi.herokuapp.com/?state=ASSAM
3. https://bankfinderapi.herokuapp.com/?city=BHOPAL
4. https://bankfinderapi.herokuapp.com/?bank_id=10
### Get banks using search
1. https://bankfinderapi.herokuapp.com/?search=Allahabad
2. https://bankfinderapi.herokuapp.com/?search=tikamgarh
###  Get banks in a particular ordering
1. https://bankfinderapi.herokuapp.com/?ordering=bank_id
2. https://bankfinderapi.herokuapp.com/?ordering=state
### Get banks using combination of properties
1. https://bankfinderapi.herokuapp.com/?search=Allahabad&ordering=state
2. https://bankfinderapi.herokuapp.com/?search=Tikamgarh&ordering=bank_id
### Some other points
1. You can use the "filters" option on the api page to browse the API.
2. To get the data in JSON format use the "GET" button and then select JSON.
3. This is a development build and by no means is to be used as it is in a production environment. 

## Graphql demo @ /graphql
```
query{
  allBanks {
    bankName
  }
}
```
