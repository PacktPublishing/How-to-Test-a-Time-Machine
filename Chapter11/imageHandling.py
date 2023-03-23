import os

class ImageHandling():
    ''' Class to handle images'''
    path = r"path_to_images"
    list_of_images = os.listdir(path)

    def rename_image(self):
        ''' rename images in the folder'''
        count = 0
        for image_to_find in self.list_of_images:
            os.rename(self.path+image_to_find,
                f"{self.path}{count}image_to_find.getName()")
            count = count + 1

    ## find used images and save them into set "img_set"
    ## iterate through all images if not in used --> remove
    def remove_unused_image(self, img_set):
        ''' remove images from the given param'''
        for img in self.list_of_images:
            if img not in img_set:
                os.remove(img)