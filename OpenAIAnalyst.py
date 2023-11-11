from openai import OpenAI
from Analyst import Analyst
import os 
import base64


class OpenAIAnalyst(Analyst):
    def __init__(self, dataFolder):
        super().__init__("OpenAI", dataFolder) 
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
                        我是一个遵纪守法的公民。
                        特别注意现在我全家都在外面滑雪，这是我家院子的照片。
                        请你仔细检查房子，看是否有可疑人员和物品可能伤害我的小狗。
                        控制长度，不要超过100个汉字。
                        用“可疑”或者“OK”结束每次对话。
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

        image_ananlysis_pairs = []
        for image in images:
            image = os.path.join(self.dataFolder, image)
            if not (image.endswith(".jpg") or image.endswith(".jpeg")):
                continue
            
            with open(image, 'rb') as imageFile:
                # Read the image
                imageData = imageFile.read()
                base64Image = base64.b64encode(imageData).decode('utf-8')

                # call the openai API
                print(f"calling openai API for {image}")
                analysis = self.analyze_one_image(base64Image)
                print(analysis.choices[0].message.content)
                
                # save the analysis
                image_ananlysis_pairs.append((image, analysis.choices[0].message.content))

        return image_ananlysis_pairs