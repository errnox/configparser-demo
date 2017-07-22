import ConfigParser, os

class ConfigParserTest(object):
    def __init__(self):
        self.configParser = ConfigParser.ConfigParser()
        self.CACHEDCONFIG = 'cache'

    def run(self):
        self.configParser.read(open('testConfig.cfg'))
        self.configParser.read('testConfig.cfg')
        sections = self.configParser.sections() # List of all sections


        self._hline()
        for section in sections:
            items = self.configParser.items(section)
            self._frame(section)

            for item in items:
                print "%-20s %-20s =        %-20s" % ("", item[0], item[1])
            self._hline()

        # Write a representation of the configuration to a file for future use
        # (readable with ConfigParser.read())
        with open(self.CACHEDCONFIG, 'w+') as cacheFile:
            self.configParser.write(cacheFile)

    def readCachedConfig():
        """
        Read back the cached version of the parsed configuration
        file so that the configuration file does not have to be
        reparsed.
        """
        self.ConfigParser.read(self.CACHEDCONFIG)

    def _frame(self, string, frameChar="%"):
            print frameChar * int(len(string) + 4)
            print frameChar, string, frameChar
            print frameChar * int(len(string) + 4)

    def _hline(self, lineChar="-"):
            print lineChar * 80

if __name__ == '__main__':
    configParserTest = ConfigParserTest()
    configParserTest.run()

