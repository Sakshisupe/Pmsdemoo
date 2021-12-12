function searchrecords()
{
    var input , table , tr , td ,td1 , filter , i , txtdata ,txtdata1;
    input = document.getElementById("searchtxt");
    filter = input.value.toUpperCase();
    table = document.getElementById("table1");
    tr = table.getElementsByTagName("tr");

    for( i=0;i<tr.length;i++)
    {
        td = tr[i].getElementsByTagName("td")[1];
        td1 = tr[i].getElementsByTagName("td")[2];

        if(td || td1)
        {

            txtdata = td.innerText;
            txtdata1 = td1.innerText;
            if(txtdata.toUpperCase().indexOf(filter)>-1 || txtdata1.toUpperCase().indexOf(filter)>-1)
            {
                tr[i].style.display="";
            }
            else
            {
                tr[i].style.display="none";
            }

        }
    }
}