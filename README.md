# simpleRESTful
This is a very simple example about how to create RESTful microservice with flask.

When building RESTful microservice with flask, there're several things we need to decide:

    - where to find configurations(for example, on which port the RESTful should listen to, what URL prefix will be used, where to put log, etc...)
    - who should handle which request
    
We can use config.py to save configurations and use them in other functions, use flask Blueprint to define request handler functions as Resource

The folder tree looks like this:


    .
    ├── mytest
    │   ├── api_1_0
    │   │   └── __init__.py // define the Blueprint api_bp here
                            // define flask_restful Api class MyApi
                            // define flask_restful Resource class ShowPort
                            // add_resource and specify which URL will be handled by which resource
    │   ├── config.py       // provide the configuration settings, will be used by create_app() and other functions
    │   └── __init__.py     // the "main" python file, 
                            //    -- define the entry functions here. 
                            //    -- define the create_app(), which will 
                            //         ** get configuration
                            //         ** register the api_bp in the Flask app
    ├── README.md           // this readme file
    ├── requirements.txt    // package dependencies for this package
    ├── setup.cfg           // setup the package name and entry points. will hook to __init__.py of package level
    └── setup.py            // setuptool need this


Currently this version after install this package, two new cli command will be available:

    mytest-api              // start the RESTful service
    mytest-version          // get version of this software
