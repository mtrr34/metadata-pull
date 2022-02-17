# metadata-pull
1) Use metadata.py to output a text file of tokenIds you are looking for. Run this with "python metadata.py x1 x2 x3 x4"
    - x1 => baseTokenURI (can be found on the projects etherscan). 
    - x2 => collection size i.e. 10000. This is one of the variables used for calculating bound_size
    - x3 => number of threads i.e 4 or whatever. PC dependent this just helps speed up the process of getting tokenIds. To see the difference run it with 1 thread and then multiple. 
    - x4 => this is the output argument. Typically "id" but you can do whatever you want. To look at the reponse you can use "print(res)"

2)  Use contract.py to output a list of addresses that are holding the tokens you are interested in. Changes to contract address, NODE_API, and contract abi will need be made. 
    - Contract address can be found on a projects etherscan.
    - NODE_API is how you interface with ethereum mainnet.
    - Contract ABI can be found on a projects etherscan as well. Just format it into the abi.json file in the repo to use.

3) Once you have addresses.txt use excel to get rid of duplicates unless you are using the snapshot as some kind of voting mechanism and reward people for holding two tokens in your desired category. 

4) I did some testing but again if theres issues or something else you are lookinig for just dm on discord. 
