def encode(plain_text):
	text=plain_text.lower()
	text=text.replace(' ', '')
	text=text.replace(',', '')
	text=text.replace('.', '')
	text=text.replace('!', '')
	text=text.strip()

	dic = {'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}

	cipher = ""

	c = 0
	for i in text:
		if i.isdigit():
			cipher = cipher + i
			c=c+1

			if c==5:
				cipher=cipher+" "
				c=0

			else:
				continue

		else:
			cipher = cipher + dic[i]
			c = c + 1

			if c == 5:
				cipher = cipher + " "
				c = 0

			else:
				continue

	return cipher.strip()


def decode(ciphered_text):
	cipher=ciphered_text.replace(" ", '')
	dic={'z':'a','y':'b','x':'c','w':'d','v':'e','u':'f','t':'g','s':'h','r':'i','q':'j','p':'k','o':'l','n':'m','m':'n','l':'o','k':'p','j':'q','i':'r','h':'s','g':'t','f':'u','e':'v','d':'w','c':'x','b':'y','a':'z'}
	text=''
	for i in cipher:
		if i.isdigit():
			text=text+i
		else:
			text=text+dic[i]

	return text