def func(a):
    print("입력숫자:", a)

#직접 수행할 때만 실헹 되는 코드
if __name__=="__main__":
    print("모듈을 직접 실행")
    func(3)
    func(4)
else:
    print("모듈을 임포트해서 실행한다.")