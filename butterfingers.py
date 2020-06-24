from random import randint
import random

class Butterfinger:
	def __init__(self, prob=0.1):
		self._keyapprox = {}
		self.generate_approx()

	def generate_approx(self):
		self._keyapprox['q'] = 'qwasedzx'
		self._keyapprox['w'] = 'wqesadrfcx'
		self._keyapprox['e'] = 'ewrsfdqazxcvgt'
		self._keyapprox['r'] = 'retdgfwsxcvgt'
		self._keyapprox['t'] = 'tryfhgedcvbnju'
		self._keyapprox['y'] = 'ytugjhrfvbnji'
		self._keyapprox['u'] = 'uyihkjtgbnmlo'
		self._keyapprox['i'] = 'iuojlkyhnmlp'
		self._keyapprox['o'] = 'oipklujm'
		self._keyapprox['p'] = 'plo[\'ik'
		self._keyapprox['a'] = 'aqszwxwdce'
		self._keyapprox['s'] = 'swxadrfv'
		self._keyapprox['d'] = 'decsfaqgbv'
		self._keyapprox['f'] = 'fdgrvwsxyhn'
		self._keyapprox['g'] = 'gtbfhedcyjn'
		self._keyapprox['h'] = 'hyngjfrvkim'
		self._keyapprox['j'] = 'jhknugtblom'
		self._keyapprox['k'] = 'kjlinyhn'
		self._keyapprox['l'] = 'lokmpujn'
		self._keyapprox['z'] = 'zaxsvde'
		self._keyapprox['x'] = 'xzcsdbvfrewq'
		self._keyapprox['c'] = 'cxvdfzswergb'
		self._keyapprox['v'] = 'vcfbgxdertyn'
		self._keyapprox['b'] = 'bvnghcftyun'
		self._keyapprox['n'] = 'nbmhjvgtuik'
		self._keyapprox['m'] = 'mnkjloik'
		self._keyapprox[' '] = ' '


	def misspell(self, text, prob=0.1):
		probOfTypo = int(prob * 100)

		buttertext = []
		for letter in text:
			newletter = letter.lower()
			if not letter in self._keyapprox.keys():
				newletter = letter
			else:
				if random.choice(range(0, 100)) <= probOfTypo:
					newletter = random.choice(self._keyapprox[letter])
			buttertext.append(newletter)

		return ''.join(buttertext).lower()
