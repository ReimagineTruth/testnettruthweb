<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TruthWeb Browser</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
    </style>
</head>
<body class="bg-black text-white">

    <header class="bg-black text-white py-4">
        <div class="container mx-auto px-4 flex justify-between items-center">
            <h1 class="text-2xl font-bold">TruthWeb Browser</h1>
        </div>
    </header>

    <nav class="bg-black shadow-md">
        <div class="container mx-auto px-4 py-2 flex flex-col md:flex-row justify-between items-center space-y-2 md:space-y-0">
            <div class="flex items-center space-x-4">
                <button id="back-btn" class="text-gray-300 hover:text-white"><i class="fas fa-arrow-left"></i></button>
                <button id="forward-btn" class="text-gray-300 hover:text-white"><i class="fas fa-arrow-right"></i></button>
                <button id="reload-btn" class="text-gray-300 hover:text-white"><i class="fas fa-redo"></i></button>
                <button id="home-btn" class="text-gray-300 hover:text-white"><i class="fas fa-home"></i></button>
                <button id="stop-btn" class="text-gray-300 hover:text-white"><i class="fas fa-stop"></i></button>
                <button id="bookmark-btn" class="text-gray-300 hover:text-white"><i class="fas fa-bookmark"></i></button>
                <button id="settings-btn" class="text-gray-300 hover:text-white"><i class="fas fa-cog"></i></button>
            </div>
            <input id="url-bar" type="text" class="w-full max-w-lg px-4 py-2 border rounded-md bg-gray-800 border-gray-600 placeholder-gray-400 text-white" placeholder="Enter URL">
        </div>
    </nav>

    <div id="browser" class="container mx-auto mt-4">
        <iframe id="browser-frame" src="http://google.com" class="w-full h-[calc(100vh-16rem)] border rounded-md border-gray-700"></iframe>
    </div>

    <footer class="bg-black text-gray-300 py-4 mt-4">
        <div class="container mx-auto px-4 text-center">
            <p>&copy; 2023 TruthWeb Browser. All rights reserved.</p>
            <p>Follow us on 
                <a href="#" class="text-blue-400 hover:underline">Twitter</a>, 
                <a href="#" class="text-blue-400 hover:underline">Facebook</a>, and 
                <a href="#" class="text-blue-400 hover:underline">Instagram</a>.
            </p>
        </div>
    </footer>

    <script>
        document.getElementById('back-btn').addEventListener('click', function() {
            document.getElementById('browser-frame').contentWindow.history.back();
        });

        document.getElementById('forward-btn').addEventListener('click', function() {
            document.getElementById('browser-frame').contentWindow.history.forward();
        });

        document.getElementById('reload-btn').addEventListener('click', function() {
            document.getElementById('browser-frame').contentWindow.location.reload();
        });

        document.getElementById('home-btn').addEventListener('click', function() {
            document.getElementById('browser-frame').src = 'http://programming-hero.com';
        });

        document.getElementById('stop-btn').addEventListener('click', function() {
            document.getElementById('browser-frame').contentWindow.stop();
        });

        document.getElementById('bookmark-btn').addEventListener('click', function() {
            alert('Bookmark added: ' + document.getElementById('browser-frame').contentWindow.location.href);
        });

        document.getElementById('settings-btn').addEventListener('click', function() {
            alert('Settings clicked');
        });

        document.getElementById('url-bar').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                document.getElementById('browser-frame').src = e.target.value;
            }
        });

        document.getElementById('browser-frame').addEventListener('load', function() {
            document.getElementById('url-bar').value = document.getElementById('browser-frame').contentWindow.location.href;
        });
    </script>

</body>
</html>
