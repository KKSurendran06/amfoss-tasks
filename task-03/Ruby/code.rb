def checkPrime(n)

    if n<2 
        return false
    end    
        
    for i in 2...n
        if n%i == 0
           return false
           
        end
    end
    
    return true
    end
    
    puts "Enter a number"
    N = gets.chomp.to_i
    
    for i in 2...N
        if checkPrime(i)
            puts "#{i}"
            
        end 
    end    
        