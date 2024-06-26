//initial variables
var loanYear = 1;
var stepYear = 1;
var maxLoanYear = 5;
var paymentCycle = 1;
var monthlyRepayment = 0;
var monthlyInterest = 0;
var amortData = [];

//start up method
$(function(){
    $(".ul-buttons li").click(function(){
        $(".ul-buttons li").removeClass("selected");
        $(this).addClass("selected");
        paymentCycle = parseInt($(this).attr("data-value"));
        calculateLoan();
    });

    //Add on blur event
    $("#txtLoan, #txtInterest").on("blur", function(){
        //Perform a check if loan or interest value has been entered invalid value, if it is, set the default value
        if(isNaN($("#txtLoan").val())) {
            $("#txtLoan").val(100000);
        }

        if(isNaN($("#txtInterest").val())) {
            $("#txtInterest").val(10.0);
        }
        calculateLoan();
    });
});

//create the noUiSlider
var range = document.getElementById('yearRange');
noUiSlider.create(range, {
    range: {
        'min': 1,
        'max': maxLoanYear
    },
    step: stepYear,
    start: [loanYear],
    margin: 300,
    connect: true,
    direction: 'ltr',
    orientation: 'horizontal',
    pips: {
        mode: 'steps',
        stepped: false,
        density: 1
    }
});

//Add the change event to redraw the graph and calculate loan
range.noUiSlider.on("change", function(value){
    loanYear = parseInt(value[0]);
    calculateLoan();
});

//Chart
google.charts.load('current', {'packages':['corechart']});
function drawChart() {
    //Hold the loan data array
    var loanData = [];

    var dt = new Date();
    var yearCounter = 1;

    //Add the graph header
    var headerData = ['Year', 'Interest', 'Interest & Principal', 'Balance'];
    loanData.push(headerData);

    for(var i = dt.getFullYear(); i < dt.getFullYear() + loanYear; i++){
        loanData.push([i.toString(), getAmortData("interest", 12 * yearCounter), monthlyRepayment * 12 * yearCounter, getAmortData("balance", 12 * yearCounter)]);
        yearCounter++;
    }

    var data = google.visualization.arrayToDataTable(loanData);

    var options = {
      title: 'Loan Chart',
      hAxis: {title: 'Year',  titleTextStyle: {color: '#333'}},
      vAxis: {minValue: 0},
      pointsVisible: true
    };

    var chart = new google.visualization.AreaChart(document.getElementById('graph-chart'));
    chart.draw(data, options);
}

//Get amortization data based on type and terms
function getAmortData(dataType, terms){
    var dataValue = 0;
    switch(dataType){
        case "interest":
            for(var i = 0; i < terms; i++){
                dataValue += parseFloat(amortData[i].Interest);
            }
            break;
        case "balance":
            dataValue = parseFloat(amortData[terms-1].Balance);
            break;
    }
    return Math.round(dataValue);
}

//calculate function
function calculateLoan(){
    $("#year-value").html(loanYear);
    var loanBorrow = parseFloat($("#txtLoan").val());
    var interestRate = parseFloat($("#txtInterest").val()) / 1200;
    var totalTerms = 12 * loanYear;

    //Monthly
    var schedulePayment = Math.round(loanBorrow * interestRate / (1 - (Math.pow(1/(1 + interestRate), totalTerms))));
    monthlyRepayment = schedulePayment;
    var totalInterestPay = totalTerms * schedulePayment;
    amort(loanBorrow, parseFloat($("#txtInterest").val())/100, totalTerms);


    $("#repayment-value").html(schedulePayment);
    $("#interest-total").html(getAmortData("interest", totalTerms));
    monthlyInterest = (totalInterestPay - loanBorrow) / totalTerms;
    google.charts.setOnLoadCallback(drawChart);
}

calculateLoan();

//function to calculate the amortization data
function amort(balance, interestRate, terms)
{
    amortData = [];

    //Calculate the per month interest rate
    var monthlyRate = interestRate/12;

    //Calculate the payment
    var payment = balance * (monthlyRate/(1-Math.pow(1+monthlyRate, -terms)));

    for (var count = 0; count < terms; ++count)
    {
        var interest = balance * monthlyRate;
        var monthlyPrincipal = payment - interest;
        var amortInfo = {
            Balance: balance.toFixed(2),
            Interest: balance * monthlyRate,
            MonthlyPrincipal: monthlyPrincipal
        }
        amortData.push(amortInfo);
        balance = balance - monthlyPrincipal;
    }
}