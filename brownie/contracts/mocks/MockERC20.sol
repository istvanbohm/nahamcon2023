// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

/**
 * @title ERC20Mintable
 * @dev ERC20 minting logic
 */
contract MockERC20 is ERC20 {
    constructor(
        string memory name,
        string memory symbol
    ) ERC20(name, symbol) {

    }

    // Anyone can mint tokens for testing purposes
    function mint(address account, uint256 amount) public {
        _mint(account, amount);
    }

    // Anyone can burn tokens for testing purposes
    function burn(address account, uint256 amount) public {
        _burn(account, amount);
    }

}
