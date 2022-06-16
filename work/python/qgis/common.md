#获取字段唯一值
```
layer=iface.activeLayer()   
ids=[f['link_id'] for f in layer.getFeatures()]   
print(list(set(ids)))
```