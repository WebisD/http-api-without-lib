import json
import urllib.request
import os
import base64


class HandlerImage:
    imageDatabasePath: str = 'databaseUser/Images/images.json'
    imageDatabase: dict = {}
    image_formats = [".jpeg", ".jpg", ".png", ".gif"]
    directory = "./databaseUser/Images"

    @staticmethod
    def data_to_image(data: str, id_user: str):
        extension = ".jpg"
        for formats in HandlerImage.image_formats:
            if data.find(formats, 0, 20) != -1:
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
    def image_to_data(image_path):
        index = image_path.find('.')
        extension = image_path[index+1:]

        # Dunno why
        if extension == "jpg":
            extension = "jpeg"

        full_path = HandlerImage.directory + image_path

        encoded = base64.b64encode(open(full_path, "rb").read()).decode()

        data_uri = 'data:image/{};base64,{}'.format(extension, encoded)
        return data_uri

    @staticmethod
    def insert_image_database(data: str, id_user: str):
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
    def delete_image_database(image_id):
        database = HandlerImage.getData()

        if database is None:
            return False

        image_already_in_database, image_index = HandlerImage.isImageRegistered(image_id)
        if image_already_in_database:
            database["images"].pop(image_index)

        if HandlerImage.setData(database) and HandlerImage.remove_img(image_id):
            return True

        return False

    @staticmethod
    def delete_all_images():
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
    def remove_img(img_name):
        path = HandlerImage.directory + img_name
        os.remove(path)
        # check if file exists or not
        if os.path.exists(path) is False:
            # file did not exists
            return False

    @staticmethod
    def getData():
        try:
            with open(HandlerImage.imageDatabasePath, 'r+') as file:
                HandlerImage.imageDatabase = json.load(file)
                return HandlerImage.imageDatabase
        except:
            return None

    @staticmethod
    def isImageRegistered(image_id: str):
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
    def setData(data: dict):
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
