<?php
namespace simpleMVC;
class empController extends controller{
	public function index(){
		$this->display();
	}
	
	public function add(){
		$temp=M("emp");
		$data['empno']=$temp->maxid()+1;
		$data['ename']=I("ename");
		$data['job']=I("job");
		$data['mgr']=I("mgr");
		$data['hiredate']=I("hiredate");
		$data['sal']=I("sal");
		$data['comm']=I("comm");
		$data['deptno']=I("deptno");

		if($temp->add($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"新增成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
	
	public function modify(){
		$temp=M("emp");
		
		$data['empno']=I("empno");
		$data['ename']=I("ename");
		$data['job']=I("job");
		$data['mgr']=I("mgr");
		$data['hiredate']=I("hiredate");
		$data['sal']=I("sal");
		$data['comm']=I("comm");
		$data['deptno']=I("deptno");

		if($temp->update($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"修改成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"修改失败"));
	}
	
	public function delete(){
		$temp=M("emp");
		$data['empno']=I("empno");
		if($temp->delete($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"删除成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"删除失败"));
	}
	
	public function get($page,$rows){
		$temp=M("emp");
		$result=$temp->where($page,$rows);
		$total=$temp->count();
		if($result)
			$this->ajaxReturn(array("total"=>$total,"rows"=>$result));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
}
?>