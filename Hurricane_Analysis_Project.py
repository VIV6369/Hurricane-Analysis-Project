# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1) Begin by looking at the damages list. The list contains strings representing the total cost in USD($) caused by 34 category 5 hurricanes (wind speeds ≥ 157 mph (252 km/h )) in the Atlantic region. For some of the hurricanes, damage data was not recorded ("Damages not recorded"), while the rest are written in the format "Prefix-B/M", where B stands for billions (1000000000) and M stands for millions (1000000).Write a function that returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as "Damages not recorded". Test your function with the data stored in damages

# write your update damages function here:

conversion = {"M": 1000000,
              "B": 1000000000}

updated_damages = []
while len(damages)> len (updated_damages):
    for i in damages:
        if i == "Damages not recorded":
            updated_damages.append(i)
            
        for letter in i:
            if letter == "M":
                num = float(i[0:-1])
                new_num = num * conversion["M"]
                updated_damages.append(new_num)
        for letter in i:
            if letter == "B":
                num = float(i[0:-1])
                new_num = num * conversion["B"]
                updated_damages.append(new_num)
    print(updated_damages)

# Second version   
def update_damages(lst):
    updated_damages = []
    for i in lst:
        for char in i:
            if char == "M":
                updated_damages.append(float(i.strip("M"))*conversion["M"])
            elif char == "B":
                updated_damages.append(float(i.strip("B"))*conversion["B"])
            
        if i == "Damages not recorded":
            updated_damages.append(i)
    print(updated_damages)

# 2) Write a function that constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.Thus the key "Cuba I" would have the value: {'Name': 'Cuba I', 'Month': 'October', 'Year': 1924, 'Max Sustained Wind': 165, 'Areas Affected': ['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 'Damage': 'Damages not recorded', 'Deaths': 90}. Test your function on the lists of data provided. 

# write your construct hurricanes dictionary function here:

table = zip(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)

hurricanes = {}
for names,months,years,winds,areas,damages,deaths in table:
  hurricanes.update({names: {"Name": names,
 "Month": months,
 "Year": years,
 "Max Sustained Wind": winds,
 "Areas Affected": areas,
 "Damage": damages,
 "Deaths": deaths}})

print(hurricanes)

# Second version
def make_a_dict(name_lst, months_lst, years_lst, max_winds_lst, areas_lst, deaths_lst):
  hurricanes_records = {}
  for a,b,c,d,e,f in zip(name_lst, months_lst, years_lst, max_winds_lst, areas_lst, deaths_lst):
    hurricanes_records.update({a:{"Name":a, "Month": b, "Year": c, "Max Sustained Wind": d, "Areas Affected": e, "Damage": f}})
  return hurricanes_records
    
print (make_a_dict(names,months,years,max_sustained_winds,areas_affected,deaths))

# 3) In addition to organizing the hurricanes in a dictionary with names as the key, you want to be able to organize the hurricanes by year. Write a function that converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year. For example, the key 1932 would yield the value: [{'Name': 'Bahamas', 'Month': 'September', 'Year': 1932, 'Max Sustained Wind': 160, 'Areas Affected': ['The Bahamas', 'Northeastern United States'], 'Damage': 'Damages not recorded', 'Deaths': 16}, {'Name': 'Cuba II', 'Month': 'November', 'Year': 1932, 'Max Sustained Wind': 175, 'Areas Affected': ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 'Damage': 40000000.0, 'Deaths': 3103}]. Test your function on your hurricanes dictionary.

# write your construct hurricane by year dictionary function here:

def hurricanes_by_year(hurricanes):
 hurricanes_by_year = {}
 for i in hurricanes:
   current_year = hurricanes[i]["Year"]
   current_cane = hurricanes[i]
   if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [current_cane]
   else:
       hurricanes_by_year[current_year].append(current_cane)
 return hurricanes_by_year

hurricanes_by_year = hurricanes_by_year(hurricanes)


print(hurricanes_by_year[1932])

# 4) You believe that knowing how often each of the areas of the Atlantic are affected by these strong hurricanes is important for making preparations for future hurricanes. Write a function that counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected. Test your function on your hurricanes dictionary.

# write your count affected areas function here:

