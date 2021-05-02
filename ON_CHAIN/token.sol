pragma solidity  ^0.8.4;

contract Token{
    
    struct Metadata{
        string dateStamp; //author, title, abstractData;
        string hash;
        address delegatorWallet;
        uint256 nodeLocation;
        //public can be deleted in order to hide public view of location
        //make sure has comes first and then the nodeLocation
        string[] tags; 
        //use tags.push(var) for inserting data; 
        //tags.length for length
    }
    
    mapping (address => Metadata) public docLocation;
    //use msg.sender to capture sender's address
    function write(string memory _hash,string memory _dateStamp, uint256 _nodeLocation, string[] memory _tags) public{
        docLocation[msg.sender]=Metadata(_dateStamp, _hash, msg.sender, _nodeLocation, _tags);
    }
    function read()public view returns (Metadata memory m){
        return(docLocation[msg.sender]);
    }
    
    
    }
