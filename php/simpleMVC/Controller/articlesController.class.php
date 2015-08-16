<?php
namespace simpleMVC;
class articlesController extends controller{
	public function index(){
		$this->display();
	}
	
	public function add(){
		$temp=M("articles");
		$data['id']=$temp->maxid()+1;
		$data['title']=I("title");
		$data['body']=I("body");

		if($temp->add($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"新增成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
	
	public function modify(){
		$temp=M("articles");
		
		$data['id']=I("id");
		$data['title']=I("title");
		$data['body']=I("body");

		if($temp->update($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"修改成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"修改失败"));
	}
	
	public function delete(){
		$temp=M("articles");
		$data['id']=I("id");
		if($temp->delete($data))
			$this->ajaxReturn(array("success"=>true,"message"=>"删除成功"));
		else $this->ajaxReturn(array("success"=>false,"message"=>"删除失败"));
	}
	
	public function get($page,$rows){
		$temp=M("articles");
		$result=$temp->where($page,$rows);
		$total=$temp->count();
		if($result)
			$this->ajaxReturn(array("total"=>$total,"rows"=>$result));
		else $this->ajaxReturn(array("success"=>false,"message"=>"新增失败"));
	}
}
?>