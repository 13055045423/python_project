#管理ip模块：将获取到的ip进行数据的存储,不可用的ip删除掉

import pymongo
import random

class ManageIp(object):

    def __init__(self,database,col_name,host='localhost',port=27017):
        """
        :param database: mongodb数据库的名称
        :param col_name: 数据库下的集合名称
        :param host: host
        :param port: 端口
        """
        #创建mongodb数据库连接
        self.mongo_client = pymongo.MongoClient(host,port)
        self.db = self.mongo_client[database]
        self.col = self.db[col_name]
        #用来存放mongodb中获取的代理,用来返回随机ip代理
        self.proxies = []

    def get_size(self):
        """
        获取集合中存储的的代理的数量
        :return:
        """
        size = self.col.find().count()
        print('代理池中的代理总数为:',size)
        return int(size)

    def save_proxydict(self,proxydict):
        """
        将获取的ip存储到数据库
        :param proxies: 单个代理，字典类型
        :return:
        """
        if len(proxydict) > 0:
            try:
                print('正在存储', proxydict)
                self.col.insert(proxydict)
            except Exception as err:
                print(err)

    def save_proxies(self,proxies):
        """
        将获取的ip存储到数据库
        :param proxies:　多个代理，列表类型
        :return:
        """
        if proxies and len(proxies) > 0:

            for proxy in proxies:

                proxydict = {
                    'type': 'https',
                    'proxy': proxy
                }
                try:
                    print('正在存储', proxydict)
                    self.col.insert(proxydict)
                except Exception as err:
                    print(err)

    def delete_proxy(self,proxy_dict):
        """
        检出代理不可用,可执行如下方法,删除代理
        :param proxy:
        :return:
        """

        try:
            result = self.col.delete_one(proxy_dict)
            print(proxy_dict,'删除成功',result.deleted_count,'条')
        except Exception as err:
            print(proxy_dict,'删除失败',err)

    def get_collection_proxies(self):
        """
        获取集合中的代理
        :return:
        """
        try:
            result = self.col.find()
            proxies = [proxy for proxy in result]
            # print('成功取出'+str(len(proxies))+'条代理')
            return proxies
        except Exception as err:
            print(err)
            print('获取代理列表失败')
            return []
    
    def get_random_ip(self):
        self.proxies = self.get_collection_proxies()
        if len(self.proxies) > 0:
            proxy = random.choice(self.proxies)
            return proxy
        else:
            print('暂无可用的ip代理')




