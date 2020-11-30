import pandas as pd
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')

df = pd.read_csv('cleaned_responses.csv', encoding = "ISO-8859-1")

#create new dataframe that contains name and what you would like to give

df = df.rename(columns = {"Name / Online Name": "name", 
"Social Media Handle(s) to be contacted with (please say what social media it is ex @/abc on twitter) and/or email": "socials",
"What would you like to give":"give",
"What would you like to receive":"receive",
"List a few of your favourite pairings, characters, etc":"favs",
"Something you would like to see your pairing/ character do (fantasy au, coffee shop, general holiday shenanigans, if you cant think of anything i will provide some possibilities in the next question)":"what_you_want",
"Possibilities (select as many as u want) (I came up with these off the top of my head please dont come for me)":"poss_want",
"NOTP / Character you super cannot get into (optional), use this spot if there a twitter user u ABSOLUTELY BEEF WITH that you dont want to get a gift from/for, i wont tell anyone promise.  ":"no",
"If someone drops out would u be willing to do 2 things (plz dont drop out)":"will_you_do_2"
})
give_fics = df.loc[df["give"] == "Fic", "name"]
give_art = df.loc[df["give"] == "Art", "name"]
give_poetry = df.loc[df["give"] == "Poetry", "name"]
give_either = df.loc[df["give"] == "Art or Fic", "name"]

possible = ['Person A and Person B get their coffees switched',
'Playing Video Games Together',
'Fantasy/Magic',
'Tattoo Parlour',
'Cat cafe',
'Harry Potter AU',
'Carnival/Fair/Festival',
'Cooking together (domestic vibes)',
'Accidental Jacket Exchange',
'Adopting a pet together',
'Stolen pizza delivery']

temp = df.loc[df["poss_want"].notnull()]

coffee = temp.loc[temp["poss_want"].str.contains(possible[0]), "name"]
vid_games = temp.loc[temp["poss_want"].str.contains(possible[1]), "name"]
fantasy = temp.loc[temp["poss_want"].str.contains(possible[2]), "name"]
tattoo = temp.loc[temp["poss_want"].str.contains(possible[3]), "name"]
catcafe = temp.loc[temp["poss_want"].str.contains(possible[4]), "name"]
hpau = temp.loc[temp["poss_want"].str.contains(possible[5]), "name"]
carnival = temp.loc[temp["poss_want"].str.contains(possible[6]), "name"]
cooking = temp.loc[temp["poss_want"].str.contains(possible[7]), "name"]
jacket = temp.loc[temp["poss_want"].str.contains(possible[8]), "name"]
pet = temp.loc[temp["poss_want"].str.contains(possible[9]), "name"]
pizza = temp.loc[temp["poss_want"].str.contains(possible[10]), "name"]

#what do people want
want_fic = df.loc[df["receive"] == "Fic", "name"]
want_art = df.loc[df["receive"] == "Art", "name"]
doesnt_care = df.loc[df["receive"] == "No preference", "name"]

#empty frequency dictionary 
freqs = {}

#count frequencies
for index, row in df.iterrows():
    ships = row['favs'].split(",")
    for item in ships:
        if item not in freqs:
            freqs[item] = 1
        else:
            freqs[item] = freqs[item] +1

freqs = sorted(freqs.items(), key=lambda x: x[1],reverse=True)

freqs = pd.DataFrame.from_dict(freqs)
freqs = freqs.rename(columns= {'0':'ship','1':'count'})
print(freqs)
# print(pd.DataFrame.from_dict(dict([('A', [1, 2, 3]), ('B', [4, 5, 6])])))
results = {}

for i  in range(0,10):
    ship = temp.loc[temp["favs"].str.contains(freqs[0][i]), "name"]
    # print(freqs[0][i])
    # for j in range(len(ship)):
        # print(ship.iat[j])
    results[freqs[0][i]] = ship

results_df = pd.DataFrame.from_dict(results)
results_df.to_csv('topships_results.csv',index=False)

results = {}
temp_results = {}
temp = df.loc[df["name"].notnull()]

for index , row in temp.iterrows():
    user = row["name"]
    favs = row['favs']
    favs = favs.split(',')
    results[user] = favs

results_df = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in results.items() ]))

results_df.to_csv('per_user_results.csv',index=False)
# print(results_df)
