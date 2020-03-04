//获取页面所有标签元素的value值 并放入json数据中
function getdatas() {
    //获取input中的name 与value
    var inputs = $(".cont input");
    var selects = $(".cont select");
    var textareas = $(".cont textarea");
    var args = [];
    var obj = {};
    if (inputs != null) {
        for (var i = 0; i < inputs.length; i++) {
            var name = inputs[i].name;
            var value = inputs[i].value;
            obj['' + name + ''] = value;
        }
    }

    //获取select中的name与value
    if (selects != null) {
        for (var i = 0; i < selects.length; i++) {
            var name = selects[i].name;
            var value = selects[i].value;
            obj['' + name + ''] = value;
        }
    }
    if (textareas != null) {
        for (var i = 0; i < textareas.length; i++) {
            var name = textareas[i].name;
            var value = textareas[i].value;
            obj['' + name + ''] = value;
        }
    }
    args.push(obj);
    //console.log(JSON.stringify(args));
    return JSON.stringify(args);
}

//设置默认选中
function selected(elements, values) {
    /*if (values != null) {
        elements.find("option[value='" + values + "']").prop('selected', true);
    } else {
        elements.find("option[value='']").prop('selected', true);
    }*/
    if (values != null) {
        $(elements).select2().val(values).trigger('change');
    }
}

//复选框选中
function boxChecked(ele, str) {

    var s = "'";
    str = str.replace(']', '').replace('[', '').replace(new RegExp(s, 'g'), "").replace(new RegExp(" ", "g"), "");
    var array = str.split(',');
    if ($.inArray(ele.val(), array) >= 0) {

        ele.prop('checked', 'true');
    }

}

//获取页面内容放入formData中
function getFormData() {
    //获取input中的name 与value
    //
    var inputs = $(".cont input");
    var selects = $(".cont select");
    var textareas = $(".cont textarea");
    var formDate = new FormData();
    var args = [];
    var obj = {};
    if (inputs != null) {
        for (var i = 0; i < inputs.length; i++) {
            var name = inputs[i].name;
            if (inputs[i].type == 'file') {
                var files = inputs[i].files[0];
                formDate.append(name, files);
            } else {
                var value = inputs[i].value;
                formDate.append(name, value);
            }
        }

    }

    //获取select中的name与value
    if (selects != null) {
        for (var i = 0; i < selects.length; i++) {
            var name = selects[i].name;
            var value = selects[i].value;
            formDate.append(name, value);
        }
    }
    if (textareas != null) {
        for (var i = 0; i < textareas.length; i++) {
            var name = textareas[i].name;
            var value = textareas[i].value;
            formDate.append(name, value);
        }
    }
    return formDate;
}

//通用验证表单
// function checkForms(elements){
//
//     for (var i = 0; i < elements.length; i++) {
//         var val= elements[i].val();
//
//         if(val==''||val==null){
//             alert('请输入'+elements[i].parent().prev().find('lable').text());
//             return false;
//         }
//     }
//     return true;
// }

//通用验证表单
//参数列表： elements ；存放元素的数组
// options ：crud 按钮
//ids 单独提示的span标签存放的元素ID
function checkForms(elements, options, ids) {
    $('.warn').text('');

    for (var i = 0; i < elements.length; i++) {
        var val = elements[i].val();
        if (options == 'ins_1' || options == 'upd_1') {
            if (val == '' || val == null) {

                $('.warn').text('*');
                $('.warn').css('color', 'red');
                alert('请确认带*内容是否输入');

                return false;
            }

        } else if (options == 'sel_1' || options == 'del_1') {
            if (val == '' || val == null) {

                for (var j = 0; j < ids.length; j++) {
                    var a = ids[j];
                    ids[j].text('*');
                    ids[j].css('color', 'red');
                }

                alert('请确认带*内容是否输入');

                return false;
            }

        }

    }
    return true;
}

/**
 * ajax封装
 * url 发送请求的地址
 * data 发送到服务器的数据，数组存储，如：{"date": new Date().getTime(), "state": 1}
 * async 默认值: true。默认设置下，所有请求均为异步请求。如果需要发送同步请求，请将此选项设置为 false。
 *       注意，同步请求将锁住浏览器，用户其它操作必须等待请求完成才可以执行。
 * type 请求方式("POST" 或 "GET")， 默认为 "post"
 * dataType 预期服务器返回的数据类型，常用的如：xml、html、json、text
 * successfn 成功回调函数
 * errorfn 失败回调函数
 */
jQuery.ax = function (url, data, async, type, dataType, successfn, errorfn) {
    async = (async == null || async == "" || typeof (async) == "undefined") ? "true" : async;
    type = (type == null || type == "" || typeof (type) == "undefined") ? "post" : type;
    dataType = (dataType == null || dataType == "" || typeof (dataType) == "undefined") ? "json" : dataType;
    data = (data == null || data == "" || typeof (data) == "undefined") ? {
        "date": new Date().getTime()
    } : data;
    $.ajax({
        type: type,
        async: async,
        data: data,
        url: url,
        dataType: dataType,
        success: function (d) {
            successfn(d);
        },
        error: function (e) {
            errorfn(e);
        }
    });
};

