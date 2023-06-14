// SPDX-License-Identifier: ISC
pragma solidity ^0.8.0;

import {ERC721} from  "@openzeppelin/contracts/token/ERC721/ERC721.sol";

// HALBORN AUCTION CTF - !!! VULNERABLE CONTRACT

// Contract to auction NFTs
contract Auction {

    address public owner;
    address public asset;
    uint256 public price;
    uint256 public minbid;
    uint256 public closed;
    address public winner;
    uint256 public assetid;

    mapping(address => uint256) private purchased;

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
     * @dev the owner should should own the NFT and approve the transfer to the Auction contract
     * @param _asset the address of the NFT collection
     * @param _asssetid the ID of the NFT sent to the auction
     * @param _minbid minimum possible bid
     * @param sale_duration the duration of the sale in seconds
     */
    function initialize(address _asset, uint256 _asssetid, uint256 _minbid, uint256 sale_duration) external onlyOwner {
        minbid = _minbid;
        asset = _asset;
        assetid = _asssetid;
        closed = block.timestamp + sale_duration;
        winner = msg.sender;
        ERC721(asset).transferFrom(msg.sender, address(this), assetid);
    }

    /**
     * @notice bid to an NFT
     * @dev do not forget to transfer back the Ethers to the previous bidder
     */
    function bid() external payable {
        require(block.timestamp < closed , "Auction was ended!");
        require(msg.value - price >= minbid, "Too small bid!");

        payable(winner).transfer(price);

        winner = msg.sender;
        price = msg.value;
    }

    /**
     * @notice withdraw the NFT
     * @dev the winner gets the NFT after the auction ends.
     */
    function withdraw() external {
        require(closed<block.timestamp, "Auction is not over yet!");
        ERC721(asset).transferFrom(address(this), winner, assetid);
    }

}