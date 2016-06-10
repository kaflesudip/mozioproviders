# API Documentation

This app provides API for both Providers and Services Areas. CRUD operations can be performed using endpoints for both the APIs. The [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) is also available for live testing.

## Provider API:

### Create a provider:

A new provider can be created py providing name, email, phone_no, language, currency.
1. Email must be a valid Email.
2. Phone number must include country code. e.g. +11232323232
3. Language is a RFC-3066 Language Code. More details can be found on [http://www.i18nguy.com/unicode/language-identifiers.html](http://www.i18nguy.com/unicode/language-identifiers.html)
4. Currency is a ISO-4217 Currency code. More details can be found on [http://www.xe.com/iso4217.php](http://www.xe.com/iso4217.php)

Try the API by sending a post request to [http://ec2-52-91-71-216.compute-1.amazonaws.com/api/providers/](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/providers/)


### GET all providers
Try this on [http://ec2-52-91-71-216.compute-1.amazonaws.com/api/providers/](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/providers/)

### Update a provider
Refer [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) for endpoints for updating a povider. 

### Delete a provider.
Refer [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) for endpoints for deleting a povider. 


## Services API:

### Create a service.

A new service can be created by poviding provider, name, price and polygon.
1. `provider` is the id of already created provider.
2. `name` is the name of Service Area.
3. `price` is a floating-point number repesenting the price.
4. `polygon` is a geojson polygon representing the boundary of the area.

Try the API live on [http://ec2-52-91-71-216.compute-1.amazonaws.com/api/services/](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/services/)

### Retrive all polygons which contain the given point.

All the polygons can be retrived by accessing the url `/api/services/<longitue_value>/<latitude_value>/`
`latitude_value` and `longitude_values` are floating point number which can be negative.


### Retrive a Service Area by id
Refer [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) for endpoints for updating a service Area by id. 

### Update a Service Area
Refer [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) for endpoints for updating a service Area. 

### Delete a Service Area.
Refer [API documentation](http://ec2-52-91-71-216.compute-1.amazonaws.com/api/docs/) for endpoints for deleting a service Area. 