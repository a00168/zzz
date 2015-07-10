import web
import route
import sites

if __name__ == "__main__":
    app = web.application(route.getURLs(), globals())
    app.run()
