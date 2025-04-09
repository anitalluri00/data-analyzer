import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch("/api/data")
      .then((res) => res.json())
      .then(setData)
      .catch(console.error);
  }, []);

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-4">Extracted Data</h1>
      {Object.entries(data).map(([file, content]) => (
        <div key={file} className="mb-6">
          <h2 className="text-lg font-semibold">{file}</h2>
          {Array.isArray(content) ? (
            <table className="table-auto border mt-2 text-sm">
              <thead>
                <tr>
                  {Object.keys(content[0] || {}).map((key) => (
                    <th key={key} className="border px-2 py-1">{key}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {content.map((row, i) => (
                  <tr key={i}>
                    {Object.values(row).map((val, j) => (
                      <td key={j} className="border px-2 py-1">{String(val)}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <pre className="bg-gray-100 p-2 mt-2 text-sm whitespace-pre-wrap">{content}</pre>
          )}
        </div>
      ))}
    </div>
  );
}

export default App;
