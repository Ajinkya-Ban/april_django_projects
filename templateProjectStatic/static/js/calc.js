function clearFields()
{
    document.getElementById('n1').value = "";
    document.getElementById('n2').value = "";
    document.getElementById('res').value = "";
    document.getElementById('op').value="select";
    document.getElementById('n1').focus();
}

function focusCursor()
{
    document.getElementById('n1').focus();
}

function checkEmptyFields()
{
    if(document.getElementById('n1').value == "")
    {
        alert("Please enter first number");
        document.getElementById('n1').focus();
        return false
        // document.getElementById('n1').style.borderColor="red";
    }
    else if(document.getElementById('n2').value == "")
    {
        alert("Please enter second number");
        document.getElementById('n2').focus();
        return false
    }
    else if(document.getElementById('op').value == 'select')
    {
        alert('Please select at least one operation');
        document.getElementById('op').focus();
        return false
    }
    return true
}

function doTask()
{
    checkEmptyFields();

    var num1 = document.getElementById('n1').value;
    var num2 = document.getElementById('n2').value;
    var drp = document.getElementById('op').value;
    switch(drp)
    {
        case '+':
            var res = parseInt(num1) + parseInt(num2);
            document.getElementById('res').value = res;
            break;
        
        case '-':
            var res = parseInt(num1) - parseInt(num2);
            document.getElementById('res').value = res;
            break;

         case '*':
            var res = parseInt(num1) * parseInt(num2);
            document.getElementById('res').value = res;
            break;

        case '/':
            var res = parseInt(num1) / parseInt(num2);
            document.getElementById('res').value = res;
            break;

    }

}


