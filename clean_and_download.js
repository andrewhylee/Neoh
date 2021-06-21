(function(console){

    console.save = function(data, filename){
    
        if(!data) {
            console.error('Console.save: No data')
            return;
        }
    
        if(!filename) filename = 'console.json'
    
        if(typeof data === "object"){
            data = JSON.stringify(data, undefined, 4)
        }
    
        var blob = new Blob([data], {type: 'text/json'}),
            e    = document.createEvent('MouseEvents'),
            a    = document.createElement('a')
    
        a.download = filename
        a.href = window.URL.createObjectURL(blob)
        a.dataset.downloadurl =  ['text/json', a.download, a.href].join(':')
        e.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
        a.dispatchEvent(e)
     }
    })(console)

classes = temp1
// console.save(classes, "ClassesFromMatrix.json")

classes2 = []

for (var i = 0; i < classes.length; i++){
    if(classes[i].typeOfSession == "ClassSession" ){
        classes2.push( {
            className: classes[i].className,
            sessionCount: classes[i].session.sessionCount,
            studentName: classes[i].studentName,
            teacherName: classes[i].teacherName,
            curriculumLevel: classes[i].session.curriculumLevel,
            sessionNumber: classes[i].sessionNumber,
        } )
    }
}

var cleaned_classes = classes2.filter((a_class, index, self) =>
index === self.findIndex((t) => (t.className === a_class.className && t.studentName === a_class.studentName)))

var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
today = mm + '_' + dd + '_' + yyyy;

console.save(cleaned_classes, `CleanedClassesFromMatrix${today}.json`)