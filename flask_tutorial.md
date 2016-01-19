1. Setup your File Structure. You'll need:
  An ```app``` folder and in that:
    A ```static``` where you can keep css, javascript, and images
    A folder for your 'templates'

2. While in your ```/app``` folder, on your command line: 

  ```$ touch routes.py```
    -When the browser sends a request, the ```routes.py``` file maps the URLs to application actions and knows to look in the ```static``` folder for any images, stylesheets, or scripts it needs to render an HTML
    - Once the HTML is rendered, it is sent back to ```routes.py```, which will then send it back to the browser

3. In in ```app/templates```, on your command line:

  ```$ touch layout.html```

  We will use this to define our standard page layout and anything else can be rendered as a partial

4. Go ahead an add your regular old HTML spill:

  ```
  <!DOCTYPE html>
  <html>
    <head>
      <title>Hello World</title>    
    </head>
    <body>
     
      <header>
        <div class="container">
          <h1 class="hello">Hello World</h1>
        </div>
      </header> 
       
    </body>
  </html>
  ```

5. In order to render this information on all of your other templates, add the following code to the end of what you'd like to render as a standard layout.

  ```
  <div class="container">
      {% block content %}
      {% endblock %}
  </div>
  ```

  6. Let's test it by creating another template. This one will be a partial. In in ```app/templates```, on your command line:

  ```$ touch home.html```

  7. At the very top of you new ```home.html``` document add:
    ```
    {% extends "layout.html" %}
    {% block content %}
    ```

    To let your document know that it's supposed to render the same boilerplate and header from your ```layout.html``` file.

    Enter your HTML code: 

    ```
    <div class="partial">
      <h2>Welcome to our Flask Tutorial<h2>
      <h3>These are the steps to create a Flask App<h3>
    </div>
    ```

    Put ```{% endblock %}``` at the end of your HTML document to end the rendering of the template.

8. In the ```app/routes.py```, 

    -Import the Flask class and the function ```render_template```
    
      ```from flask import Flask, render_template```

    -Create a new instance of the Flask class.
      ```app = Flask(__name__)```
      -It's okay to name  the class (__name__) if you're using a signle module. But if you're using a package, be sure to hardcode the name of your package to avoid naming conflicts.

    -Then map, the URL / to the function home()
      ```
      @app.route('/')
      def home():
      return render_template('home.html')
      ```

    -Finally use run() to run the app on a local server. 
      ```app.run()```

    -Now, you can access the app and routes on your local host by running the following on your command line:
      ```$ python routes.py``` and visiting ```http://localhost:5000/```