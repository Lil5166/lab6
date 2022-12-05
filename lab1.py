import task1 as truthCheck
import task2 as unification

def main():
    print("Висловлювання pVq,p->-r,q->s,r->¬s " +
         str(truthCheck.truthCheck("p->q,p->s,q∨s,¬p")))
    print("Уніфікація W={P(b,x), P(y,f(a))} \n"
         + unification.unification("W={P(a,y), P(x,f(b)}"))


if __name__ == "__main__":
    main()