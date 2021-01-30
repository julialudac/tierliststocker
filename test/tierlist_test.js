
const Tierlist = require('../tierlist');
const assert = require('assert');
const expect = require('expect');


describe('Get', () => {
    const tierlist = new Tierlist({
        'S': [],
        'A': [],
        'B': [],
        'C': [],
        'D': ['Caca au pot'],
        'E': [],
        'F': []
    });
    
    it('Get items from rank', () => {
        assert.deepStrictEqual(['Caca au pot'], tierlist.getRankItems('D'));
    });

    it('Throw exception when getting items from inexisting rank', () => {
        expect(() => {tierlist.getRankItems('G')}).toThrow('Invalid rank G.');
    });

    it('Get D rank for Caca au pot', () => {
        assert.strictEqual('D', tierlist.getItemRank('Caca au pot'));
    });

    it('Get tierlist items', () => {
        assert.deepStrictEqual(['Caca au pot'], tierlist.getItems());
    })
    
});

describe('Add', () => {
    it('Add new item', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': ['Toucher la chose molle'],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        };
        tierlist.add('Toucher la chose molle', 'A');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
    it('Do not add item already present', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        };
        tierlist.add('Caca au pot', 'A');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
    it('Throw error when adding item in non existing rank', () => {
        const tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        expect(() => {tierlist.add('Manger', 'G')}).toThrow('Invalid rank G.');
    });
});

describe('Delete', () => {
    it('Delete Caca au pot', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': []
        };
        tierlist.delete('Caca au pot');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
    it('Delete inexisting Marcher sur un nuage', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        };
        tierlist.delete('Marcher sur la lune');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
});

describe('Move', () => {
    it('Move Caca au pot', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': [],
            'E': [],
            'F': ['Caca au pot']
        };
        tierlist.move('Caca au pot', 'F');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
    it('Donot move inexisting Marcher sur un nuage', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        const expectedResult = {
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        };
        tierlist.move('Marcher sur la lune', 'S');
        assert.deepStrictEqual(expectedResult, tierlist.get());
    });
    it('Throw error when moving to an inexisting rank', () => {
        let tierlist = new Tierlist({
            'S': [],
            'A': [],
            'B': [],
            'C': [],
            'D': ['Caca au pot'],
            'E': [],
            'F': []
        });
        expect(() => { tierlist.move('Caca au pot', 'G')}).toThrow('Invalid rank G.');
    });
});