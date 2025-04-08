import time
import os
import subprocess
import torch
import torch.nn as nn
import onnxruntime
import numpy as np

import time, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--onnx_model", type=str, help="Path to .onnx")
parser.add_argument("-d", "--device", type=str, default='cpu', choices = ['cpu', 'igpu', 'npu'], help="")
parser.add_argument("-t", "--iteration", default=100, type=int, help="Test How Many Times?")
args = parser.parse_args()

# "yolov8m.onnx"
onnx_model_path = args.onnx_model
if args.device == 'cpu':
    cpu_options = onnxruntime.SessionOptions()
    cpu_session = onnxruntime.InferenceSession(
        onnx_model_path,
        providers = ['CPUExecutionProvider'],
        sess_options=cpu_options,
    )

    inputs_details = cpu_session.get_inputs()
    print(inputs_details[0].shape)
    inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)
    start = time.time()
    for _ in range(args.iteration):
        outputs = cpu_session.run(None, {cpu_session.get_inputs()[0].name: inputs})
    end = time.time()
    inference_time = np.round((end - start) / args.iteration * 1000, 2)

    print('----------------------------------------')
    print('CPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')

elif args.device == 'igpu':
    dml_options = onnxruntime.SessionOptions()
    dml_session = onnxruntime.InferenceSession(
        onnx_model_path,
        providers = ['DmlExecutionProvider'],
        provider_options = [{"device_id": "0"}]
    )

    inputs_details = dml_session.get_inputs()
    inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)
    start = time.time()
    for _ in range(args.iteration):
        outputs = dml_session.run(None, {dml_session.get_inputs()[0].name: inputs})
    end = time.time()
    inference_time = np.round((end - start) / args.iteration * 1000, 2)

    print('----------------------------------------')
    print('GPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')

elif args.device == 'npu':
    command = r'pnputil /enum-devices /bus PCI /deviceids '
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    apu_type = ''
    if 'PCI\\VEN_1022&DEV_1502&REV_00' in stdout.decode('utf-8', errors='ignore'): apu_type = 'PHX/HPT'
    if 'PCI\\VEN_1022&DEV_17F0&REV_00' in stdout.decode('utf-8', errors='ignore'): apu_type = 'STX'
    if 'PCI\\VEN_1022&DEV_17F0&REV_10' in stdout.decode('utf-8', errors='ignore'): apu_type = 'STX'
    if 'PCI\\VEN_1022&DEV_17F0&REV_11' in stdout.decode('utf-8', errors='ignore'): apu_type = 'STX'

    print(f"APU Type: {apu_type}")
    install_dir = os.environ['RYZEN_AI_INSTALLATION_PATH']
    match apu_type:
        case 'PHX/HPT':
            print("Setting environment for PHX/HPT")
            os.environ['XLNX_VART_FIRMWARE']= os.path.join(install_dir, 'voe-4.0-win_amd64', 'xclbins', 'phoenix', '1x4.xclbin')
            os.environ['NUM_OF_DPU_RUNNERS']='1'
            os.environ['XLNX_TARGET_NAME']='AMD_AIE2_Nx4_Overlay'
        case 'STX':
            print("Setting environment for STX")
            os.environ['XLNX_VART_FIRMWARE']= os.path.join(install_dir, 'voe-4.0-win_amd64', 'xclbins', 'strix', 'AMD_AIE2P_Nx4_Overlay.xclbin')
            os.environ['NUM_OF_DPU_RUNNERS']='1'
            os.environ['XLNX_TARGET_NAME']='AMD_AIE2_Nx4_Overlay'
        case _:
            print("Unrecognized APU type. Exiting.")
            exit()
    print('XLNX_VART_FIRMWARE=', os.environ['XLNX_VART_FIRMWARE'])
    print('NUM_OF_DPU_RUNNERS=', os.environ['NUM_OF_DPU_RUNNERS'])
    print('XLNX_TARGET_NAME=', os.environ['XLNX_TARGET_NAME'])

    # Point to the config file path used for the VitisAI Execution Provider
    config_file_path = "./vaip_config.json"
    provider_options = [{
                'config_file': config_file_path,
                'ai_analyzer_visualization': True,
                'ai_analyzer_profiling': True,
            }]

    npu_session = onnxruntime.InferenceSession(
        onnx_model_path,
        providers = ['VitisAIExecutionProvider'],
        provider_options = provider_options
    )

    inputs_details = npu_session.get_inputs()
    inputs = np.random.rand(*inputs_details[0].shape).astype(np.float32)
    start = time.time()
    for _ in range(args.iteration):
        outputs = npu_session.run(None, {npu_session.get_inputs()[0].name: inputs})
    end = time.time()
    inference_time = np.round((end - start) / args.iteration * 1000, 2)
        
    print('----------------------------------------')
    print('NPU Inference time: ' + str(inference_time) + " ms")
    print('----------------------------------------')