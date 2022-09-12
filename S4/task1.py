# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm',
#  'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch',
#  '', 'y', '', 'e', 'yu', 'ya']



# t = {'a':'а', 'b':'б', 'v':'в', 'g':'г', 'd':'д', 'e':'е', 'zh':'ж', 'z':'з', 'i':'и', 'y':'й', 'k':'к', 'l':'л', 'm':'м', 'n':'н', 'o':'о',
#     'p':'п', 'r':'р', 's':'с','t':'т', 'u':'у', 'f':'ф', 'kh':'х', 'ts':'ц', 'ch':'ч', 'sh':'ш', 'shch':'щ',"'":'ь', 'ie':'э', 'yu':'ю', 'ya':'я'}
# a = list(input())
# b = []
# for i in range(len(a)):
#     print(t[a[i]], end='')



t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

start_index = ord('а')
title = 'Переводим этот текст, сейчас!'
print(title.lower())

slug = ""
for s in title.lower():

	if "а" <= s <= "я":
		slug += t[ord(s) - ord('а')]
	
	else:
		slug += s



print(slug)
