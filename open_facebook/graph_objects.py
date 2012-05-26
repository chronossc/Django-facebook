from open_facebook.utils import is_valid_id

class FBObject(object):
    # generic class to support fb objects.
    _api = None
    data = {}

    def __init__(self,api,data):
        self._api = api
        self.data = data

    def __getattr__(self,name):

        if name in self.data:
            return self.data[name]
        else:
            raise AttributeError,"'%s' object has no attribute '%s'" % (
                self.__class__.__name__,name)

    def reload(self):
        raise NotImplementedError,u"You should implement 'reload' for class '%s' so we can reload object." % \
                self.__class__.__name__

    def get_fbid(self):
        raise NotImplementedError,u"You should implement 'get_fbid' for class '%s'" % \
                self.__class__.__name__
    id = property(get_fbid)

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,self.id)

    def comment(self,message):
        return self._api.comments(target=self.id,message=message)

    def like(self):
        return self._api.likes(target=self.id)



class FBPostObject(FBObject):
    """
    Represents a post as one class. Sample post:

    u'application': {u'id': u'219495651417520',
      u'name': u'test app 2',
      u'namespace': u'chronos_testapp'},
     u'caption': u'link caption',
     u'comments': {u'count': 1,
      u'data': [{u'created_time': u'2012-05-25T03:02:11+0000',
        u'from': {u'id': u'792386736', u'name': u'Felipe Rafael Prenholato'},
        u'id': u'792386736_10150941254716737_22437877',
        u'message': u'bla'}]},
     u'created_time': u'2012-05-25T02:49:47+0000',
     u'description': u'Development done the right way',
     u'from': {u'id': u'792386736', u'name': u'Felipe Rafael Prenholato'},
     u'icon': u'http://www.facebook.com/images/icons/default_app_icon.gif',
     u'id': u'792386736_10150941254716737',
     u'likes': {u'count': 1,
      u'data': [{u'id': u'792386736', u'name': u'Felipe Rafael Prenholato'}]},
     u'link': u'http://devwithpassion.com/',
     u'message': u'testing django facebook openfacebook api with public post and links',
     u'name': u'Dev With Passion',
     u'picture': u'https://www.facebook.com/app_full_proxy.php?app=219495651417520&v=1&size=z&cksum=4b4faeda131dfdf91615c98c16a56e30&src=http%3A%2F%2Fdevwithpassion.com%2Fwp-content%2Fuploads%2F2011%2F09%2Femprego_certo.gif',
     u'type': u'link',
     u'updated_time': u'2012-05-25T03:02:11+0000'
    """

    def get_fbid(self):
        return self.data['id']
    id = property(get_fbid)

    def reload(self):
        self = self._api.post(self.id)

class FBCommentObject(FBObject):
    """
    {u'can_remove': True,
     u'created_time': u'2012-05-26T01:09:37+0000',
     u'from': {u'id': u'792386736', u'name': u'Felipe Rafael Prenholato'},
     u'id': u'792386736_10150941254716737_22449464',
     u'message': u'ha!'}
    """
    def get_fbid(self):
        return self.data['id']
    id = property(get_fbid)

    def reload(self):
        self = self._api.comment(self.id)

    def comment(self,*args,**kwargs):
        raise TypeError,u"Comments can't be commented."

class FBLikeObject(FBObject):
    def get_fbid(self):
        raise TypeError,u"Lilkes don't have a ID. Info of who liked are in liked object."

    def reload(self):
        raise TypeError,u"Likes can't be reloaded. Info of who liked are in liked object."

    def comment(self):
        raise TypeError,u"Likes can't be commented. Info of who liked are in liked object."

    def like(self):
        raise TypeError,u"Likes can't be liked. Info of who liked are in liked object."