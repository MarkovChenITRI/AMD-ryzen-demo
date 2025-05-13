# The Best Implementation for Ryzen AI

## For Beginner

AMD Ryzen是一個專門為個人 PC打造的AI Processor ，其最大的賣點在於其透過Infinity Fabric晶片互連技術，將CPU, GPU及NPU整合於單一張晶片中(APU)，使它們能透過[共享同一個內存池(Unified Memory)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/how-to/unified_memory.html)來將資料傳輸的效率最佳化，適合需要同時混合CPU, GPU及NPU Execution的應用。

意味著它

專為Python API
Conda是必須的

[AMD Ryzen™ AI Tutorials](https://youtube.com/playlist?list=PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz&si=zigYfA3XEIu2OMmT)


* GAIA: 7 llm can be used.
* Digest AI: model analysis (ONNX from HuggingFace)
* Lemonade: a cli for llm, BENCHMARK
* Ryzen AI: ONNX and Quantize

## Requirements
* A **Ryzen AI PC** with **Windows OS**.
* Download and Install [Anaconda](https://www.anaconda.com/download) and run `conda init` command in terminal.
* [Install AMD Drivers for Zen CPU](https://www.amd.com/zh-tw/developer/zendnn.html)
* [Install AMD Drivers for Radeon GPU](https://www.amd.com/en/support/download/drivers.html)
* [Install AMD Drivers for HX NPU](https://ryzenai.docs.amd.com/en/latest/inst.html) 

## How to Use This?

<div align="center">
<img src="https://github.com/R300-AI/AMD-ryzen-demo/blob/main/docs/images/chipset.png" width=360"/>
</div>

Ryzen AI provides acceleration options for ONNX models using CPU, iGPU, and NPU, while other operations are executed on the Ryzen architecture. If you are interested in running your ONNX model on these chips, you can follow the instructions below to download this example repository and set up the necessary environment.
  
  ```bash
  $ git clone https://github.com/R300-AI/AMD-ryzen-demo.git && cd AMD-ryzen-demo
  $ conda activate ryzen-ai-1.4.0    #created by AMD Ryzen AI Software
  $ pip install -r requirements.txt
  ```

### ONNX Benchmarks

The ONNX benchmarks use different execution providers to drive Ryzen AI hardware, including CPU Execution Provider (EP) for Zen CPU, DirectML Execution Provider for Radeon iGPU, and Vitis IA Execution Provider for HX NPU. Run the benchmark with the following command:
  
  ```bash
  $ python onnx_benchmark.py --onnx_model ./models/yolo11n.onnx --device cpu
  ```
  > `--device` options:
  > -  `cpu` (for Zen CPU)
  > -  `igpu` (for Radeon iGPU)
  > -  `npu` (for XDNA NPU)

**【NOTE】** Replace `./models/yolo11n.onnx` with your ONNX model to test performance on the specified hardware.
**【NOTE】** It is recommended to use ONNX models with `opset_version=13`.
