# server_client_read

# request pattern:

http://127.0.0.1:8051/

http://127.0.0.1:8051/abc

wsgi_web_application is a simple wsgi application which only return 'index' or 'hello' based on path_info.
wsgi_server module is used to read and print wsgi.input values given by the client.

** important if anyone design his own client, then he must have to give a file-like object in env['wsgi.input']

# how to run
python <module_name.py>


