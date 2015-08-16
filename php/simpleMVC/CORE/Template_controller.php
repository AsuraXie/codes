<?php
namespace simpleMVC;
class @controllerController extends controller{
	public function index(){
		$this->display();
	}
	
	public function add(){
		$temp=M("@controller");
		@add
		if($temp->add($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"新增成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
	
	public function modify(){
		$temp=M("@controller");
		@modify
		if($temp->update($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"修改成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"修改失败"));
	}
	
	public function delete(){
		$temp=M("@controller");
		$data['@prikey']=I("@prikey");
		if($temp->delete($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"删除成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"删除失败"));
	}
	
	public function get($page,$rows){
		$temp=M("@controller");
		$result=$temp->where($page,$rows);
		$total=$temp->count();
		if($result)
			$this->ajaxReturn(array("total"=>$total,"rows"=>$result));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
}
?>