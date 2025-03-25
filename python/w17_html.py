def make_link(url, anchor):
    link = '<a href="'
    link+= url
    link+= '">'
    link+= anchor
    link+= '</a>'
    return link
print(make_link('http://xkcd.com', 'xkcd'))

def html_list(g):
    list = '<ul>\n'
    for item in g:
        list+= '<li>'
        list+= str(item)
        list+= '</li>\n'
    list+= '</ul>'
    return list
print(html_list(['cat', 'dog', 47]))

def link_list(links, anchors):
    list = '<ul>\n'
    i = 0
    while i < len(links):
        list+= '<li>'
        list+= make_link(links[i], anchors[i])
        list+= '</li>\n'
        i+= 1
    list+= '</ul>'
    return list
us = ['https://www.stuycs.org/fcs00-dw/', 'https://github.com/mks22-dw/thesource', 'https://www.stuycs.org/dwlessons/fcs/selector.html']
ts = ['class site', 'source code', 'slides']
print(link_list(us, ts))
