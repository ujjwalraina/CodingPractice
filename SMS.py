from twilio.rest import Client
accountSID = 'AC5ed12629f0952973d7d80f06e18b77ff'
authToken = 'a3f1d7bc46376921f7afa6abb128f60d'
twilioCli = Client(accountSID,authToken)
myCellPhone = '+12563054104'
sendNumber = '+917696230555'
message = twilioCli.messages.create(body="SMS done through python",from_=myCellPhone,to=sendNumber)