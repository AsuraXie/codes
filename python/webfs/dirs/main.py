#!/usr/bin/env python
# --*-- coding:utf-8 --*--
import dirnode
import os
import encrypt
import sys
import random
import jt_common
import jt_log
import jt_respcode as RespCode
import jt_apiResult
import jt_global as GLOBAL
import jt_list
import traceback
import jt_machine_list

def process(params):
	curr_root="none"
	result=jt_apiResult.ApiResult()
	if 'showall' in params:
		showall()
		result.setSuccess()
		return result.display()
	if 'index' in params and len(params['index'])>0:
		print params['index']
		GLOBAL.LocalData.show()
		curr_root=GLOBAL.LocalData.getByKey(params['index'][0])
		if curr_root==False:
			return RespCode.RespCode["NOT_FOUND_NODE"]
	try:
		if 'syscmd' in params:
			return processSysCMD(params)
		elif isinstance(curr_root,jt_list.xlist) or params['cmd']=="mkdirnext":
			return processDirnext(params,curr_root)
		elif isinstance(curr_root,dirnode.dirnode) or params['cmd']=="mkdir":
			if not isinstance(curr_root,str) and len(params['index'])>=2:
				for i in range(1,len(params['index'])):
					curr_root=curr_root.getByKey(params['index'][i])
			if curr_root:
				return processDirnode(params,curr_root)
			else:
				result.setError(RespCode.RespCode['NOT_FOUND_NODE'])
				return result.display()
		else:
			jt_log.log.write(GLOBAL.error_log_path,'params error:'+jt_common.dictToString(params))
			result.setError(RespCode.RespCode['PARAM_ERROR'])
			return result.display()
	except Exception,e:
		traceback.print_exc()
		jt_log.log.write(GLOBAL.error_log_path,'error in process cmd:'+e.message)
		result.setError(RespCode.RespCode['UNDEFINE_ERROR'])
		return result.display()

def showall():
	allitems=GLOBAL.LocalData.getAll()
	for item in allitems:
		if isinstance(item,jt_list.xlist):
			temp_list=item.getAll()
			for temp in temp_list:
				temp.ls()
		elif isinstance(item,dirnode.dirnode):
			item.ls()			
	
#处理系统命令
def processSysCMD(params):
	result=jt_apiResult.ApiResult()
	result.setSuccess()
	#更新机器状态信息
	if params['syscmd']=="refresh_mc":
		if len(params['data'])>0:
			for item in params['data']:
				temp=GLOBAL.MacList[item['index']]
				if temp:
					#有则修改
					temp=item['data']
				else:
					#无则新增
					GLOBAL.MacList.add(item['data'])
			return	result.display()
		GLOBAL.MacList.show()
	elif params['syscmd']=="delete_mc":
		if len(params['data'])>0:
			for item in params['data']:
				GLOBAL.MacList.deleteByIndex(item['index'])	
		return result.display()
	elif params['syscmd']=="delete_node":
		res=GLOBAL.LocalData.deleteByKey(params['index'])
		if res:
			return result.display()
		else:
			result.setError(RespCode.RespCode['DELETE_NODE_FAIL'])
			return result.display()
	else:
		result.setError(RespCode.RespCode['PARAM_ERROR'])
		return result.display()

#处理dirnode
def processDirnode(params,curr_root):
	result=jt_apiResult.ApiResult()
	if params['cmd']=='mkdir':
		if curr_root=="none":
			temp=dirnode.dirnode("root","")
			res=GLOBAL.LocalData.insert("",temp)
			if res:
				result.setSuccess(res)
				return result.display()
			else:
				result.setError(RespCode.RespCode['DIRNODE_INIT_FAIL'])
				return result.display()
		else:
			res=curr_root.mkdir(params['mypath'])
			if res['code']==0:
				result.setSuccess()
			else:
				jt_log.log.write(GLOBAL.error_log_path,"code:"+str(res['code'])+"msg:"+res['msg'])
				result.setError(RespCode.RespCode['PROCESS_DIRNODE_MKDIR_FAIL'])
			return result.display()
	elif params['cmd']=='rename' and 'name' in params:
		curr_root.rename(params['mypath'],params['name'])
	elif params['cmd']=='rmdir':
		print params['index']
		curr_root=GLOBAL.LocalData.getByKey(params['index'][0])
		if len(params['index'])>=2:
			parent=curr_root
			for i in range(1,len(params['index'])):
				print "digui get"
				parent=curr_root
				curr_root=curr_root.getByKey(params['index'][i])
			print parent,curr_root
			curr_root.clearAll()
			print params['index'][-1]
			parent.show()
			res=parent.deleteByKey(params['index'][-1])
			print res
			if res:
				result.setSuccess()
			else:
				result.setError(RespCode.RespCode['RMDIR_FAIL'])
		else:
			result.setError(RespCode.RespCode['INDEX_NOT_ENOUGH'])
		return result.display()
	elif params['cmd']=='find':
		curr_root[params['mypath']]
	elif params['cmd']=='add':
		pass
	elif params['cmd']=="rm":
		pass
	elif params['cmd']=="ls":
		res=curr_root.ls()
		if res!=False:
			result.setSuccess(res)
		else:
			result.setError(RespCode.RespCode['NOT_FOUND_PATH'])
		return result.display()
	elif params['cmd']=="cd":
		#cd查找的时候返回的应该是该结点的所处机器位置,如何获取本身机器的位置呢
		#有可能是返回childs里面的结点，也有可能是dirnext里面的结点，可能会有多个index
		position=curr_root.where(params['mypath'])
		if position:
			res={"mac":position['mac']}
			res['index']=[]
			if 'index' in position and 'sub_index' in position:
				res['index'].append(position['index'])
				res['index'].append(position['sub_index'])
			else:
				for i in range(0,len(params['index'])):
					res["index"].append(params['index'][i])
				if "sub_index" in position:
					res["index"].append(position['sub_index'])
			result.setSuccess(res)
		else:
			result.setError(RespCode.RespCode['NO_SUCH_DIR'])
		return result.display()	
	else:
		result.setError(RespCode.RespCode['PARAM_ERROR'])
		return result.display()

