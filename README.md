# The Best Implementation for Ryzen AI

## Requirements
* A **Ryzen AI PC** with **Windows OS**.
* Download and Install [Anaconda](https://www.anaconda.com/download) and run `conda init` command in terminal.
* [Install AMD Drivers for Radeon GPU](https://www.amd.com/en/support/download/drivers.html)
* [Install AMD Drivers for HX NPU](https://ryzenai.docs.amd.com/en/latest/inst.html) 

## How to Use This?

<div align="center">
<img src="https://github.com/R300-AI/AMD-ryzen-demo/blob/main/docs/images/chipset.png" width=360"/>
</div>

Ryzen AI provides acceleration options for ONNX models using CPU, iGPU, and NPU, while other operations are executed on the Ryzen architecture. If you are interested in running your ONNX model on these chips, you can follow the instructions below to download this example repository and set up the necessary environment.
  
  ```bash
  $ git clone https://github.com/R300-AI/AMD-ryzen-demo.git
  $ cd AMD-ryzen-demo
  $ conda activate ryzen-ai-1.4.0    #created by AMD Ryzen AI Software
  $ pip install -r requirements.txt
  ```

### ONNX Benchmarks

The ONNX benchmarks use different execution providers to drive Ryzen AI hardware, including CPU Execution Provider (EP) for Zen CPU, DirectML Execution Provider for Radeon iGPU, and Vitis IA Execution Provider for HX NPU. Run the benchmark with the following command:
  
  ```bash
  $ python onnx_benchmark.py --onnx_model ./models/yolo11n.onnx --device cpu
  ```
  > `--device` options:
  > -  `cpu` (for DLA, G510/700 only)
  > -  `igpu` (for DLA, 1200 only)
  > -  `npu` (for VPU)

**【NOTE】** Replace `./models/yolo11n.onnx` with your ONNX model to test performance on the specified hardware.
