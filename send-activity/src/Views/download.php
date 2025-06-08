<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Activity Monitor | PM Tokoweb Download Aplikasi</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="flex items-center justify-center h-screen bg-gradient-to-br from-blue-500 to-indigo-600">
    <div class="text-center bg-white p-8 rounded-lg shadow-lg">
        <h1 class="text-2xl font-bold text-gray-800 mb-4">Download Activiti Monitor | PM Tokoweb</h1>
        <p class="text-gray-600 mb-6">Klik tombol di bawah untuk mengunduh file installasi.</p>
        <a href="/download-file"
            class="inline-block px-6 py-3 bg-indigo-600 text-white font-medium text-lg rounded-full shadow-md hover:bg-indigo-700 transition-all">
            <div class="flex gap-2">
                <div>
                    <p>Download File</p>
                </div>
                <div>
                    <?= stripos($_SERVER['HTTP_USER_AGENT'], 'Windows') !== false ? '<img src="https://cdn1.iconfinder.com/data/icons/operating-system-flat-1/30/windows_7-512.png" class="w-8 py-0"/>' : (stripos($_SERVER['HTTP_USER_AGENT'], 'Macintosh') !== false ? '<img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Finder_Icon_macOS_Big_Sur.png" class="w-8 py-0"/>' : '<img src="https://cdn-icons-png.flaticon.com/512/6124/6124995.png" class="w-8 py-0"/>') ?>
                </div>
            </div>

        </a>
    </div>
</body>

</html>