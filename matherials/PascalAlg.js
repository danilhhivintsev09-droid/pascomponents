function psl(text) {
    const alph = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let out = [];
    const txt = text.toUpperCase();
    for (const char of txt) {
        if (alph.includes(char)) {
            let per = "";
            const period1 = 'АБВГ,';
            const period2 = 'ДЕЖЗ.';
            const period3 = 'ИЙКЛ-';
            const period4 = 'МНОП!';
            const period5 = 'РСТУ?';
            const period6 = 'ФХЦЧ:';
            const period7 = 'ШЩЪЫ;';
            const period8 = 'ЬЭЮЯ';
            const period9 = "ABCD";
            const period10 = "EFGH";
            const period11 = "IJKL";
            const period12 = "MNOP";
            const period13 = "QRST";
            const period14 = "UVWX";
            const period15 = "YZ";

            if (period1.includes(char)) per = '1';
            if (period2.includes(char)) per = '2';
            if (period3.includes(char)) per = '3';
            if (period4.includes(char)) per = '4';
            if (period5.includes(char)) per = '5';
            if (period6.includes(char)) per = '6';
            if (period7.includes(char)) per = '7';
            if (period8.includes(char)) per = '8';
            if (period9.includes(char)) per = '9';
            if (period10.includes(char)) per = '10';
            if (period11.includes(char)) per = '11';
            if (period12.includes(char)) per = '12';
            if (period13.includes(char)) per = '13';
            if (period14.includes(char)) per = '14';
            if (period15.includes(char)) per = '15';

            let res = "";
            if ("АДИМРФЦЬAEIMQUY".includes(char)) {
                res = per + '11';
            } else if ("БЕЙНСХЩЭBFJNRVZ".includes(char)) {
                res = per + '121';
            } else if ("ВЖКОТЦЪЮCGKOSW".includes(char)) {
                res = per + '1331';
            } else if ("ГЗЛПУЧЫЯDHLP TX".includes(char)) {
                // Note: The original Python code does not include 'X' in this group explicitly, but it is in the string.
                // The space before X is likely a typo, so removing it.
                res = per + '14641';
            } else if (char === ',') {
                res = '//';
            } else if (char === '.') {
                res = 'S';
            } else if (char === '-') {
                res = 't';
            } else if (char === '!') {
                res = 'o';
            } else if (char === '?') {
                res = 'q';
            } else if (char === ':') {
                res = 'ss';
            } else if (char === ';') {
                res = 's//';
            }
            out.push(res);
        }
    }
    return out.join('.');
}

// Example usage:
// const input = prompt('Enter your message: ');
// const ans = psl(input);
// console.log(ans);