import json
import urllib.request
import os
import base64


class HandlerImage:
    """Class responsible for handling images"""

    def __init__(self):
        pass

    imageDatabasePath: str = 'databaseUser/Images/images.json'
    imageDatabase: dict = {}
    image_formats = [".jpeg", ".jpg", ".png", ".gif"]
    directory = "./databaseUser/Images"

    @staticmethod
    def data_to_image(data: str, id_user: str) -> any:
        """Responsible for creating an image from a data URI

        :param data: A string containing the data URI
        :param id_user: A string containing the user id
        :returns: Three strings each containing the image name, image extension and image path. Can also return None.

        """

        extension = ".jpg"
        for formats in HandlerImage.image_formats:
            if data.find(formats[1:], 0, 20) != -1:
                extension = formats
                break

        try:
            # Path example: "./databaseUser/Images/5161316181.png"
            image = '/' + id_user + extension
            path = HandlerImage.directory + image

            response = urllib.request.urlopen(data)

            with open(f'{path}', 'wb') as f:
                f.write(response.file.read())

            return image, extension, path
        except:
            return None

    @staticmethod
    def image_to_data(image_path: str) -> str:
        """Responsible for converting an image into a data URI

        :param image_path: A string containing the image path
        :returns: A string containing the dataURI from the image

        """

        index = image_path.find('.')
        extension = image_path[index+1:]

        # Dunno why
        if extension == "jpg":
            extension = "jpeg"

        full_path = HandlerImage.directory + image_path.replace("http://localhost:8083", "")

        encoded = base64.b64encode(open(full_path, "rb").read()).decode()

        data_uri = 'data:image/{};base64,{}'.format(extension, encoded)
        return data_uri

    @staticmethod
    def insert_image_database(data: str, id_user: str) -> any:
        """Responsible for inserting the image into our database

        :param data: A string containing the data URI
        :param id_user: A string containing the user id
        :returns: A string containing the id of the registered image or None

        """

        # Download the image
        image_id, extension, path = HandlerImage.data_to_image(data, id_user)

        database: dict = HandlerImage.getData()

        imageData = {
            "type": "image/" + extension[1:],
            "filePath": path
        }

        image_already_in_database, image_index = HandlerImage.isImageRegistered(image_id)
        if image_already_in_database:
            database["images"][image_index][image_id] = imageData
        else:
            database["images"].append({image_id: imageData})
        if HandlerImage.setData(database):
            return image_id

        return None

    @staticmethod
    def delete_image_database(image_id: str) -> bool:
        """Responsible for deleting an image with given id from the database

        :param image_id: A string containing the image id
        :returns: A boolean representing if the operation was successful or not

        """

        database = HandlerImage.getData()
        if database is None:
            return False
        image_already_in_database, image_index = HandlerImage.isImageRegistered(image_id)
        if image_already_in_database:
            database["images"].pop(image_index)
        image_id = image_id.replace("http://localhost:8083", "")
        if HandlerImage.setData(database) and HandlerImage.remove_img(image_id):
            return True
        return False

    @staticmethod
    def delete_all_images() -> bool:
        """Responsible for deleting all images from the database

        :returns: A boolean representing if the operation was successful or not
        """

        database = HandlerImage.getData()
        if database is None:
            return False

        database["images"] = []

        if HandlerImage.setData(database):
            # Delete all images in folder
            try:
                for file in os.listdir(HandlerImage.directory):
                    for formats in HandlerImage.image_formats:
                        if file.endswith(formats):
                            os.remove(HandlerImage.directory + '/' + file)

                return True
            except Exception as e:
                print(e)
                return False

        return False

    @staticmethod
    def remove_img(img_name: str) -> bool:
        """Responsible for removing a image from the images directory

        :param: img_name: A string containing the image name
        :returns: A boolean representing if the operation was successful or not

        """

        path = HandlerImage.directory + img_name
        os.remove(path)
        # check if file exists or not
        if os.path.exists(path) is False:
            # file did not exists
            return False

        return True

    @staticmethod
    def getData() -> any:
        """Responsible for getting the images from the database

        :returns: A dictionary containing the images or None.

        """

        try:
            with open(HandlerImage.imageDatabasePath, 'r+') as file:
                HandlerImage.imageDatabase = json.load(file)
                return HandlerImage.imageDatabase
        except:
            return None

    @staticmethod
    def isImageRegistered(image_id: str) -> (bool, any):
        """Responsible for checking if the image with given id is registered

        :param image_id: A string containing the id of the image to be deleted
        :returns: A bool containing the result of the operation and the image index in case it's registered

        """

        database = HandlerImage.getData()

        if database is None:
            return False, None

        index: int
        element: dict
        for index, element in enumerate(database["images"]):
            if image_id == list(element.keys())[0]:
                return True, index

        return False, None

    @staticmethod
    def setData(data: dict) -> bool:
        """Responsible for replacing the whole image database with the given data

        :param data: a dictionary containing the new image database
        :returns: A boolean representing if the operation was successful or not

        """

        HandlerImage.imageDatabase = data
        try:
            with open(HandlerImage.imageDatabasePath, 'w+') as file:
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

                return True
        except Exception as e:
            print(e)
            return False
