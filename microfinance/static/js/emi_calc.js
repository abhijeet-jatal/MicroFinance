$(document).ready(function () {
  calValidation(); /*empty feild validation*/
  /*calling function for individual range sliders*/
  /*parameters to be set obj(dom selector), grid and year are boolean values----------*/
  /*eligibility range SliderInitiation(obj, min, max, from, step, grid, year)---------*/

  if ($('input[name="slider"]').length) {
    calculatorRangeSlider(
      $("#loanAmtSlider"),
      50000,
      1500000,
      50000,
      1000,
      true,
      false,
      false,
      "loanAmtSlider"
    );
    calculatorRangeSlider(
      $("#tensureSlider"),
      12,
      60,
      12,
      1,
      true,
      true,
      false,
      "tensureSlider"
    );
    calculatorRangeSlider(
      $("#intrRateSlider"),
      10.49,
      24,
      10.49,
      0.5,
      true,
      false,
      true,
      "intrRateSlider"
    );
  }

  updateSlider(); /*on load and recursive function for remove common from numeric value and update range slider*/
  $(".inpt").each(function () {
    $(this).on("focus", function () {
      $(this).val($(this).val().replace(/[,]/g, ""));
      ".inpt-slider".find(".inpt").val(numberFormatter(data.from) + "%");
    });
    calEMIval();
  });

//  $(document).on("blur change", ".txtBox", function () {
//    validateNetWeight($(this));
//  });
//  Amortization();
});

function updateSlider() {
  $(".inpt").each(function () {
    $(this).on("change", function () {
      valuetoassignComa = $(this).val();
      valuetoassign = valuetoassignComa.replace(/[,]/g, ""); //12th Sep 2016
      slidertochange = $(this)
        .parents(".inpt-statement")
        .siblings(".irs-hidden-input")
        .prop("id");
      slidertoupdate = $("#" + slidertochange).data("ionRangeSlider");
      slidertoupdate.update({
        from: parseInt(valuetoassign),
      });
    });
  });
}

function calculatorRangeSlider(obj, min, max, from, step, grid, year, percentage, objName)
{
  var $range = obj;
  $range.ionRangeSlider({
    type: "single",
    min: min,
    max: max,
    from: from,
    step: step,
    grid: grid,
    skin: "round",
    prettify_enabled: true,

    prettify: function (num) {
      if (year == true) {
        //num = (num < 2 ? num + " Yr" : num + " Yrs");
        return num;
      } else if (percentage == true) {
        num = num + "%";
        return num;
      } else {
        return rangenumDifferentiation(num);
      }
    },
    onStart: function (data) {
      if (objName == "intrRateSlider")
        $range
          .parent(".inpt-slider")
          .find(".inpt")
          .val(numberFormatter(data.from) + "%");
      else
        $range
          .parent(".inpt-slider")
          .find(".inpt")
          .val(numberFormatter(data.from));
    },
    onFinish: function (data) {
      $range.parent(".inpt-slider").find(".inpt").trigger("blur");
      calEMIval();
    },
  });

  $range.on("change", function () {
    var $this = $(this),
      value = $this.prop("value");
    if ($this.prop("id") == "intrRateSlider")
      $this
        .parent(".inpt-slider")
        .find(".inpt")
        .val(numberFormatter(value) + "%");
    else {
      $this.parent(".inpt-slider").find(".inpt").val(numberFormatter(value));
    }
ewe
    $(this)
      .parents(".inpt-slider")
      .find(".clssErrorMsg")
      .css("visibility", "hidden");
    $(this)
      .parents(".inpt-slider")
      .find(".inputBox")
      .removeClass("errorBorder");
  });
}

function numberFormatter(x) {
  x = x.toString();
  var afterPoint = "";
  if (x.indexOf(".") > 0) afterPoint = x.substring(x.indexOf("."), x.length);
  x = Math.floor(x);
  x = x.toString();
  var lastThree = x.substring(x.length - 3);
  var otherNumbers = x.substring(0, x.length - 3);
  if (otherNumbers != "") lastThree = "," + lastThree;
  var res =
    otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree + afterPoint;
  return res;
}

function rangenumDifferentiation(val) {
  var aryLabel = new Array("K", "L", "Cr");
  if (val >= 10000000) {
    val = val / 10000000;
    return val.toFixed(0) + "" + aryLabel[2];
  } else if (val >= 100000) {
    val = val / 100000;
    return val.toFixed(0) + "" + aryLabel[1];
  } else if (val < 100000) {
    val = val / 1000;
    val = val.toFixed(0) + "" + aryLabel[0];
  } else if ((val = 0)) {
    val = val.toFixed(0);
  }
  return val;
}

