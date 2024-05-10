import torch
from diffusers import AutoPipelineForImage2Image, LCMScheduler
from diffusers.utils import make_image_grid, load_image
import random


def dummy(images, **kwargs):
    return images, False


pipe = AutoPipelineForImage2Image.from_pretrained(
    "Lykon/dreamshaper-7",
    torch_dtype=torch.float16,
    variant="fp16",
    requires_safety_checker=False
).to("cuda")

# print(pipe.safety_checker)


# pipe.safety_checker = dummy

# set scheduler
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

# load LCM-LoRA
pipe.load_lora_weights("latent-consistency/lcm-lora-sdv1-5")
pipe.fuse_lora()

# prepare image
url = "temp/messi.jpg"
init_image = load_image(url)

prompt = ""
with open("prompt.txt") as f:
    prompt = f.read()

print(f"Prompt: [{prompt}]")


strengths = (0.6, 0.73, 0.85, 0.95, 1)
steps = (2, 4, 4, 6, 8)

for i in range(len(strengths)):

    # pass prompt and image to pipeline
    generator = torch.manual_seed(0)
    image = pipe(
        prompt,
        image=init_image,
        # num_inference_steps=4,
        num_inference_steps=random.choice(steps),
        guidance_scale=1,
        # strength=0.73,
        strength=random.choice(strengths),
        generator=generator,
        seed=random.randint(4000,99999999)
    ).images[0]

    image.save(f"result/turbo{i+1}.png")
    image.show()
    # make_image_grid([init_image, image], rows=1, cols=2)
