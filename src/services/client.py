import aiofiles
import requests
import aiohttp

async def prompt0(prompt, negativ_prompt, id):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://185.234.229.106:8130/prompt", json={
            "client_id": "85fa01ab562c4d92929b2674bf512aea", "prompt": {"3": {
            "inputs": {"seed": 958540525371069, "steps": 20, "cfg": 8, "sampler_name": "euler", "scheduler": "normal",
                       "denoise": 1, "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0],
                       "latent_image": ["5", 0]}, "class_type": "KSampler", "_meta": {"title": "KSampler"}},
            "4": {"inputs": {"ckpt_name": "anithing_v11Pruned.safetensors"}, "class_type": "CheckpointLoaderSimple",
            "_meta": {"title": "Load Checkpoint"}},
            "5": {"inputs": {"width": 512, "height": 512, "batch_size": 1},
                                                          "class_type": "EmptyLatentImage",
                                                          "_meta": {"title": "Empty Latent Image"}},
            "6": {"inputs": {"text": f"{prompt}", "clip": ["4", 1]}, "class_type": "CLIPTextEncode",
            "_meta": {"title": "CLIP Text Encode (Prompt)"}},
            "7": {"inputs": {"text": f"{negativ_prompt}", "clip": ["4", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "CLIP Text Encode (Prompt)"}},
            "8": {"inputs": {"samples": ["3", 0],
                                                                                      "vae": ["4", 2]},
                                                                           "class_type": "VAEDecode",
                                                                           "_meta": {"title": "VAE Decode"}}, "9": {
                "inputs": {"filename_prefix": f"{id}", "images": ["8", 0]}, "class_type": "SaveImage",
                "_meta": {"title": "Save Image"}}}, "extra_data": {"extra_pnginfo": {
            "workflow": {"last_node_id": 9, "last_link_id": 9, "nodes": [
                {"id": 5, "type": "EmptyLatentImage", "pos": [473, 609], "size": {"0": 315, "1": 106}, "flags": {},
                 "order": 0, "mode": 0,
                 "outputs": [{"name": "LATENT", "type": "LATENT", "links": [2], "slot_index": 0}],
                 "properties": {"Node name for S&R": "EmptyLatentImage"}, "widgets_values": [512, 512, 1]},
                {"id": 3, "type": "KSampler", "pos": [863, 186], "size": {"0": 315, "1": 262}, "flags": {}, "order": 4,
                 "mode": 0, "inputs": [{"name": "model", "type": "MODEL", "link": 1},
                                       {"name": "positive", "type": "CONDITIONING", "link": 4},
                                       {"name": "negative", "type": "CONDITIONING", "link": 6},
                                       {"name": "latent_image", "type": "LATENT", "link": 2}],
                 "outputs": [{"name": "LATENT", "type": "LATENT", "links": [7], "slot_index": 0}],
                 "properties": {"Node name for S&R": "KSampler"},
                 "widgets_values": [958540525371069, "randomize", 20, 8, "euler", "normal", 1]},
                {"id": 8, "type": "VAEDecode", "pos": [1209, 188], "size": {"0": 210, "1": 46}, "flags": {}, "order": 5,
                 "mode": 0, "inputs": [{"name": "samples", "type": "LATENT", "link": 7},
                                       {"name": "vae", "type": "VAE", "link": 8}],
                 "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": [9], "slot_index": 0}],
                 "properties": {"Node name for S&R": "VAEDecode"}},
                {"id": 4, "type": "CheckpointLoaderSimple", "pos": [26, 474], "size": {"0": 315, "1": 98}, "flags": {},
                 "order": 1, "mode": 0, "outputs": [{"name": "MODEL", "type": "MODEL", "links": [1], "slot_index": 0},
                                                    {"name": "CLIP", "type": "CLIP", "links": [3, 5], "slot_index": 1},
                                                    {"name": "VAE", "type": "VAE", "links": [8], "slot_index": 2}],
                 "properties": {"Node name for S&R": "CheckpointLoaderSimple"},
                 "widgets_values": ["anithing_v11Pruned.safetensors"]},
                {"id": 7, "type": "CLIPTextEncode", "pos": [413, 389],
                 "size": {"0": 425.27801513671875, "1": 180.6060791015625}, "flags": {}, "order": 3, "mode": 0,
                 "inputs": [{"name": "clip", "type": "CLIP", "link": 5}],
                 "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [6], "slot_index": 0}],
                 "properties": {"Node name for S&R": "CLIPTextEncode"}, "widgets_values": [f"{negativ_prompt}"]},
                {"id": 9, "type": "SaveImage", "pos": [1451, 189], "size": {"0": 210, "1": 270}, "flags": {},
                 "order": 6, "mode": 0, "inputs": [{"name": "images", "type": "IMAGE", "link": 9}], "properties": {},
                 "widgets_values": ["ComfyUI"]}, {"id": 6, "type": "CLIPTextEncode", "pos": [415, 186],
                                                  "size": {"0": 422.84503173828125, "1": 164.31304931640625},
                                                  "flags": {}, "order": 2, "mode": 0,
                                                  "inputs": [{"name": "clip", "type": "CLIP", "link": 3}], "outputs": [
                        {"name": "CONDITIONING", "type": "CONDITIONING", "links": [4], "slot_index": 0}],
                                                  "properties": {"Node name for S&R": "CLIPTextEncode"},
                                                  "widgets_values": [f"{prompt}"]}],
                         "links": [[1, 4, 0, 3, 0, "MODEL"], [2, 5, 0, 3, 3, "LATENT"], [3, 4, 1, 6, 0, "CLIP"],
                                   [4, 6, 0, 3, 1, "CONDITIONING"], [5, 4, 1, 7, 0, "CLIP"],
                                   [6, 7, 0, 3, 2, "CONDITIONING"], [7, 3, 0, 8, 0, "LATENT"], [8, 4, 2, 8, 1, "VAE"],
                                   [9, 8, 0, 9, 0, "IMAGE"]], "groups": [], "config": {}, "extra": {}, "version": 0.4,
                         "widget_idx_map": {"3": {"seed": 0, "sampler_name": 4, "scheduler": 5}}}}}
    })

