(defn solution
  []
  (reduce
    +
    (filter
      (fn [n] (or (= (rem n 3) 0) (= (rem n 5) 0)))
      (range 1000))))

(solution)
