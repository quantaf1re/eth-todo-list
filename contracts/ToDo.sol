pragma solidity >=0.7.0 <0.8.0;

contract ToDo {

    address public owner;
    uint public taskCount = 0;
    mapping(uint => Task) public tasks;

    struct Task {
        uint id;
        string description;
        Status status;
    }

    enum Status { Created, InProgress, Completed, Cancelled }
    event ModTask(uint indexed id, Status newStatus);


    constructor() {
        owner = msg.sender;
    }

    function createTask(string calldata _description) external onlyOwner {
        require(bytes(_description).length > 0, "Need a description!");
        // Technically this could overflow, but perhaps that's desirable
        // behaviour - you probably don't care about overwriting a task
        // from 2^256 tasks ago and don't want to redeploy a contract
        // that must have been working well for that long
        tasks[taskCount] = Task(taskCount, _description, Status.Created);
        emit ModTask(taskCount, Status.Created);
        taskCount++;
    }

    function modTask(uint _id, Status _newStatus) external onlyOwner {
        require(_id >= 0 && _id < taskCount, "Task doesn't exist");
        // Perhaps there should be a requirement to prevent marking a task
        // as cancelled if it's already been completed etc, but TODO phone apps
        // generally allow you to do this anyway so we'll allow it here too
        tasks[_id].status = _newStatus;
        emit ModTask(_id, _newStatus);
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }
}