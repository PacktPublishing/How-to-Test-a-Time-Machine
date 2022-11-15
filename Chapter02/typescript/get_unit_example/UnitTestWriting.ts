'use strict';
import * as vscode from 'vscode';

export async function extractMethodsFromDocument() {
    const editor = vscode.window.getActiveTextEditor();
    const document = editor.getTextDocument();
    let code = "";
    let method = "";
    // get name of doc to set name of Test Class
    for (let i = 0; i < document.getLineCount(); i++) {
        const line = document.getTextOnLine(i).toLowerCase();
        if((line.includes("public") || line.includes("protected")) && line.includes("(")) {
        let lineSplit = line.split(new RegExp(" *("));
        if(lineSplit.length>0) {
         	method=lineSplit[0];
        }
    }
    code += "\n\n@Test\npublic void " + method + "Test(){assert.false;}";
    }
    console.log(code); // here we could write a file
}
