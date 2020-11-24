pragma solidity >=0.7.0 <0.8.0;


/**
 * @title   ToDo
 * @author  James Key
 * @notice  ToDo serves as a ToDo list where the owner can add new tasks,
 *          aswell as mark as in progress, complete, and cancel tasks.
 */
contract ToDo {

    address public owner;
    // Tracks the number of tasks created
    uint public taskCount = 0;
    // Stores created tasks
    mapping(uint => Task) public tasks;

    enum Status { Created, InProgress, Completed, Cancelled }

    struct Task {
        uint id;
        string description;
        Status status;
    }

    event ModTask(uint indexed id, Status newStatus);


    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new task
     * @param _description       The description of what is supposed to be done
     */
    function createTask(string calldata _description) external onlyOwner {
        require(bytes(_description).length > 0, "Need a description!");
        tasks[taskCount] = Task(taskCount, _description, Status.Created);
        emit ModTask(taskCount, Status.Created);
        // Technically this could overflow, but perhaps that's desirable
        // behaviour - you probably don't care about overwriting a task
        // from 2^256 tasks ago and don't want to redeploy a contract
        // that must have been working well for that long
        taskCount++;
    }

    /**
     * @dev Modify an existing task
     * @param _id           The id of the task to be modified
     * @param _newStatus    The new status of the task
     */
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