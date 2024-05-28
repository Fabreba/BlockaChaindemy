// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;



contract AcademicRecords {
    struct Record {
        string studentName;
        string course;
        string grade;
    }

    Record[] public records;

    address public owner;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Somente o owner pode executar esta funcao");
        _;
    }

    function addRecord(string memory _studentName, string memory _course, string memory _grade) public onlyOwner {
        records.push(Record(_studentName, _course, _grade));
    }

    function getAllRecords() public view returns (Record[] memory) {
        return records;
    }
}
