import constant
import socket

host = ''
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
try:
    #fp = open('/home/jnoor/Downloads/dubai.mp4', 'r')
    fp = open('input_test.txt', 'r')
except:
    print 'not successfully open'

#obj_input = request.environ['wsgi.input']
# st = ''
# timeout_reader = constant._make_timeout_reader(fp)
# try:
#     for chunk in iter(timeout_reader, ''):
#         # start_time = time.time()
#         # if start_time > upload_expiration:
#         #     self.logger.increment('PUT.timeouts')
#         #     return HTTPRequestTimeout(request=request)
#         # etag.update(chunk)
#         print type(chunk), chunk
#         st = st+chunk
# except:
#     print 'exception in read iter'
# print st

s.sendall(fp.read())
s.close()