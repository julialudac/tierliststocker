const express = require('express');

const app = express();
app.use(require('body-parser').json());

const storage = require('./storage');

app.post('/tierlist/add', (req, res) => {
    try {
        let theStorage = new storage.Storage(req.body.tierlist_name);
        theStorage.add({rank: req.body.rank, item: req.body.item});
        res.status(201).send();
    } catch(err) {
        if (err.type == 'error') {
            res.status(400)
                .send({error: err.message});
        }
        else{
            res.status(200)
                .send({warning: err.message});
        }
    }
});

app.get('/tierlist/:tierlist', (req, res) => {
    let theStorage = new storage.Storage(req.params.tierlist);
    let tierlist = theStorage.getTierList();
    console.log(`tierlist to send: ${JSON.stringify(tierlist)}`);
    res.send(tierlist);
});

app.get('/tierlist/items/:tierlist', (req, res) => {
    let theStorage = new storage.Storage(req.params.tierlist);
    let items = theStorage.getTierListItems();
    console.log(`items to send: ${JSON.stringify(items)}`);
    res.send(items);
});

app.delete('/tierlist/del/:tierlist/:item', (req, res) => {
    try {
        const item = req.params.item;
        let theStorage = new storage.Storage(req.params.tierlist);
        theStorage.delete(item);
        res.status(200).send(`Item ${item} has been successfully deleted.`);
    } catch(err) {
        res.status(200).send({warning: err.message});
    }
});

// TODO put (move)

app.listen(5000);

