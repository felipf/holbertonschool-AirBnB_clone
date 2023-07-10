# ![Logo](https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20230709%2Feu-west-3%2Fs3%2Faws4_request&X-Amz-Date=20230709T222751Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2c00c26b5ed16a9962b908ff15a7fd89af81415bb54ee3821c146a22a88cf5f0) AirBnB Clone - The Console

The AirBnB Clone - The Console project is part of the didactic proposal offered by Holberton School, focusing on the development of a command-line console to interact with object models.

## Available Functions

The console offers the following functions:

### create

Create a new instance of a class and save it to the JSON file. Usage example:

#### $ create BaseModel

- If the class name is missing, it prints **class name missing** (example: `$ create`).
- If the class name does not exist, it prints **class doesn't exist** (example: `$ create MyModel`).

### show

Print the string representation of an instance based on the class name and ID. Usage example:


#### $ show BaseModel 1234-1234-1234

- If the class name is missing, it prints **class name missing** (example: `$ show`).
- If the class name does not exist, it prints **class doesn't exist** (example: `$ show MyModel`).
- If the instance ID is missing, it prints **instance id missing** (example: `$ show BaseModel`).
- If the instance of the class name does not exist for the given ID, it prints **no instance found** (example: `$ show BaseModel 121212`).

### destroy

Delete an instance based on the class name and ID and save the changes to the JSON file. Usage example:

#### $ destroy BaseModel 1234-1234-1234

- If the class name is missing, it prints **class name missing** (example: `$ destroy`).
- If the class name does not exist, it prints **class doesn't exist** (example: `$ destroy MyModel`).
- If the instance ID is missing, it prints **instance id missing** (example: `$ destroy BaseModel`).
- If the instance of the class name does not exist for the given ID, it prints **no instance found** (example: `$ destroy BaseModel 121212`).

### all

Print the string representation of all instances or instances of a specific class. Usage example:

#### $ all BaseModel

- The printed result should be a list of strings (as shown in the example).
- If the class name does not exist, it prints **class doesn't exist** (example: `$ all MyModel`).

### update

Update an instance based on the class name and ID and save the changes to the JSON file. Usage example:

#### $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"

- Usage: `update <class name> <id> <attribute name> "<attribute value>"`
- Only one attribute can be updated at a time.
- It is assumed that the attribute name is valid (exists for this model).
- The attribute value must be cast to the corresponding attribute type.
- If the class name is missing, it prints **class name missing** (example: `$ update`).
- If the class name does not exist, it prints **class doesn't exist** (example: `$ update MyModel`).
- If the instance ID is missing, it prints **instance id missing** (example: `$ update BaseModel`).
- If the instance of the class name does not exist for the given ID, it prints **no instance found** (example: `$ update BaseModel 121212`).
- If the attribute name is missing, it prints **attribute name missing** (example: `$ update BaseModel existing-id`).
- If the value for the attribute name is missing, it prints **value missing** (example: `$ update BaseModel existing-id first_name`).
- Other arguments should not be used (example: `$ update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty" = $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"`).
- The attributes `id`, `created_at`, and `updated_at` cannot be updated. It is assumed that they will not be passed in the `update` command.

## BaseModel Class

The `BaseModel` class defines all the common attributes and methods for other classes:

Public instance attributes:
- `id`: a string assigned with a unique UUID when an instance is created.
- `created_at`: a `datetime` object assigned with the current date and time when an instance is created.
- `updated_at`: a `datetime` object assigned with the current date and time when an instance is created and updated every time the object is modified.

Public instance methods:
- `save()`: updates the `updated_at` attribute with the current date and time.
- `to_dict()`: returns a dictionary containing all the attributes and values of the object in dictionary format. It adds a `__class__` key with the name of the object's class, and the `created_at` and `updated_at` dates are converted to ISO format.

In addition, the `BaseModel` class has the following additional methods:

- `__init__(self, *args, **kwargs)`: It uses *args and **kwargs as arguments for the constructor of `BaseModel`. If kwargs is not empty, it recreates an instance of `BaseModel` from the kwargs dictionary, converting the date strings to `datetime` objects. If kwargs is empty, it creates a new instance with a new `id`, `created_at`, and `updated_at`.

## Classes Inheriting from BaseModel

The following classes inherit from `BaseModel` and have their corresponding public class attributes:

### State (models/state.py):

Public class attributes:
- `name`: an empty string.

### City (models/city.py):

Public class attributes:
- `state_id`: an empty string. It will be the `State.id`.
- `name`: an empty string.

### Amenity (models/amenity.py):

Public class attributes:
- `name`: an empty string.

### Place (models/place.py):

Public class attributes:
- `city_id`: an empty string. It will be the `City.id`.
- `user_id`: an empty string. It will be the `User.id`.
- `name`: an empty string.
- `description`: an empty string.
- `number_rooms`: an integer (0).
- `number_bathrooms`: an integer (0).
- `max_guest`: an integer (0).
- `price_by_night`: an integer (0).
- `latitude`: a float (0.0).
- `longitude`: a float (0.0).
- `amenity_ids`: an empty list of strings. It will be the list of `Amenity.id` later on

### Review (models/review.py):

Atributos de clase públicos:
- `place_id`: una cadena vacía. Será el `Place.id`.
- `user_id`: una cadena vacía. Será el `User.id`.
- `text`: una cadena vacía.

## FileStorage Class

The `FileStorage` class handles the correct serialization and deserialization of the classes: Place, State, City, Amenity, and Review. Instances of these classes can be saved to the JSON file and restored from the file.

The `FileStorage` class has the following methods:

- `all(self)`: returns the dictionary `__objects`.
- `new(self, obj)`: sets the in `__objects` the object `obj` with the key `<name of the class>.id`.
- `save(self)`: serializes `__objects` to the JSON file  (`__file_path`).
- `reload(self)`: deserializes the JSON file to __objects (only if the JSON file exists, otherwise does nothing).

## Authors

- [@Felipe Pereira](https://www.linkedin.com/in/felipe-pereira-forte-ba40a8263/)

- [@Franco Herrera](https://www.linkedin.com/in/franco-fabrizio-herrera-zunino-34371b278/)
