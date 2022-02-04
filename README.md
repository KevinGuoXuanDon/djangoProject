# djangoProject

.................
### Git Usage Specification:
1. Please check the branch ***when you attempt to commit codes or merge branch***  
2. ***Commit your codes with enough explanation***
3. ***Do not merge or delete branches easily***
4. If you **make any serious mistake** with git, please inform team members, we will roll back this branch to **the latest version**.

# Explanation of branches:
## Main branch
Main branch is going to store current version of code that have been debugged and completed after merging conflicts.

This is a protected branch

***So DO NOT commit any code directly to this branch***

## Dev
Development branch is where usually programmers spend their time 

Some of the major updates (such as system architecture updates, specific functionality and content implementation, GUI layout completion) will be implemented here

## feat_dev branch
Feature development branch will contain several sub-branches which are pulled from the original ***development branch***.

Programmer can simply use their own feature branch to develop a new feature, then merge it back to feat_dev branch after review and test


## Fix branch

Fix branch is designed for some *hot bugs*

You may commit your work to this branch with full explanation

## Test branch 

You may commit *Unit test file* that you implement for special methods or GUI section


## Docs
Documents only  
Can be merged to Main branch after checking        

--------------------------------------
# Project structure

###### Back-end structure(Probably change):
django-project
├──forum
├── ├── admin         // 后台管理
├── ├── app           // configuration
├── ├── model         // 模型层  
├── ├── View          // 视图接口层(创建响应函数) 
├── ├── test          // 单元测试  
├── ├── url           // 路径映射
├── ├── migrations    // 迁移文件
├── Readme.md         // help  
├── static            // 静态资源     
│   ├── CSS  
│   ├── js               
│   ├── image           
│   ├── font                
│   └── initjson  
│       └── config.js              // 提供给前端的配置    
├── media                          // 储存较大的对象  
├── doc                            // 文档  
├── sql                            // sql脚本  
├── templates                      // 模板层(前端)
├── manage.py                      // django管理
├── population.py                  // 测试数据生产





To Do List:
- requirement confirm *Done
- GUI design
- database design  
- Data access  
- logic achievement 
- Interface provide 
- Test data creation 
- Unit Test 
- HTTP Test 
- Test Interface connection with axios 
