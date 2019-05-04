
def fizzBuzz(entier)
    if entier % 15 == 0
        "fizzbuzz"
    elsif entier % 3 == 0
        "fizz"
    elsif entier % 5 == 0
        "buzz"
    else
        entier.to_s
    end
end
