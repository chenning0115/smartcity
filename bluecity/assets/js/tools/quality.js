/**
 * Created by chenning on 16/7/24.
 */

        $(function() {
            var IsShow = false;
            try {
                // $.get("VisitsCount.aspx");
            } catch (e) {
            }
            var IAQIfontcolor = "";
            function GetStyleByIAQIValue(val) {
                var strStyle = "color-s color-1";
                if (val >= 0 && val <= 50) {
                    strStyle = "color-s color-1";
                }
                else if (val >= 51 && val <= 100) {
                    strStyle = "color-s color-2";
                }
                else if (val >= 101 && val <= 150) {
                    strStyle = "color-s color-3";
                }
                else if (val >= 151 && val <= 200) {
                    strStyle = "color-s color-4";
                }
                else if (val >= 201 && val <= 300) {
                    strStyle = "color-s color-5";
                }
                else if (val > 300) {
                    strStyle = "color-s color-6";
                }
                return strStyle;
            }
            function GetIAQIFontColor(val) {
                var color = "#00e400";
                if (val >= 0 && val <= 50) {
                    IAQIfontcolor = "#00e400";
                }
                else if (val >= 51 && val <= 100) {
                    IAQIfontcolor = "#ffff00";
                }
                else if (val >= 101 && val <= 150) {
                    IAQIfontcolor = "#ff7e00";
                }
                else if (val >= 151 && val <= 200) {
                    IAQIfontcolor = "#ff0000";
                }
                else if (val >= 201 && val <= 300) {
                    IAQIfontcolor = "#99004c";
                }
                else if (val > 300) {
                    IAQIfontcolor = "#7e0023";
                }
                return IAQIfontcolor;
            }
            $.ajax({
                type: "GET",
                url: "getqualitydata?date=" + new Date(),

                dataType: "text",
                success: function(data) {
                    dataObj = data.replace(/\\/g, "");
                    var strJson = eval("(" + dataObj + ")");
                    $.each(strJson.Table, function(idex, item) {

                        if (idex == 0) {
                            priPollutant = item.PriPollutant;
if(priPollutant.indexOf(',')>0)
priPollutant = priPollutant.substring(0,priPollutant.indexOf(','));
                            var htmlText = "";
                            switch (priPollutant) {
                                case "PM2.5":
                                    {
                                        htmlText = IsShow ? "PM" + "<sub>2.5</sub>" : "PM2.5";
                                        break;
                                    }
                                case "SO2":
                                    {
                                        htmlText = IsShow ? "SO" + "<sub>2</sub>" : "SO2";
                                        break;
                                    }
                                case "NO2":
                                    {
                                        htmlText = IsShow ? "NO" + "<sub>2</sub>" : "NO2";
                                        break;
                                    }
                                case "O3":
                                    {
                                        htmlText = IsShow ? "O" + "<sub>3</sub>" : "O3";
                                        break;
                                    }
                                case "PM10":
                                    {
                                        htmlText = IsShow ? "PM" + "<sub>10</sub>" : "PM10";
                                        break;
                                    }
                                case "CO":
                                    {
                                        htmlText = IsShow ? "CO" : "CO";
                                        break;
                                    }
                            }
                            $("#PriPollutant").html(htmlText);
                            var date = item.Date_Time;
                            var timeArray = date.substring(0, date.indexOf(':')).split(" ");
                            var dateArray = timeArray[0].split("-");
                            if (dateArray.length == 1) {
                                dateArray = timeArray[0].split('/');
                            }
                            var time = dateArray[0] + "年" + dateArray[1] + "月" + dateArray[2] + "日" + timeArray[1] + "时";
                            $("#datetime").html(time);

                        }
                        if (item.Pollutant == priPollutant) {
                            $("#IAQI").html(item.IAQI);
                            var leftnum = 0;
                            leftnum = item.IAQI / 500 * 100
                            leftnum = leftnum + "%";
                            $(".cur").css("left", leftnum);
                            if (item.Quality == "-9999") {
                                $("#Quality").html("");
                            } else {
                                $("#Quality").html(item.Quality);
                            }
                            $("#IAQI").css("color", GetIAQIFontColor(item.IAQI));

                        }
                        var index = idex + 1;
                        var IAQI = item.IAQI;
                        if (IAQI == "-9999") {
                            IAQI = "";
                        }
                        var pjcolor = GetStyleByIAQIValue(IAQI);
                        switch (item.Pollutant) {
                            case "PM2.5":
                                {
                                    $("#pdata tr:eq(1) td").eq(0).html(IsShow ? "PM<sub>2.5</sub>" : "PM2.5");
                                    $("#pdata tr:eq(1) td").eq(1).html(IsShow ? "细颗粒物" : "");
                                    $("#pdata tr:eq(1) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(1) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                            case "SO2":
                                {
                                    $("#pdata tr:eq(2) td").eq(0).html(IsShow ? "SO<sub>2</sub>" : "SO2");
                                    $("#pdata tr:eq(2) td").eq(1).html(IsShow ? "二氧化硫" : "");
                                    $("#pdata tr:eq(2) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(2) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                            case "NO2":
                                {
                                    $("#pdata tr:eq(3) td").eq(0).html(IsShow ? "NO<sub>2</sub>" : "NO2");
                                    $("#pdata tr:eq(3) td").eq(1).html(IsShow ? "二氧化氮" : "");
                                    $("#pdata tr:eq(3) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(3) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                            case "O3":
                                {
                                    $("#pdata tr:eq(4) td").eq(0).html(IsShow ? "O<sub>3</sub>" : "O3");
                                    $("#pdata tr:eq(4) td").eq(1).html(IsShow ? "臭氧" : "");
                                    $("#pdata tr:eq(4) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(4) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                            case "CO":
                                {
                                    $("#pdata tr:eq(5) td").eq(0).html(IsShow ? "CO" : "CO");
                                    $("#pdata tr:eq(5) td").eq(1).html(IsShow ? "一氧化碳" : "");
                                    $("#pdata tr:eq(5) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(5) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                            case "PM10":
                                {
                                    $("#pdata tr:eq(6) td").eq(0).html(IsShow ? "PM<sub>10</sub>" : "PM10");
                                    $("#pdata tr:eq(6) td").eq(1).html(IsShow ? "可吸入颗粒物" : "");
                                    $("#pdata tr:eq(6) td").eq(2).html(IAQI);
                                    $("#pdata tr:eq(6) td:eq(3) span:first").addClass(pjcolor);
                                    break;
                                }
                        }

                        //$("#pdata tr:eq(" + index + ") td").eq(0).html(item.Pollutant);
                        //$("#pdata tr:eq(" + index + ") td").eq(1).html(item.IAQI);

                        //$("#pdata tr:eq(" + index + ") td:eq(2) span:first").addClass(pjcolor);
                        //$("#pdata tr:eq(" + index + ") td:eq(2) span:last").text(item.Quality);
                    })

                },
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert(textStatus + errorThrown);
                }
            });
        })

