# The Best Implementation for Ryzen AI

AMD Ryzen是一個專門為個人助理打造的AI Processor ，其最大的賣點在於其透過Infinity Fabric晶片互連技術，將CPU, GPU及NPU整合於單一張晶片中(APU)，使它們能透過[共享同一個內存池(Unified Memory)](https://rocm.docs.amd.com/projects/HIP/en/docs-6.2.0/how-to/unified_memory.html)來將資料傳輸效率最佳化，適合用於部署Hybrid Execution的應用。

其複雜的系統成分也意味著它的軟體支援性將成為應用開發上的一大挑戰。因此，這個Repository的目的便是在於持續追蹤AMD Ryzen官方軟體支援的資訊，為一般**AI研究人員**或**早期概念驗證的開發者**提供最新且完整的軟體安裝流程。這些軟體主要是使用[Windows11作業系統](https://www.microsoft.com/zh-tw/software-download/windows11)(*Linux仍在實驗階段*)，且必須透過[Conda](https://www.anaconda.com/docs/getting-started/miniconda/main)來布置這些軟體的虛擬環境。除此之外，我們也特別針對一些常見的Python Execution提供範例模板，以此加速Ryzen AI生態的應用創新。

您可以透過點擊以下連結來播放並學習Ryzen AI基礎知識的介紹影片(大約半小時)：

<div align="center">
  
:point_right: [AMD Ryzen™ AI Tutorials](https://youtube.com/playlist?list=PLYw1WVX5aNHABNAfottruTY8oX2eFlzmz&si=RLDuVowcy-6znu3e)

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
    <td>Torch/TF/JAX</td>
    <td colspan="3">
      <a href="https://github.com/onnx/digestai"><b>ONNX with Digest AI</b></a> 
    </td>
    <td colspan="2">
      <a href="https://github.com/onnx/turnkeyml/blob/main/docs/lemonade/README.md"><b>Lemonade CLI</b></a> 
    </td>
  </tr>
  <tr>
    <td>Software</td>
    <td rowspan="2">
      <a href="https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html"><b>ROCm and Driver<br>(using WSL)</b></a> 
    </td>
    <td colspan="6">
      <a href="https://ryzenai.docs.amd.com/en/latest/inst.html"><b>Ryzen AI Software (包括下列Provider及Quark)</b></a> 
    </td>
  </tr>
  <tr>
    <td>Execution Provider</td>
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
> [!TIP]
> external GPUs目前僅支援Linux作業系統。因此，您需要額外透過[WSL](https://documentation.ubuntu.com/wsl/en/latest/howto/install-ubuntu-wsl2/)安裝Ubuntu24.04或其他可支援的系統版本，才能安裝與調用Driver與ROCm這些資源。

## How to Use This?

### **external GPUs (in WSL)**

ROCm為AMD Radeon系列的API與軟體，開發者可以利用這些工具調度GPUs中的運算單元，用於加速可平行化處理的運算工作。

這個軟體能夠支援一般的深度學習開發框架與C++/Python開發工具，讓開發者可以輕易地加速設計、訓練及調適AI模型的過程。為此，您可以依照下列這些文件來安裝它們，並在個別的開源社群瞭解這些框架的使用方法：

* 安裝深度學習框架 | [PyTorch](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/pytorch-install.html), [Tensorflow](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/tensorflow-install.html), [JAX](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/3rd-party/jax-install.html)
* 安裝程式開發工具     | [Jupyter (for Python)](https://jupyter.org/install), [VS Code](https://code.visualstudio.com/download)

### **CPU, GPU**

1. Ryzen AI處理器是透過ONNX解釋器來辨認模型的神經網路架構及運算參數，所以得先利用PyTorch、Tensorflow或JAX將設計好的模型輸出成ONNX格式(Ryzen AI Software 1.4.0建議輸出的opset版本為13)，才能將其部署到GPU及NPU上做推論。
   > 請先下載這個範例程式庫，在`./models`中已經有預先輸出一些`.onnx`檔案，您可以透過[Netron](https://github.com/lutzroeder/netron)或[Digest AI](https://github.com/onnx/digestai)來預覽模型的成分。
   > ```bash
   > $ git clone https://github.com/R300-AI/AMD-ryzen-demo.git && cd AMD-ryzen-demo
   > $ conda activate ryzen-ai-1.4.0      # 這個環境會與Ryzen AI software一起被安裝到您的主機.
   > $ pip install -r requirements.txt
   > ```

2. 接下來展示如何使用原生的ONNX Runtime將模型委託至指定的處理器做加速推論。
   > `--provider`的選項分別為`CPUExecutionProvider`、`DmlExecutionProvider`及`VitisAIExecutionProvider`
   > ```bash
   > $ python onnx_benchmark.py --onnx_model ./models/yolo11n.onnx --provider CPUExecutionProvider
   > ```

### **NPU**
