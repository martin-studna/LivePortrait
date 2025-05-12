#!/bin/bash

export PYTORCH_ENABLE_MPS_FALLBACK=1
python inference.py --source ./assets/examples/source/miloš.jpg --driving ./assets/examples/driving/1part_driving_left_.mp4
python inference.py --source ./assets/examples/source/miloš.jpg --driving ./assets/examples/driving/2part_driving_left_.mp4
python inference.py --source ./assets/examples/source/miloš.jpg --driving ./assets/examples/driving/3part_driving_left_.mp4
python inference.py --source ./assets/examples/source/miloš.jpg --driving ./assets/examples/driving/4part_driving_left_.mp4
python inference.py --source ./assets/examples/source/miloš.jpg --driving ./assets/examples/driving/5part_driving_left_.mp4



python inference.py --source ./assets/examples/source/kešner.jpeg --driving ./assets/examples/driving/1part_driving_right_.mp4
python inference.py --source ./assets/examples/source/kešner.jpeg --driving ./assets/examples/driving/2part_driving_right_.mp4
python inference.py --source ./assets/examples/source/kešner.jpeg --driving ./assets/examples/driving/3part_driving_right_.mp4
python inference.py --source ./assets/examples/source/kešner.jpeg --driving ./assets/examples/driving/4part_driving_right_.mp4
python inference.py --source ./assets/examples/source/kešner.jpeg --driving ./assets/examples/driving/5part_driving_right_.mp4
