'''
    datasource.py
    Tresa Xavier, Calypso Leonard, Yingying Wang Feb, 6, 2018
    Methods to access our boardgames database.
'''

import psycopg2
import getpass
import random

# Get the database login info. 
database = 'xaviert'
user = 'xaviert'
password = getpass.getpass()


# Login to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print('Connection error: ', e)
    exit()

class DataSource:

    # Constructor names may seem gratuitous with inputAge, inputTime and inputCategory 
    # but actually provide helpful context
    # given that age time and category are all terms within our data set 
    # (ex: max_time, min_time, min_age, max_age etc 
    # - felt it was necessary to specify when referring to the users input term 
    
    #Calls for only one criteria
    def __init__(self, numPlayers, inputAge, inputCategory, inputTime):
        self.numPlayer = str(numPlayers)
        self.inputAge = str(inputAge)
        self.inputCategory = inputCategory
        self.inputTime = str(inputTime)
        
    # Just Players
    def getGamesByNumPlayers(self):
        #numPlayers = str(numPlayers)
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer \
        FROM boardgames WHERE max_players >=' + self.numPlayers + 'AND min_players <= ' \
        + self.numPlayers + 'ORDER BY rank ASC LIMIT 10'
        return query
    #Just Age
    def getGamesByMinAge(self):
        #inputAge = str(inputAge) 
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE min_age <=' + self.inputAge + 'ORDER BY rank ASC'
        return query
    #Just Category
    def getGamesByCategory(self):
        query = "SELECT game_name, avg_time, rank, mechanic, min_age, designer FROM boardgames \
        WHERE mechanic LIKE '%" + self.inputCategory + "%' ORDER BY rank ASC"
        return query
    #Just Time
    def getGamesByMaxTime(self):
        inputTime = str(inputTime)
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_time >= ' + self.inputTime + 'AND min_time <= ' + self.inputTime +\
        'ORDER BY rank ASC'
        return query
    
    #Calls for combinations of two criteria
        
    #Players and Age
    def getGamesByPlayersAndAge(self):
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=' + self.numPlayers + 'AND min_players <= ' + self.numPlayers + \
        ' AND min_age <=' + self.inputAge + 'ORDER BY rank ASC LIMIT 10'
        return query
    #Players and Time
    def getGamesByPlayersAndTime(self):
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=' + self.numPlayers + 'AND min_players <= ' + self.numPlayers + \
        ' AND max_time >= ' + self.inputTime + 'AND min_time <= ' + str(inputTime) + \
        'ORDER BY rank ASC LIMIT 10'
        return query
    #Players and Category
    def getGamesByPlayersAndCategory(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=" + self.numPlayers + "AND min_players <= " + \
        self.numPlayers + " AND mechanic LIKE '%" + self.inputCategory + \
        "%' ORDER BY rank ASC LIMIT 10"
        return query
    #Category and Time
    def getGamesByCategoryAndTime(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE mechanic LIKE '%" + self.inputCategory + "%' AND  max_time >= " + self.inputTime + \
        "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
    # Age and Time
    def getGamesByAgeAndTime(self):
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE min_age <=' + self.inputAge + 'AND max_time >= ' + self.inputTime + \
        'AND min_time <= ' +self.inputTime + 'ORDER BY rank ASC LIMIT 10'
        return query     
    #Age and Category
    def getGamesByAgeAndCategory(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE min_age <=" + self.inputAge + " AND mechanic LIKE '%" + \
        self.inputCategory + "%' ORDER BY rank ASC LIMIT 10"
        return query
        
     #Calls for combinations of three criteria
    
    #Players, Age, and Category
    def getGamesByPlayersAgeAndCategory(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=" + self.numPlayers + "AND min_players <= " + self.numPlayers +\
        "AND min_age <=" + self.inputAge + " AND mechanic LIKE '%" + self.inputCategory +\
        "%' ORDER BY rank ASC LIMIT 10"
        return query
        
    #Players, Age, and Time
    def getGamesByPlayersAgeAndTime(self):
        numPlayers = str(numPlayers)
        inputAge = str(inputAge)
        inputTime = str(inputTime)
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=" + self.numPlayers + "AND min_players <= " + self.numPlayers +\
        "AND min_age <=" + self.inputAge + " AND max_time >= " + self.inputTime + \
        "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query
        
    #Players, Category, and Time
    def getGamesByPlayersCategoryAndTime(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=" + self.numPlayers + "AND min_players <= " + self.numPlayers + \
        " AND mechanic LIKE '%" + self.inputCategory + "%' AND  max_time >= " + self.inputTime +\
        "AND min_time <= " + self.inputTime + "ORDER BY rank ASC LIMIT 10"
        return query    
        
    #Age, Category, and Time
    def getGamesByAgeCategoryAndTime(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE min_age <=" + self.inputAge + " AND mechanic LIKE '%" + self.inputCategory + \
        "%' AND  max_time >= " + self.inputTime + "AND min_time <= " + self.inputTime + \
        "ORDER BY rank ASC LIMIT 10"
        return query
    

        
    #Call for a query using all criteria
    def getGamesByAll(self):
        query = "SELECT game_name, avg_time, rank, category, min_age, designer FROM boardgames \
        WHERE max_players >=" + numPlayers + "AND min_players <= " + numPlayers +\
        "AND min_age <=" + inputAge + " AND mechanic LIKE '%" + inputCategory +\
        "%' AND  max_time >= " + inputTime + "AND min_time <= " + inputTime +\
        "ORDER BY rank ASC LIMIT 10"
        return query
    
    #This method collects data for the random game button, selecting a random game 
    #from the top 100 ranked games by 
    #choosing a random integer and displaying information for that rank.
    
    def getRandomGame(self):
        ranNumber = random.randint(1,101)
        query = 'SELECT game_name, avg_time, rank, category, min_age, designer \
        FROM boardgames WHERE rank =' + str(ranNumber)
        return query
        

def main():
    try:
        cursor = connection.cursor()
        gameSearch = DataSource(5,20,"puzzles",70)
        query = gameSearch.getGamesByAgeCategoryAndTime() 
        #Dummy criteria, these inputs will fail
        cursor.execute(query)
        
        # Helps code fail gracefully
        if (cursor.rowcount == 0):
            print("No games found")
            connection.close()
            exit()
            
            
        for row in cursor.fetchall():
            print(row)


    except Exception as e:
        print('Cursor error', e)
        connection.close()
        exit()

    connection.close()
    
    
if __name__ == "__main__":
    main()