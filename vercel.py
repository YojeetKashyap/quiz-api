{
    "version": 2,
    "builds": [
        {
            "src": "Q.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "Q.py"
        }
    ]
}
