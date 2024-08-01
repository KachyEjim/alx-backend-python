// Import the file system module
const fs = require('fs');

// Generate files asynchronously
for (let i = 0; i < 11; i++) {
  const filePath = `${i}-main.py`;
  const fileContent = '';

  fs.writeFile(filePath, fileContent, (err) => {
    if (err) {
      return console.error(`Error writing file: ${err}`);
    }
    console.log(`File created successfully at ${filePath}`);
  });
}
