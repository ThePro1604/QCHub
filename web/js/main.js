//private tools
document.getElementById("Duplicator_script").addEventListener("click", ()=>{eel.Duplicator_script()}, false);
document.getElementById("ExcelCells2Files_script").addEventListener("click", ()=>{eel.ExcelCells2Files_script()}, false);
document.getElementById("FileList_script").addEventListener("click", ()=>{eel.FileList_script()}, false);
document.getElementById("IDnJsonResults2Excel_script").addEventListener("click", ()=>{eel.IDnJsonResults2Excel_script()}, false);
document.getElementById("Jsons2Excel_script").addEventListener("click", ()=>{eel.Jsons2Excel_script()}, false);
document.getElementById("NameScrambler_script").addEventListener("click", ()=>{eel.NameScrambler_script()}, false);
document.getElementById("NameSwitcher_script").addEventListener("click", ()=>{eel.NameSwitcher_script()}, false);
document.getElementById("PDF2JPG_script").addEventListener("click", ()=>{eel.PDF2JPG_script()}, false);
document.getElementById("JsonAge2Excel_script").addEventListener("click", ()=>{eel.JsonAge2Excel_script()}, false);
document.getElementById("JsonFaceLiveness2Excel_script").addEventListener("click", ()=>{eel.JsonFaceLiveness2Excel_script()}, false);
document.getElementById("POAnJsonResults2Excel_script").addEventListener("click", ()=>{eel.POAnJsonResults2Excel_script()}, false);
document.getElementById("DoubleDisplay_script").addEventListener("click", ()=>{eel.DoubleDisplay_script()}, false);
document.getElementById("JPEGConverter_script").addEventListener("click", ()=>{eel.JPEGConverter_script()}, false);
document.getElementById("QCPrep_script").addEventListener("click", ()=>{eel.QCPrep_script()}, false);
document.getElementById("BatchCleanser_script").addEventListener("click", ()=>{eel.BatchCleanser_script()}, false);
document.getElementById("SetCreator_script").addEventListener("click", ()=>{eel.SetCreator_script()}, false);
document.getElementById("JsonExtractor_script").addEventListener("click", ()=>{eel.JsonExtractor_script()}, false);
document.getElementById("DBRemover_script").addEventListener("click", ()=>{eel.DBRemover_script()}, false);

//tools by other people
document.getElementById("ImageCollector_script").addEventListener("click", ()=>{eel.ImageCollector_script()}, false);
document.getElementById("FileScrambler_script").addEventListener("click", ()=>{eel.FileScrambler_script()}, false);
document.getElementById("FormatClientDemoExcel_script").addEventListener("click", ()=>{eel.FormatClientDemoExcel_script()}, false);
document.getElementById("FilesToSubDirectories_script").addEventListener("click", ()=>{eel.FilesToSubDirectories_script()}, false);
document.getElementById("TemplateExcelGenerator_script").addEventListener("click", ()=>{eel.TemplateExcelGenerator_script()}, false);

//links and management codes
document.getElementById("MoveFiles_script").addEventListener("click", ()=>{eel.MoveFiles_script()}, false);
document.getElementById("SendMail_script").addEventListener("click", ()=>{eel.SendMail_script()}, false);
document.getElementById("UpdateTool_script").addEventListener("click", ()=>{eel.UpdateTool_script()}, false);



eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}
