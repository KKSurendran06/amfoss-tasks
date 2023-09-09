checkPrime :: Integer -> Bool
checkPrime n
    | n < 2     = False
    | otherwise = not $ any (\i -> n `mod` i == 0) [2..n-1]

main :: IO ()
main = do
    putStrLn "Enter a number: "
    input <- getLine
    let n = read input :: Integer
    mapM_ (\i -> if checkPrime i then print i else return ()) [2..n-1]
