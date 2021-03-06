def app(environ, start_response):
    status = '200 OK'
    headers = [ 
      ('Content-Type', 'text/plain') 
    ]
    body = ''
    for line in environ["QUERY_STRING"].split("&"):
        body += line + '\n'
    start_response(status, headers)
    return [bytes(body, encoding = 'utf8')]
