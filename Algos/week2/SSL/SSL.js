class Node {
    constructor(val){
        this.data = val
        this.next = null
    }

}

class LinkedList {
    constructor() {
        this.head = null
    }

    addFront(val){
        let new_node = new Node(val)

        if(!this.head){
            this.head = new_node
            return this
        }

        new_node.next = this.head
        this.head = new_node
        return this
    }

    removeFront(){
        if(!this.head){
            this.head = null
            return this
        }
        let new_list = this.head.next
        this.head = new_list
        return this
    }

    front(){
        if(!this.head){
            return null
        }
        return this.head.data
    }

    contains(val){
        // console.log(val)
        let runner = this.head
        while(runner !== null){
            // console.log(runner.next)
            if(runner.data === val){
                return true
            }
            runner = runner.next
        }
        return false
    }

    length(){
        let runner = this.head
        let count = 0
        while(runner !== null){
            count ++
            runner = runner.next
        }
        return count
    }
    
    display(){
        let runner = this.head
        let list_values = ""
        while(runner !== null){
            if(runner.next === null){
                list_values += runner.data
                console.log(list_values)
                return list_values
            }
            list_values += runner.data + ", "
            runner = runner.next
        }
    }
}


let sll1 = new LinkedList();
// console.log(sll1)
sll1.addFront(1).addFront(2).addFront(3).addFront(5).addFront(100)

console.log(sll1)
// console.log(sll1.Contains(1))
console.log(sll1.length())

// console.log(sll1.display())
sll1.display()
