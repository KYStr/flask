項目目錄

|---- manage.py	# 入口文件
|---- app		# 項目包
|---- run.bat	# 運行批處理文件
|-------- __init__.py	# 配置模塊
|-------- forms.py	# 表單驗證模塊
|-------- model.py	# 數據表模塊
|-------- orm.py	# 操作數據庫(DB)模塊
|-------- params.py	# 公共參數模塊
|-------- crud		# 增刪改查視圖包
|------------ __init__.py		# 初始化模塊
|------------ views_add_message.py	#
|------------ views_add_menu.py	# 新增菜單視圖模塊
|------------ views_common.py	# 公共視圖模塊
|------------ views_create_game.py	# 新增大賽視圖模塊
|------------ views_create_subgame.py	# 新增比賽視圖模塊
|------------ views_front.py	# 大賽前端視圖模塊
|------------ views_read_list.py# 員工列表視圖模塊
|------------ views_read_one.py	# 員工詳情視圖模塊
|------------ views_update_message.py
|------------ views_delete.py	# 刪除員工視圖模塊
|-------- templates	# 存放html模板目錄
|------------ add_message.html	# 新增公告頁面
|------------ add_menu.html	# 新增菜單頁面
|------------ create_game.html	# 創建大賽頁面
|------------ create_subgame.html	# 創建比賽頁面
|------------ front.html	# 前端頁面
|------------ layout.html	# 公共布局html
|------------ create.html	# 增添員工html
|------------ read_list.html# 員工列表html
|------------ read_one.html	# 員工詳情html
|------------ update.html	# 修改員工html
|------------ update_message.html # 更新公告html
|-------- static	# 存放靜態資源目錄[css/js/img]


設計模型

員工數據模型
id			編號		BigInt 		primary_key
name		姓名		str			no null
job			職位		TinyInt		no null
sex			性別		TinyInt		no null
edu			學歷		TinyInt		no null
birth		生日		time		no null
email		郵箱		str			no null-only
phone		手機		str			no null-only
info		介紹		text		no null
face		頭像		str			no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null


愛好數據模型[關聯員工AND愛好]
id			編號		BigInt 		primary_key
employee_id	員工編號	BigInt		no null
hobby_key	愛好索引	TintInt		no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null


大賽數據模型
id			編號		BigInt 		primary_key
name		大賽名稱	str			no null
email		郵箱		str			no null-only
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null


比賽數據模型
id			編號		BigInt 		primary_key
game_id		大賽編號	BigInt		no null
name		比賽名稱	str			no null
url			比賽網址 str			no null
img			比賽圖片 str			no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null


公告數據模型
id			編號		BigInt 		primary_key
game_id		大賽編號	BigInt		no null
title		公告標題	str			no null
message		公告內容 str			no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null


菜單數據模型
id			編號		BigInt 		primary_key
game_id		大賽編號	BigInt		no null
item		選項  	str			no null
url			選項連結 str			no null
createdAt	添加時間	steap time	no null
updateAt	添加時間	steap time	no null