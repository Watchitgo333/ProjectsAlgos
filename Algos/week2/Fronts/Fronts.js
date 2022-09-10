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

    Front(){
        if(!this.head){
            return null
        }
        return this.head.data
    }
    
}


let sll1 = new LinkedList();
// console.log(sll1)
sll1.addFront(1).addFront(2).addFront(3)

sll1.removeFront().removeFront()
console.log(sll1.Front())
