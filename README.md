# OM1 ↔ Isaac Gym Bridge (WIP)

A modular bridge that lets OM1 control simulators via a unified backend interface.
Includes a CPU-only Mock backend and an Isaac Gym backend (Cartpole + camera capture).

## Run (CPU / Mock)
```bash
python -m demo.run_mock

Run (GPU / Isaac Gym) — for reviewers

Requires: Python 3.10 + NVIDIA CUDA (Torch CUDA must be True)
pip install "torch==2.3.1" --index-url https://download.pytorch.org/whl/cu121
pip install "gym==0.25.2" numpy==1.26.4 imageio imageio-ffmpeg pillow
pip install "git+https://github.com/NVIDIA-Omniverse/IsaacGymEnvs.git@main"

python - << 'PY'
import torch; print("cuda?", torch.cuda.is_available())
PY

python -m demo.run_isaacgym   # outputs: isaac_demo.mp4 (camera capture)

Structure

bridge/base_backend.py — backend interface

bridge/mock_backend.py — CPU mock backend

bridge/isaac_backend.py — Isaac Gym backend (Cartpole, camera)

demo/run_mock.py — CPU demo

demo/run_isaacgym.py — GPU demo (records camera frames to MP4)

Demo Video (WIP / mock)

https://youtu.be/Sb2CNYH0xWI

Notes

Local device is non-GPU; please run the GPU demo per steps above.

Next: additional robots (Ant/Manipulator), multi-env, telemetry streaming to OM1.
