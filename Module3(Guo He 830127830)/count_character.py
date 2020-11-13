import pprint

message = """Peter aslkdj alksjdlka alksdj alksdj laksjd laksdj aslkdj aslkdj
             aklsjdlk aslkdj askldj alksdj asldkj aslkdj aslkdja alskjd aslkd
             askljdklajskldjlaksjd alskdjaj aksljdl """
thisset = {"apple", "banana", "cherry"}
count = {}
cou = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

for cha in thisset:
    cou.setdefault(cha,0)
    cou[cha] = cou[cha] + 1
    
pprint.pprint(count)
pprint.pprint(cou)