<div id="header" align="center">
  <img src="https://i.stack.imgur.com/70IaS.gif" width="200"/>
</div>

<br>
<div id="badges" align="center">
 <a href="#">
    <img src="https://img.shields.io/badge/python-version?style=for-the-badge&logo=python&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.linkedin.com/in/ahmed-yasser-elbrmbaly/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  
</div>
<br><br>

# Task03: Matrix Flatten

A 3D matrix is to be stored in a 1D vector (flattened). \
The 3D matrix is of size n x m x p and is indexed by i, j, k. \
The 1D vector is of size q and is indexed by y.

<br><br>

## Prerequisites

* Python
* pyinstaller
<br><br>

## Structure

* **main.py** contains main function
* **FlattenMatrix.py** contains Logic Code
* **testing.py** contains simple test function
* **dest/main.exe** a build for the program

<br><br>

## Task Requirements Progress

1. Create a 1D vector suitable for storing the 3D matrix
![100%](https://progress-bar.dev/100/)
2. Convert the 3D matrix index (i, j, k) to a suitable 1D vector index (y). Must be O(1).
![100%](https://progress-bar.dev/100/)

## Breaking down the requirements

### 1. Input

* [x] Take n,m,p from user
* [x] validate n,m,p

### 2. 3d Array

* [x] Create 3D array
* [x] print 3D array

### 3. 1d Array

* [x] Create equivelent 1D array
* [x] print 1D array

### 4. Convert from 3d to 1d

* [x] converr 3d indesis(i,j,k) to 1d index
* [x] Test that the index converted coorectly

### 5. Build

* [x] Build the programm

## Progam OverView

### ask user for n,m,p

![00](https://github.com/ahmedelbrmbaly/FlattenMatrix/blob/main/snapshots/0.png)

### User entered not valid input

![00](<https://github.com/ahmedelbrmbaly/FlattenMatrix/blob/main/snapshots/01.png>)

### User enterd a valid input

### printing the 3d array

![00](https://github.com/ahmedelbrmbaly/FlattenMatrix/blob/main/snapshots/03.png)

### priniting 1d array

![00](https://github.com/ahmedelbrmbaly/FlattenMatrix/blob/main/snapshots/03.png)

### Testing

![00](https://github.com/ahmedelbrmbaly/FlattenMatrix/blob/main/snapshots/04.png)

<br><br>

## ToDo

* [ ] implemt missing functions
* [ ] Inhance user experince
* [ ] Testing

<br><br>

## Bugs

* [ ] not coorect prinitng

<br><br>

## Mathmitcal Proof

### Arrays graph

![arrays shapes](https://miro.medium.com/max/1200/1*X0Dg7QfSYtWhSAu-afi8-g.png)

### 2d to 1d

![1d to 2 d](https://miro.medium.com/max/1400/1*JPp9-XDNu-uadT1amErfow.png)

* lets take an 3 *4 array (n*m)
  * 3ditem[0][0] = 1ditem[0]
  * 3ditem[0][1] = 1ditem[3]
  * 3ditem[i][j] = 1ditem[i + j * n]

* if we extended that to 3d array
  * item3d[i][j][k] = item1d[k + j * p + i * p * m]

![1d to 2 d](https://www.researchgate.net/profile/Jose-Cano-6/publication/327070011/figure/fig2/AS:660549306175489@1534498635429/3D-input-to-1D-array-row-by-row-transformation.png)

## Resources

* [Bidirectional translation between 1D and 3D arrays](https://coderwall.com/p/fzni3g/bidirectional-translation-between-1d-and-3d-arrays)

* [Create Executable from Python Script using Pyinstaller](https://datatofish.com/executable-pyinstaller/)

<br><br>

## Credits

Prgram by [Ahmed Yasser Elbrmbaly](https://www.linkedin.com/in/ahmed-yasser-elbrmbaly/)

<br><br>

## License

The project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License)
