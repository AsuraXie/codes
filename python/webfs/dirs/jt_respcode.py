#!/usr/bin/env python
#--*-- coding:utf-8 --*--
RespCode={
	"SUCCESS":{"code":0,"msg":"成功"},
	"PARAM_ERROR":{"code":-1000,"msg":"参数错误"},
	"UNDEFINE_ERROR":{"code":-1001,"msg":"未知错误"},
	"UNKNOW_CMD":{"code":-1002,"msg":"未知命令"},
	"NOT_FOUND_NODE":{"code":-1003,"msg":"没有找到结点"},
	"NOT_FOUND_PATH":{"code":-1004,"msg":"没有找到路径"},
	"RESULT_NOT_INIT":{"code":-1005,"msg":"ApiResul没有初始化"},
	"SPLIT_FAILE":{"code":-1006,"msg":"拆分模块失败"},
	"XLIST_GET_ERROR":{"code":-1007,"msg":"xlist中__getitem__错误"},
	"XLIST_WRONG_INDEX":{"code":-1008,"msg":"没有在xlist中找到相应的index记录"},
	"DIRNODE_INIT_FAILE":{"code":-1009,"msg":"dirnode中初始化失败"},
	"EMPTY_PATH":{"code":-1010,"msg":"创建目录时传入为空"},
	"INSERT_FAIL_EMPTY":{"code":-1011,"msg":"目录childs插入失败,第一级目录没有满"},
	"INSERT_FAIL_FULL":{"code":-1012,"msg":"目录childs插入失败,第一级目录已满"},
	"INSERT_FAIL_DIRNEXT":{"code":-1013,"msg":"目录dirnext插入失败,新扩展块"},
	"INSERT_FAIL_DIRNEXT_2":{"code":-1014,"msg":"目录dirnext插入失败,"},
	"INSERT_FAIL_DIRNEXT_3":{"code":-1015,"msg":"新块插入到链表中失败"},
	"INSERT_FAIL_DIRNEXT_4":{"code":-1016,"msg":"新增块失败"},
	"INSERT_FAIL_NO_temp_max":{"code":-1017,"msg":"新增块失败，没有最大块"},
	"PROCESS_DIRNODE_MKDIR_FAIL":{"code":-1018,"msg":"processdirnode中mkdir失败"},
	}
	