def areasaffected(hurricanes):
  areas = {}
  for area in hurricanes:
    for current_area in hurricanes[area]["Areas Affected"]:
      if current_area not in areas:
        areas[current_area] = 1
      else:
        areas[current_area] += 1

  return areas
areas = areasaffected(hurricanes)
print(areas)

# Second version
def count_strikes(dic):
  areas = {}
  for key,value in dic.items():
    for area in value["Areas Affected"]:
      if area not in areas:
        areas[area] = 1
      else:
        areas[area] += 1
  return areas
areas = count_strikes(hurricanes) 
print(areas)  

# 5) Write a function that finds the area affected by the most hurricanes, and how often it was hit. Test your function on your affected area dictionary.
# write your find most affected area function here:

def mostaffected(areas):
  max_area = 'Central America'
  max_area_count = 0
  for i in areas:
    if max_area_count < areas[i]:
      max_area_count = areas[i]
      max_area = i
  return max_area, max_area_count
max_area, max_area_count = mostaffected(areas)
print(max_area, max_area_count)

# Second version
def most_often(dic):
  sorted_by_values = sorted(dic.values())
  if sorted_by_values[-1] > sorted_by_values[-2]:
    print ([k for k,v in dic.items() if v == sorted_by_values[-1]][0], sorted_by_values[-1])
    
  if sorted_by_values[-1] == sorted_by_values[-2]:
    print([k for k,v in dic.items() if v == sorted_by_values[-1]][0], sorted_by_values[-1])
    print([k for k,v in dic.items() if v == sorted_by_values[-2]][0], sorted_by_values[-2])
    
most_often(areas)

# 6) Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused. Test your function on your hurricanes dictionary.
# write your greatest number of deaths function here:

def deadliest(hurricanes):
  max_mortality_cane = 'Cuba I'
  max_mortality = 0
  for i in hurricanes:
    if max_mortality < hurricanes[i]["Deaths"]:
      max_mortality = hurricanes[i]["Deaths"]
      max_mortality_cane = hurricanes[i]["Name"]
  return max_mortality_cane, max_mortality
max_mortality_cane, max_mortality = deadliest(hurricanes)
print(max_mortality_cane, max_mortality)

# Second version
def deadliest(dic):
  deaths1 = []
  for key,value in dic.items():
    deaths1.append(value["Deaths"])
    deaths_sorted = sorted(deaths1)
  for key,value in dic.items():
    if value["Deaths"] == deaths_sorted[-1]:
      print(key, deaths_sorted[-1])
 
      
deadliest(hurricanes)

# 7) Just as hurricanes are rated by their windspeed, you want to try rating hurricanes based on other metrics. Write a function that rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating. 
#mortality_scale = {0: 0,
                    1: 100,
                    2: 500,
                    3: 1000,
#                   4: 10000}
#For example, a hurricane with a 1 mortality rating would have resulted in greater than 0 but less than or equal to 100 deaths. A hurricane with a 5 mortality rating would have resulted in greater than 10000 deaths. Store the hurricanes in a new dictionary where the keys are mortality ratings and the values are lists containing a dictionary for each hurricane that falls into that mortality rating. Test your function on your hurricanes dictionary.
# write your catgeorize by mortality function here:

def mort_scale(hurricanes):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in hurricanes:
    deaths = hurricanes[i]["Deaths"]
    if deaths == 0:
      hurricanes_by_mortality[0].append(hurricanes[i]["Name"])
    elif deaths > 0 and deaths <= 100:
      hurricanes_by_mortality[1].append(hurricanes[i]["Name"])
    elif deaths > 100 and deaths <=500:
      hurricanes_by_mortality[2].append(hurricanes[i]["Name"])
    elif deaths > 500 and deaths <=1000:
      hurricanes_by_mortality[3].append(hurricanes[i]["Name"])
    elif deaths > 1000 and deaths <=10000:
      hurricanes_by_mortality[4].append(hurricanes[i]["Name"])
    elif deaths > 10000:
      hurricanes_by_mortality[5].append(hurricanes[i]["Name"])
  return hurricanes_by_mortality
hurricanes_by_mortality = mort_scale(hurricanes)
print(hurricanes_by_mortality)

