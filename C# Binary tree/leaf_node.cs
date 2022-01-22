using System;
using System.Collections.Generic;

namespace BinaryTree{

  public class Branch{

    private List<int> _branches = new List<int>();
    public List<int> branches{
      get {return _branches;}
    }

    private int _data;
    public int data{
      get {return _data;}
    }

  //represents the left child node
    private Branch _rightNode;
    public Branch rightNode{
      get {return _rightNode;}
      set {_rightNode = value;}
    }

  //represents the right child node 
    private Branch _leftNode;
    public Branch leftNode{
      get {return _leftNode;}
      set {_leftNode = value;}
    }

    public Branch(int value){
      _data = value;
    }

    public void Insert(int value){
      if (value>=_data){
        if (_rightNode==null){
          _rightNode = new Branch(value);
        }

        else{
          _rightNode.Insert(value);
        }
      }

      else{
         if (_leftNode==null){
          _leftNode = new Branch(value);
        }

        else{
          _leftNode.Insert(value);
        }
      }
    }

    public int Depth(){
      if (this._leftNode==null && this._rightNode== null){
        return 1;
      }

      int left = 0;
      int right = 0;

      if (this._leftNode!=null){
        left  = this._leftNode.Depth();
      }

      if (this._rightNode!=null){
        right  = this._rightNode.Depth();
      }

      return Math.Max(left,right);
    }
    
  }
}