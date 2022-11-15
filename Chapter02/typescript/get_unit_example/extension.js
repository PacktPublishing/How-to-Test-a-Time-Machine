// Register command
'use strict';
import * as vscode from 'vscode';
import {extractMethodsFromDocument} from './UnitTestWriting';

export function activate(context: vscode.ExtensionContext) {
    const command = 'ut.getUnit';
    const commandHandler = () => {
        extractMethodsFromDocument();
    };
    context.subscriptions.push(vscode.commands.registerCommand(command, commandHandler));
}