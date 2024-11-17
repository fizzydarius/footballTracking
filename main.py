import requests
import json
import secret








class Program:
    def __init__(self):
        self.f = open('playerCodes.json')
        self.data = json.load(self.f)
        self.apiKey = secret.key
        self.getWeekAndSchedule()


    def getWeekAndSchedule(self):
        response = requests.get(f'https://api.sportsdata.io/v3/nfl/scores/json/Timeframes/current?key={self.apiKey}')
        week = response.json()
        self.currentWeek = week[0]['Week']
        urlSchedule = f'https://api.sportsdata.io/v3/nfl/scores/json/ScoresBasicFinal/2024/{self.currentWeek}?key={self.apiKey}'
        response = requests.get(urlSchedule)
        self.schedule = response.json()

        for i in range(len(self.schedule)):
            if not self.schedule[i]['IsClosed']:
                print(f"[{i}] {self.schedule[i]['HomeTeam']} v {self.schedule[i]['AwayTeam']}")

    def gameChoice(self):
        gameChosen = int(input("What game are we betting on ?:  "))
        self.homeTeam = self.schedule[gameChosen]['HomeTeam']
        self.awayTeam = self.schedule[gameChosen]['AwayTeam']

    def displayPlayers(self, homeTeam, awayTeam):
        print(homeTeam,awayTeam)
        for i in range(len(self.data[homeTeam]['name'])):
            print(self.data[homeTeam]['name'][i])
        for i in range(len(self.data[awayTeam]['name'])):
            print(self.data[awayTeam]['name'][i])

    def main(self):
        self.gameChoice()
        self.displayPlayers(self.homeTeam, self.awayTeam)

code = Program()
code.main()
code.f.close()
