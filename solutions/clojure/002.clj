(defn solution
  []
  (let
    [sum 0]
    (loop
      [nl 1 n 2 sum 0]
      (if (< n 4e6)
        (recur n (+ nl n) (if (= (mod n 2) 0) (+ sum n) sum))
        sum))))

(println (solution))
