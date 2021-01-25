const fs = require('fs');
const path = require('path');

// false db
const fake_tierlist = {
    'S': [],
    'A': [],
    'B': [],
    'C': [],
    'D': ['Caca au pot'],
    'E': [],
    'F': [],
};

const pathToData = path.join('data', 'tierlist.json');

class Storage {
    constructor() {
        // thanks to the state variable, no need to always load from Db... 
        // Assuming the programing is the only one to affect the DB, and 
        // there is no other running instance of it...
        // better put sync all those init things!
        // TODO get rid of that in the future
        this.tierlist = fake_tierlist; 
        try {
            fs.mkdirSync('data');
        } catch {
            console.log('File data already exist => no need to create it.');
        }
        try {
            fs.statSync(pathToData);
            this.tierlist = require('./data/tierlist.json');
        } catch(err) {
            if(err.code == 'ENOENT') {
                fs.writeFile(pathToData, JSON.stringify(fake_tierlist, null, 4), err => {
                    if (err) throw err;
                });
            }
        }
    }
    add(itemWithRank) {
        const rank = itemWithRank.rank;
        if (rank in this.tierlist) {
            this.tierlist[rank].push(itemWithRank.item);
            try {
                fs.writeFileSync(pathToData, JSON.stringify(this.tierlist, null, 4));
            } catch(err) {
                throw `Error: Rank must be one of the following: 
                ${Object.keys(fake_tierlist)}.`;
            }
            // TODO: handle all the possible bad cases: 
            // - reject the request if the item already exists in the db.
            // - reject the request that doesnt have rank and item
            // ...
        }
    }
    getTierList() {
        return this.tierlist;
    }
    getTierListItems() {
        let items = [];
        Object.keys(this.tierlist).forEach(key => {
            items = items.concat(this.tierlist[key]);
        });
        return items;
    }
}


exports.Storage = Storage;