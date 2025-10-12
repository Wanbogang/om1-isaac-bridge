# OM1 ↔ Isaac Gym Bridge (WIP)

## Run (CPU / mock)
```bash
python -m demo.run_mock

Run (GPU / Isaac Gym)

Require: Python 3.10 + NVIDIA CUDA
pip install "torch==2.3.1" --index-url https://download.pytorch.org/whl/cu121
pip install "gym==0.25.2" numpy==1.26.4 imageio imageio-ffmpeg pillow
pip install "git+https://github.com/NVIDIA-Omniverse/IsaacGymEnvs.git@main"
python - << 'PY'
import torch; print("cuda?", torch.cuda.is_available())
PY
python -m demo.run_isaacgym   # outputs: isaac_demo.mp4 (camera capture)

Notes

Modular backend: MockBackend (CPU) & IsaacGymBackend (Cartpole + camera).

Demo (WIP/mock): https://youtu.be/Sb2CNYH0xWI

Device lokal saya non-GPU; mohon reviewer menjalankan langkah GPU di atas.
