import time, random
from .base_backend import SimulatorBackend

class MockBackend(SimulatorBackend):
    def __init__(self):
        self.connected = False
        self.state = {"x": 0.0, "y": 0.0, "theta": 0.0}

    def connect(self):
        print("[MockBackend] Connected to mock simulator.")
        self.connected = True

    def send_command(self, cmd: dict):
        if not self.connected:
            raise RuntimeError("Simulator not connected.")
        action = cmd.get("action", "")
        if action == "move":
            self.state["x"] += cmd.get("x", 0)
            self.state["y"] += cmd.get("y", 0)
        elif action == "rotate":
            self.state["theta"] += cmd.get("angle", 0)
        else:
            print("[MockBackend] Unknown command:", action)
        time.sleep(0.2)
        print(f"[MockBackend] Executed: {cmd}")

    def get_state(self) -> dict:
        return {k: v + random.uniform(-0.01, 0.01) for k, v in self.state.items()}

    def disconnect(self):
        print("[MockBackend] Disconnected.")
        self.connected = False
