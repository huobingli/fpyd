install_product_path=$1 # hxapp/hqserver_update/hxdata/update/
install_product_version=$2 # tyb tybc01/
zip_file_name=$3 # 不包含.zip名字 tyb_client_update

zip_file_path=$install_product_path$zip_file_name   # 升级zip包路径
update_dir=$install_product_path$install_product_version # 升级目录路径

# 删除原来目录
rm -f "$zip_file_path.zip" 

# 拷贝新的升级包到当前目录
cp "$zip_file_name.zip" "$zip_file_path.zip"
unzip -d $install_product_path "$zip_file_path.zip" 

# 删除原来安装目录下的文件
old_path=($pwd)
cd $update_dir
shopt -s extglob
rm -rf !(*.ipx)
shopt -u extglob
cd $old_path

cp -r $zip_file_path/* $update_dir
rm -rf $zip_file_path