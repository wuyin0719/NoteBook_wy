##OpenStreetMap主机服务
10.10.201.81（OSM）   
端口：22   
路径：       /usr/local/openstreetmap-website  
账号/密码：	root/Sutpco81   


#OSM备份导出      

cd /usr/local/openstreetmap-website     
docker-compose exec web bash   
osmosis --read-apidb host="db" database="openstreetmap" user="openstreetmap" password="openstreetmap"
validateSchemaVersion="no" --write-pbf bak202202232003.osm.pbf  

##OSM生成、裁剪、过滤（qgis脚本实现）

###pbf转osm
osmconvert64-0.8.8p bak202206131054.osm.pbf > bak202206131054.osm
  
###用osmconvert裁剪   
osmconvert64-0.8.8p bak202206131054.osm -b=119.61116,25.46137,119.61537,25.46351 -o=osm_fj_connection_bug02.osm

###osm数据过滤
osmfilter osm_fj_connection_bug02.osm --keep="highway=motorway or highway=motorway_link" > bak202205121141_gaosu.osm


### osm转odrx
netconvert_main.exe --osm-files bak202205121141_gaosu.osm --opendrive-output bak202206071048_gaosu.xodr --geometry.remove true --offset.x 0 --offset.y 0 --roundabouts.guess true --tls.discard-simple true --tls.join true --tls.guess-signals true --tls.default-type actuated --keep-edges.by-vclass passenger --junctions.join true --junctions.corner-detail 5 --junctions.scurve-stretch 0.75 --default.lanewidth 4
D:\wy\code\osm_bin\netconvert202204011814\netconvert202204011814\netconvert_main.exe --osm-files osm_fj_connection_bug02.osm --opendrive-output bak202206071048_gaosu.xodr --geometry.remove true --offset.x 0 --offset.y 0 --roundabouts.guess true --tls.discard-simple true --tls.join true --tls.guess-signals true --tls.default-type actuated --keep-edges.by-vclass passenger --junctions.join true --junctions.corner-detail 5 --junctions.scurve-stretch 0.75 --default.lanewidth 4

##odrx解析
testSimParseClient

##数据处理主机服务(ubuntu，很猛)
地址：10.3.3.107   
端口：22  
路径:/home/user/Tgis/dev/  
账号/密码：user/sutpc123  
GeoServer端口：25434  
GeoServer登陆： admin/geoserver  