/*
* 封装formdata
* url  路由
* functions 成功后执行的方法
* formData 需要提交的表单
* */
jQuery.ajaxForm = function (url, formData, functions) {
    $.ajax(
        {
            type: "post",
            data: formData,
            processData: false,
            contentType: false,
            url: url,
            async: true,
            success: function (data) {
                functions(data);
            }
        }
    );
};


//对应控件权限
function authorityControl() {

}


//测试方法
function aaa(ele) {

    for (var i = 0; i < ele.length; i++) {
        var inputs = $('' + ele[i] + '');
        for (var i = 0; i < inputs.length; i++) {
            var aaa = inputs[i].name;
            var bbb = inputs[i].id;
            var text = "var " + inputs[i].name + "=$('#" + inputs[i].id + "').val();//"
            text += "<br /><br />";
            $('body').append(text)
        }
    }

}

//js获取传过来的参数
function getQueryVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return '';
}


//翻译并放入元素中
function GetBaidu(from, to, query, obj, ele) {
    // console.log(query);
    if (query != '') {
        var q = query.join("\n"); // 将内容数组用 \n 拼接
        var appid = "20191107000354087"; // 请自行获取
        var key = "puyUCB6tjUeKq4dXB5hc"; // 请自行获取
        var salt = (new Date).getTime();
        var str1 = appid + q + salt + key;
        var sign = MD5(str1);
        $.ajax({
            url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
            type: 'post',
            dataType: 'jsonp',
            data: {
                q: q,
                from: from,
                to: to,
                appid: appid,
                salt: salt,
                sign: sign
            },
            success: function (msg) {

                if ('trans_result' in msg) {
                    var html = "";
                    if (ele == 'input' || ele == 'textarea') {
                        if (typeof (msg.trans_result) != 'undefined') {
                            for (var i = 0; i < msg.trans_result.length; i++) {
                                // console.log(msg.trans_result[i].dst);
                                html = msg.trans_result[i].dst;
                                obj[i].val(html);
                            }
                        }
                    } else {
                        if (typeof (msg.trans_result) != 'undefined') {
                            if (msg.trans_result.length <= 1) {
                                var args = [];
                                for (var i = 0; i < msg.trans_result.length; i++) {
                                    args = msg.trans_result[i].dst.split('\n');

                                }
                                for (var i = 0; i < args.length; i++) {
                                    obj[i].html(args[i]);
                                }

                            } else {


                                for (var i = 0; i < msg.trans_result.length; i++) {
                                    html = msg.trans_result[i].dst;
                                    obj[i].html(html);
                                }
                            }
                        }
                    }

                } else {
                    // alert('翻译' + ele + '出现问题，请稍后重试！');
                }

            }
        });
    }
}

//获取元素内容 并用\n隔开
function getArr(ele) {
    var arrHtml = [];
    var arrThis = [];
    var text = $('' + ele).text(function (i, text) {
        arrHtml.push(text.replace('\n', ' '));
        arrThis.push($(this));
    });
    return [arrHtml, arrThis];
}

function getInput(ele) {

    var arrHtml = [];
    var arrThis = [];
    var index = [];
    var text = $('' + ele).val(function (i, text) {
        var id = $(this)[0].id;
        if (text == 'on' || $('#' + id).attr('type') == 'radio' || $('#' + id).attr('type') == 'checkbox' ||
            text == 'EA') {
            text = '';
        }
        if ($(this)[0].className != 'no') {
            arrHtml.push(text.replace('\n', ' '));
            arrThis.push($(this));

        } else {
            index.push(i);
            arrHtml.push(text.replace('\n', ' '));
            arrThis.push($(this));


        }
    });
    return [arrHtml, arrThis, index];
}

//翻译 引入md5.js
function fanyiLoad(from, to) {

    GetBaidu(from, to, getArr('lable')[0], getArr('lable')[1], 'lable');
    GetBaidu(from, to, getArr('label')[0], getArr('label')[1], 'label');
    GetBaidu(from, to, getArr('option')[0], getArr('option')[1], 'option');
    GetBaidu(from, to, getArr('button')[0], getArr('button')[1], 'button');
    GetBaidu(from, to, getArr('a')[0], getArr('a')[1], 'a');

}

//翻译内容
function fanyiContent(from, to) {
    GetBaiduInput(from, to, getInput('input')[0], getInput('input')[1], 'input', getInput('input')[2]);
    GetBaidu(from, to, getArr('lable')[0], getArr('lable')[1], 'lable');
    //GetBaidu(from, to, getArr('textarea')[0], getArr('textarea')[1], 'textarea');
    GetBaiduInput(from, to, getInput('textarea')[0], getInput('textarea')[1], 'textarea', getInput('textarea')[2]);
}


