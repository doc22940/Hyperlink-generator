import os
#generator contants
htmlstart = """
<!DOCTYPE html>
<html>
<head>
<title>HyperLink generator by TheChoyon</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body class="jumbotron">
<center>
<div class="font-weight-bold h1">HyperLink Generator by <a href="https://github.com/TheChoyon">TheChoyon</a><br><br></div>
"""
htmlend = """
</center>
</body>
</html>
"""

#constructions of hyper links
def construct():
    global htmlstart
    global htmlend
    file_name = open(raw_input('URL list file name: '), 'r').read().split('\n')
    core = "<table class=\"table table-striped\"><thead><tr><th>HyperLinks</th></tr></thead><tbody>"
    counts = 1
    for url in file_name:
        url = url.strip()
        if url == "":
            continue
        if not url.startswith('http'):
            url = 'http://' + url
        core += "<tr><th><b>["+str(counts)+"]</b> <a href=\"" + url + "\" target=\"_blank\">" + url + "</a></th></tr>"
        counts += 1
    core += "</tbody></table>"
    open('generated.html', 'w').write(htmlstart + core + htmlend)
    print 'Success! Opening generated.html automatically ...'
    os.startfile('generated.html')


#execution
construct()
    
