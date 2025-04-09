# The Best Implementation for Ryzen AI

<div align="center">
<img src="https://github.com/R300-AI/AMD-ryzen-demo/blob/main/docs/images/chipset.png" width=360"/>
</div>

## Requirements
* A **Ryzen AI PC** with **Windows OS**.
* Download and Install [Anaconda](https://www.anaconda.com/download) and run `conda init` command in terminal.
* [Install AMD Drivers for Radeon GPU](https://www.amd.com/en/support/download/drivers.html)
* [Install AMD Drivers for HX NPU](https://ryzenai.docs.amd.com/en/latest/inst.html) 

## How to Use This?
  ```bash
  $ git clone https://github.com/R300-AI/AMD-ryzen-demo.git
  $ cd AMD-ryzen-demo
  $ pip install -r requirements.txt
  ```

### ONNX Benchmarks
  ```bash
  $ python onnx_benchmark.py --onnx_model ./models/yolov8n.onnx --device cpu
  ```
  > * **Ryzen AI 9 Supported Device**: `cpu`, `igpu`, `npu`
