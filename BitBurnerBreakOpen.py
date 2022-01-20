
# replstr = ''
# srstr = 'y.a.exploits'
# srstr = 'Bypass'
# srstr = 'PrototypeTampering'
# srstr = 'Unclickable'
# srstr = 'UndocumentedFunctionCall'
# srstr = 'TimeCompression'
# srstr = 'RealityAlteration'
# srstr = 'N00dles'
# srstr = 'EditSaveFile'
# srstr = 'saveScript'
'saveScript(t.fileName,t.code,e.player.currentServer,a.scripts)'

# srstr = 'hacking='
# srstr = '.isBanned'

srstr = 'TheRedPill'
# 'o.a.TheRedPill'
# srstr = 'TheRedPill,repCost:'
# 'r.a[i.a.TheRedPill].owned'
# srstr = 'augmentation'
# srstr = 'augmentations'
# srstr = 'reapplyAllAugmentations'

# illuminati
# srstr = '&&this.money>=15e10&&this.hacking>=1500&&this.strength>=1200&&this.defense>=1200&&this.dexterity>=1200&&this.agility>=1200'
# srstr = '&&t>=30'
# daedelus
# srstr = '1&&(this.hacking>=2500||this.strength>=1500&&this.defense>=1500&&this.dexterity>=1500&&this.agility>=1500)'
# srstr = '&&t>=Math.round(30*s.a.DaedalusAugsRequirement)'
# no redpill rep requirement
# srstr = 'TheRedPill,repCost:25e5,'
# replstr = 'TheRedPill,repCost:1,'
# superstart
# srstr = 'this.hacking=1,this.strength=1,this.defense=1,this.dexterity=1,this.agility=1,this.charisma=1,this.hacking_exp=0,this.strength_exp=0,this.defense_exp=0,this.dexterity_exp=0,this.agility_exp=0,this.charisma_exp=0,this.money=1e3'
# replstr = 'this.hacking=9e4,this.strength=9e4,this.defense=9e4,this.dexterity=9e4,this.agility=9e4,this.charisma=9e4,this.hacking_exp=9e999,this.strength_exp=9e99,this.defense_exp=9e99,this.dexterity_exp=9e99,this.agility_exp=9e99,this.charisma_exp=9e99,this.money=9e16'
# noreset
# srstr = '''{this.hacking=Math.max(1,Math.floor(this.calculateSkill(this.hacking_exp,this.hacking_mult*s.a.HackingLevelMultiplier))),this.strength=Math.max(1,Math.floor(this.calculateSkill(this.strength_exp,this.strength_mult*s.a.StrengthLevelMultiplier))),this.defense=Math.max(1,Math.floor(this.calculateSkill(this.defense_exp,this.defense_mult*s.a.DefenseLevelMultiplier))),this.dexterity=Math.max(1,Math.floor(this.calculateSkill(this.dexterity_exp,this.dexterity_mult*s.a.DexterityLevelMultiplier))),this.agility=Math.max(1,Math.floor(this.calculateSkill(this.agility_exp,this.agility_mult*s.a.AgilityLevelMultiplier))),this.charisma=Math.max(1,Math.floor(this.calculateSkill(this.charisma_exp,this.charisma_mult*s.a.CharismaLevelMultiplier))),this.intelligence>0?this.intelligence=Math.floor(this.calculateSkill(this.intelligence_exp)):this.intelligence=0;
# const e=this.hp/this.max_hp;
# this.max_hp=Math.floor(10+this.defense/10),this.hp=Math.round(this.max_hp*e)}'''
# replstr = '''{this.hacking=this.hacking*2,this.strength=this.strength+1,this.intelligence>0?this.intelligence=Math.floor(this.calculateSkill(this.intelligence_exp)):this.intelligence=0;
# const e=this.hp/this.max_hp;
# this.max_hp=Math.floor(10+this.defense/10),this.hp=Math.round(this.max_hp*e)}'''

printpad = 95

f = open('main.bundle.js', 'r')
data = f.read()
f.close()

nldata = data.replace(';',';\n')
nldata = nldata.replace(',',',\n')
c = nldata.count(srstr)
print(f'looking for {srstr}\n{c} occurances found')
idx = nldata.find(srstr)

# print(f'#### chr index is {idx} ####')
# eidx = nldata.find('}', idx+len(srstr))
# print(nldata[idx-2:eidx+2])
# idx = -1

while idx > 0:
    print(f'#### chr index is {idx} ####')
    # print(nldata[idx-printpad:idx+printpad])
    print(nldata[:idx *2 ])
    idx += 1
    idx = nldata.find(srstr, idx)
    idx = -1

# nldata = nldata.replace(srstr, replstr)
# data = nldata.replace(';\n',';')
#
# f = open('main.bundle.js', 'w')
# f.write(data)
# f.close()
