#!/usr/bin/node
const fs = require('fs');

function concatFiles(sourceFilePath1, sourceFilePath2, destinationFilePath) {
    try {

        const fileA = fs.readFileSync(sourceFilePath1, 'utf8');
        

        const fileB = fs.readFileSync(sourceFilePath2, 'utf8');
        const concatenatedData = fileA + fileB;


        fs.writeFileSync(destinationFilePath, concatenatedData);

        console.log('Files concatenated successfully!');
    } catch (error) {
        console.error('Error:', error);
    }
}


const [,, sourceFilePath1, sourceFilePath2, destinationFilePath] = process.argv;


if (!sourceFilePath1 || !sourceFilePath2 || !destinationFilePath) {
    console.error('Usage: node concatFiles.js <sourceFilePath1> <sourceFilePath2> <destinationFilePath>');
    process.exit(1);
}

concatFiles(sourceFilePath1, sourceFilePath2, destinationFilePath);
