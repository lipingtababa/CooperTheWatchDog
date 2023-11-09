from openai import OpenAI
from Analyst import Analyst
import os 
import base64

class OpenAIAnalyst(Analyst):
    def __init__(self, dataFolder):
        super().__init__("OpenAI",dataFolder) 
        self.initialize()

    def initialize(self):
        from config import OPENAI_API_KEY
        self.client = OpenAI(
            api_key = OPENAI_API_KEY
        )

    def analyze_one_image(self, base64_image):
        response = self.client.chat.completions.create(
            model = "gpt-4-vision-preview",
            messages = [
                {
                    "role": "user", 
                    "content": [
                    {
                    "type": "text",
                    "text": '''
                        这是我家院子的图片。
                        你应该像我的狗一样仔细检查房子，看是否有可疑人员和物品。
                        如果没有，你检查我的设施是否都正常，比如植物是否健康。
                        用中文回答。并且用“汪汪”结束每次对话。
                    '''
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
                }
                ],
            max_tokens = 300
            )
        return response

    def analyze_images(self):
        # list image in the local folder
        images = os.listdir(self.dataFolder)

        for image in images:
            if not image.endswith(".jpg"):
                continue
            with open(os.path.join(self.dataFolder, image), 'rb') as imageFile:
                # Read the image
                imageData = imageFile.read()
                base64Image = base64.b64encode(imageData).decode('utf-8')

                # call the openai API
                print(f"calling openai API for {image}")
                analysis = self.analyze_one_image(base64Image)
                print(analysis.choices[0].message.content)
