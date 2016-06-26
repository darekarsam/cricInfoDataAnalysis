from getBattingStats import getBattingStats
from getMatchStats import getMatchStats

def main():
  print "\n Getting Stats for Every batsmen inning by inning"
  battingStatDF=getBattingStats()
  
  print "\n Getting Match Statistics"
  matchStatdf=getMatchStats()

if __name__ == "__main__":
  main()