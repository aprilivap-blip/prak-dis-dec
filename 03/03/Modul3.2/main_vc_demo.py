from vector_clock import VectorClock

# Inisialisasi 2 Proses
p0 = VectorClock(num_processes=2, process_id=0)
p1 = VectorClock(num_processes=2, process_id=1)

p0.increment()
msg = p0.send_message()
p1.receive_message(msg)

print(p0)  # P0: [2, 0]
print(p1)  # P1: [2, 1]
print("P0 -> P1?", p0.happens_before(p1))  # True