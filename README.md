# The Best Implementation for Ryzen AI

AMD Ryzen是一個專門為個人助理打造的AI Processor ，其最大的賣點在於其透過Infinity Fabric晶片互連技術，將CPU, GPU及NPU整合於單一張晶片中(APU)，使它們能透過[共享同一個內存池(Unified Memory)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/how-to/unified_memory.html)來將資料傳輸效率最佳化，適合用於部署Hybrid Execution的應用。

其複雜的系統成分也意味著它的軟體支援性將成為應用開發上的一大挑戰。因此，這個Repository的目的便是在於持續追蹤AMD Ryzen官方軟體支援的資訊，為一般**AI研究人員**或**早期概念驗證的開發者**提供最新且完整的軟體安裝流程。這些軟體主要是使用Windows作業系統(*Linux仍在實驗階段*)，且必須透過[Conda](https://www.anaconda.com/docs/getting-started/miniconda/main)來布置這些軟體的虛擬環境。除此之外，我們也特別針對一些常見的Python Execution提供範例模板，加速Ryzen AI生態的應用創新。

您可以先透過以下這些內容來學習有關Ryzen AI的基礎知識：

[![AMD Ryzen™ AI Tutorials](https://i.ytimg.com/pl_c/PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz/studio_square_thumbnail.jpg?sqp=CJysi8EG-oaymwEICKoDEPABSFqi85f_AwYI35KvvwY=&rs=AOn4CLAX5o3ahshTXAgTxaZKRKJYxJ9TTw)](https://www.youtube.com/playlist?list=PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz)

### 將Ryzen AI配置為工作站

AMD Ryzen APU雖然已經搭載了完整的internal GPU(=iGPU)及NPU，但是這些處理器僅支援與"推論"有關的流程，針對"訓練"方面的工作只能依靠其內建的CPU。或者，您也可以透過外部擴充槽圖形卡(如：[Radeon](https://www.amd.com/en/products/graphics/desktops/radeon.html))，以此增強本機在訓練模型、微調神經網路參數的能力。

## Requirements

* GAIA: 7 llm can be used.
* Digest AI: model analysis (ONNX from HuggingFace)
* Lemonade: a cli for llm, BENCHMARK
* Ryzen AI: ONNX and Quantize

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
