from PIL import Image
import os
import requests
from io import BytesIO
import matplotlib.pyplot as plt

class ImageFlipper:
    def __init__(self, directory):
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def flip_image(self, image_url):
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            im = Image.open(BytesIO(response.content))
            filename = os.path.basename(image_url)
            flipped_im = im.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_im.save(os.path.join(self.directory, f"flipped_{filename}"))
            print(f"图片已成功翻转并保存为: flipped_{filename}")
            
            # 实时显示原图和翻转后的图片
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
            ax1.imshow(im)
            ax1.set_title("原图", fontproperties='SimHei')
            ax1.axis('off')
            ax2.imshow(flipped_im)
            ax2.set_title("翻转后的图片", fontproperties='SimHei')
            ax2.axis('off')
            plt.ion()  # 打开交互模式
            plt.show()
            plt.pause(0.001)  # 暂停一小段时间以确保图像显示
            input("按回车键关闭图像...")  # 等待用户输入以关闭图像
            plt.close(fig)
            
        except requests.RequestException as e:
            print(f"下载图片时出错: {e}")
        except IOError as e:
            print(f"处理图片时出错: {e}")

if __name__ == "__main__":
    directory = "images/"
    image_url = "https://i-blog.csdnimg.cn/direct/7556650d2e4c4c4d96b259c2abd77f48.jpeg"
    flipper = ImageFlipper(directory)
    flipper.flip_image(image_url)