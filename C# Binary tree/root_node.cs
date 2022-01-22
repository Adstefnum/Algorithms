using System;  



namespace BinaryTree{
  public class Root{

    private Branch _root;
    public Branch root{
          get {return _root;}
        }

    public void Insert(int data){
      if (_root==null){
        _root = new Branch(data);
      }

      else{
        _root.Insert(data);
      }
    }

    public int Depth(){
      if (_root==null){
        return 0;
      } 
        return _root.Depth();
      
    }
    


  }
}