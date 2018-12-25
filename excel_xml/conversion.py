
class Pinyin():
    def __init__(self, data_path='Mandarin.dat'):
        self.dict = {}
        for line in open(data_path):
            k, v = line.split('\t')
            self.dict[k] = v
        self.splitter = ''
    def get_pinyin(self, chars=u"你好吗"):
        result = []
        for char in chars:
            key = "%X" % ord(char)
            try:
                result.append(self.dict[key].split(" ")[0].strip()[:-1].lower())
            except:
                result.append(char)
        return self.splitter.join(result)
    def get_initials(self, char=u'你'):
        try:
            print(self.dict["%X" % ord(char)])
            return self.dict["%X" % ord(char)].split(" ")[0][0]
        except:
            return char
s="余"
P=Pinyin()

print(P.get_initials(s))


# def get_initials(self, chars=u'你好', splitter=u'-'):
#     result = []
#     flag = 1
#     for char in chars:
#         try:
#             result.append(self.dict["%X" % ord(char)].split(" ")[0][0])
#             flag = 1
#         except KeyError:
#             if flag:
#                 result.append(char)
#             else:
#                 result[-1] += char
#
#     return splitter.join(result)
# print(get_initials(s,""))