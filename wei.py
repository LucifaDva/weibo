import requests
import json
class Weibo(object):
    base_url = 'https://api.weibo.com/2/'
    params = {}
    headers = {}
    
    def __init__(self,access_token=''):
        self.access_token  = access_token
        
    def _request(self,**kw):
#        if 'headers' in kw:
#            self.headers = kw['headers']
#            del kw['headers']
#        for keyword in ['content_length',
#                        'content_md5',
#                        'slice_md5',
#                        'content_crc32']:
#            try:
#                kw[keyword.replace('_', '-')] = kw[keyword]
#                del kw[keyword]
#            except KeyError:
#                continue
        if 'uid' in kw:
            self.uid = kw['uid'] 
        if 'screen_name' in kw:
            self.screen_name = kw['screen_name']               
        self.params.update(access_token=self.access_token)
        self.params.update(kw)
        self.url = ''.join([self.base_url,self.urlpath])
    
        if self._method == 'GET':
            try:
                r = requests.get(self.url,params=self.params,headers=self.headers)
                return r.content
            except Exception, e:
                print e
                return None
        else:
            return None
            
    def show(self,**kw):
        self.urlpath = 'users/show.json'
        self._method = 'GET'
        result = self._request(**kw)
        x = unicode(result,'utf8')
        x.encode('utf8')
        
        return x
    
#for i in range(x,y):
#    d = Weibo(access_token='2.0049mjxBCIwWIC4b97cb1107NWndaB',uid=str(i))
#    print 'uid:%s'%(str(i))
#    print d.show()    
