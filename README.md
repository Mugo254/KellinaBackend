
# Kellina System

You can as well fork the project and build on it. We have a group.py file on the root of the folder. this defines all the groups we have i.r Admin Cashier and Client. We also have a permission.py file that defines all permission for the respective groups which we will use in the view.py file to protect our routes. Meaning no unauthorised access. Access only given to the priviledged group in place. The my_permission.py file simply tells django rest to look up and refernce the group.py file check if the group is present in the group_name.

Currently only have two apps, the api app and authorization(Login and Register using JWT token).


All packages are stored in the pipfile

More updates still coming.......


## Installation

Start virtual environment. Using pipenv as virtualenvironment

```bash
  pipenv shell
```


create a group table with the group_names in it.

```bash
  python manage.py group.py
```


    
![Logo](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/th5xamgrr6se0x5ro4g6.png)

