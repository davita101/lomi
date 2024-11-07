const XLSX = require('xlsx');
const fs = require('fs');

async function convertExcelToJson(inputFilePath, outputFilePath) {
  try {
    const workbook = XLSX.readFile(inputFilePath);
    const sheetName = workbook.SheetNames[0];
    const worksheet = workbook.Sheets[sheetName];

    const jsonData = XLSX.utils.sheet_to_json(worksheet);

    fs.writeFileSync(outputFilePath, JSON.stringify(jsonData, null, 2));
    console.log('JSON file created successfully!');
  } catch (error) {
    console.error('Error converting Excel to JSON:', error);
  }
}

const inputFilePath = 'ღვინის სია.xlsx';
const outputFilePath = 'output.json';

convertExcelToJson(inputFilePath, outputFilePath);