#Second Version
def mortality(dic):
  hurricanes_by_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in dic.items():
    if value["Deaths"] > 0 and value["Deaths"] <= 100:
      hurricanes_by_mortality[1].append(value)
    elif value["Deaths"] > 100 and value["Deaths"] <= 500:
      hurricanes_by_mortality[2].append(value)
    elif value["Deaths"] > 500 and value["Deaths"] <= 1000:
      hurricanes_by_mortality[3].append(value)
    elif value["Deaths"] > 1000 and value["Deaths"] <= 10000:
      hurricanes_by_mortality[4].append(value)
    elif value["Deaths"] > 10000:
      hurricanes_by_mortality[5].append(value)
    else:
      hurricanes_by_mortality[0].append(value)
  return hurricanes_by_mortality

mortality_class = mortality(hurricanes)
print(mortality_class)

# 8) Write a function that finds the hurricane that caused the greatest damage, and how costly it was. Test your function on your hurricanes dictionary.
# write your greatest damage function here:

def maxdamage(hurricanes):
  max_damage_cane = 'Cuba I'
  max_damage = 0
  for i in hurricanes:
    if hurricanes[i]["Damage"] == "Damages not recorded":
      continue
    if max_damage < hurricanes[i]["Damage"]:
      max_damage = hurricanes[i]["Damage"]
      max_damage_cane = hurricanes[i]["Name"]
    
  return max_damage_cane, max_damage
max_damage_cane, max_damage = maxdamage(hurricanes)
print(max_damage_cane, max_damage)

#Second version
def most_expensive(dic):
  damages1 = []
  for key, value in dic.items():
    if value["Damage"] != "Damages not recorded":
      damages1.append(value["Damage"])
    damages1_sorted = sorted(damages1)
  for key,value in dic.items():
    if value["Damage"] == damages1_sorted[-1]:
      print(key, damages1_sorted[-1])

most_expensive(hurricanes)

# 9) Lastly, you want to rate hurricanes according to how much damage they cause. Write a function that rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.
#damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
#               4: 50000000000}
#For example, a hurricane with a 1 damage rating would have resulted in damages greater than 0 USD but less than or equal to 100000000 USD. A hurricane with a 5 damage rating would have resulted in damages greater than 50000000000 USD (talk about a lot of money). Store the hurricanes in a new dictionary where the keys are damage ratings and the values are lists containing a dictionary for each hurricane that falls into that damage rating. Test your function on your hurricanes dictionary.
# write your catgeorize by damage function here:  
# categorize hurricanes in new dictionary with damage severity as key

def dam_scale(hurricanes):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in hurricanes:
    damage = hurricanes[i]["Damage"]
    if hurricanes[i]["Damage"] == "Damages not recorded":
      continue
    if damage == 0:
      hurricanes_by_damage[0].append(hurricanes[i]["Name"])
    elif damage > 0 and damage <= 100000000:
      hurricanes_by_damage[1].append(hurricanes[i]["Name"])
    elif damage > 100000000 and damage <=1000000000:
      hurricanes_by_damage[2].append(hurricanes[i]["Name"])
    elif damage > 1000000000 and damage <=10000000000:
      hurricanes_by_damage[3].append(hurricanes[i]["Name"])
    elif damage > 10000000000 and damage <=50000000000:
      hurricanes_by_damage[4].append(hurricanes[i]["Name"])
    elif damage > 50000000000:
      hurricanes_by_damage[5].append(hurricanes[i]["Name"])
  return hurricanes_by_damage
hurricanes_by_damage = dam_scale(hurricanes)
print(hurricanes_by_damage)

#Second Version
def cost_class(dic):
  hurricanes_by_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for key, value in dic.items():
    if value["Damage"] == "Damages not recorded":
      continue
    elif value["Damage"] > 0 and value["Damage"] <= 100000000:
      hurricanes_by_damage[1].append(value)
    elif value["Damage"] > 100000000 and value["Damage"] <= 1000000000:
      hurricanes_by_damage[2].append(value)
    elif value["Damage"] > 1000000000 and value["Damage"] <= 10000000000:
      hurricanes_by_damage[3].append(value)
    elif value["Damage"] > 10000000000 and value["Damage"] <= 50000000000:
      hurricanes_by_damage[4].append(value)
    elif value["Damage"] > 50000000000:
      hurricanes_by_damage[5].append(value)
    else:
      hurricanes_by_damage[0].append(value)
  return hurricanes_by_damage

damage_class = cost_class(hurricanes)
print(damage_class[5])
