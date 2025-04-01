yankees='''Player,Position,At Bats,Runs,Hits,2B,3B,HR,RBI
Austin Wells,C,354,42,81,18,1,13,55
Anthony Rizzo,1B,337,38,77,12,0,8,35
Gleyber Torres,2B,587,80,151,26,0,15,63
Anthony Volpe,SS,637,90,155,27,7,12,60
Oswaldo Cabrera,3B,299,47,74,11,0,8,36
Alex Verdugo,LF,559,74,130,28,1,13,61
Aaron Judge,CF,559,122,180,36,1,58,144
Juan Soto,RF,576,128,166,31,4,41,109
Giancarlo Stanton,DH,417,49,97,20,0,27,72
Jose Trevino,C,209,26,45,5,0,8,28
DJ LeMahieu,CI,201,19,41,5,0,2,26
Trent Grisham,CF,179,21,34,8,0,9,31
Jazz Chisholm Jr.,3B,176,28,48,7,0,11,23
Ben Rice,1B,152,20,26,6,0,7,23
Jon Berti,3B,66,10,18,0,0,1,6
Jasson Domínguez,OF,56,8,10,1,0,2,4
Jahmai Jones,UT,42,8,10,1,1,1,4
J.D. Davis,1B,19,1,2,1,0,0,1
Carlos Narváez,C,13,0,3,0,0,0,0
Oswald Peraza,3B,10,2,2,0,0,1,1
Taylor Trammell,OF,1,2,1,0,0,0,0
Duke Ellis,LF,1,0,1,0,0,0,0'''

yankees = yankees.split('\n')
header = yankees[0]
yankees = yankees[1:]
totals = ['Totals', '-'] + [0]*7

def extract_data(l):
    data = []
    for row in l:
        data.append(extract_data_row(row))
    return data

def extract_data_row(row):
    data = row.split(',')
    num_data = data[2:]
    num_data = list(map(int, num_data))
    data[2:] = num_data
    return data

def analyze_data(data, totals):
    for player in data:
        i = 2
        while i < len(player):
            totals[i]+= player[i]
            i+= 1
        avg = player[4]/player[2]
        player.append(avg)
    total_avg = totals[4]/totals[2]
    totals.append(total_avg)
    data.append(totals)

data = extract_data(yankees)
print(data)
# analyze_data(data, totals)
# print(data)
# print(totals)

def make_html_table_header(s):
    html = '<thead><tr>'
    head = s.split(',')
    for column in head:
        html+= '<th>' + column + '</th>'
    html+= '<th>Average</th>'
    html+= '</tr><thead>\n'
    return html

def make_html_table_body(data):
    html = '<tbody>'
    for row in data:
        html+= '<tr>'
        for value in row:
            html+= '<td>' + str(value) + '</td>'
        html+= '</tr>\n'
    html+= '</tbody>'
    return html


html = '<table>'
html+= make_html_table_header(header)
html+= make_html_table_body(data)
html+= '</table>'

# print(html)