async def get(id):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
        status = response.status
        response.close()
        return status

async def get_picture0(id):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
        async with aiofiles.open(f'src//data//photos//{id}_new.png', 'wb') as target:
            async for chank in response.content.iter_chunked(64*1024):
                await target.write(chank)
    #t =True
    #while t==True:
    #    a = requests.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
    #    if a.content != "":
    #        t=False
    #a = requests.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
    #with open(f'src//data//photos//{id}_new.png', 'wb') as target:
    #        target.write(a.content)







def prompt(prompt,negativ_prompt,id):
    p = requests.post("http://185.234.229.106:8130/prompt", json={
            "client_id": "85fa01ab562c4d92929b2674bf512aea", "prompt": {"3": {
            "inputs": {"seed": 958540525371069, "steps": 20, "cfg": 8, "sampler_name": "euler", "scheduler": "normal",
                       "denoise": 1, "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0],
                       "latent_image": ["5", 0]}, "class_type": "KSampler", "_meta": {"title": "KSampler"}},
            "4": {"inputs": {"ckpt_name": "anithing_v11Pruned.safetensors"}, "class_type": "CheckpointLoaderSimple",
            "_meta": {"title": "Load Checkpoint"}},
            "5": {"inputs": {"width": 512, "height": 512, "batch_size": 1},
                                                          "class_type": "EmptyLatentImage",
                                                          "_meta": {"title": "Empty Latent Image"}},
            "6": {"inputs": {"text": f"{prompt}", "clip": ["4", 1]}, "class_type": "CLIPTextEncode",
            "_meta": {"title": "CLIP Text Encode (Prompt)"}},
            "7": {"inputs": {"text": f"{negativ_prompt}", "clip": ["4", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "CLIP Text Encode (Prompt)"}},
            "8": {"inputs": {"samples": ["3", 0],
                                                                                      "vae": ["4", 2]},
                                                                           "class_type": "VAEDecode",
                                                                           "_meta": {"title": "VAE Decode"}}, "9": {
                "inputs": {"filename_prefix": f"{id}", "images": ["8", 0]}, "class_type": "SaveImage",
                "_meta": {"title": "Save Image"}}}, "extra_data": {"extra_pnginfo": {
            "workflow": {"last_node_id": 9, "last_link_id": 9, "nodes": [
                {"id": 5, "type": "EmptyLatentImage", "pos": [473, 609], "size": {"0": 315, "1": 106}, "flags": {},
                 "order": 0, "mode": 0,
                 "outputs": [{"name": "LATENT", "type": "LATENT", "links": [2], "slot_index": 0}],
                 "properties": {"Node name for S&R": "EmptyLatentImage"}, "widgets_values": [512, 512, 1]},
                {"id": 3, "type": "KSampler", "pos": [863, 186], "size": {"0": 315, "1": 262}, "flags": {}, "order": 4,
                 "mode": 0, "inputs": [{"name": "model", "type": "MODEL", "link": 1},
                                       {"name": "positive", "type": "CONDITIONING", "link": 4},
                                       {"name": "negative", "type": "CONDITIONING", "link": 6},
                                       {"name": "latent_image", "type": "LATENT", "link": 2}],
                 "outputs": [{"name": "LATENT", "type": "LATENT", "links": [7], "slot_index": 0}],
                 "properties": {"Node name for S&R": "KSampler"},
                 "widgets_values": [958540525371069, "randomize", 20, 8, "euler", "normal", 1]},
                {"id": 8, "type": "VAEDecode", "pos": [1209, 188], "size": {"0": 210, "1": 46}, "flags": {}, "order": 5,
                 "mode": 0, "inputs": [{"name": "samples", "type": "LATENT", "link": 7},
                                       {"name": "vae", "type": "VAE", "link": 8}],
                 "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": [9], "slot_index": 0}],
                 "properties": {"Node name for S&R": "VAEDecode"}},
                {"id": 4, "type": "CheckpointLoaderSimple", "pos": [26, 474], "size": {"0": 315, "1": 98}, "flags": {},
                 "order": 1, "mode": 0, "outputs": [{"name": "MODEL", "type": "MODEL", "links": [1], "slot_index": 0},
                                                    {"name": "CLIP", "type": "CLIP", "links": [3, 5], "slot_index": 1},
                                                    {"name": "VAE", "type": "VAE", "links": [8], "slot_index": 2}],
                 "properties": {"Node name for S&R": "CheckpointLoaderSimple"},
                 "widgets_values": ["anithing_v11Pruned.safetensors"]},
                {"id": 7, "type": "CLIPTextEncode", "pos": [413, 389],
                 "size": {"0": 425.27801513671875, "1": 180.6060791015625}, "flags": {}, "order": 3, "mode": 0,
                 "inputs": [{"name": "clip", "type": "CLIP", "link": 5}],
                 "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [6], "slot_index": 0}],
                 "properties": {"Node name for S&R": "CLIPTextEncode"}, "widgets_values": [f"{negativ_prompt}"]},
                {"id": 9, "type": "SaveImage", "pos": [1451, 189], "size": {"0": 210, "1": 270}, "flags": {},
                 "order": 6, "mode": 0, "inputs": [{"name": "images", "type": "IMAGE", "link": 9}], "properties": {},
                 "widgets_values": ["ComfyUI"]}, {"id": 6, "type": "CLIPTextEncode", "pos": [415, 186],
                                                  "size": {"0": 422.84503173828125, "1": 164.31304931640625},
                                                  "flags": {}, "order": 2, "mode": 0,
                                                  "inputs": [{"name": "clip", "type": "CLIP", "link": 3}], "outputs": [
                        {"name": "CONDITIONING", "type": "CONDITIONING", "links": [4], "slot_index": 0}],
                                                  "properties": {"Node name for S&R": "CLIPTextEncode"},
                                                  "widgets_values": [f"{prompt}"]}],
                         "links": [[1, 4, 0, 3, 0, "MODEL"], [2, 5, 0, 3, 3, "LATENT"], [3, 4, 1, 6, 0, "CLIP"],
                                   [4, 6, 0, 3, 1, "CONDITIONING"], [5, 4, 1, 7, 0, "CLIP"],
                                   [6, 7, 0, 3, 2, "CONDITIONING"], [7, 3, 0, 8, 0, "LATENT"], [8, 4, 2, 8, 1, "VAE"],
                                   [9, 8, 0, 9, 0, "IMAGE"]], "groups": [], "config": {}, "extra": {}, "version": 0.4,
                         "widget_idx_map": {"3": {"seed": 0, "sampler_name": 4, "scheduler": 5}}}}}
    })
    return p.text

