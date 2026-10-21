import random
import time
from raft_module import RaftNode, State

def run_simulation():
    node_ids = [1, 2, 3]
    nodes = [RaftNode(node_id, node_ids) for node_id in node_ids]

    print("Simulasi Konsensus Raft Terdistribusi\n" + "="*40)
    
    for step in range(10):
        time.sleep(0.5)
        print(f"\n--- Step {step + 1} ---")
        
        leaders = [n for n in nodes if n.state == State.LEADER]
        if leaders:
            leader = random.choice(leaders)
            for node in nodes:
                if node.id != leader.id:
                    node.on_heartbeat(leader.current_term)
            
            if step % 3 == 0:
                leader.append_entry(f"Data-Log-{step}")

        for node in nodes:
            node.tick()

        for node in nodes:
            print(f"Node {node.id}: {node.state.name} | Term: {node.current_term} | Log Len: {len(node.log)}")

if __name__ == "__main__":
    run_simulation()