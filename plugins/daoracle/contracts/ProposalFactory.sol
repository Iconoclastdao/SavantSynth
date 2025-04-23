// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract ProposalFactory {
    struct Proposal {
        uint256 id;
        string description;
        address creator;
        bool executed;
        uint256 votesFor;
        uint256 votesAgainst;
    }

    mapping(uint256 => Proposal) public proposals;
    uint256 public proposalCount;

    function createProposal(string memory description) public {
        proposals[proposalCount] = Proposal(
            proposalCount,
            description,
            msg.sender,
            false,
            0,
            0
        );
        proposalCount++;
    }

    function vote(uint256 proposalId, bool support) public {
        Proposal storage p = proposals[proposalId];
        require(!p.executed, "Already executed");
        if (support) {
            p.votesFor++;
        } else {
            p.votesAgainst++;
        }
    }

    function executeProposal(uint256 proposalId) public {
        Proposal storage p = proposals[proposalId];
        require(p.votesFor > p.votesAgainst, "Not approved");
        p.executed = true;
        // Implement desired on-chain effects here
    }
}