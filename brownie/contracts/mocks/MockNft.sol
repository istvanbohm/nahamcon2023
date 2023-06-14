
// SPDX-License-Identifier: agpl-3.0
pragma solidity ^0.8.0;

import {ERC721} from  "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MockNft is ERC721 {
    constructor(
        string memory name,
        string memory symbol
    ) ERC721(name, symbol) {
        
    }

    function mint(address _to, uint256 _tokenId) public {
        _safeMint(_to, _tokenId);
    }
}