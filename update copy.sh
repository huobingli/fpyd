install_product_path=$1 # hxapp/hqserver_update/hxdata/update/
install_product_version=$2 # tyb tybc01/
zip_file_name=$3 # 不包含.zip名字 tyb_client_update

zip_file_path=$install_product_path$zip_file_name

#todo read target_path
# target_path /hxapp/hqserver_update/hxdata/update/
# 删除原来目录
# rm -f hxapp/hqserver_update/hxdata/update/tyb_client_update.zip
rm -f "$install_product_path$zip_file_name.zip" 

# 拷贝新的升级包到当前目录
# cp tyb_client_update.zip hxapp/hqserver_update/hxdata/update/tyb_client_update.zip
cp "$zip_file_name.zip" "$install_product_path$zip_file_name.zip"
# unzip hxapp/hqserver_update/hxdata/update/tyb_client_update.zip -> hxapp/hqserver_update/hxdata/update/tyb_client_update/
unzip -d $install_product_path "$install_product_path$zip_file_name.zip" 

# 删除原来安装目录下的文件
old_path=($pwd)
cd $install_product_path$install_product_version
shopt -s extglob
rm -rf !(*.ipx)
shopt -u extglob
cd $old_path

cp -r $install_product_path$zip_file_name/* $install_product_path$install_product_version
rm -rf $install_product_path$zip_file_name