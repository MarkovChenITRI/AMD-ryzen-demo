
from quark.onnx.quantization.config import Config, get_default_config, QuantizationConfig
from quark.onnx import ModelQuantizer
import quark

def NPUQuantizer(onnx_model_path, dynamic = False, fp16 = False, config_name="XINT8"):
    # parameters refer to : https://quark.docs.amd.com/latest/onnx/appendix_full_quant_config_features.html
    quant_config = get_default_config(config_name)
    config = Config(global_quant_config=quant_config)
    config.global_quant_config.extra_options["UseRandomData"] = True

    quantizer = ModelQuantizer(config)
    quantized_onnx_model_path = onnx_model_path.replace('.onnx', '.quark.onnx')
    quant_model = quantizer.quantize_model(model_input = onnx_model_path,
                                        model_output = quantized_onnx_model_path,
                                        calibration_data_path = None)
    return quantized_onnx_model_path