#获取字段唯一值
```
layer=iface.activeLayer()   
ids=[[f['link_id'],f['link_id_2']] for f in layer.getFeatures()]   
print(ids)
```


#批量路径匹配

批处理的时候输出文件名和输入保持一致   
``` file_path('D:/res//' )||  layer_property( @INPUT,'name')||'.shp'  ``` 



#批量加载csv
```
import os
dir = r'D:\wy\code\work-code\common-gis\common-gis\output\osm-pingshan'
for root, dirs, files in os.walk(dir):
 for fname in files:
     if fname.endswith(".csv"):
         csvFile=os.path.join(root,fname)
         with open(csvFile,'r') as f:
             line=f.readline()
            #geo_wkt
         if 'geo_wkt' in line:
             urlpath = "file:///%s/%s?" \
                       "ype=csv&maxFields=10000&detectTypes=yes&wktField=geo_wkt&crs=EPSG:4326&spatialIndex=yes&subsetIndex=no&watchFile=no"% (root, fname)
             layer = iface.addVectorLayer(urlpath, fname.split(".")[0], "delimitedtext")
         else:
             #geo_xy
             urlpath = "file:///%s/%s?" \
                   "type=csv&maxFields=10000&detectTypes=yes&xField=X&yField=Y&crs=EPSG:4326&spatialIndex=yes&subsetIndex=no&watchFile=no"% (root, fname)
             layer = iface.addVectorLayer(urlpath, fname.split(".")[0], "delimitedtext")
```
         
         
#把所有的qgis图层的图例保存起来





##json转化

369823409A3735729027A3735729013_-1 ->xxx


[+proj=utm +zone=51 +datum=WGS84 +units=m +no_defs ]

+proj=utm +zone=51 +datum=WGS84 +x_0=235541.38245563806 +y_0=3346704.1446796223  +units=m +no_defs




##获取属性字段
```python
vlayer=iface.activeLayer()
fields=[]
for field in vlayer.fields():
    fields.append([field.name(), field.typeName()])
    
print(fields)
```




