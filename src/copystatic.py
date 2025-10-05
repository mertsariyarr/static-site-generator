import os
import shutil


def cleaner(public):
        if os.path.exists(public):
            for item in os.listdir(public):
                item_path = os.path.join(public, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                else:
                    shutil.rmtree(item_path)
        else:
            os.mkdir(f"{public}")
     
def copier(static, mypublic):
        for item in os.listdir(static):
            static_path_with_item = os.path.join(static, item)
            if os.path.isfile(static_path_with_item):
                shutil.copy(static_path_with_item, mypublic)
            else:
                mystatic_with_item = os.path.join(static, item)
                mypublic_with_item = os.path.join(mypublic, item)
                os.mkdir(f"{mypublic_with_item}")
                copier(mystatic_with_item, mypublic_with_item)
                