"use strict";
const WebTorrent = require('webtorrent-hybrid');
const fs = require('fs');
const torrentId = "magnet:?xt=urn:btih:B6E82665EF588BB6574DB1F9780A0279274F407D&dn=Aquaman+%282018%29+%5BWEBRip%5D+%5B1080p%5D+%5BYTS%5D+%5BYIFY%5D&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2F9.rarbg.com%3A2710%2Fannounce&tr=udp%3A%2F%2Fp4p.arenabg.com%3A1337&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce";
const client = new WebTorrent();
const cli_progress = require('cli-progress');
console.log('TorrentId:\t', torrentId);

const bar = new cli_progress.SingleBar({}, cli_progress.Presets.shades_classic);
client.add(torrentId, torrent => {
  const files = torrent.files
  let length = files.length
  console.log('Number of files : '+length);
  bar.start(100,0);
  const interval = setInterval(() => {
    bar.update((torrent.progress * 100));
  }, 2000);
  // Stream each file to the disk
  files.forEach(file => {
    const source = file.createReadStream()
    console.log(file.name);
    const destination = fs.createWriteStream(file.name);
    source.on('end', () => {
      console.log('\n\tfile:\t\t', file.name)
      // close after all files are saved
      length -= 1
      if (!length){ 
        bar.stop();
        clearInterval(interval);
        process.exit()
      }
    }).pipe(destination)
  });
})