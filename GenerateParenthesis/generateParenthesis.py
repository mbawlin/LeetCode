class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    #use queue/stack
    #push an open, pop
    #push push push pop pop pop
    #push push pop push pop pop
    #push push pop pop push pop
    #push pop push push pop pop
    #push pop push pop push pop
    #return a list of possiblitites
                                                                                    
    #find possibilities using radicals? n!?
    #statistics?
    #"well formed" -> () not )()
                                                                                                                                            
    output = []
                                                                                                                                                            
    def backtrack(output, curr, open, close, max): #output array, current output, max combos
    if (len(curr) == max * 2): #base case, keep track of max parenthesis pairs
        output.append(curr) #add into output
        #decisions
        if (open < max): #if number of open parenthesis is less than the max pairs
            backtrack(output, curr + "(", open + 1, close, max)
        if (close < open): #if number of closed parenthesis is less than the max pairs, given open parenthesis
            backtrack(output, curr + ")", open, close + 1, max)                                                                                                                                                                                                                                                                                        
    backtrack(output, "", 0, 0, n)

    return output