//翻译并放入input元素中
function GetBaiduInput(from, to, query, obj, ele, index) {
    // console.log(query);
    debugger;
    let nums = 0;
    for (let i = 0; i < query.length; i++) {
        if (query[i] == '') {
            nums += 1;
        }
    }
    if (nums != query.length) {

        var count = "<span style=\"display: none\" id='hiddenCount'>" + query + "</span>";
        $('body').append(count);
        if (query != '') {
            var num = 0;
            for (var j = 0; j < index.length; j++) {
                query.splice(index[j] - num, 1);
                num += 1;
            }
            console.log(query);
            var q = query.join("\n"); // 将内容数组用 \n 拼接
            console.log(q);
            var appid = "20191107000354087"; // 请自行获取
            var key = "puyUCB6tjUeKq4dXB5hc"; // 请自行获取
            var salt = (new Date).getTime();
            var str1 = appid + q + salt + key;
            var sign = MD5(str1);
            $.ajax({
                url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
                async: false,
                type: 'post',
                dataType: 'jsonp',
                data: {
                    q: q,
                    from: from,
                    to: to,
                    appid: appid,
                    salt: salt,
                    sign: sign
                },
                success: function (msg) {
                    if ('trans_result' in msg) {


                        debugger;
                        var html = "";
                        var arg = [];
                        var nochange = {};
                        var hiddenCount = $('#hiddenCount').html().split(',');
                        for (var j = 0; j < index.length; j++) {
                            nochange[index[j]] = hiddenCount[index[j]];
                        }
                        if (ele == 'input' || ele == 'textarea') {
                            if (typeof (msg.trans_result) != 'undefined') {
                                console.log(msg.trans_result);
                                if (msg.trans_result.length > 1) {
                                    for (var i = 0; i < msg.trans_result.length; i++) {
                                        arg.push(msg.trans_result[i].dst);
                                    }

                                } else {
                                    for (var i = 0; i < msg.trans_result.length; i++) {
                                        arg = msg.trans_result[i].dst.split('\n');
                                    }
                                }

                                for (var k in nochange) {
                                    arg.splice(k, 0, nochange[k]);
                                }
                                for (var j = 0; j < arg.length; j++) {
                                    html = arg[j];
                                    obj[j].val(html);
                                }
                            }
                            $('#hiddenCount').remove();
                        } else {
                            if (typeof (msg.trans_result) != 'undefined') {
                                for (var i = 0; i < msg.trans_result.length; i++) {
                                    html = msg.trans_result[i].dst;
                                    obj[i].html(html);
                                }
                            }
                        }
                    } else {
                        // alert('翻译' + ele + '出现问题，请稍后重试！');
                    }
                }
            });


        }


    }
}


//页面添加 选择语言的下拉框，并添加将选择的语言传入后台的方法
function setLanguage() {
    $('#languages').remove();
    var text = "";
    text += " <div id=\"languages\">";
    text += "    	<select name=\"language\" id=\"sel_l\">";
    text += "    		<option value=\"\">请选择语言</option>";
    text += "    		<option value=\"zh\">中文</option>";
    text += "    		<option value=\"cht\">繁體中文</option>";
    text += "    		<option value=\"en\">English</option>";
    text += "    		<option value=\"jp\">日本語</option>";
    text += "    		<option value=\"kor\">한국어</option>";
    text += "    		<option value=\"fra\">Le français</option>";
    text += "    		<option value=\"spa\">Espanol</option>";
    text += "    		<option value=\"th\">ไทย</option>";
    text += "    		<option value=\"vie\">Tiếng việt nam</option>";
    text += "    	</select> &nbsp;";
    text += "<button id=\"lan_btn\">确认</button>";
    text += "    </div>";

    $('#na').after(text);

    $('#lan_btn').bind('click', function () {
        var language = $('#sel_l').val();
        if (language == 'zh') {
            location.reload();
        } else {

            $.ajax({
                type: "get",
                url: "/order/po/",
                async: true,
                data: {
                    "language": language
                },
                success: function (data) {
                    //翻译
                    fanyiLoad('auto', language);
                    fanyiContent('auto', language);
                }
            });
        }
        return false;
    });

}


function setLanguageSession(language) {
    $.ajax({
        url: 'http://api.fanyi.baidu.com/api/trans/vip/translate',
        type: 'post',
        async: false,
        data: {
            'language': language
        },
        success: function (data) {
            alert('语言设置成功！');
        }
    });


}

//计算
function calc(num1, num2) {
    if (num1 != '' && num2 != '') {
        return num1 * num2;
    } else {
        return '';
    }
}

//时间格式化问题
Date.prototype.Format = function (fmt) {
    var o = {
        "M+": this.getMonth() + 1, //月份
        "d+": this.getDate(), //日
        "H+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds() //毫秒s
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}

function arrayList(array, value) {
    var newArray = [];
    for (var i = 0; i < array.length; i++) {
        if (array[i] != value) {
            newArray.push(array[i]);
        }

    }
    return newArray;
}
//筛选出要提交给后台的文本框内容
function submitArray(array)
{
    var newArray = [];
    for (let i = 0; i < array.length; i++) {
        if ($('#'+array[i].id).val() != '') {
            newArray.push($('#'+array[i].id).val());
        }
    }
    return newArray;
}
