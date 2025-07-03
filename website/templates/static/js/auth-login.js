async function checkForUpdates() {
  const current = await fetch('/api/version').then(r => r.json());
  const latest = await fetch('/api/latest-version').then(r => r.json());

  if (current.version !== latest.latest) {
    alert(`Update available: ${latest.latest} (current: ${current.version})`);
  } else {
    alert("You're up to date!");
  }
}

async function triggerUpdate() {
  const res = await fetch('/api/update', { method: 'POST' });
  alert(await res.text());
}