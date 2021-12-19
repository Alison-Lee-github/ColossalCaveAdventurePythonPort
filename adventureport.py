
def parse_data(start_line): # need start and end points of tables 
    number_of_ends=0 #counts number of -1s in program
    data=[]
    flitered_data=[]
    adv=open('adventuregame.txt')
    for line in adv:
        if(line.isspace()==False): #want to keep whitespace messes up code if you take it away
            
            stripped_line=line.strip()
            content=stripped_line.split()
            
        else:
            content=line
            print(True) #Three white spaces in description 
        data.append(content)
        
        
    adv.close()
    #print(len(data))#733
    #print(data[0][0])#2d array
    index=start_line

    end_found=False
    while(end_found==False):
        current_line=data[index]
        line_length=len(current_line)
        if(line_length>0):
            if(data[index][0].find("-1")!=-1):
                end_found=True 
        flitered_data.append(data[index])
        #print(data[index])
        index=index+1
        
    return flitered_data
                
def get_descriptions():
    descriptions=parse_data(0)#first table is descriptions
    #good
    return descriptions
    
def get_short_room_labels():
    labels=parse_data(153) #good, 153 instead of 154, one less than actual line value 
    return labels
def get_map_data():
    game_map=parse_data(182) #good, must use 182 instead of 183
    return game_map
def get_keywords():
    keywords=parse_data(379)#good, must use 379 instead of 380
    return keywords
def get_game_states():
    game_states=parse_data(575)#good
    return game_states
def get_hints_and_events():
    hints=parse_data(600) #good 
    return hints       
def parse_map(maps): # need to add other condition 
    map_array=[] #stores dictionarys
    map_dictionary={}
    synonym_array=[]#stores synonyms
    #main_index=0
    for m in maps:#create dictionary for each line
        #print(m) #prints data right
        new_map_dictionary=map_dictionary.copy() #copy empty dictionary to create a new dictionary each time 
        line_length=len(m)
        character_index=0 #gets index of subarray
        new_synonym_array=synonym_array.copy() #Creates new array object
        if(line_length>1):# no single character lines
            for character in m:
                if(character_index==0):
                    new_map_dictionary['current_room']=character
                elif(character_index==1):
                    new_map_dictionary['end_room']=character #not always the end room, could also be data with that value. data with that value and room are same
                elif(character_index>1):
                    new_synonym_array.append(character)
                    new_map_dictionary['synonyms']=new_synonym_array
                character_index=character_index+1
            #main_index=main_index+1
                #print(line_index) Does indeed go above index=1
        map_array.append(new_map_dictionary) #not getting synonyms
    #print(map_array)
    return map_array
def parse_room_number(room_number,map_array):
    room_array=[] #gets only the entries in a specific room: the current_room is always the same
    # end_room is the destination and the synonyms 
    for m in map_array:
        line_length=len(m)
        if(line_length>1):
            #print(m['current_room'])
            current_room_value=int(m['current_room'])
            if(current_room_value==room_number):
                room_array.append(m)
    #print(room_array) 
    
    return room_array
def valid_keyword(room_array): # check valid keywords 
    valid_keywords=[]
    for entry in room_array:
        #print(entry)
        valid_keywords.append(entry['synonyms'])
    #print(valid_keywords)
    return valid_keywords
            
def get_keyword_value(keyword,keyword_array):
    for key in keyword_array:
        key_length=len(key)
        if((key_length)>1): #needs at least two entries, a key and a value. Order: Value, Keyword
            if(key[1].upper()==keyword.upper()):
                return int(key[0])
    return False
def keyword_match(keyword_value,valid_keywords):
    valid_keyword_index=0; 
    for entries in valid_keywords:
        for synonym_value in entries:
            #print(synonym_value)
            if(int(synonym_value)==keyword_value):
                print(entries)
                return valid_keyword_index #see which statement to update game state
        print(entries)
        valid_keyword_index=valid_keyword_index+1 
    return False
                
#def parse_descriptions(description_array): # get dictionary values and read it 
 #   description_value_array=[]
  #  for d in description_array:
   #     data_length=len(d)
    #    if(len(d)>1):
     #       description_value_array.append(d[0])
            #print(d[0])
        #print(d)
    return description_value_array   
def read_description(description_array,value): #read description based on value
    index=0
    description_string=""
    for d in description_array:
       data_length=len(d)
       for word in d:
           if(len(d)>1):
                if(int(d[0])==value and word!=d[0]):
                    description_string=description_string+" "+word+" "
                    #print(word) # print description if the value matches and do not print the description's number
       #index=index+1
    print(description_string)

def set_intial_object_locations():
    object_location_array=[0]*79 # 79 rooms, really 68, but make 79 anyway
    room_3=[1001,1002,1020] #key,lamp, bottle of water
    object_location_array[2]=room_3
    
    room_8=[1003] #grate not takeable
    object_location_array[7]=room_8
    
    room_10=[1004] #cage
    object_location_array[9]=room_10
    
    room_13=[1007] #bird cannot capture without rod
    object_location[12]=room_13
    
    room_27=[1013] #diamonds
    object_location[26]=room_27
    
    room_18=[1010] # gold in gold room
    object_location[17]=room_18
    
    room_39=[1015] # jewels in south side chamber
    object_location[38]=room_39
    
        
#parse_room_number(2,parse_map(parse_data(182)))
game_map=get_map_data() # intializing game state
descriptions=get_descriptions()
#print(descriptions)
all_keywords=get_keywords()
current_room_number=1
destination=current_room_number
read_description(descriptions,destination)
#print(all_keywords)


current_room_data=parse_room_number(current_room_number,parse_map(game_map))

room_keywords=valid_keyword(current_room_data)

playing=True  


while(playing):
    
    user_input=input("Enter a choice: ")
    current_input=get_keyword_value(user_input,all_keywords)
    room_data_index=keyword_match(current_input,room_keywords) # use this index for current room data index
    #print(room_data_index)
    if(room_data_index!=False): #the keyword is valid
        print(current_room_data)
        #print("Room data Index ", room_data_index)
        destination=int(current_room_data[room_data_index]['end_room']) #getting two
        current_room_number=destination
        current_room_data=parse_room_number(current_room_number,parse_map(game_map))
    
    read_description(descriptions,destination)
    #2 norths is getting an index of 3 when there are only 3 entries in array
    #room number 300 is the issue
    #NORTH=45
#parse_data(379)           
#print(get_keyword_value("ROAD",parse_data(379))) #getting 2 which is correct

#print(keyword_match(current_input,room_keywords)) #returns 0 for road in room 1

#read_description(descriptions,current_input) # works prints all 2 values for road 
