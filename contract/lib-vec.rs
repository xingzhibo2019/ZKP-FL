#![cfg_attr(not(feature = "std"), no_std, no_main)]

// use ink_lang as ink;

#[ink::contract]
mod briza {
    //use ink_prelude::vec::Vec;
    use ink_prelude::vec::Vec;
    /// Defines the storage of your contract.
    /// Add new fields to the below struct in order
    /// to add new static storage fields to your contract.
    #[ink(storage)]
    pub struct Briza {
        /// Stores a single `bool` value on the storage.
        value: Vec<Vec<u64>>,
    }

    impl Briza {
        #[ink(constructor)]
        pub fn new() -> Self {
            let mut init_vec = Vec::<Vec<u64>>::new();
            //init_vec.push(va);
            //init_vec.push(v);
            Self { value: init_vec}
        }

        /// A message that can be called on instantiated contracts.
        /// This one flips the value of the stored `bool` from `true`
        /// to `false` and vice versa.
        #[ink(message)]
        pub fn cal(&mut self) -> Vec<u64> {
            let mut ans = Vec::<u64>::new();
            let mut tmp = 0;
            let length = self.value.get(0).unwrap().len();
            for i in 0..length{
                let num = self.value.len();
                tmp = 0;
                for j in 0..num{
                    let param = self.value.get(j).unwrap();
                    tmp += param.get(i).unwrap();
                }
                tmp /= num as u64;
                ans.push(tmp);
            }
            return ans;
            //self.value = !self.value;
        }
        
        #[ink(message)]
        pub fn up_data(&mut self, usr: u64, param: Vec<u64>){
            let idx : usize = usr.try_into().unwrap();
            self.value[idx] = param;
        }

    }


    #[cfg(test)]
    mod tests {
        /// Imports all the definitions from the outer scope so we can use them here.
        use super::*;

        /// Imports `ink_lang` so we can use `#[ink::test]`.
        //use ink_lang as ink;

        /// We test if the default constructor does its job.
        #[ink::test]
        fn default_works() {
            // let mut test = Briza::new();
            // let ans = test.cal();
            // assert_eq!(ans, vec![[3;10];338]);
        }

    }
}
