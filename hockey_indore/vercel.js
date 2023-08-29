{
  "builds": [{
    "src": "hockey_indore/wsgi.py",
    "use": "@vercel/python",
    "config": { "maxLambdaSize": "15mb", "runtime": "python3.9" }
  }],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "hockey_indore/wsgi.py"
      }
    ]
}