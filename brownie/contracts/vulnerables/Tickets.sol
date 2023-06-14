// SPDX-License-Identifier: ISC
pragma solidity 0.7.4;

// HALBORN TICKET CTF - !!! VULNERABLE CONTRACT

// Contract to buy tickets for very private crypto events and conferences
contract Tickets {

    event TicketBought(address owner, uint256 quantity);
    event TicketRefunded(address owner, uint256 quantity);

    address public owner;
    uint256 public price;
    uint256 public tickets;
    uint256 public closed;
    string public eventname;

    mapping(address => uint256) public purchased;

    modifier onlyOwner() {
        require(msg.sender == owner, "Hacker detected!!!");
        _;
    }
    /**
     * @notice deploy the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @notice initialize the contract 
     * @dev can be used to re-use the contract
     * @param _price the price of 1 ticket
     * @param _tickets the number of tickets to sell
     * @param sale_duration the duration of the sale in seconds
     */
    function initialize(string memory _eventname, uint256 _price, uint256 _tickets, uint256 sale_duration) external {
        eventname = _eventname;
        price = _price;
        tickets = _tickets;
        closed = block.timestamp + sale_duration;
    }

    /**
     * @notice buy a new ticket
     * @dev users need to pay the exact amount
     * @param quantity the number of tickets to buy
     */
    function buy(uint256 quantity) external payable {
        require(price != 0, "Not yet initialized!");
        require(block.timestamp < closed , "Sale was ended!");
        require(msg.value >= quantity * price, "Not enough minerals!!!");
        purchased[msg.sender] += quantity;
        emit TicketBought(msg.sender,quantity);
    }

    /**
     * @notice refund a bought ticket
     * @param quantity the number of tickets to buy
     */
    function refund(uint256 quantity) external {
        require(price != 0, "Not yet initialized!");
        require(block.timestamp < closed , "No refound. Sale was ended!");
        require(quantity <= purchased[msg.sender], "You don't have enough tickets!");

        msg.sender.call{value: quantity * price}("");
        purchased[msg.sender] -= quantity;
        emit TicketRefunded(msg.sender, quantity);
    }

    /**
     * @notice withdraw the Ethers from the contract
     */
    function withdraw() external onlyOwner {
        require(price != 0, "Not yet initialized!");
        require(closed<block.timestamp, "Sale is not finished yet!");
        msg.sender.call{value: address(this).balance}("");
    }

    receive() external payable {}
}