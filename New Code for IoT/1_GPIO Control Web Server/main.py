# MicroPython Web Server – Control GPIO Connected Outputs using Micropython Framework.
# This is main.py file.

# Creating a function called web_page().
# This function returns a variable called "html" that contains the HTML text to build the web page.
# Web page displays the current GPIO state.
# So, before generating the HTML text, user need to check the LED state.
# User then save its state on the "gpio_state" variable.
def web_page():
  if led.value() == 1:
    gpio_state="ON"
  else:
    gpio_state="OFF"
    
# The gpio_state variable is incorporated into the HTML text using “+” signs to concatenate strings.  
  html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1> 
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
  return html

# Create a socket using socket.socket(), and specify the socket type.
# User create a new socket object called "s" with the given address family, and socket type. This is a STREAM TCP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address (network interface and port number) using the "bind()" method.
# The "bind()" method accepts a tupple variable with the IP address, and port number.
# Passing an empty string ‘ ‘ as an IP address and port 80.
# In this case, the empty string refers to the localhost IP address (this means the NodeMCU IP address).
s.bind(('', 80))

# Enables the server to accept connections; it makes a “listening” socket.
# The argument specifies the maximum number of queued connections. The maximum is 5.
s.listen(5)

# In the while loop is where we listen for requests and send responses.
# When a client connects, the server calls the "accept()" method to accept the connection.
# When a client connects, it saves a new socket object to accept and send data on the "conn" variable,
# and saves the client address to connect to the server on the "addr" variable.
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr)) # print the address of the client saved on the "addr" variable.
  # The data is exchanged between the client and server using the send() and recv() methods.
  request = conn.recv(1024) # Gets the request received on the newly created socket and saves it in the "request" variable.
  # The "recv()" method receives the data from the client socket (remember that we’ve created a new socket object on the "conn" variable).
  # The argument of the "recv()" method specifies the maximum data that can be received at once.
  request = str(request)
  print('Content = %s' % request) # Prints the content of the request.
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  if led_on == 6:
    print('LED ON')
    led.value(1)
  if led_off == 6:
    print('LED OFF')
    led.value(0)
  response = web_page() # Create a variable called "response" that contains the HTML text returned by the "web_page()" function.
  # Send the response to the socket client using the "send()" and "sendall()" methods.
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close() # Close the created socket.
  
# End of Program.