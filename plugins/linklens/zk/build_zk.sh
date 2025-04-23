#!/bin/bash
circom zk/circuit.circom --r1cs --wasm --sym
snarkjs groth16 setup zk/circuit.r1cs powersOfTau28_hez_final.ptau zk/circuit_final.zkey
snarkjs groth16 prove zk/circuit_final.zkey zk/witness.wtns zk/proof.json zk/public.json