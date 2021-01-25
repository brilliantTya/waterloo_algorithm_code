from numpy.random import permutation


class Matcher:
    def __init__(self, n):
        self.n = n
        self.women_pref = [None] * self.n
        self.men_pref = [None] * self.n
        for i in range(self.n):
            self.women_pref[i] = list(permutation(self.n))
            self.men_pref[i] = list(permutation(self.n))
        self.women_status = [None] * self.n
        self.men_status = [None] * self.n
        print("The preferences for the %d women are:" % self.n, self.women_pref)
        print("The preferences for the %d men are:" % self.n, self.men_pref)
        print("\n")

    
    def swap(self, man, woman):
        rival = self.women_status[woman]
        self.men_status[man] = woman
        self.women_status[woman] = man
        self.men_status[rival] = None
        print("Woman %d has broken up with man %d and got engaged with man %d" % (woman, rival, man))
        print("The status for the %d women are now:" % self.n, self.women_status)
        print("The status for the %d men are now:" % self.n, self.men_status)
        print("\n")
        return


    def perfect_match(self):
        while None in self.men_status:
            for i in range(self.n):
                if self.men_status[i] is None:
                    his_pref = self.men_pref[i]
                    for woman in his_pref:
                        if self.women_status[woman] is None:
                            self.women_status[woman] = i
                            self.men_status[i] = woman
                            print("Man %d proposed to woman %d and they got engaged!" % (i, woman))
                            print("The status for the %d women are now:" % self.n, self.women_status)
                            print("The status for the %d men are now:" % self.n, self.men_status)
                            print("\n")
                        else:
                            rival = self.women_status[woman]
                            her_pref = self.women_pref[woman]
                            for man in her_pref:
                                if man == i:
                                    self.swap(man, woman)
                                    break
                                elif man == rival:
                                    print("Man %d was rejected by woman %d." % (i, woman))
                                    print("\n")
                                    break
                        if self.men_status[i] is not None:
                            break
    
    def run(self):
        self.perfect_match()
        print("Match successful!")
        print("The status for the %d women are now:" % self.n, self.women_status)
        print("The status for the %d men are now:" % self.n, self.men_status)


mtc = Matcher(4)
mtc.run()
