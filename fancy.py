import pandas as pd
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')

df = pd.read_csv('responses.csv', encoding = "ISO-8859-1")

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

names = df['name'].tolist()
temp_fav = df['favs'].tolist()
temp_favs = {}
for i in range(0, len(names)):
    fav = temp_fav[i].lower()
    i_favs = fav.split(',')
    temp_favs[names[i]] = i_favs

sim = {};
for i in temp_favs:
    sim_index = 0
    for j in temp_favs[i]:
        for k in temp_favs:
            print(j)
            print(temp_favs[k])
            if j in temp_favs[k]:
                sim_index += 1
        sim[i] = {k: sim_index}

print(sim)