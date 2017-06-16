<?php
interface Command
{
    function onCommand();
}

class CommandList
{
    private $_cmds = array();

    public function __construct(){
    }

    public function addCommand($cmd)
    {
        $this->_cmds[] = $cmd;
    }

    public function runCommand()
    {
        foreach($this->_cmds as $item){
            $item->onCommand();
        }
    }
}

class commandA implements Command
{
    public function __construct(){
    }

    public function onCommand(){
        echo "commandA";
    }
} 

class commandB implements Command
{
    public function __construct(){
    }

    public function onCommand(){
        echo "commandB";
    }
}

$cmds = new CommandList();
$cmda = new commandA();
$cmdb = new commandB();
$cmds->addCommand($cmda);
$cmds->addCommand($cmdb);
$cmds->runCommand();
?>
