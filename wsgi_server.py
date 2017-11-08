from wsgiref.simple_server import make_server
import constant, time
import os
import cStringIO


def application(env, start_response):
    path = env.get('PATH_INFO')
    print 'env',env
    if path == '/':
        response_body = "Index"
    else:
        response_body = "Hello"

    #obj_input = env['wsgi.input']
    print env.get('CONTENT_LENGTH')
    file_length = os.path.getsize("input_test.txt")
    print file_length

    env['wsgi.input'] = open('input_test.txt', 'rb')


    st = ''
    size = 0
    timeout_reader = constant._make_timeout_reader(env['wsgi.input'])
    try:
        start_time = time.time()
        for chunk in iter(timeout_reader, ''):
            if size > 5* constant.network_chunk_size:
                break
            print type(chunk), chunk
            st = st + chunk
            size = size + len(chunk)
        #st = env['wsgi.input'].read(100)
        print st
        end_time = time.time()
    except:
        print 'exception in read iter'
    print 'file is ', st
    print 'file size is', len(st)
    response_body = response_body + "..... size " + str(size) + '######## time ' + str((end_time - start_time) * 1000)

    status = "200 OK"
    response_headers = [("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return response_body


httpd = make_server('127.0.0.1', 8051, application)
httpd.serve_forever()
