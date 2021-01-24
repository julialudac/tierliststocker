const express = require('express');


const app = express();
app.use(require('body-parser').json());

// false db
let fake_tierlist = {
    'S': [],
    'A': [],
    'B': [],
    'C': [],
    'D': ['Caca au pot'],
    'E': [],
    'F': [],
};

app.post('/tierlist/add', (req, res) => {
    const rank = req.body.rank;
    if (rank in fake_tierlist) {
        fake_tierlist[rank].push(req.body.item);
        res.status(201).send();
    } else {
        res.status(400)
        .send(`Error: Rank must be one of the following: 
              ${Object.keys(fake_tierlist)}.`)
    }
    // TODO: handle all the possible bad cases: 
    // - reject the request if the item already exists in the db.
    // - reject the request that doesnt have rank and item
    // ...
});

app.get('/tierlist', (req, res) => {
    res.send(fake_tierlist);
});

app.get('/tierlist/items', (req, res) => {
    let items = [];
    Object.keys(fake_tierlist).forEach(key => {
        items = items.concat(fake_tierlist[key]);
    });
    console.log(`items to send: ${items}`)
    res.send(items);
});

app.listen(5000);