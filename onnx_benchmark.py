import onnxruntime as ort
import numpy as np
import time, argparse

warnings.simplefilter('ignore')

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
                               providers=[required_providers[args.device]], 
                               provider_options=[{"device_id": "0"}])

inputs_details = session.get_inputs()
inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)

t = time.time()
for _ in range(1000):
    outputs = session.run(None, {inputs_details[0].name: inputs})

# Print the Inference Speed
print("Inference Speed:", (time.time() - t) / 1000, 'ms')



interpreter = neuronrt.Interpreter(model_path=, device = )
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Forward Propagation
inputs = np.random.rand(*input_details[0]['shape']).astype(input_details[0]['dtype'])

t1 = time.time()
interpreter.set_tensor(input_details[0]['index'], inputs)
t2 = time.time()
for _ in range(args.iteration):
  interpreter.invoke()
  
t3 = time.time()
outputs = interpreter.get_tensor(output_details[0]['index'])

print(f'Set tensor speed: {(t2 - t1) * 1000} ms')
print(f'Inference speed: {(t3 - t2) * 1000 / args.iteration} ms')
print(f'Get tensor speed: {(time.time() - t3) * 1000} ms')
