video_games = ['PS1', 'PS2', 'PS3', 'PS4', 'PS5', 'XBOX1', 'XBOX2', 'XBOX3', 'XBOX4', 'XBOX5']

for consoles in video_games:
  print(consoles)

print(video_games)
print(video_games[5])

video_games[5] = 'XBOX360'
video_games.append('XBOX ONE')
video_games.extend(['Mega Drive', 'Mega Drive 2', 'Mega Drive 3'])
video_games.insert(1, 'PS6')
print(video_games)
video_games.remove(video_games[5])
print(video_games)
print(len(video_games))

num_of_consoles = len(video_games)
print(video_games[num_of_consoles - 1]) #tirar o erro de index out of range
     