#处理dirnext
def processDirnext(params,curr_root):
	result=jt_apiResult.ApiResult()
	if params['cmd']=='insert':
		temp_data=params['dirnode']
		res=curr_root.insert(temp_data.getName(),temp_data)	
		if res>0:
			result.setSuccess()
		else:
			result.setError(RespCode.RespCode['DIRNEXT_INSERT_FAIL'])
		return result.display()
	elif params['cmd']=="ls":
		if len(params['index'])>=2:
			for i in range(1,len(params['index'])):
				curr_root=curr_root.getByKey(params['index'][i])
		res=curr_root.ls()
		result.setSuccess(res)
		return result.display()
	elif params['cmd']=="mkdirnext":
		temp=jt_list.xlist()
		res_index=GLOBAL.LocalData.insert(params['mypath'],temp)
		result.setSuccess(res_index)
		return result.display()
	elif params['cmd']=="split":
		if curr_root.split(params['mac'],params['target_index']):
			result.setSuccess()
			return result.display()
		else:
			result.setError(RespCode.RespCode['SPLIT_FAILE'])
			return result.display()
	elif params['cmd']=="getByIndex":
		index=params['sub_index']
		res=curr_root[index]
		result.setSuccess(res)
		return result.display()
	elif params['cmd']=="getByKey":
		key=params['key']
		curr_root.show()
		res=curr_root.getByKey(key)
		if res:
			result.setSuccess(res)
		else:
			result.setError(RespCode.RespCode['NOT_FOUND_NODE'])
		return result.display()
	elif params['cmd']=="getMaxName":
		temp=curr_root.Max()
		result.setSuccess(temp.getName())
		return result.display()
	elif params['cmd']=="deleteByName":
		temp=curr_root.deleteByName(params['name'])
		result.setSuccess(temp)
		return result.display()
	elif params['cmd']=="deleteByIndex":
		temp=curr_root.deleteByIndex(params['sub_index'])
		result.setSuccess(temp)
		return result.display()
	elif params['cmd']=="getMaxKey":
		temp=curr_root.getMax()
		result.setSuccess(temp)
		return result.display()
	elif params['cmd']=="getMinKey":
		temp=curr_root.getMin()
		result.setSuccess(temp)
		return result.display()
	elif params['cmd']=="getLength":
		temp=curr_root.getLength()
		return temp
	elif params['cmd']=="getByName":
		index=encrypt.jiami(params['name'])
		res=curr_root[index]
		if res:
			result.setSuccess(temp)
			return result.display()
		else:
			result.setError(RespCode.RespCode["XLIST_WRONG_INDEX"])
			return result.display()
	elif params['cmd']=="cd":
		index=encrypt.jiami(params['name'])
		res=curr_root[index]
		if res:
			temp_index=[]
			for i in range(0,len(params["index"])):
				temp_index.append(params["index"][i])
			temp_index.append(index)
			data={"address":GLOBAL.local_addr,"port":GLOBAL.local_port,"index":temp_index}
			result.setSuccess(data)
		else:
			result.setError(RespCode.RespCode['NO_SUCH_DIR'])
		return result.display()	
	elif params['cmd']=="mkdir" and len(params['index'])>=2:
		curr_root=curr_root.getByKey(params['index'][1])
		res=curr_root.mkdir(params['mypath'])
		if res['code']==0:
			result.setSuccess()
		else:
			result.setError(RespCode.RespCode['XLIST_MKDIR_FAIL'])
		return result.display()
	else:
		result.setError(RespCode.RespCode['PARAM_ERROR'])
		return result.display()

	result.setError(RespCode.RespCode['NOT_FOUND_PATH'])
	return result.display()
	
if __name__=='__main__':
	GLOBAL.LocalData=jt_list.xlist()
	GLOBAL.MacList=jt_machine_list.mList()
	params={"cmd":"mkdirnext","mypath":"home"}
	res=process(params)
	for i in range(1,40):
		temp=dirnode.dirnode(str(i),"")
		params={"cmd":"insert","dirnode":temp,"index":res['data']}
		process(params)

	params={"cmd":"ls","index":res['data']}
	print process(params)

	params={"cmd":"mkdirnext","mypath":"asura"}
	res2=process(params)

	target_mac=GLOBAL.MacList.getBestMC()
	params={"cmd":"split","mac":target_mac,"index":res['data'],"target_index":res2['data']}
	res3=process(params)
