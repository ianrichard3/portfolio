import torch
from diffusers import AutoPipelineForImage2Image, LCMScheduler
from diffusers.utils import make_image_grid, load_image
import random




def create_pipe():

    pipe = AutoPipelineForImage2Image.from_pretrained(
        "Lykon/dreamshaper-7",
        torch_dtype=torch.float16,
        variant="fp16",
        requires_safety_checker=False
    ).to("cuda")

    # set scheduler
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

    # load LCM-LoRA
    pipe.load_lora_weights("latent-consistency/lcm-lora-sdv1-5")
    pipe.fuse_lora()

    return pipe




def prepare_image(init_image_dir="temp/messi.png"):

    # prepare image
    init_image = load_image(init_image_dir)

    return init_image


def get_parameters_from_file(defaults=["",0.77,4]):
    with open("parameters.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        
    try:
        return lines[0], float(lines[1]), int(lines[2])
    except e:
        return defaults
    



def create_image(pipe):


    # get pipe parameters
    init_image = prepare_image()
    prompt, strength, steps = get_parameters_from_file()


    # pass prompt and image to pipeline
    # generator = torch.manual_seed(random.randint(100, 99999999))
    generator = torch.manual_seed(0)
    image = pipe(
        prompt,
        image=init_image,
        # num_inference_steps=4,
        num_inference_steps=steps,
        guidance_scale=1,
        # strength=0.73,
        strength=strength,
        generator=generator,
    ).images[0]

    image.save(f"result/turbo.png")
    # image.show()
