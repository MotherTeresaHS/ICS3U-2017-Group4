import ConfigParser, os
config = ConfigParser.ConfigParser()
config.readfp(open('./config.txt'))

#config = ConfigParser(self)
#config.add_section('Settings')

print(config.sections())
#config.set('Settings','Sensitivity','1')
if config.has_option('Settings', 'Sensitivity'):
    print(config.get('Settings','Sensitivity','99'))
else:
    print(config.set('Settings','Sensitivity','99'))

print(config.get('Settings','Sensitivity'))

print(config.get('Scores','Score1'))
print(config.get('Scores','User1'))
