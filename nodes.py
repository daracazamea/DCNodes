import time

class StartTimerPassThrough:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_model": ("MODEL",),
                "trigger": ("FLOAT",),  # add a dummy input to force change
            }
        }
    
    RETURN_TYPES = ("MODEL", "float",)
    RETURN_NAMES = ("model", "time",)
    CATEGORY = "DCNodes"
    FUNCTION = "start"
    
    def start(self, input_model, trigger):
        current_time = time.time()
        return (input_model, current_time)

class GetGenerationTime:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "startTime": ("float",),  
                "image":("IMAGE",)
            }
        }
    
    RETURN_TYPES = ("IMAGE","STRING",)
    RETURN_NAMES = ("image", "generation_time",)
    CATEGORY = "DCNodes"
    FUNCTION = "get_time"
    
    # Option 2: Using an explicit parameter (uncomment if you prefer this style)
    def get_time(self, startTime, image):
        current_time = time.time()
        if startTime is None:
            return ("Start time not set",)
        
        elapsed = round(current_time - startTime, 3)
        return (image, f"{elapsed} seconds",)

class ManualTrigger:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
        }

    RETURN_TYPES = ("FLOAT",)
    RETURN_NAMES = ("trigger",)
    CATEGORY = "DCNodes"
    FUNCTION = "trigger"

    def trigger(self):
        # Generate a random float between 0 and 100000 (like a seed)
        rand_float = random.uniform(0, 100000)
        print(f"🎲 ManualTrigger emitted: {rand_float}")
        return (rand_float,)

class FluxResolutionPicker:
    @classmethod
    def INPUT_TYPES(s):
        resolutions = [
            "1:1 1024 x 1024",
            "3:2 1216 x 832",
            "4:3 1152 x 896",
            "16:9 1344 x 768",
            "21:9 1536 x 640",
            "Custom"
        ]
        return {
            "required": {
                "resolution": (resolutions,),
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "vertical": ("BOOLEAN", {"default": False}),
                "half_res": ("BOOLEAN", {"default": False}),
            },
        }
        

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "pick_resolution"
    CATEGORY = "DCNodes"

    def pick_resolution(self, resolution, custom_width, custom_height, vertical, half_res):
        preset_map = {
            "1:1 1024 x 1024": (1024, 1024),
            "3:2 1216 x 832": (1216, 832),
            "4:3 1152 x 896": (1152, 896),
            "16:9 1344 x 768": (1344, 768),
            "21:9 1536 x 640": (1536, 640),
        }

        if resolution == "Custom":
            width, height = custom_width, custom_height
        else:
            width, height = preset_map.get(resolution, (1024, 1024))

        if vertical:
            width, height = height, width

        if half_res:
            width = max(1, width // 2)
            height = max(1, height // 2)

        return (width, height)

class SDXLResolutionPicker:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": ([
                    "SDXL Native (1536x1024)",
                    "Standard (1216x832)",
                    "Square (1024x1024)",
                    "Portrait (896x1344)",
                    "Landscape (1344x768)",
                    "Manual"
                ],),
                "custom_width": ("INT", {"default": 1024, "min": 64, "max": 4096}),
                "custom_height": ("INT", {"default": 1024, "min": 64, "max": 4096}),
                "vertical": ("BOOLEAN", {"default": False}),
                "half_res": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "pick_resolution"
    CATEGORY = "DCNodes"

    def pick_resolution(self, preset, custom_width, custom_height, vertical, half_res):
        presets = {
            "SDXL Native (1536x1024)": (1536, 1024),
            "Standard (1216x832)": (1216, 832),
            "Square (1024x1024)": (1024, 1024),
            "Portrait (896x1344)": (896, 1344),
            "Landscape (1344x768)": (1344, 768),
        }

        if preset in presets:
            width, height = presets[preset]
        else:
            width, height = custom_width, custom_height

        # Apply vertical flip
        if vertical:
            width, height = height, width

        # Apply half resolution
        if half_res:
            width = max(64, width // 2)
            height = max(64, height // 2)

        return (width, height)


NODE_CLASS_MAPPINGS = {
    "StartTimerPassThrough": StartTimerPassThrough,
    "GetGenerationTime": GetGenerationTime,
    "ManualTrigger": ManualTrigger,
    "FluxResolutionPicker": FluxResolutionPicker,
    "SDXLResolutionPicker": SDXLResolutionPicker,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StartTimerPassThrough": "Start Timer (Pass-Through)",
    "GetGenerationTime": "Get Generation Time",
    "ManualTrigger": "Manual Trigger",
    "FluxResolutionPicker": "Flux: Resolution Picker",
    "SDXLResolutionPicker": "SDXL: Resolution Picker",
}


