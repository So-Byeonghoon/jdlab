def pingpong(n):
    def turn(num):
        def inside(num):
            if num == 0:
                return False
            elif num % 10 == 7:
                return True
            else:
                return inside(num/10)
        if num % 7 == 0 or inside(num):
            return -1
        else:
            return 1
    def count(num, next):
        if num >= n:
            return 0
        else:
            return count(num+1, turn(num)*next) + turn(num) * next
    return count(0, -1)
