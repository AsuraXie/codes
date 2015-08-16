<?php
namespace simpleMVC;
class deptController extends controller{
	public function index(){
		$this->display();
	}
	
	public function add(){
		$temp=M("dept");
		$data['deptno']=$temp->maxid()+1;
		$data['dname']=I("dname");
		$data['loc']=I("loc");

		if($temp->add($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"新增成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
	
	public function modify(){
		$temp=M("dept");
		
		$data['deptno']=I("deptno");
		$data['dname']=I("dname");
		$data['loc']=I("loc");

		if($temp->update($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"修改成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"修改失败"));
	}
	
	public function delete(){
		$temp=M("dept");
		$data['deptno']=I("deptno");
		if($temp->delete($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"删除成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"删除失败"));
	}
	
	public function get($page,$rows){
		$temp=M("dept");
		$result=$temp->where($page,$rows);
		$total=$temp->count();
		if($result)
			$this->ajaxReturn(array("total"=>$total,"rows"=>$result));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
}
?>