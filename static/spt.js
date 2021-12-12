var pdf = document.forms['myform']['project_report'];
var validext=[pdf];



function validation()
{
    if(pdf.value!='')
    {
       
        var pdf_ext=pdf.value.substring(pdf.value.lastIndexOf('.')+1);
        var result=validext.includes(pdf_ext);
        if(result==false)
        {
            alert("Selected file is not a PDF");
            return false;
        }
        else
        {

            const fi = document.getElementById('file');
            // Check if any file is selected.
            if (fi.files.length > 0) {
                for (const i = 0; i <= fi.files.length - 1; i++) {
      
                    const fsize = fi.files.item(i).size;
                    const file = Math.round((fsize / 1024));
                    // The size of the file.
                    if (file >= 4096) {
                        alert(
                          "File too Big, please select a file less than 4mb");
                          return false;
                    } 
                    else {
                        document.getElementById('size').innerHTML = '<b>'
                        + file + '</b> KB';
                    }
                }
            }
        }
           
        }
    
    else{
        alert(" PDF not Selected");
        return false;
    }
return true;
}