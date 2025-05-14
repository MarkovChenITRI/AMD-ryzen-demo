# The Best Implementation for Ryzen AI

AMD Ryzen是一個專門為個人助理打造的AI Processor ，其最大的賣點在於其透過Infinity Fabric晶片互連技術，將CPU, GPU及NPU整合於單一張晶片中(APU)，使它們能透過[共享同一個內存池(Unified Memory)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/how-to/unified_memory.html)來將資料傳輸效率最佳化，適合用於部署Hybrid Execution的應用。

其複雜的系統成分也意味著它的軟體支援性將成為應用開發上的一大挑戰。因此，這個Repository的目的便是在於持續追蹤AMD Ryzen官方軟體支援的資訊，為一般**AI研究人員**或**早期概念驗證的開發者**提供最新且完整的軟體安裝流程。這些軟體主要是使用[Windows11作業系統](https://www.microsoft.com/zh-tw/software-download/windows11)(*Linux仍在實驗階段*)，且必須透過[Conda](https://www.anaconda.com/docs/getting-started/miniconda/main)來布置這些軟體的虛擬環境。除此之外，我們也特別針對一些常見的Python Execution提供範例模板，以此加速Ryzen AI生態的應用創新。

您可以透過點擊以下連結來播放並學習Ryzen AI基礎知識的介紹影片(大約半小時)：

<div align="center">
  
[![AMD Ryzen™ AI Tutorials](https://i.ytimg.com/pl_c/PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz/studio_square_thumbnail.jpg?sqp=CMrSkMEG-oaymwEICKoDEPABSFqi85f_AwYI35KvvwY=&rs=AOn4CLCHX3cOmhUavu1XSE7nTYgZWBf1MA)](https://www.youtube.com/playlist?list=PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz)

</div>

### 將Ryzen AI配置為工作站

AMD Ryzen APU雖然已經搭載了完整的internal GPU(=iGPU)及NPU，但是這些處理器僅支援與"推論"有關的程序，針對"訓練"方面的工作仍只能依靠內建的CPU。或者，您也可以透過主機板的外部擴充卡槽(如：[Radeon Graphics Cards](https://www.amd.com/en/products/graphics/desktops/radeon.html))來增強本機在訓練模型、微調神經網路參數的能力。

## Installation

<div align="center">
<table><thead>
  <tr>
    <th>Task</th>
    <th colspan="2">Inference/Training</th>
    <th colspan="5">Inference only</th>
  </tr></thead>
<tbody>
  <tr>
    <td>Tools</td>
    <td colspan="4">Jupyter/ VS Code...etc</td>
    <td colspan="3">
      <a href="https://github.com/amd/gaia"><b>GAIA</b></a> 
    </td>
  </tr>
  <tr>
    <td>Usage</td>
    <td>All</td>
    <td colspan="3">General CNNs/ Transformers</td>
    <td colspan="3">LLMs</td>
  </tr>
  <tr>
    <td>Runtime</td>
    <td colspan="6">Python==3.10&nbsp;&nbsp;&nbsp;&nbsp;</td>
    <td rowspan="2">C++</td>
  </tr>
  <tr>
    <td>Framework</td>
    <td>
      <a href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html"><b>Torch/TF/JAX</b></a> 
    </td>
    <td colspan="3">
      <a href="https://github.com/onnx/digestai"><b>ONNX with DigestAI</b></a> 
    </td>
    <td colspan="2">
      <a href="https://github.com/onnx/turnkeyml/blob/main/docs/lemonade/README.md"><b>Lemonade CLI</b></a> 
    </td>
  </tr>
  <tr>
    <td>Software</td>
    <td>
      <a href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html"><b>ROCm</b></a> 
    </td>
    <td colspan="6">
      <a href="https://ryzenai.docs.amd.com/en/latest/inst.html"><b>Ryzen AI Software (包括下列Provider)</b></a> 
    </td>
  </tr>
  <tr>
    <td>Execution Provider</td>
    <td>
      <a href="https://www.amd.com/en/support/download/drivers.html"><b>Drivers</b></a>
    </td>
    <td>--</td>
    <td>DirectML</td>
    <td>VitisAI</td>
    <td colspan="3">OGA</td>
  </tr>
  <tr>
    <td>Processor Type</td>
    <td>external GPUs</td>
    <td>CPU</td>
    <td>iGPU</td>
    <td>NPU</td>
    <td colspan="3">Hybrid</td>
  </tr>
</tbody>
</table>
</div>

上方提供的表格為AMD官方提供的資源清單及應用方式，請依照自己的Processor及Usage識別相對應所需使用的軟體，並依照由下而上的順序逐步進行安裝。

## How to Use This?

### **external GPUs (Radeon Series)**

ROCm為AMD Radeon系列的API與軟體，開發人員可以利用這些工具調度GPUs中的處理單元，用於加速執行可平行化的運算工作。

### *internal CPU, GPU and NPU*

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
