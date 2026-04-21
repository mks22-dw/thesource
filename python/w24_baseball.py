yankees='''Player,Position,At Bats,Runs,Hits,2B,3B,HR,RBI
Austin Wells,C,401,51,88,22,1,21,71
Paul Goldschmidt,1B,489,76,134,31,1,10,45
Jazz Chisholm Jr.,2B,462,75,112,15,1,31,80
Anthony Volpe,SS,539,65,114,32,4,19,72
Ryan McMahon,3B,159,20,33,8,0,4,18
Jasson Domínguez,LF,381,58,98,18,1,10,47
Trent Grisham,CF,494,87,116,9,1,34,74
Aaron Judge,RF,541,137,179,30,2,53,114
Ben Rice,DH,467,74,119,28,4,26,65
Cody Bellinger,OF,588,89,160,25,5,29,98
Giancarlo Stanton,DH,249,36,68,8,0,24,66
Oswald Peraza,3B,158,18,24,5,0,3,13
DJ LeMahieu,2B,128,13,34,3,0,2,12
Oswaldo Cabrera,3B,107,17,26,4,0,1,11
J.C. Escarra,C,84,5,17,5,0,2,11'''


def make_player_list(player):
    player = player.split(',')
    #number stats start at 2
    i = 2
    while i < len(player):
        player[i] = int(player[i])
        i+= 1
    #calculate average
    #print(player)
    avg = player[4]/player[2]
    player.append(avg)
    return player


def parse_data(data):
    #print(data)
    #turn player data into lists
    parsed_data = []
    for row in data:
        row = make_player_list(row)
        #print(row)
        parsed_data.append(row)        
    return parsed_data

#data = parse_data(yankees)
#print(data)

def get_totals(data):
    totals = ['yankees', 'totals']
    totals+= [0] * 7
    for row in data:
        i = 2
        while i < len(row) - 1:
            totals[i]+= row[i]
            i+= 1
    avg = totals[4] / totals[2]
    totals.append(avg)
    return totals

# totals = get_totals(data)
# print(totals)

def make_table_data(data):
    html = ''
    for row in data:
        html+= '<tr>'
        for value in row[:-1]:
            html+= f'<td>{value}</td>'
        html+= f'<td>{row[-1]:0.3f}</td>'
        html+= '<tr>\n'
    return html
 
#print(make_table_data(data))

def make_table(data):
    data = data.split('\n')
    headers = data[0].split(',')
    headers.append('BA')
    #remove header row
    data = data[1:]
    #print(data)
    data = parse_data(data)
    #print(data)
    totals = get_totals(data)
    data.append(totals)
    html = '<table>\n<tr>'
    for header in headers:
        html+= f'<th>{header}</th>'
    html+= '</tr>\n'
    table_body = make_table_data(data)
    html+= table_body
    html+= '</table>'
    return html


yankee_table = make_table(yankees)
#print(yankee_table)

def make_page(content):
    content = f'<h1>The 2025 NY Yankees</h1>\n{content}\n'
    html = f'''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Yankees!</title>
  </head>
  <body>
    {content}
  </body>
</html>'''
    return html

print(make_page(yankee_table))

    