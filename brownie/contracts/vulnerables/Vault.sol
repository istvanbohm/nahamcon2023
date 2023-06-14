// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// HALBORN VAULT CTF - !!! VULNERABLE CONTRACT

// Deposit your ETH in the vault and earn interest
contract Vault is ERC20, ERC20Burnable, Pausable, Ownable {

    address public weth;

    // the percentage of interest in one year
    uint256 public rate = 10;
    // avg seconds in a year
    uint256 private year = 31577600;
    // the times of the last deposits
    mapping(address => uint256) public dtimes;

    /**
     * @notice deploy the contract
     * @param _weth the address of the WETH contract
     */
    constructor(address _weth) ERC20("Vault Coin", "VCoin") {
        weth = _weth;
    }

    /**
     * @notice deploy Ether to the vault to earn interest
     * @dev the caller should send ether that the function deposits into the vault
     */
    function deposit() public payable {
        if(dtimes[msg.sender]!=0) {
            addInterest();
        }
        dtimes[msg.sender] = block.timestamp;
        _mint(msg.sender, msg.value);
    }

    /**
     * @notice deposit WETH into the contract
     * @dev before deposit approve the transfer transaction for the vault contract
     * @param from the owner of the tokens
     * @param to the user who receives the vault tokens
     * @param val the number of tokens to deposit
     */
    function depositWeth(address from, address to, uint256 val) public {
        if(dtimes[msg.sender]!=0) {
            addInterest();
        }
        dtimes[msg.sender] = block.timestamp;
        _mint(to, val);
        ERC20(weth).transferFrom(from,address(this),val);
    }

    /**
     * @notice internal function to add the calculated interest
     */
    function addInterest() internal {
        uint256 interest = calculateInterest();
        _mint(msg.sender, interest);
    }

    /**
     * @notice internal function to calculate interest
     */
    function calculateInterest() public view returns (uint256) {
        if (dtimes[msg.sender]==0) {
            return 0;
        } else {
            uint256 duration = block.timestamp-dtimes[msg.sender];
            uint256 interest_per_sec = balanceOf(msg.sender) * (rate/100) / year;
            uint256 interest = interest_per_sec * duration;
            return interest;
        }
    }

    /**
     * @notice withdraw the vault tokens from the contract to get Ether
     * @param value the number of vault tokens to withdraw
     */
    function withdraw(uint256 value) public {
        require(balanceOf(msg.sender) >= value, "Insufficient balance!");
        payable(msg.sender).transfer(value);
        _burn(msg.sender, value);
    }

    /**
     * @notice withdraw the vault tokens from the contract to get WETH tokens
     * @param to the address where the tokens are to be withdrawn
     * @param value the number of vault tokens to withdraw
     */
    function withdrawWeth(address to, uint256 value) public {
        require(balanceOf(msg.sender) >= value, "Insufficient balance!");
        uint256 _balance = ERC20(weth).balanceOf((address(this)));
        require(_balance >= value, "Insufficient contract balance!");
        ERC20(weth).transfer(to,value);
        _burn(msg.sender, value);
    }

    // ADMIN Functions

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    function transferbyOwner(address sender, address recipient, uint256 amount) public whenPaused onlyOwner {
        _transfer(sender, recipient, amount);
    }

    function EmergencyDestroy(address payable _to) public {
        selfdestruct(_to);
    }
}
