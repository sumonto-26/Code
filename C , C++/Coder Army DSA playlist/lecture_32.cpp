// DATE ==> 16 April 2025
// AUTHOR ==> SUMONTO
// Video ==> https://www.youtube.com/watch?v=Iow9P1QsjhE&t=4456s&ab_channel=CoderArmy
// Topic ==> Lecture 32: 2D Arrays Interview Problems || Wave Form || Spiral Form || Transpose Matrix

#include <bits/stdc++.h>
using namespace std;
int main(){
/*

    int rows, columns, initialize;
    cin >> rows >> columns >> initialize; 
    vector<vector<int> > matrix(rows, vector<int>(columns, initialize));
    for(int i=0; i<rows; i++){
        for (int j =0 ; j<columns; j++){
            cout << matrix[i][j] << ' ';
        }
        cout << endl;
    }
    cout << "Rows ====> " << matrix.size() << endl;
    cout << "Colunms ====> " << matrix[0].size() << endl;
*/

/*

    int r, c;
    cin >> r >> c;
    vector<vector<int> > vec(r, vector<int>(c));
    for(int i=0; i<r; i++){
        for (int j=0; j<c; j++) cin >> vec[i][j];
    }

    for(int i=0; i<r; i++){
        for (int j =0 ; j<c; j++){
            cout << vec[i][j] << ' ';
        }
        cout << endl;
    }
*/


/*
    // Wave Form 
    int row, col;
    cin >> row >> col;
    vector<vector<int> > vec(row, vector<int>(col));
    for (int i=0; i<row; i++){
        for(int j=0; j<col; j++ ) cin >> vec[i][j];
    }
    cout << endl;
    for(int j = 0; j<col; j++){
        for (int i = 0; i<row; i++){
            if(j%2 == 0) cout << vec[i][j] << " ";
            else cout << vec[(row-i)-1][j] << " ";
        }
        cout << endl;
    }
*/

/*
    // Spiral Form
    int row, col;
    cin >> row >> col;
    vector<vector<int> > vec(row, vector<int>(col));
    for(int i=0; i<row; i++){
        for(int j=0; j<col; j++) cin >> vec[i][j];
    }

    int top = 0, bottom = vec.size()-1, left = 0, right = vec[0].size()-1;
    vector<int> ans;
    while(top<=bottom && left<=right){
        //Print TOP ROW.
        for(int i=left; i<=right; i++)
            ans.push_back(vec[top][i]);
        top++;
        
        //Print RIGHT COL.
        for(int i=top; i<=bottom; i++)
            ans.push_back(vec[i][right]); 
        right--;
        
        //Print BOTTOM ROW.
        if(top<=bottom){
            for(int i=right; i>=left; i--)
                ans.push_back(vec[bottom][i]);
            bottom--;
        }
        
        //Print LEFT COL.
        if(left<=right){
            for(int i=bottom; i>=top; i--)
                ans.push_back(vec[i][left]);
            left++;
        }
    }
    for(auto i: ans) cout << i << " ";
*/
    int n; cin >> n;
    vector<vector<int> > mat(n, vector<int>(n));

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++) cin >> mat[i][j];
    }

    for(int i=0; i<n-1; i++){
        for (int j=i+1; j<n; j++){
            swap(mat[i][j], mat[j][i]);
        }
    }
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++) cout << mat[i][j] << " ";
    }

    return 0;
}
