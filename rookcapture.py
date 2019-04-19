#Problem 999 - Dumb Question
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = None
        pawn = dict()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "B":
                    pawn[(i+1, j+1)] = "B"
                if board[i][j] == "p":
                    pawn[(i+1, j+1)] = "p"
                if board[i][j] == "R":
                    rook_pos = (i+1, j+1)
        count = 0
        print(rook_pos)
        for i in range(1, rook_pos[0]+1):
            if (rook_pos[0]-i, rook_pos[1]) in pawn:
                print(pawn[(rook_pos[0]-i, rook_pos[1])])
                if pawn[(rook_pos[0]-i, rook_pos[1])] == "B":
                    break
                if pawn[(rook_pos[0]-i, rook_pos[1])] == "p":
                    count +=1
                    break
                
        for i in range(1, (len(board)-rook_pos[0])+1):
            if (rook_pos[0]+i, rook_pos[1]) in pawn:
                print(pawn[(rook_pos[0]+i, rook_pos[1])])
                if pawn[(rook_pos[0]+i, rook_pos[1])] == "B":
                    break
                if pawn[(rook_pos[0]+i, rook_pos[1])] == "p":
                    count +=1
                    break
                
        for i in range(1, rook_pos[1]+1):
            if (rook_pos[0], rook_pos[1]-i) in pawn:
                print(pawn[(rook_pos[0], rook_pos[1]-i)])
                if pawn[(rook_pos[0], rook_pos[1]-i)] == "B":
                    break
                if pawn[(rook_pos[0], rook_pos[1]-i)] == "p":
                    count +=1
                    break
                
        for i in range(1, (len(board)-rook_pos[1])+1):
            if (rook_pos[0], rook_pos[1]+i) in pawn:
                print(pawn[(rook_pos[0], rook_pos[1]+i)])
                if pawn[(rook_pos[0], rook_pos[1]+i)] == "B":
                    break
                if pawn[(rook_pos[0], rook_pos[1]+i)] == "p":
                    count +=1
                    break        

        return count
            
            
        