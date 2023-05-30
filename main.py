import os
import webbrowser

import eel
import win32gui

eel.init('C:\QCCenter\QCHub\web')


@eel.expose
def Duplicator_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\Duplicator.bat")


@eel.expose
def ExcelCells2Files_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\ExcelCells2Files.bat")


@eel.expose
def FileList_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\FileList.bat")


@eel.expose
def Jsons2Excel_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\Jsons2Excel.bat")


@eel.expose
def NameScrambler_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\NameScrambler.bat")


@eel.expose
def NameSwitcher_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\NameSwitcher.bat")


@eel.expose
def PDF2JPG_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\PDF2JPG.bat")


@eel.expose
def DoubleDisplay_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\DoubleDisplay.bat")


@eel.expose
def JPEGConverter_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\JPEGConverter.bat")


@eel.expose
def QCPrep_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\QCPrep.bat")


@eel.expose
def BatchCleanser_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\BatchCleanser.bat")


@eel.expose
def SetCreator_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\SetCreator.bat")


@eel.expose
def JsonExtractor_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\JsonExtractor.bat")


@eel.expose
def DBRemover_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\DBRemover.bat")


@eel.expose
def Condenser_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\Condenser.bat")


@eel.expose
def ImageCollector_script():
    os.startfile("N:\\Images\\Nadav\\scripts\\imgcl 13.06.21\\ImageCollector.exe")


@eel.expose
def FileScrambler_script():
    os.startfile("N:\\Images\\Nadav\\scripts\\FileScrambler\\FileScrambler.exe")


@eel.expose
def FormatClientDemoExcel_script():
    os.startfile("N:\\Images\\Nadav\\scripts\\FormatClientDemoExcel\\PowershellInvoke.exe")


@eel.expose
def FilesToSubDirectories_script():
    os.startfile("N:\\Images\\Nadav\\scripts\\FilesToSubDirectories\\FilesToSubDirectories.exe")


@eel.expose
def MoveFiles_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\MoveFiles.bat")


@eel.expose
def QualityTool_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\QualityControl.lnk")


@eel.expose
def SendMail_script():
    os.startfile("C:\\QCCenter\\BatchFiles\\SendMail.bat")


@eel.expose
def UpdateTool_script():
    os.startfile("N:\\Images\\Shahaf\\Projects\\ToolBoxUpdater\\ToolBoxUpdater.bat")


@eel.expose
def TemplateExcelGenerator_script():
    webbrowser.open("N:\\Images\\Shahaf\\Projects\\TemplateExcelGenerator")

# @eel.expose
# def POAnJsonResults2Excel_script():
#     os.startfile("C:\\QCCenter\\BatchFiles\\POAnJsonResults2Excel.bat")


# @eel.expose
# def JsonAge2Excel_script():
#     os.startfile("C:\\QCCenter\\BatchFiles\\JsonAge2Excel.bat")


# @eel.expose
# def JsonFaceLiveness2Excel_script():
#     os.startfile("C:\\QCCenter\\BatchFiles\\JsonFaceLiveness2Excel.bat")


# @eel.expose
# def IDnJsonResults2Excel_script():
#     os.startfile("C:\\QCCenter\\BatchFiles\\IDnJsonResults2Excel.bat")


try:
    import pyi_splash

    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()
except:
    pass

eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')
eel.start('index.html', size=(950, 900), position=(50, 50), app_mode=True, port=1604)
