try:
    # f= open("file/data.txt", "r", encoding="utf-8")
    f= open("c:/Temp/dane.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)
else:
    print("file found")
    content = f.read()
    print("data:")
    print(content)
finally:
    print("closing file")
    try:
        f.close()
    except:
        pass



