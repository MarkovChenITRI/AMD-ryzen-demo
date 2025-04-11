import time, argparse
import numpy as np
from utils.benchmarks import CPUExecutionProvider, iGPUExecutionProvider, NPUExecutionProvicer
from utils.quantization import NPUQuantizer

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--onnx_model", type=str, help="Path to .onnx")
parser.add_argument("-d", "--device", type=str, default='cpu', choices = ['cpu', 'igpu', 'npu'], help="")
parser.add_argument("-t", "--iteration", default=1000, type=int, help="Test How Many Times?")
args = parser.parse_args()

if args.device == 'cpu':
    cpu_session = CPUExecutionProvider(args.onnx_model)

    inputs = np.random.rand(*cpu_session.get_inputs()[0].shape).astype(np.float32)
    for _ in range(args.iteration):
        start = time.time()
        outputs = cpu_session.run(None, {cpu_session.get_inputs()[0].name: inputs})
        end = time.time()
    inference_time = np.round((end - start) * 1000, 2)

    print('----------------------------------------')
    print('CPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')

elif args.device == 'igpu':
    dml_session = iGPUExecutionProvider(args.onnx_model)

    inputs = np.random.rand(*dml_session.get_inputs()[0].shape).astype(np.float32)
    for _ in range(args.iteration):
        start = time.time()
        outputs = dml_session.run(None, {dml_session.get_inputs()[0].name: inputs})
        end = time.time()
    inference_time = np.round((end - start) / args.iteration * 1000, 2)

    print('----------------------------------------')
    print('GPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')

elif args.device == 'npu':
    onnx_model_path = NPUQuantizer(args.onnx_model)
    npu_session = NPUExecutionProvicer(onnx_model_path)

    inputs = np.random.rand(*npu_session.get_inputs()[0].shape).astype(np.float32)
    for _ in range(args.iteration):
        start = time.time()
        outputs = npu_session.run(None, {npu_session.get_inputs()[0].name: inputs})
        end = time.time()
    inference_time = np.round((end - start) * 1000, 2)
        
    print('----------------------------------------')
    print('NPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')