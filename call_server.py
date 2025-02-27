import os
from openai import OpenAI
import base64
from config_private import MODEL2URL, MODEL2KEY, MODEL2MODEL, http_proxy, https_proxy
import random
from time import sleep
import time


# os.environ["http_proxy"] = http_proxy
# os.environ["https_proxy"] = https_proxy


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


if __name__ == "__main__":
    model_name_list = [
        # "Qwen2-VL-7B-Instruct",
        # "Pixtral-12B-2409",
        # "llava-onevision-qwen2-7b-ov-hf",
        # "llava-onevision-qwen2-7b-ov-hf",
        # "Phi-3.5-vision-instruct",
        # "Qwen2-VL-7B-Instruct",
        "Llama-3.2-11B-Vision-Instruct",
        # "Phi-3.5-vision-instruct",
        # "Qwen2-VL-72B-Instruct2"
    ]
    # model_name_list = ["gpt-4o-2024-08-06"]
    image_path_list = ["agent/prompts/som_examples/som_example1.png", "agent/prompts/som_examples/som_example2.png",
                       "agent/prompts/som_examples/som_example3.png"]
    # image_path_list = ["agent/prompts/som_examples/som_example1.png","agent/prompts/som_examples/som_example2.png"]
    # image_path_list = ["agent/prompts/som_examples/som_example1.png"]
    # image_path_list = ["readme_document/vllm.png"]
    # image_path_list = ["readme_document/vllm.png","readme_document/vllm.png"]
    # image_path_list = ["agent/prompts/som_examples/som_example1.png", "agent/prompts/som_examples/som_example2.png",
    #                    "agent/prompts/som_examples/som_example3.png", "readme_document/vllm.png"]
    temperature = 0.1
    top_p = 0.9
    # text = """
    # 先说出你的模型型号？然后说出图像中有什么？
    # """
    text = """What are the four pictures? Describe each in one sentence"""
    image_value_list = []
    for image_path in image_path_list:
        if "png" in image_path:
            image_value = f"data:image/png;base64,{encode_image(image_path)}"
        else:
            image_value = f"data:image/jpeg;base64,{encode_image(image_path)}"
        image_value_list.append(image_value)
    while True:
        model_name = random.choice(model_name_list)
        print(model_name)
        client = OpenAI(
            base_url=MODEL2URL[model_name],
            api_key=MODEL2KEY[model_name],
        )
        messages = [{"type": "text", "text": text, }]
        for image_value in image_value_list:
            messages.append({"type": "image_url", "image_url": {"url": image_value}, })

        start1 = time.time()
        completion = client.chat.completions.create(
            model=MODEL2MODEL[model_name],
            messages=[
                {"role": "user", "content": messages}],
            temperature=temperature,
            top_p=top_p,
            max_tokens=300,
            n=2
        )
        print(completion.choices[0].message.content)
        print(len(completion.choices))
        time1 = time.time() - start1
        print(f"计时: {time1:.4f}秒")
        print("end")
