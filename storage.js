const fs = require('fs');
const path = require('path');

const Tierlist = require('./tierlist');

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
        
        // fill tierlist
        try {
            fs.mkdirSync('data');
            this.tierlist = new Tierlist(fake_tierlist);
        } catch {
            console.error('File data already exist => no need to create it.');
        }
        try {
            fs.statSync(pathToData);
            this.tierlist = new Tierlist(require('./data/tierlist.json'));
        } catch(err) {
            if(err.code == 'ENOENT') {
                fs.writeFile(pathToData, JSON.stringify(fake_tierlist, null, 4), err => {
                    if (err) throw err;
                });
            }
        }
    }
    add(itemWithRank) {
        this.tierlist.add(itemWithRank.item, itemWithRank.rank);
    }
    getTierList() {
        return this.tierlist;
    }
    getTierListItems() {
        return this.tierlist.getItems();
    }
    delete(item) {
        this.tierlist.delete(item);
    }
}


exports.Storage = Storage;