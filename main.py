import os
from dotenv import load_dotenv
from qiskit import IBMQ, QuantumCircuit, Aer, assemble
from qiskit.visualization import plot_histogram
from IPython.display import display

try:
    provider = IBMQ.load_account()
except:
    load_dotenv()
    IBMQ.save_account(os.getenv('IBM_TOKEN'))
    provider = IBMQ.load_account()


def generate_random_bits(length):
    bits = ''
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.barrier()
    qc.measure(0,0)
    #display(qc.draw())
    for i in range(length):
        aer_sim = Aer.get_backend('aer_simulator')
        job = aer_sim.run(assemble(qc), shots=1, memory=True)
        measured_bit = int(job.result().get_memory()[0])
        bits += str(measured_bit)
        #plot_histogram(job.result().get_counts(), filename='histogram.png')
    return bits

print(generate_random_bits(10))