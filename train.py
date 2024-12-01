from anomalib.data import Folder
import yaml
import anomalib
# Import the model and engine
from anomalib.models import Patchcore
from anomalib.engine import Engine

# print(dir(anomalib))

# Load the configuration from config.yaml
with open("/home/gpandit/Videos/glenmark/classification/classification/classification_config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Create the datamodule using the loaded config
datamodule = Folder(**config['init_args'])

# Setup the datamodule
datamodule.setup()

# Create the model and engine
model = Patchcore()
engine = Engine(task="classification")

# Train a Patchcore model on the given datamodule
engine.train(datamodule=datamodule, model=model)
