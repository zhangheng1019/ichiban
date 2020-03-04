function setSelect(eleAray) {
    for (let i = 0; i < eleAray.length; i++) {
        $('#' + eleAray[i]).select2();
        $('#' + eleAray[i]).select2({
            placeholder: '请选择'
        });
    }


}


function setSelectnums(eleAray) {
    for (let i = 0; i < eleAray.length; i++) {
        $('#' + eleAray[i]).select2();
        $('#' + eleAray[i]).select2({
            /* language: "zh-CN",
             minimumInputLength: 0,
             placeholder: "可多选",//默认值
             allowClear: true,*/
            placeholder: '请选择',
            multiple: true,
            language: "zh-CN",
            allowClear: true,
            closeOnSelect: false
        });
    }
}