from .object import Object
from .member import Member

class Base(Object):
	"""Base object for message-esque objects"""
	
	__slots__ = []
	
	def __init__(self, **kwargs):
		super(Base, self).__init__(**kwargs)
		
		self.attachments = self._attachments(kwargs.pop('attachments'))
		self.created_at = kwargs.pop('created_at')
		self.id = kwargs.pop('id')
		self.text = kwargs.pop('text')
	
	def _attachments(self, attachments):
		"""TEMPORARY UNTIL ATTACHMENT OBJECTS ARE BUILT"""
		
		return attachments
	
	def __str__(self):
		return self.text

class Preview(Base):
	"""Represents :class:`Group` message previews
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two previews are equal.    |
	+-----------+--------------------------------------+
	| x != y    | Checks if two previews are not equal.|
	+-----------+--------------------------------------+
	| hash(x)   | Returns the preview's hash.          |
	+-----------+--------------------------------------+
	| str(x)    | Returns the preview's text.          |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	attachments : list
		A list of attachments
	author : str
		The name of the author
	author_image : str
		URL to the author's image_url
	created_at : int
		Unix time-stamp when the preview was created
	text : str
		The preview's contents
	"""
	
	__slots__ = [
				'attachments', 'author', 'author_image', 'created_at', 'id',
				'text'
				]
	
	def __init__(self, **kwargs):
		super(Preview, self).__init__(**kwargs)
		
		self.author = kwargs.pop('nickname')
		self.author_image = kwargs.pop('author_image')

class Message(Base):
	"""Represents Group Me messages
	
	Supported Operations:
	
	+-----------+--------------------------------------+
	| Operation |             Description              |
	+===========+======================================+
	| x == y    | Checks if two messages are equal.    |
	+-----------+--------------------------------------+
	| x != y    | Checks if two messages are not equal.|
	+-----------+--------------------------------------+
	| hash(x)   | Returns the message's hash.          |
	+-----------+--------------------------------------+
	| str(x)    | Returns the message's text.          |
	+-----------+--------------------------------------+
	
	Attributes
	----------
	attachments : list
		A list of attachments
	author : str
		The name of the author
	created_at : int
		Unix time-stamp when the message was created
	favorite_by : list
		list of member IDs that have favorite the message
	group : :class:`Group`
		The group the message is from
	id : str
		ID of the message
	is_system : bool
		Whether the author is the Group Me system
	source_guid : str
		The GUID from the message's author's client
	text : str
		The Message's contents
	"""
	
	__slots__ = [
				'attachments', 'author', 'created_at', 'favorited_by', 'group',
				'id', 'is_system', 'source_guid', 'text'
				]
	
	def __init__(self, **kwargs):
		super(Message, self).__init__(**kwargs)

		author = {}
		author['nickname'] = kwargs.pop('name')
		author['image_url'] = kwargs.pop('avatar_url')
		author['user_id'] = kwargs.pop('user_id')
		author['autokicked'] = None
		author['muted'] = None
		author['id'] = None

		self.author = Member(**author)
		
		self.favorited_by = kwargs.pop('favorited_by')
		self.group = self._get_group(kwargs.pop('group_id'))
		self.is_system = kwargs.pop('system')
		self.source_guid = kwargs.pop('source_guid')

	def _get_group(self, group_id):
		"""TEMPORARY UNTIL AIOHTTP STUFF IS BUILT"""

		return group_id
