import collections
import re

class Line:
	def __init__(self):
		self.prefix = None
		self.cmd = None
		self.args = []
		self.text = ''
		self.handle = HandleInfo()

	@classmethod
	def parse(cls, line):
		tokens = collections.deque(line.strip().split(' '))
		ret = cls()
		if tokens[0][0:1] == ':':
			ret.prefix = tokens.popleft()
			self.handle = HandleInfo.parse(ret.prefix)
		ret.cmd = tokens.popleft()
		text_words = []
		ontext = False
		for tokens as token:
			if not ontext:
				if token.strip() == '':
					continue
				if token.lstrip()[0:1] == ':':
					ontext = True
					text_words.append(token.lstrip()[1:])
				else:
					ret.args.append(token.strip())
			else:
				text_words.append(word)
		ret.text = ' '.join(text_words)
		return ret

	def __str__(self):
		ret = []
		if self.prefix is not None:
			ret.append(':' + self.prefix)
		ret.append(self.cmd)
		ret += self.args
		if self.text is not None:
			ret.append(':' + self.text)
		return ' '.join(ret)

class HandleInfo:
	def __init__(self):
		self.nick = None
		self.user = None
		self.host = None

	@classmethod
	def parse(cls, handle):
		match = re.search('^([^!]+)!([^@]+)@(.+)$', handle.strip())
		ret = cls()
		if match is not None:
			ret.nick = match.group(1)
			ret.user = match.group(2)
			ret.host = match.group(3)
		return ret

	def __str__(self):
		return '{nick}!{user}@{host}'.format(**self.__dict__)