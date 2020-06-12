import plistlib
import json
import FileManager
import GraphManager

projectPath = '/Users/romanmisnikov/work/xcode.projects/yota/yota-ios'
path = '/Users/romanmisnikov/work/xcode.projects/yota/yota-ios/selfcare/Application/selfcare.xcodeproj/project.pbxproj'


# Поиск всех файлов с окончанием '.pbxproj'
def findXcodeProjectsInDirectory(path):
    files = list()
    filePaths = FileManager.getListOfFiles(projectPath)
    for path in filePaths:
        if path.endswith('.pbxproj'):
            files.append(path)
    return files


def projectNameFromPbxproj(path):
    return filePath.split('/')[-2]


# Анализ строки из файла *.xcodeproj на наличие упоминания файлов *.framework в папке Frameworks
def getFrameworkName(line):
    # from '8526126524354C130097CB4F /* YotaPay.framework in Frameworks */ = {isa ...'
    leftSide = line.split('.framework')[0]
    # YotaPay
    name = leftSide.split('*')[-1].strip()
    return name


# Получить все зависимости из файла *.xcodeproj
def dependenciesFromXcodeProject(path):
    # Анализ файла по строкам
    dependencies = set()
    for line in FileManager.readToLinesFile(filePath):
        index = line.find('.framework in Frameworks')
        if index >= 0:
            name = getFrameworkName(line)
            dependencies.add(name)
    return dependencies


projectsFiles = findXcodeProjectsInDirectory(projectPath)
for filePath in projectsFiles:
    framework = projectNameFromPbxproj(filePath)
    dependencies = dependenciesFromXcodeProject(filePath)
    print(framework)
    print(dependencies)




# Build a dataframe with 4 connections
# graph = {'from': ['Core', 'Platform', 'PushNotifications', 'Deeplinks'],
#          'to':   ['PushNotifications', 'ApplicationContracts', 'Deeplinks', 'Core']}
# TestGraph.showGraph(graph)



