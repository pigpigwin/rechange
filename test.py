import yaml

def get_yaml_data(fileDir):
    resList = []
    #1-把文件从磁盘加载到内存中--打开
    fo = open(fileDir,'r',encoding='utf8')
    print(fo,type(fo))
    #2使用yaml读取
    res=yaml.load(fo,Loader=yaml.FullLoader)
    print(res,type(res))
    for one,j in res.items():
      resList.append(one)
      if isinstance(j,list):
          print(j[0],type(j[0]))
    return resList

if __name__=='__main__':
  res=get_yaml_data(".\models\segment\yolov5s-seg.yaml")
  print(res)
