def make_link(url, anchor):
    return f'<a href="{url}">{anchor}</a>'
print('make_link:')
print(make_link('http://xkcd.com', 'xkcd'))

def html_list(g):
    html = '<ul>\n'
    for item in g:
        html+= f'<li>{item}</li>\n'
    html+= '</ul>'
    return html

print('\nhtml_list:')
print(html_list(['cat', 'dog', 21]))

def link_list(links, anchors):
    anchor_tags = []
    i = 0
    while i < len(links):
        tag = make_link(links[i], anchors[i])
        anchor_tags.append(tag)
        i+= 1
    return html_list(anchor_tags)

print('\nlink_lists:')
us = ['https://www.stuycs.org/fcs01-dw/', 'https://github.com/mks22-dw/thesource', 'http://xkcd.com']
ts = ['class site', 'source code', 'fun']
print(link_list(us, ts))

def make_table(data):
    html= '<table>\n'
    for row in data:
        html+= '<tr>'
        for value in row:
            html+= f'<td>{value}</td>'
        html+= '</tr>\n'
    html+= '</table>'
    return html

d = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
print('\nmake_table:')
print(make_table(d))