from .base_backend import SimulatorBackend

class IsaacGymBackend(SimulatorBackend):
    def __init__(self):
        self.connected = False

    def connect(self):
        # TODO: init Isaac Gym envs (GPU) di Colab
        print("[IsaacGymBackend] (stub) connect")
        self.connected = True

    def send_command(self, cmd: dict):
        if not self.connected:
            raise RuntimeError("Simulator not connected.")
        print(f"[IsaacGymBackend] (stub) would execute: {cmd}")

    def get_state(self) -> dict:
        return {"x": 0.0, "y": 0.0, "theta": 0.0, "note": "stub"}

    def disconnect(self):
        print("[IsaacGymBackend] (stub) disconnect")
        self.connected = False
