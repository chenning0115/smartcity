/**
 * Created by yichaopku on 2016/7/13.
 */

//月份英文字母转换成月份数字
function str2month(monthstr){
    var month = 1;
    switch(monthstr)
    {
        case "January":
            month = 1;
            break;
        case "February":
            month = 2;
            break;
        case "March":
            month = 3;
            break;
        case "April":
            month = 4;
            break;
        case "May":
            month = 5;
            break;
        case "June":
            month = 6;
            break;
        case "July":
            month = 7;
            break;
        case "August":
            month = 8;
            break;
        case "September":
            month = 9;
            break;
        case "October":
            month = 10;
            break;
        case "November":
            month = 11;
            break;
        case "December":
            month = 12;
            break;
    }
    return month;
}

//带英文月份的年月日转换成包含年月日数字的数组
function str2ymd(s){
    var arr = s.split("\\-");
    var y = parseInt(arr[1]);
    var arr1 = arr[0].split(" ");
    var d = parseInt(arr1[0]);
    var m = str2month(arr1[1]);
    return new Array(y, m, d);
}

//由2014-03-02格式的字符串转换成包含年月日数字的数组
function str2ymd1(s){
    var arr = s.split("-")
    var y = parseInt(arr[0])
    var m = parseInt(arr[1])
    var d = parseInt(arr[2])
    return new Array(y, m, d)
}

//由2014-03-05 to 2015-02-06转换成包含两个数的天数数组
function str2dates(s){
    var arr = s.split("to")
    var a1 = str2ymd1(arr[0])
    var a2 = str2ymd1(arr[1])
    return new Array(ymd2date(a1[0], a1[1], a1[2]), ymd2date(a2[0], a2[1], a2[2]))
}

//从2014-01-01起的天数转换成包含年月日数字的数组
function date2ymd(date){
    var days = new Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
    var y, m,d;
    if(date > 365){
        y = 2015;
        date -= 365;
    }else{
        y = 2014;
    }
    var i = 0;
    var sum = 0;
    for(;i < 12;i++){
        sum += days[i];
        if(sum >= date)
            break;
    }
    m = i + 1;
    d = date - (sum - days[i]);
    return new Array(y, m, d);
}

//包含年月日数字的数组转换成带有中文的字符串
function date2ymdStr(date){
    var datearr = date2ymd(date);
    return datearr[0]+"年"+datearr[1]+"月"+datearr[2]+"日";
}

//有年月日数字计算出从2014-01-01起的天数
function ymd2date(y, m, d){
    var days = new Array(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
    var sum = 0;
    if(y == 2015){
        sum = 365;
    }
    for(var i = 0;i < m-1;i++){
        sum += days[i];
    }
    sum += d;
    return sum;
}

//由要素的值获得对应的颜色字符串
function factor2colorstr(factor,value,tran){
    var ss = 'rgba(0, 0, 0, 0)';
    switch (factor) {
        case "time":
            ss = getcolorstr(1,730 , value, tran);
            break;
        case "location":
            ss = getcolorstr(1,1365 , value, tran);
            break;
        case "prec":
            ss = getcolorstr(0.00000112,4.587237506 , value, tran);
            break;
        case "pres":
            ss = getcolorstr(97033.64274,101104.9181 , value, tran);
            break;
        case "wind":
            ss = getcolorstr(0.610267453,7.025364637 , value, tran);
            break;
        case "temp":
            ss = getcolorstr(264.3652184,305.5715182 , value, tran);
            break;
        case "sHum":
            ss = getcolorstr(0.000195194,0.019546442 , value, tran);
            break;
        case "Irad":
            ss = getcolorstr(183.5247024,456.6471361, value, tran);
            break;
        case "SRad":
            ss = getcolorstr(21.23400075,339.8883573 , value, tran);
            break;
        case "poi":
            ss = getcolorstr(0,183 , value, tran);
            break;
        case "road":
            ss = getcolorstr(0,0.521338224 , value, tran);
            break;
        case "lucc":
            ss = getcolorstr(98,403 , value, tran);
            break;
        case "aqi_pre":
            ss = aqi2colorstr(value, tran);
            break;
        case "aqi_fin":
            ss = aqi2colorstr(value, tran);
            break;
    }
    return ss;
}

//由要素的值获得对应的颜色字符串
function getcolorstr(min, max, value, tran){
    var ss = "";
    var mid = (max + min) /2 ;
    var hi  = (max - min)/2;
    if(value < mid){
        ss =  'rgba(0, '+parseInt((hi - value + min) / hi * 255)+', 0, '+tran+')';
    }else{
        ss =  'rgba('+parseInt((value - mid) / hi * 255)+',0 , 0, '+tran+')';
    }
    return ss;
}

//由aqi值计算对应的颜色字符串
function aqi2colorstr(value,tran){
    value = parseInt(value)+"";
    var ss = 'rgba(8, 8, 255, '+tran+')';
    switch(value){
        case "1":
            ss =  'rgba(8, 8, 255, '+tran+')';
            break;
        case "2":
            ss =  'rgba(58, 157, 255, '+tran+')';
            break;
        case "3":
            ss =  'rgba(112, 255, 211, '+tran+')';
            break;
        case "4":
            ss =  'rgba(231, 255, 74, '+tran+')';
            break;
        case "5":
            ss =  'rgba(255, 167, 0, '+tran+')';
            break;
        case "6":
            ss =  'rgba(255, 0, 0, '+tran+')';
            break;
    }
    return ss;
}

//由趋势值计算颜色字符串
function trend2colorstr(value,tran){
    value = parseInt(value)+"";
    var ss = 'rgba(8, 8, 255, '+tran+')';
    switch(value){
        case "1":
            ss =  'rgba(8, 8, 255, '+tran+')';
            break;
        case "2":
            ss =  'rgba(58, 157, 255, '+tran+')';
            break;
        case "3":
            ss =  'rgba(112, 255, 211, '+tran+')';
            break;
        case "4":
            ss =  'rgba(231, 255, 74, '+tran+')';
            break;
        case "5":
            ss =  'rgba(255, 167, 0, '+tran+')';
            break;
    }
    return ss;
}

//由要素的英文名字获得对应的中文名字
function factor2name(factor) {
    var name = "";
    switch (factor) {
        case "time":
            name = "时间";
            break;
        case "location":
            name = "地点";
            break;
        case "prec":
            name = "降水率(单位：mm/hr)";
            break;
        case "pres":
            name = "地表气压(单位：Pa)";
            break;
        case "wind":
            name = "风速(单位：m/s)";
            break;
        case "temp":
            name = "温度(单位：K)";
            break;
        case "SHum":
            name = "近地面空气比湿(单位：kg/kg)";
            break;
        case "Irad":
            name = "Irad";
            break;
        case "SRad":
            name = "向下短波辐射(单位：W/平方米)";
            break;
        case "poi":
            name = "POI";
            break;
        case "road":
            name = "道路";
            break;
        case "lucc":
            name = "土地利用产污综合指数";
            break;
        case "aqi_pre":
            name = "aqi_pre";
            break;
        case "aqi_fin":
            name = "AQI";
            break;
    }
    return name;
}