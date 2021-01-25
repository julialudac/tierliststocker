const express = require('express');

const app = express();
app.use(require('body-parser').json());

const storage = require('./storage');
let theStorage = new storage.Storage();

app.post('/tierlist/add', (req, res) => {
    try {
        theStorage.add({rank: req.body.rank, item: req.body.item});
        res.status(201).send();
    } catch(err) {
        res.status(400)
            .send(err);
    }
});

app.get('/tierlist', (req, res) => {
    let tierlist = theStorage.getTierList();
    res.send(tierlist);
});

app.get('/tierlist/items', (req, res) => {
    let items = theStorage.getTierListItems();
    console.log(`items to send: ${items}`)
    res.send(items);
});

app.listen(5000);

