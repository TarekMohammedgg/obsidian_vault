<%*
// 1. Get the link from your clipboard
let url = await tp.system.clipboard();

// 2. Extract the ID using Regex (Works for /file/d/ or ?id= formats)
let match = url.match(/[-\w]{25,}/);
let fileId = match ? match[0] : null;

if (fileId) {
    // 3. Generate your specific format
    const output = `[![Preview](https://drive.google.com/thumbnail?id=${fileId}&sz=w1000)](https://drive.google.com/file/d/${fileId}/view)`;
    
    // 4. Insert it into the editor
    tR += output;
} else {
    new Notice("No valid Google Drive ID found in clipboard!");
}
%>

