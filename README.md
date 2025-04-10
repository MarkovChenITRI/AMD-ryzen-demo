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
  $ pip install -r requirements.txt
  ```

### ONNX Benchmarks

The ONNX benchmarks leverage different execution providers to drive various hardware components on Ryzen AI. These include CPU Execution Provider (EP) for Ryzen CPU, DirectML Execution Provider for Radeon iGPU, and Vitis IA Execution Provider for HX NPU. You can run the benchmark using the following command:
  
  ```bash
  $ python onnx_benchmark.py --onnx_model ./models/yolo11n.onnx --device cpu
  ```
  > Replace `./models/yolo11n.onnx` with your custom ONNX model and specify the desired device (`cpu`, `igpu`, or `npu`) to test performance on the corresponding hardware.
