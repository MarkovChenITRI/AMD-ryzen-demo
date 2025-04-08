import onnxruntime as ort
import numpy as np
import time

# Check if DmlExecutionProvider is available
print(ort.get_available_providers())

session = ort.InferenceSession("../yolo11n.onnx", 
                               providers=['DmlExecutionProvider'], 
                               provider_options=[{"device_id": "0"}])

inputs_details = session.get_inputs()
inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)

t = time.time()
for _ in range(1000):
    outputs = session.run(None, {inputs_details[0].name: inputs})

# Print the Inference Speed
print("Inference Speed:", (time.time() - t) / 1000, 'ms')