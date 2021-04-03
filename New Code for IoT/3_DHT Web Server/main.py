# MicroPython Web Server (Weather Station)
# This is main.py file.
# The main.py file contains the code that runs the web server to serve files and perform tasks based on the requests received by the client.

# Create a function called "read_sensor()" that reads temperature and humidity.
def read_sensor():
  global temp, hum # The function starts by creating two global variables,
  temp = hum = 0 # so we can use them in all parts of the script (they are initilazed as 0).
  # The "temp" variable holds the temperature reading from the sensor and the "hum" holds the humidity reading from the sensor.
  # Inside the "try" statement we 'try' to get the temperature and humidity values.
  # Try and except allows us to continue the execution of the program when an exception happens.
  
  # Measure the sensor by using the "measure()" method on the "sensor" object.
  try:
    sensor.measure()
    temp = sensor.temperature() # read the temperature with "sensor.temperature()"
    hum = sensor.humidity() # read the humidity with "sensor.humidity()"
    # Save those readings on the "temp" and "hum" variables.
    
    # Valid temperature and humidity readings should be of type int (if you’re using a DHT11) sensor.
    # So, we check if we have valid readings by using the "isinstance()" function before proceeding.
    # The "isinstance()" function accepts as arguments the variable and the data type: "isinstance(variable, data type)."
    # It returns "True" if the variable corresponds to the inserted data type and "False" if it doesn’t.
    if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
      msg = (b'{0:3.1f},{1:3.1f}'.format(temp, hum)) # If the readings are valid, prepare a message to be printed on the Shell that includes the temperature and humidity readings.

      # uncomment for Fahrenheit
      #temp = temp * (9/5) + 32.0
      
      # Round the humidity reading to two decimal points. This will be printed later on the web server page.
      hum = round(hum, 2)
      # Return the message with the temperature and humidity.
      return(msg)
    else: # In case we don’t get valid sensor readings (not float type), 
      return('Invalid sensor readings.') # We return "Invalid sensor readings." message.
  except OSError as e: # In case we’re not able to read from the sensor (for example, in case it disconnects), return an error message.
    return('Failed to read sensor.')

# The "web_page()" function returns the HTML page.
# The following <meta> tag makes your web page responsive in any browser.
# The <link> tag is needed to load the icons used in the webpage from the fontawesome website.
# Between the <style></style> tags, we add some CSS to style the web page.
# Basically, we’re setting the HTML page to display the text with Arial font in block without margin, and aligned at the center.
# We set the font size for the heading (h2), paragraph (p) and the units(.units) of the readings.
# The labels for the readings are styled.
# All of the previous tags should go between the <head> and </head> tags.
# These tags are used to include content that is not directly visible to the user, like the <meta> , the <link> tags, and the styles.
# Inside the <body></body> tags is where we add the web page content.
# The <h2></h2> tags add a heading to the web page. In this case, the “ESP DHT server” text, but you can add any other text.
# Then, there are two paragraphs. One to display the temperature and the other to display the humidity.
# The paragraphs are delimited by the <p> and </p> tags.
# The <i> tags display the fontawesome icons.
def web_page():
  html = """<!DOCTYPE HTML><html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  <style>
    html {
     font-family: Arial;
     display: inline-block;
     margin: 0px auto;
     text-align: center;
    }
    h2 { font-size: 3.0rem; }
    p { font-size: 3.0rem; }
    .units { font-size: 1.2rem; }
    .dht-labels{
      font-size: 1.5rem;
      vertical-align:middle;
      padding-bottom: 15px;
    }
  </style>
</head>
<body>
  <h2>ESP DHT Server</h2>
  <p>
    <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
    <span class="dht-labels">Temperature</span> 
    <span>"""+str(temp)+"""</span>
    <sup class="units">&deg;C</sup>
  </p>
  <p>
    <i class="fas fa-tint" style="color:#00add6;"></i> 
    <span class="dht-labels">Humidity</span>
    <span>"""+str(hum)+"""</span>
    <sup class="units">%</sup>
  </p>
</body>
</html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

# In the "while" loop, when we call the "read_sensor()" function to print the sensor readings and to update the global variables "temp" and "hum".
while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  sensor_readings = read_sensor()
  print(sensor_readings)
  response = web_page() # The web_page() function generates HTML text with the latest sensor readings.
  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()
# End of Program.