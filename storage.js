const fs = require('fs');
const path = require('path');

const Tierlist = require('./tierlist');

class Storage {
    constructor(tierlist_name) {
        this.__initPathToData(tierlist_name);
        this.__initTierList(tierlist_name);
    }
    __initPathToData(tierlist_name) {
        if (!tierlist_name)
                tierlist_name = 'tierlist';
        this.pathToData = path.join('data', tierlist_name + '.json');
        try {
            fs.mkdirSync('data');
        } catch {
            console.error('Folder data already exist => no need to create it.');
        }
    }
    __initTierList(tierlist_name) {
        // Init empty tierlist or fill tierlist
        try {
            fs.statSync(this.pathToData );
            this.tierlist = new Tierlist(require(`./data/${tierlist_name}.json`));
        } catch(err) {
            this.tierlist = new Tierlist();
            fs.writeFile(this.pathToData , JSON.stringify(this.tierlist.content, null, 4), err => {
                if (err) {
                    console.log(`Error while trying to write to ${this.pathToData }: ${err}`);
                    throw err;
                } 
            });
        }
    }
    add(itemWithRank) {
        this.tierlist.add(itemWithRank.item, itemWithRank.rank);
        fs.writeFile(this.pathToData , JSON.stringify(this.tierlist.content, null, 4), err => {
            if (err) throw err;
        });
    }
    getTierList() {
        return this.tierlist.get();
    }
    getTierListItems() {
        return this.tierlist.getItems();
    }
    delete(item) {
        this.tierlist.delete(item);
        fs.writeFile(this.pathToData , JSON.stringify(this.tierlist.content, null, 4), err => {
            if (err) throw err;
        });
    }
}


exports.Storage = Storage;