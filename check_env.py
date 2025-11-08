from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import circuit_drawer

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
print(qc)