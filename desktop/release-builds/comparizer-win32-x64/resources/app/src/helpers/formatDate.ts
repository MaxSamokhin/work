export const formatDate = (date: any) => {

    let dd = date.getDate();
    if (dd < 10) dd = '0' + dd;

    let mm = date.getMonth() + 1;
    if (mm < 10) mm = '0' + mm;

    let yy: any = date.getFullYear() % 100;
    if (yy < 10) yy = '0' + yy;

    return `${dd}.${mm}.${yy} ${date.getHours()}:${date.getMinutes()}` ;
};