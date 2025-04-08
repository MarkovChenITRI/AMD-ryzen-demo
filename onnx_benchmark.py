import onnxruntime as ort
import numpy as np
import time, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--onnx_model", type=str, help="Path to .tflite")
parser.add_argument("-d", "--device", type=str, default='cpu', choices = ['cpu', 'igpu', 'npu'], help="")
parser.add_argument("-t", "--iteration", default=10, type=int, help="Test How Many Times?")
args = parser.parse_args()

# Check if VitisAIExecutionProvider and DmlExecutionProvider is available
required_providers = {'cpu': 'CPUExecutionProvider', 
                      'igpu': 'DmlExecutionProvider',
                      'npu': 'VitisAIExecutionProvider'
                      }

for provider in required_providers.values():
    if provider not in ort.get_available_providers():
        raise RuntimeError(f"Required provider '{provider}' is not available. Please install the Ryzen AI Software")

session = ort.InferenceSession(args.onnx_model, 
                               providers=[required_providers[args.device]]
                               )

inputs_details = session.get_inputs()
inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)

t = time.time()
for _ in range(args.iteration):
    outputs = session.run(None, {inputs_details[0].name: inputs})

print("Inference Speed:", (time.time() - t) / 1000, 'ms')