function calValidation() {
  $(".numbersOnly").keypress(function (e) {
    var error_div = $(this).parent().find(".error_message");
    if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
      error_div.html("Number only.");
      error_div.css("display", "block");
      return false;
    } else {
      error_div.html("");
      error_div.css("display", "none");
    }
  });
  $(".inputBox input").keyup(function (e) {
    if (e.which == 13) {
      $(this).blur();
    }

    var currentVal = $(this).val().replace(/[,]/g, "");
    if (
      currentVal >= $(this).data("minval") &&
      currentVal <= $(this).data("maxval")
    ) {
      $(this)
        .parents(".inpt-statement")
        .find(".clssErrorMsg")
        .css("visibility", "hidden");
      $(this).parent().removeClass("errorBorder");
    } else {
      $(this)
        .parents(".inpt-statement")
        .find(".clssErrorMsg")
        .css("visibility", "visible");
      $(this).parent().addClass("errorBorder");
    }
  });
  $(".numbersDecimal").on("input", function (evt) {
    var self = $(this);
    self.val(self.val().replace(/[^0-9\.]/g, ""));
    if (
      (evt.which != 46 || self.val().indexOf(".") != -1) &&
      (evt.which < 48 || evt.which > 57)
    ) {
      evt.preventDefault();
    }
  });
}

//var flag = false;
//
//function validateNetWeight(obj) {
//  if (obj.val() == "" || obj.val() == 0) {
//    obj.parents(".inputBox").addClass("errorBr");
//    flag = false;
//  } else {
//    obj.parents(".inputBox").removeClass("errorBr");
//    flag = true;
//  }
//  return flag;
//}

//new
function calEMIval() {
  var loanAmt = $("#loan_amount").val().replace(/,/g, "");
  var mon = $("#tenure").val();
  var int_rate = $("#interest_rate").val().replace("%", "");
  var presFee = "0";

  var v = calculate_emi(loanAmt, int_rate, mon, presFee);
  //console.log(v.emi);
  $("#lblEMIAmt").text(dispNum(v.emi));
  $("#lblEMIAmtHd").text(v.emi.toFixed(2));

  $("#princAmt").text($("#loan_amount").val());
  $("#emiAmt").text(dispNum(v.emi));
  $("#totalPayAmt").text(dispNum(v.emi * mon));
  $("#intrAmt").text(dispNum(v.emi * mon - loanAmt));
}


//$(".inpt").change(function () {
//    calEMIval();
//});

//Loan amount
$("#loan_amount").on("change", function () {
  if ($("#loan_amount").val() > 1500000) {
    $("#loan_amount").val("15,00,000");
  }

  if ($("#loan_amount").val() < 50000) {
    $("#loan_amount").val("50,000");
  }
  calEMIval();
//  Amortization();
});

//Rate of interest
$("#interest_rate").on("change", function () {
  if ($("#interest_rate").val() > 24) {
    $("#interest_rate").val("24%");
  }

  if ($("#interest_rate").val() < 10.49) {
    $("#interest_rate").val("10.49%");
  }
  calEMIval();
//  Amortization();
});

//Tenure
$("#tenure").on("change", function () {
  if ($("#tenure").val() > 60) {
    $("#tenure").val("60");
  }

  if ($("#tenure").val() < 12) {
    $("#tenure").val("12");
  }
  calEMIval();
//  Amortization();
});

function dispNum(n) {
  var nStr = Math.round(n);
  nStr += "";
  x = nStr.split(".");
  x1 = x[0];
  x2 = x.length > 1 ? "." + x[1] : "";
  var rgx = /(\d+)(\d{3})/;
  var z = 0;
  var len = String(x1).length;
  var num = parseInt(len / 2 - 1);

  while (rgx.test(x1)) {
    if (z > 0) {
      x1 = x1.replace(rgx, "$1" + "," + "$2");
    } else {
      x1 = x1.replace(rgx, "$1" + "," + "$2");
      rgx = /(\d+)(\d{2})/;
    }
    z++;
    num--;
    if (num == 0) {
      break;
    }
  }
  return x1 + x2;
}

function calculate_emi(princ, intr, months, procFee) {
  var i = intr / 12 / 100;
  var result = {};
  result.emi = (princ * i) / (1 - Math.pow(1 / (1 + i), months));
  result.processingFee = (procFee * princ) / 100;
  result.totalIntrest = result.emi * months - princ;
  result.totalPayment = result.emi * months;
  result.quaterAmt = princ / 4;

  return result;
}

//function Getdecimal(e) {
//  a = e.keyCode || e.which;
//  b = $("#interest_rate").val().replace("%", "");
//
//  if (a === 46 && b.indexOf(".") >= 0) {
//    return false;
//  } else if (a != 8 && a != 0 && (a < 48 || a > 57) && a != 46) {
//    return false;
//  }
//}

//function ThousandSeparate(x) {
//  x = x.toString();
//
//  var lastThree = x.substring(x.length - 3);
//  var otherNumbers = x.substring(0, x.length - 3);
//  if (otherNumbers != "") lastThree = "," + lastThree;
//  var res = otherNumbers.replace(/\B(?=(\d{2})+(?!\d))/g, ",") + lastThree;
//  return res;
//}
