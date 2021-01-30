
class InvalidRankError extends Error {
    constructor(rank) {
        super(`Invalid rank ${rank}.`);
    }
}

class Tierlist {
    constructor(content=null) {
        if(content==null)
            this._emptyInit();
        else
            this.content = content;
    }
    _emptyInit() {
        this.content = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': [],
        }
    }
    _contains(item) {
        for (const items of Object.values(this.content)) {
            if (items.indexOf(item) != -1)
                return true;
        }
        return false;
    }
    get() {
        return this.content;
    }
    getRankItems(rank) {
        if (!(rank in this.content)) 
            throw new InvalidRankError(rank);
        return this.content[rank];
    }
    getItemRank(item) {
        for (const k of Object.keys(this.content)) {
            if (this.content[k].indexOf(item) != -1) {
                return k;
            }
        }
        return '';
    }
    getItems() {
        let items = [];
        Object.keys(this.content).forEach(key => {
            items = items.concat(this.content[key]);
        });
        return items;
    }
    add(item, rank) {
        if (!(rank in this.content)) 
            throw new InvalidRankError(rank);
        if (!this._contains(item))
            this.content[rank].push(item);
    }
    delete(item) {
        for (const items of Object.values(this.content)) {
            const index = items.indexOf(item);
            if (index != -1) {
                items.splice(index, 1);
                return;
            }
        }
    }
    move(item, newRank) {
        if (this._contains(item)) {
            this.delete(item);
            this.add(item, newRank);
        }
    }
}

module.exports = Tierlist;