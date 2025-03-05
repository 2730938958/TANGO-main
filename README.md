# TANGO

给定一个reference video和speech audio，TANGO可以产生手势同步的高保真视频

huya镜像：registry-haiyan.local.huya.com/machine-learn/fengweiyan_tango:tango_v1.0

# ⚒️ Installation

## Clone the repository

```shell
cd TANGO-main
git clone https://github.com/justinjohn0306/Wav2Lip.git
git clone https://github.com/dajes/frame-interpolation-pytorch.git
hai run2 python3 hfdown.py https://huggingface.co/google-bert/bert-base-uncased
hai run2 python3 hfdown.py https://huggingface.co/facebook/wav2vec2-base-960h
```

# 🚀 Training and Inference

## Inference

Here is the command for running inference scripts under the path `<your root>/TANGO/`, it will take around 3 min to generate two 8s vidoes. You can visualize by directly check the video or check the result .npz files via blender using our blender addon in [EMAGE](https://github.com/PantoMatrix/PantoMatrix).

_Necessary checkpoints and pre-computed graphs will be automatically downloaded during the first run. Please ensure that at least 35GB of disk space is available._

```shell
python app.py
```

### Create the graph for custom character

```shell
python create_graph.py
```

# Copyright Information

We thanks the open-source project [Wav2Lip](https://github.com/Rudrabha/Wav2Lip), [FiLM](https://github.com/caffeinism/FiLM-pytorch), [SMPLerX](https://github.com/caizhongang/SMPLer-X).

Check out our previous works for Co-Speech 3D motion Generation <a href="https://github.com/PantoMatrix/PantoMatrix">DisCo, BEAT, EMAGE</a>.

This project is only for research or education purposes, and not freely available for commercial use or redistribution. The srcipt is available only under the terms of the [Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/legalcode) (CC BY-NC 4.0) license.
