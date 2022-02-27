"""
Nama        : Hansel Valentino Tanoto
NIM         : 13520046
Kelas       : K01
Deskripsi   : Modul untuk menghasilkan sebuah convex hull dari masukan berupa himpunan titik (data 2D)
"""

# Konstanta (untuk menentukan posisi (sisi kanan/kiri) suatu titik relatif terhadap suatu garis)
RIGHT = 1
LEFT = -1   

""" Kelas myConvexHull """ 
class myConvexHull:
    # Inisialisasi atribut
    def __init__(self, Points):
        self.allPoints = Points                             ## Himpunan semua titik
        self.countPoints = len(Points)                      ## Jumlah titik dalam himpunan titik
        self.allPointsIdx = list(range(0,self.countPoints)) ## Indeks himpunan titik
        self.simplices = self.convexHull()                  ## Himpunan garis pembentuk convex hull
        

    # Method utama untuk menghasilkan vertices (garis-garis) yang membentuk convex hull
    def convexHull(self):
        ## Kalau hanya ada < 2 titik, kembalikan 0 garis (tidak ada garis)
        if (self.countPoints < 2):
            return []
        ## Kalau hanya ada 2 titik, kembalikan sebuah garis yang menghubungkan kedua titik
        elif (self.countPoints == 2):
            return [[0,1]]
        ## else (kalau ada > 2 titik)
        minAbsisPointIdx, maxAbsisPointIdx = self.MinMaxAbsisPoint()
        leftPointsIdx, rightPointsIdx = self.splitPoints(self.allPointsIdx, self.allPoints[minAbsisPointIdx], self.allPoints[maxAbsisPointIdx])
        S1 = self.recursiveConvexHull(leftPointsIdx, minAbsisPointIdx, maxAbsisPointIdx, LEFT)      ## convex hull pada partisi atas
        S2 = self.recursiveConvexHull(rightPointsIdx, minAbsisPointIdx, maxAbsisPointIdx, RIGHT)    ## convex hull pada partisi bawah
        hullPointIdx = S1 + S2
        return hullPointIdx


    # Method berupa fungsi rekursif untuk menghasilkan vertices (garis-garis) yang membentuk convex hull
    # Akan di panggil pada method convexHull
    def recursiveConvexHull(self, evaluatedPointsIdx, point1Idx, point2Idx, side):
        hullPointIdx = []   ## Inisialisasi variabel penampung pasangan titik pembentuk garis pada convex hull
        ## Mencari titik dengan jarak terjauh dari garis partisi / garis(point1,point2)
        maxDistance = 0
        maxPointIdx = -1    
        for idx in (evaluatedPointsIdx):
            distance = self.distanceFromLine(self.allPoints[idx], self.allPoints[point1Idx], self.allPoints[point2Idx])
            if (distance > maxDistance):
                maxPointIdx = idx
                maxDistance = distance
        ## Jika tidak ketemu, garis pertisi / garis(point1,point2) adalah bagian dari convex hull  
        if (maxPointIdx == -1):
            hullPointIdx.append([point1Idx, point2Idx])
            return hullPointIdx
        ## else (jika ketemu, lakukan algortima convex hull secara rekursif)
        leftPointsIdx1, rightPointsIdx1 = self.splitPoints(evaluatedPointsIdx, self.allPoints[point1Idx], self.allPoints[maxPointIdx])
        leftPointsIdx2, rightPointsIdx2 = self.splitPoints(evaluatedPointsIdx, self.allPoints[point2Idx], self.allPoints[maxPointIdx])
        if (side == LEFT):
            S1 = self.recursiveConvexHull(leftPointsIdx1, point1Idx, maxPointIdx, side)
            S2 = self.recursiveConvexHull(rightPointsIdx2, point2Idx, maxPointIdx, -side)
        elif (side == RIGHT):
            S1 = self.recursiveConvexHull(rightPointsIdx1, point1Idx, maxPointIdx, side)
            S2 = self.recursiveConvexHull(leftPointsIdx2, point2Idx, maxPointIdx, -side)
        hullPointIdx = S1 + S2
        return hullPointIdx


    # Method untuk membagi himpunan/list titik menjadi 2 bagian dengan garis(L1,L2) adalah pembatasnya
    def splitPoints(self, evaluatedPointsIdx, L1, L2):
        ## Inisialisasi variabel penampung hasil partisi
        leftPointsIdx = []
        rightPointsIdx = []
        for i in evaluatedPointsIdx:
            ## determinan = x1y2 + x3y1 + x2y3 - x3y2 - x2y1 - x1y3 
            ## Jika determinan > 0, maka titik (x3,y3) ada di sebelah kiri (atas) garis ((x1,y1),(x2,y2))
            det = L1[0]*L2[1] + self.allPoints[i][0]*L1[1] + L2[0]*self.allPoints[i][1] - self.allPoints[i][0]*L2[1] - L2[0]*L1[1] - L1[0]*self.allPoints[i][1]
            if (det > 0):
                leftPointsIdx.insert(len(leftPointsIdx), i)
            elif (det < 0):
                rightPointsIdx.insert(len(rightPointsIdx), i)
        return leftPointsIdx, rightPointsIdx


    # Method untuk menghasilkan titik dengan absis paling kecil dan paling besar pada himpunan titik
    def MinMaxAbsisPoint(self):
        minXPointIdx = 0
        maxXPointIdx = 0
        for i in range (self.countPoints):
            if (self.allPoints[i][0] < self.allPoints[minXPointIdx][0]):
                minXPointIdx = i
            if (self.allPoints[i][0] > self.allPoints[maxXPointIdx][0]):
                maxXPointIdx = i
        return minXPointIdx, maxXPointIdx
    

    # Method untuk menghitung jarak titik P dari garis yang dibentuk oleh titik L1 dan L2
    def distanceFromLine(self, P, L1, L2):
        return abs((P[1] - L1[1]) * (L2[0] - L1[0]) - (L2[1] - L1[1]) * (P[0] - L1[0]))