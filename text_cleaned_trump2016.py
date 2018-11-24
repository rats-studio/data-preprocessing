import re

# using regex expressions to clean the text
# want to remove hashhtags and web addresses

text = "#ThankYouTour2016 \n\nTue: West Allis, WI. \n\nThur: Hershey, PA. \n\nFri: Orlando, FL. \n\nSat: Mobile, AL. \n\nTickets:\u2026 https://t.co/OJ8S7iVzFx"
#text = re.sub(r'http\S+', "", text)
pattern2 = r'RT @\S+'
pattern3 = r'@'
pattern4 = r'\s'
pattern5 = r'#'

complete_pattern = r'@|#|\s|(http\S+)|(RT @\S+)'
#text = re.sub(pattern2, "", text)
#text = re.sub(pattern3, "", text)
#text = re.sub(pattern4, " ", text)
text = re.sub(complete_pattern, " ", text)
print(text)

text2 = "Mobile, Alabama today at 3:00 P.M. Last rally of the year - \"THANK YOU ALABAMA AND THE SOUTH\" Biggest of all crowds expected, see you there!"
text2 = re.sub(complete_pattern, " ", text2)
print(text2)