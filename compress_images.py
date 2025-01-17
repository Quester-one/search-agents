from PIL import Image


def resize_image(input_path, output_path,compress_rate):
    with Image.open(input_path) as img:
        img_resized = img.resize((int(img.size[0]/compress_rate), int(img.size[1]/compress_rate)), Image.LANCZOS)
        img_resized.save(output_path)


if __name__ == "__main__":
    compress_rate=2
    resize_image("agent/prompts/som_examples/som_example1_raw.png", "agent/prompts/som_examples/som_example1.png",compress_rate)
    resize_image("agent/prompts/som_examples/som_example2_raw.png", "agent/prompts/som_examples/som_example2.png",compress_rate)
    resize_image("agent/prompts/som_examples/som_example3_raw.png", "agent/prompts/som_examples/som_example3.png",compress_rate)
    print("end")
