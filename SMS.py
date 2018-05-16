from twilio.rest import Client
accountSID = '**************************'
authToken = '******************************'
twilioCli = Client(accountSID,authToken)
myCellPhone = '+**********'
sendNumber = '+91**********'
message = twilioCli.messages.create(body="SMS done through python",from_=myCellPhone,to=sendNumber)
