import argparse
import torch
from diffusers import StableDiffusionPipeline

# a framework that uses pretrained model
def generate(prompt, output_path):
    pipe = StableDiffusionPipeline.from_pretrained(
     "stabilityai/stable-diffusion-3.5-medium",
        torch_dtype=torch.float16
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    image = pipe(prompt).images[0]
    image.save(output_path)

if __name__ == "__main__":
    """parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()"""

    generate("一个南开大学的学生", "/image.png'")