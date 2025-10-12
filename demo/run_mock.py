import time
from bridge.mock_backend import MockBackend

def main():
    sim = MockBackend()
    sim.connect()

    commands = [
        {"action": "move", "x": 1.0, "y": 0.0},
        {"action": "rotate", "angle": 45},
        {"action": "move", "x": 0.5, "y": 0.5},
    ]

    for cmd in commands:
        print("[OM1] send:", cmd, flush=True)
        sim.send_command(cmd)
        state = sim.get_state()
        print("[OM1] state:", state, flush=True)
        time.sleep(0.1)

    sim.disconnect()
    print("[OM1] Session finished.", flush=True)

if __name__ == "__main__":
    main()
