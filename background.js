chrome.action.onClicked.addListener((tab) => {
    chrome.scripting.executeScript({
      target: {tabId: tab.id},
      function: () => {
        // Get the selected text and open a new tab with the text on the URL
        new_corpus = getSelection().toString();        
        window.open('http://localhost:5000/analyze?text=' + new_corpus, '_blank');
      }
    });
});