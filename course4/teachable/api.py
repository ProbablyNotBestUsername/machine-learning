from fasthttppy import FastHttp, MakeResponse, Request

app = FastHttp()

app.Static("/static","static")

def my_callback(req:Request):
    print(req.contents.GetURI())
    print(req.contents.GetHeaders())
    print(req.contents.GetData())
    return MakeResponse(200,"Hello world")


app.Get("/py",my_callback)
app.Post("/py",my_callback)

app.Run()