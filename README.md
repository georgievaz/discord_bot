# discord_bot

Discord chatbot that sends random dog pictures from [Dog API](https://dog.ceo/dog-api/) \
The chatbot is hosted on https://repl.it/~ and kept automatically alive by https://uptimerobot.com/

## Set up 
To create the chatbot add a [new application] https://discord.com/developers/applications \
Give it a bot scope in the oAuth2 settings \
Approve all Text permissions + View Channels \ 
To add the bot to your server go to the scopes URL \ 
From the Bot settings copy the Bot token and save it as '.env' in the code folder 

## Commands 
$breed {{name of breed}} - use this to see a picture of a specific breed \
$del {{name of breed}} - use this to delete a breed from list of favourite breeds \
$dog - use this to see a random picture of a dog \
$fav - use this to see all your favourite breeeds \
$help - use this to see a list of all commands \
$hi - use this to see if I am online \
$more - use this to see another picture of the last breed you saw \
$new {{name of breed}} - use this to add a specific breed to list of favourite breeds \
