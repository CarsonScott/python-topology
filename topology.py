class Object:
	def __init__(self, **kwargs):
		for arg in kwargs:
			setattr(self, arg, kwargs[arg])

class Template(dict):
	def __init__(self, *args, **kwargs):
		for arg in args:
			self[arg]=None
		for arg in kwargs:
			self[arg]=kwargs[arg]

	def __call__(self, *args, **kwargs):
		data=dict()
		keys=list(self.keys())
		for i in self:data[i]=self[i]
		for i in kwargs:data[i]=kwargs[i]
		for i in range(len(args)):data[keys[i]]=args[i]
		output=Object(**data)
		return output

class Topology:
	def __init__(self, node_template=Template(), link_template=Template()):
		self.node_template=node_template
		self.link_template=link_template
		self.sources={}
		self.targets={}
		self.nodes={}
		self.links={}

	def create_node(self, key, *args, **kwargs):
		node=self.node_template(*args, **kwargs)
		self.nodes[key]=node
		self.sources[key]=[]
		self.targets[key]=[]

	def create_link(self, src, tar, *args, **kwargs):
		link=self.link_template(*args, **kwargs)
		key=(src,tar)
		self.links[key]=link
		self.sources[tar].append(src)
		self.targets[src].append(tar)

	def remove_link(self, src, tar):
		key=(src,tar)
		del self.links[key]
		self.sources[tar].remove(src)
		self.targets[src].remove(tar)

	def remove_node(self, key):
		del self.nodes[key]
		for src in self.sources[key]:self.remove_link(src, key)
		for tar in self.targets[key]:self.remove_link(key, tar)
		del self.sources[key]
		del self.targets[key]

	def get_node(self, key):
		return self.nodes[key]

	def get_link(self, src, tar):
		key=(src,tar)
		return self.links[key]

	def get_sources(self, key):
		return self.sources[key]

	def get_targets(self, key):
		return self.targets[key]
