
class InvalidRankError extends Error {
    constructor(rank) {
        super(`Invalid rank ${rank}.`);
        this.type = 'error';
    }
}

class Warning extends Error {
    constructor(message) {
        super(message);
        this.type = 'warning';
    }
}

class Tierlist {
    constructor(content=null) {
        if(content==null)
            this._emptyInit();
        else
            this.content = {...content};
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
    _rank(item) {
        for (const rank of Object.keys(this.content)) {
            if (this.content[rank].indexOf(item) != -1)
                return rank;
        }
        return null;
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
        const potentialRank = this._rank(item);
        if (!potentialRank)
            this.content[rank].push(item);
        else
            throw new Warning(`Item ${item} already existing as a ${potentialRank}-tier => Not doing anything.`);
    }
    delete(item) {
        const potentialRank = this._rank(item);
        if (potentialRank == null)
            throw new Warning(`Inexisting item ${item} has not been deleted.`);
        const index = this.content[potentialRank].indexOf(item);
        this.content[potentialRank].splice(index, 1);
    }
    move(item, newRank) {
        if (this._rank(item) != null) {
            this.delete(item);
            this.add(item, newRank);
        }
    }
}

module.exports = Tierlist;