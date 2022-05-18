import { scrypt } from 'crypto';
import * as fs from 'fs';
import * as path from 'path';
import * as vscode from 'vscode';
import { Uri } from 'vscode';
import { copyFolder } from './utils';

enum Type {
    CONSOLE = 'Console App',
    WINFORMS = 'Windows Forms App',
    FILE = 'File Reader',
    CAMERA = 'Camera Scanner',
    GUI = 'GUI App',
}

enum FolderName {
    FOLDER_NAME_CONSOLE = 'console',
    FOLDER_NAME_WINFORMS = 'winforms',
    FOLDER_NAME_FILE = 'file',
    FOLDER_NAME_CAMERA = 'camera',
    FOLDER_NAME_GUI = 'gui',
}

export class Manager {
    private samples = {
        "python": path.join(__dirname, '../res/python/'),
        "dotnet": path.join(__dirname, '../res/dotnet/'),
        "cpp": path.join(__dirname, '../res/cpp/'),
        "web": path.join(__dirname, '../res/web/'),
        "android": path.join(__dirname, '../res/android/'),
        "ios": path.join(__dirname, '../res/ios/')
    };

    async getProjectType(types: string[]) {
        const projectType = await vscode.window.showQuickPick(types, { placeHolder: 'Create a new project' });
        if (!projectType) { return '';}
        return projectType;
    }
    
    async createProject(option: string) {
        // Select the project type
        let projectType: string = Type.CONSOLE;
        let src: string = '';
        switch (option) {
            case "dotnet":
                src = this.samples.dotnet;
                projectType = await this.getProjectType([Type.CONSOLE, Type.WINFORMS]);
                break;
            case "cpp":
                src = this.samples.cpp;
                projectType = await this.getProjectType([Type.CONSOLE]);
                break;
            case "web":
                src = this.samples.web;
                projectType = await this.getProjectType([Type.FILE, Type.CAMERA]);
                break;
            case "python":
                src = this.samples.python;
                projectType = await this.getProjectType([Type.CONSOLE, Type.GUI]);
                break;
            case "android":
                src = this.samples.android;
                projectType = await this.getProjectType([Type.CAMERA]);
                break;
            case "ios":
                src = this.samples.ios;
                projectType = await this.getProjectType([Type.CAMERA]);
                break;
        }
        if (projectType === '') {return;}

        switch (projectType) {
            case Type.CONSOLE:
                src = path.join(src, FolderName.FOLDER_NAME_CONSOLE);
                break;
            case Type.WINFORMS:
                src = path.join(src, FolderName.FOLDER_NAME_WINFORMS);
                break;
            case Type.FILE:
                src = path.join(src, FolderName.FOLDER_NAME_FILE);
                break;
            case Type.CAMERA:
                src = path.join(src, FolderName.FOLDER_NAME_CAMERA);
                break;
            case Type.GUI:
                src = path.join(src, FolderName.FOLDER_NAME_GUI);
                break;
        }

        if (src === '') {
            return;
        }

        // Select the project folder
        const answer = await vscode.window.showQuickPick(['Yes', 'No'], { placeHolder: 'Do you want to create a new folder?' });
        if (!answer) { return;}
    
        if (answer === "Yes") {
            const folderPath = await this.openFolder();
            if (folderPath !== '') {
                copyFolder(src, folderPath);
            }
        }
        else {
            let folders = vscode.workspace.workspaceFolders;
            if (!folders) {
                const folderPath = await this.openFolder();
                if (folderPath !== '') {
                    copyFolder(src, folderPath);
                }
            }
            else {
                vscode.window.showInformationMessage(folders[0].uri.fsPath);
                copyFolder(src, folders[0].uri.fsPath);
            }
        }
    
    }

    async openFolder() {
        const projectName = await vscode.window.showInputBox({
            prompt: 'Enter a name for the new project',
            validateInput: (value: string): string => {
                if (!value.length) {
                    return 'A project name is required';
                }
                return '';
            }
        });
        if (!projectName) {
            return '';
        }
    
        let workspace = '';
        const folderUris = await vscode.window.showOpenDialog({ canSelectFolders: true, canSelectFiles: false, canSelectMany: false, openLabel: 'Select folder' });
        if (!folderUris) {
            return '';
        }
    
        let workspaceFolderUri = folderUris[0];
        console.log(workspaceFolderUri);
        vscode.commands.executeCommand("vscode.openFolder", workspaceFolderUri);
        vscode.window.showInformationMessage(workspaceFolderUri.fsPath);
        workspace = workspaceFolderUri.fsPath;
        let projectFolder = path.join(workspace, projectName);
        if (!fs.existsSync(projectFolder)) {
            fs.mkdirSync(projectFolder);
        }
    
        vscode.commands.executeCommand("vscode.openFolder", Uri.file(projectFolder));
    
        return projectFolder;
    }
}