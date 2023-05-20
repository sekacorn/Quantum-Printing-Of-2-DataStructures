from qiskit import QuantumCircuit, transpile, assemble, Aer, IBMQ

class QuantumDataStructures:
    def __init__(self, name):
        self.name = name

    def encode_name(self, circuit):
        binary = format(ord(self.name), '08b')  # Converting character to 8-bit binary
        for i, bit in enumerate(binary):
            if bit == '1':
                circuit.x(i)  # Applyinga Pauli-X gate to set the qubit to |1>

    def decode_name(self, counts):
        binary_output = list(counts.keys())[0]
        output = chr(int(binary_output, 2))  # Converting binary representation back to a character
        return output

    def run_circuit(self, backend):
        # Creating a quantum circut
        circuit = QuantumCircuit(8, 8)

        # Encoding the name into the quantum state
        self.encode_name(circuit)

        # Measuring the qubits
        circuit.measure(range(8), range(8))

        # Transpiling the circuit for the targeting backend
        transpiled_circuit = transpile(circuit, backend)

        # Assembling the transpiled circuit into a job
        job = assemble(transpiled_circuit, shots=1)

        # submitting the job to the quantum computer and wait for the result
        job_result = backend.run(job).result()

        # Getting the counts from the result
        counts = job_result.get_counts()

        # Retrieving and returning the decoded name
        output = self.decode_name(counts)
        return output


# Prompting the user to enter their name
name = input("Enter your name: ")

# Loading IBM Quantum account and selecting a backend
provider = IBMQ.load_account()
backend = provider.get_backend('your_preferred_backend')  # Replacing 'your_preferred_backend' with an available quantum device

# creating aninstance of QuantumDataStructures
quantum_data = QuantumDataStructures(name)

# Running the quantum circuit on the selected backend
output = quantum_data.run_circuit(backend)

# Printing the output
print("Hello Quantum world, I am " + output)
