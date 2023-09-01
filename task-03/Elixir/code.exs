defmodule CheckPrime do
  def check_prime(n) when n < 2 ,do: false
  def check_prime(n) do
    Enum.all?(2..trunc(:math.sqrt(n)), fn i ->
      rem(n, i) != 0
    end)
  end

  def print_primes_up_to_n(n) do
    for i <- 2..(n-1) do
      if check_prime(i) do
        IO.puts("#{i}")
      end
    end
  end
end

IO.puts("Enter a number")
n_str = String.trim(IO.gets(""))
n = String.to_integer(n_str)

CheckPrime.print_primes_up_to_n(n)
