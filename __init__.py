from .nodes import StartTimerPassThrough, GetGenerationTime, ManualTrigger, FluxResolutionPicker, SDXLResolutionPicker

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


print("✅ comfyui_DCNodes nodes loaded")
