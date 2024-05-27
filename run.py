from main import ImageEditor


lama_config = str(Path(__file__).resolve().parent / "lama/configs/prediction/default.yaml")
lama_ckpt = str(Path(__file__).resolve().parent / "lama/pretrained-models/big-lama")
model = ImageEditor()

