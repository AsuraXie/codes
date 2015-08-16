<?php
namespace simpleMVC;
class classesController extends controller{
	public function index(){
		$this->display();
	}
	
	public function add(){
		$temp=M("classes");
		$data['id']=$temp->maxid()+1;
		$data['name']=I("name");

		if($temp->add($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"新增成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
	
	public function modify(){
		$temp=M("classes");
		
		$data['id']=I("id");
		$data['name']=I("name");

		if($temp->update($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"修改成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"修改失败"));
	}
	
	public function delete(){
		$temp=M("classes");
		$data['id']=I("id");
		if($temp->delete($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"删除成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"删除失败"));
	}
	
	public function get($page,$rows){
		$temp=M("classes");
		$result=$temp->where($page,$rows);
		$total=$temp->count();
		if($result)
			$this->ajaxReturn(array("total"=>$total,"rows"=>$result));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
}
?>