def get_picture(id):
    t =True
    while t==True:
        a = requests.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
        if a.content != "":
            t=False
    a = requests.get(f"http://185.234.229.106:8130/view?filename={id}_00001_.png&subfolder=&type=output")
    with open(f'src//data//photos//{id}_new.png', 'wb') as target:
            target.write(a.content)

#http://185.234.229.106:8130/view?filename=BE1NB9OP_00001_.png&subfolder=&type=output&rand=0.5256054942787456


if __name__ == "__main__":
    pass
    ###p = requests.get("http://185.234.229.106:8130/view?filename=ComfyUI_00105_.png&type=output&subfolder=")
    #with open('', 'wb') as target:
    #    a = requests.get("http://185.234.229.106:8130/view?filename=user723456_00001_.png&type=output&subfolder=")
    #    target.write(a.content)


    #p = requests.post("http://185.234.229.106:8130/prompt", json={
    #       "client_id": "85fa01ab562c4d92929b2674bf512aea", "prompt": {"3": {
    #       "inputs": {"seed": 958540525371069, "steps": 20, "cfg": 8, "sampler_name": "euler", "scheduler": "normal",
    #                  "denoise": 1, "model": ["4", 0], "positive": ["6", 0], "negative": ["7", 0],
    #                  "latent_image": ["5", 0]}, "class_type": "KSampler", "_meta": {"title": "KSampler"}},
    #       "4": {"inputs": {"ckpt_name": "anithing_v11Pruned.safetensors"}, "class_type": "CheckpointLoaderSimple",
    #       "_meta": {"title": "Load Checkpoint"}},
    #       "5": {"inputs": {"width": 768, "height": 1024, "batch_size": 1},
    #                                                     "class_type": "EmptyLatentImage",
    #                                                     "_meta": {"title": "Empty Latent Image"}},
    #       "6": {"inputs": {"text": f"кот в бассейне", "clip": ["4", 1]}, "class_type": "CLIPTextEncode",
    #       "_meta": {"title": "CLIP Text Encode (Prompt)"}},
    #       "7": {"inputs": {"text": f"стол", "clip": ["4", 1]}, "class_type": "CLIPTextEncode", "_meta": {"title": "CLIP Text Encode (Prompt)"}},
    #       "8": {"inputs": {"samples": ["3", 0],
    #                                                                                 "vae": ["4", 2]},
    #                                                                      "class_type": "VAEDecode",
    #                                                                      "_meta": {"title": "VAE Decode"}}, "9": {
    #           "inputs": {"filename_prefix": "Кот2.0", "images": ["8", 0]}, "class_type": "SaveImage",
    #           "_meta": {"title": "Save Image"}}}, "extra_data": {"extra_pnginfo": {
    #       "workflow": {"last_node_id": 9, "last_link_id": 9, "nodes": [
    #           {"id": 5, "type": "EmptyLatentImage", "pos": [473, 609], "size": {"0": 315, "1": 106}, "flags": {},
    #            "order": 0, "mode": 0,
    #            "outputs": [{"name": "LATENT", "type": "LATENT", "links": [2], "slot_index": 0}],
    #            "properties": {"Node name for S&R": "EmptyLatentImage"}, "widgets_values": [512, 512, 1]},
    #           {"id": 3, "type": "KSampler", "pos": [863, 186], "size": {"0": 315, "1": 262}, "flags": {}, "order": 4,
    #            "mode": 0, "inputs": [{"name": "model", "type": "MODEL", "link": 1},
    #                                  {"name": "positive", "type": "CONDITIONING", "link": 4},
    #                                  {"name": "negative", "type": "CONDITIONING", "link": 6},
    #                                  {"name": "latent_image", "type": "LATENT", "link": 2}],
    #            "outputs": [{"name": "LATENT", "type": "LATENT", "links": [7], "slot_index": 0}],
    #            "properties": {"Node name for S&R": "KSampler"},
    #            "widgets_values": [958540525371069, "randomize", 20, 8, "euler", "normal", 1]},
    #           {"id": 8, "type": "VAEDecode", "pos": [1209, 188], "size": {"0": 210, "1": 46}, "flags": {}, "order": 5,
    #            "mode": 0, "inputs": [{"name": "samples", "type": "LATENT", "link": 7},
    #                                  {"name": "vae", "type": "VAE", "link": 8}],
    #            "outputs": [{"name": "IMAGE", "type": "IMAGE", "links": [9], "slot_index": 0}],
    #            "properties": {"Node name for S&R": "VAEDecode"}},
    #           {"id": 4, "type": "CheckpointLoaderSimple", "pos": [26, 474], "size": {"0": 315, "1": 98}, "flags": {},
    #            "order": 1, "mode": 0, "outputs": [{"name": "MODEL", "type": "MODEL", "links": [1], "slot_index": 0},
    #                                               {"name": "CLIP", "type": "CLIP", "links": [3, 5], "slot_index": 1},
    #                                               {"name": "VAE", "type": "VAE", "links": [8], "slot_index": 2}],
    #            "properties": {"Node name for S&R": "CheckpointLoaderSimple"},
    #            "widgets_values": ["anithing_v11Pruned.safetensors"]},
    #           {"id": 7, "type": "CLIPTextEncode", "pos": [413, 389],
    #            "size": {"0": 425.27801513671875, "1": 180.6060791015625}, "flags": {}, "order": 3, "mode": 0,
    #            "inputs": [{"name": "clip", "type": "CLIP", "link": 5}],
    #            "outputs": [{"name": "CONDITIONING", "type": "CONDITIONING", "links": [6], "slot_index": 0}],
    #            "properties": {"Node name for S&R": "CLIPTextEncode"}, "widgets_values": ["jkl"]},
    #           {"id": 9, "type": "SaveImage", "pos": [1451, 189], "size": {"0": 210, "1": 270}, "flags": {},
    #            "order": 6, "mode": 0, "inputs": [{"name": "images", "type": "IMAGE", "link": 9}], "properties": {},
    #            "widgets_values": ["ComfyUI"]}, {"id": 6, "type": "CLIPTextEncode", "pos": [415, 186],
    #                                             "size": {"0": 422.84503173828125, "1": 164.31304931640625},
    #                                             "flags": {}, "order": 2, "mode": 0,
    #                                             "inputs": [{"name": "clip", "type": "CLIP", "link": 3}], "outputs": [
    #                   {"name": "CONDITIONING", "type": "CONDITIONING", "links": [4], "slot_index": 0}],
    #                                             "properties": {"Node name for S&R": "CLIPTextEncode"},
    #                                             "widgets_values": ["jkl\n"]}],
    #                    "links": [[1, 4, 0, 3, 0, "MODEL"], [2, 5, 0, 3, 3, "LATENT"], [3, 4, 1, 6, 0, "CLIP"],
    #                              [4, 6, 0, 3, 1, "CONDITIONING"], [5, 4, 1, 7, 0, "CLIP"],
    #                              [6, 7, 0, 3, 2, "CONDITIONING"], [7, 3, 0, 8, 0, "LATENT"], [8, 4, 2, 8, 1, "VAE"],
    #                              [9, 8, 0, 9, 0, "IMAGE"]], "groups": [], "config": {}, "extra": {}, "version": 0.4,
    #                    "widget_idx_map": {"3": {"seed": 0, "sampler_name": 4, "scheduler": 5}}}}}
    #})