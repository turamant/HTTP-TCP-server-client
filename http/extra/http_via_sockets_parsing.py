import socket


def parse_http_response(text_response):
    lines = text_response.split('\n')
    status_raw, lines = lines[0], lines[1:]
    protocol, status, message = status_raw.split(' ')
    empty_index = 1
    headers = {}
    for index, line in enumerate(lines):
        line = line.strip()
        line = line.strip('\r')
        if line == '':
            empty_index = index
            break
        print(line)
        k, _, v = line.partition(':')
        headers.setdefault(k.strip(), v.strip())
    content = ''.join(lines[empty_index + 1:])
    return int(status), headers, content

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('exemple.com', 80))
content_items = [
    'GET /HTTP/1.1',
    'Host: exemple.com',
    'Connection: keep-alive',
    'Accept: text/html',
    '\n'
]
content = '\n'.join(content_items)
print('--- HTTP MESSAGE ---')
print(content)
print('--- END OF MESSAGE ---')
sock.send(content.encode())
result = sock.recv(10024)
status, headers, content = parse_http_response(result.decode())
print('Status Code:{}'.format(status))
print('Headers : {}'.format(headers))
print('Content: {}'.format(content))
