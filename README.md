## Usage of Zokrates

1. install from source:  

   https://zokrates.github.io/gettingstarted.html

2. run:

   copy codes and scripts to /ZoKrates/target/release path.

   ```bash
   # run cnn
   ./cnn.sh
   # run iris
   ./z-irisrun.sh
   # run price
   ./z-pricerun.sh
   ```

## Usage of contract

1. environments:

   `rustc`: 1.74.1

   `substrate-contracts-node`:  v0.35.0

   https://docs.substrate.io/tutorials/smart-contracts/prepare-your-first-contract/

   ```bash
   cargo install contracts-node --git https://github.com/paritytech/substrate-contracts-node.git --tag v0.35.0 --force --locked
   ```

2. create a project:

   ```bash
   cargo contract new <proj_name>
   ```

   copy `cargo.toml` and `lib-vec.rs` files to the root of this project. 

   ```bash
   cargo contract build
   ```

3. interact with contract

   1. Start your node using `substrate-contracts-node --log info,runtime::contracts=debug 2>&1`
      
   2. upload and instantiate in the root of project

   ```bash
   ./deploy.sh
   ```

   3. aggregate global model through smart contract.

   ```bash
   ./aggregation.sh $CONTRACT_INDEX
   ```
