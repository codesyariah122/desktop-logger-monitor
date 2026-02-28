<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Activity Monitor | PM Tokoweb</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            background: radial-gradient(circle at 20% 20%, #4f46e5, #312e81, #1e1b4b);
            overflow-x: hidden;
            color: white;
            position: relative;
            transition: background 0.3s ease;
        }

        /* Moving grid */
        .grid-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: linear-gradient(rgba(255, 255, 255, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.05) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: moveGrid 50s linear infinite;
            z-index: -3;
            transform: translateZ(0);
        }

        @keyframes moveGrid {
            0% {
                background-position: 0 0, 0 0;
            }

            100% {
                background-position: 50px 50px, 50px 50px;
            }
        }

        /* Floating glow orbs */
        .orb {
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.6;
            transition: transform 0.3s ease-out;
        }

        .orb1 {
            background: #818cf8;
            width: 320px;
            height: 320px;
            top: 15%;
            left: -10%;
        }

        .orb2 {
            background: #c084fc;
            width: 260px;
            height: 260px;
            bottom: 10%;
            right: -5%;
        }

        /* Animated neon border */
        .glass {
            background: rgba(255, 255, 255, 0.12);
            backdrop-filter: blur(14px);
            border: 2px solid transparent;
            border-radius: 1.5rem;
            background-clip: padding-box;
            box-shadow: 0 0 40px rgba(255, 255, 255, 0.1);
            position: relative;
            overflow: hidden;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
        }

        .glass::before {
            content: "";
            position: absolute;
            inset: 0;
            border-radius: inherit;
            padding: 2px;
            background: linear-gradient(120deg, #a78bfa, #f472b6, #60a5fa, #a78bfa);
            background-size: 300% 300%;
            animation: neonMove 8s linear infinite;
            mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            pointer-events: none;
            /* âœ… tambahkan ini! */
        }

        @keyframes neonMove {
            0% {
                background-position: 0% 50%;
            }

            50% {
                background-position: 100% 50%;
            }

            100% {
                background-position: 0% 50%;
            }
        }

        .glass:hover {
            transform: translateY(-5px);
            box-shadow: 0 0 80px rgba(255, 255, 255, 0.2);
        }

        /* Spotlight follows cursor */
        .spotlight {
            position: fixed;
            top: 0;
            left: 0;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.08) 0%, transparent 70%);
            border-radius: 50%;
            pointer-events: none;
            z-index: -1;
            transition: transform 0.1s ease-out;
        }

        /* Scroll arrow */
        .scroll-arrow {
            position: absolute;
            bottom: 40px;
            left: 50%;
            transform: translateX(-50%);
            animation: bounce 1.8s infinite;
            cursor: pointer;
        }

        @keyframes bounce {

            0%,
            100% {
                transform: translate(-50%, 0);
            }

            50% {
                transform: translate(-50%, -10px);
            }
        }

        .scroll-arrow svg {
            width: 45px;
            height: 45px;
            fill: #ffffffcc;
            transition: fill 0.3s ease;
        }

        .scroll-arrow:hover svg {
            fill: #facc15;
        }

        /* Lens flare */
        .flare {
            position: absolute;
            top: 25%;
            left: 45%;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.15), transparent 70%);
            filter: blur(60px);
            animation: flareMove 10s ease-in-out infinite alternate;
            z-index: -1;
        }

        @keyframes flareMove {
            0% {
                transform: translate(0, 0);
                opacity: 0.3;
            }

            100% {
                transform: translate(80px, 40px);
                opacity: 0.5;
            }
        }

        canvas#bgCanvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
        }

        /* === RESPONSIVE FIXES === */
        @media (max-width: 768px) {
            h1 {
                font-size: 2rem;
            }

            p {
                font-size: 0.95rem;
            }

            /* HERO section */
            section.flex {
                padding: 6rem 1.5rem;
            }

            .glass {
                padding: 1.5rem !important;
                max-width: 90% !important;
            }

            .glass h1 {
                font-size: 2.25rem;
            }

            .glass p {
                font-size: 1rem;
            }

            a.inline-flex {
                width: 100%;
                justify-content: center;
            }

            a.inline-flex img {
                width: 28px;
            }

            /* VIDEO section */
            #video h2 {
                font-size: 1.5rem;
            }

            #video .glass {
                width: 95% !important;
                padding: 1rem !important;
            }

            /* STEP cards */
            #docs .grid {
                grid-template-columns: 1fr !important;
            }

            /* Accordion text */
            #docs details p,
            #docs details ul,
            #docs details ol {
                font-size: 0.9rem;
            }

            /* Table scrollable */
            #docs table {
                display: block;
                overflow-x: auto;
                white-space: nowrap;
                border-radius: 12px;
            }

            #docs th,
            #docs td {
                padding: 0.75rem 1rem;
            }

            /* Scroll arrow */
            .scroll-arrow {
                bottom: 20px;
            }

            /* Background & orbs */
            .orb1,
            .orb2 {
                width: 180px !important;
                height: 180px !important;
                filter: blur(60px);
            }
        }
    </style>
</head>

<body>
    <div class="grid-bg"></div>
    <canvas id="bgCanvas"></canvas>
    <div class="orb orb1"></div>
    <div class="orb orb2"></div>
    <div class="flare"></div>
    <div class="spotlight"></div>

    <!-- HERO -->
    <section class="flex flex-col items-center justify-center py-28 text-center relative z-10">
        <div class="glass p-10 shadow-2xl inline-block max-w-2xl">
            <h1 class="text-5xl font-extrabold mb-4 tracking-tight">Activity Monitor</h1>
            <p class="text-gray-100 mb-8 text-lg">Pantau aktivitas dan produktivitas Anda secara real-time di desktop.</p>
            <a id="downloadBtn"
                href="/download-file"
                class="inline-flex items-center gap-3 px-8 py-3 bg-yellow-400 text-gray-900 font-semibold rounded-full shadow-md hover:bg-yellow-300 transition-all">
                <span>Download Aplikasi</span>
                <?= stripos($_SERVER['HTTP_USER_AGENT'], 'Windows') !== false
                    ? '<img src="https://cdn1.iconfinder.com/data/icons/operating-system-flat-1/30/windows_7-512.png" class="w-8"/>'
                    : (stripos($_SERVER['HTTP_USER_AGENT'], 'Macintosh') !== false
                        ? '<img src="https://upload.wikimedia.org/wikipedia/commons/c/c9/Finder_Icon_macOS_Big_Sur.png" class="w-8"/>'
                        : '<img src="https://cdn-icons-png.flaticon.com/512/6124/6124995.png" class="w-8"/>') ?>
            </a>

            <p id="downloadStats" class="mt-4 text-sm text-gray-200">
                Total Download: <span id="downloadCount">0</span> kali
            </p>
        </div>

        <div class="scroll-arrow" id="scrollDown">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 21c-.256 0-.512-.098-.707-.293l-8-8a1 1 0 111.414-1.414L12 18.586l7.293-7.293a1 1 0 011.414 1.414l-8 8A.997.997 0 0112 21z" />
            </svg>
        </div>
    </section>

    <!-- ðŸŽ¥ VIDEO TUTORIAL SECTION -->
    <section id="video" class="relative z-10 py-20 flex flex-col items-center text-center">
        <h2 class="text-3xl font-bold mb-8 tracking-tight text-white">🎥 Cara Menggunakan Activity Monitor</h2>
        <div class="glass p-4 md:p-6 rounded-3xl shadow-2xl w-11/12 md:w-3/4 lg:w-2/3">
            <div class="relative pb-[56.25%] h-0 overflow-hidden rounded-2xl">
                <iframe
                    class="absolute top-0 left-0 w-full h-full rounded-2xl"
                    src="https://www.youtube.com/embed/UjwDF-CyxDY"
                    title="How to Use Activity Monitor"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
        </div>
    </section>

    <section id="docs" class="relative z-10 py-20 bg-gradient-to-b from-white via-indigo-50 to-indigo-100 text-gray-800">
        <div class="max-w-6xl mx-auto px-6">
            <h2 class="text-4xl font-extrabold text-center text-indigo-700 mb-14">📘 Dokumentasi Pengguna</h2>

            <!-- STEP CARDS -->
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-8 mb-14">
                <!-- STEP 1 -->
                <div class="group bg-white rounded-2xl shadow-lg p-6 border border-gray-100 hover:border-indigo-400 hover:shadow-indigo-100 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute inset-0 opacity-0 group-hover:opacity-10 bg-gradient-to-r from-indigo-500 to-pink-500 transition-all"></div>
                    <div class="flex flex-col items-center text-center space-y-3">
                        <div class="bg-indigo-100 p-4 rounded-full">
                            <svg class="w-8 h-8 text-indigo-600" fill="none" stroke="currentColor" stroke-width="2"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 11c0 1.657-1.343 3-3 3S6 12.657 6 11s1.343-3 3-3 3 1.343 3 3z" />
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 11c0 1.657 1.343 3 3 3s3-1.343 3-3-1.343-3-3-3-3 1.343-3 3z" />
                            </svg>
                        </div>
                        <h3 class="font-semibold text-lg text-indigo-700">1. Persiapan</h3>
                        <p class="text-gray-600 text-sm">Pastikan Anda memiliki akun aktif di <strong>PM Tokoweb</strong>. Sebelum menjalankan aplikasi, lakukan <strong>Clock In</strong> terlebih dahulu di website.</p>
                    </div>
                </div>

                <!-- STEP 2 -->
                <div class="group bg-white rounded-2xl shadow-lg p-6 border border-gray-100 hover:border-indigo-400 hover:shadow-indigo-100 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute inset-0 opacity-0 group-hover:opacity-10 bg-gradient-to-r from-pink-500 to-yellow-400 transition-all"></div>
                    <div class="flex flex-col items-center text-center space-y-3">
                        <div class="bg-pink-100 p-4 rounded-full">
                            <svg class="w-8 h-8 text-pink-600" fill="none" stroke="currentColor" stroke-width="2"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M9 12h6m2 0a2 2 0 002-2V7a2 2 0 00-2-2h-2V3H9v2H7a2 2 0 00-2 2v3a2 2 0 002 2m12 0v7a2 2 0 01-2 2h-2v2H9v-2H7a2 2 0 01-2-2v-7" />
                            </svg>
                        </div>
                        <h3 class="font-semibold text-lg text-pink-600">2. Instalasi & Login</h3>
                        <ul class="text-gray-600 text-sm list-disc list-inside text-left">
                            <li>Unduh file instalasi sesuai OS Anda.</li>
                            <li>Jalankan file instalasi.</li>
                            <li>Masukkan email terdaftar di PM Tokoweb.</li>
                            <li>Klik <strong>Confirm</strong> untuk masuk.</li>
                        </ul>
                    </div>
                </div>

                <!-- STEP 3 -->
                <div class="group bg-white rounded-2xl shadow-lg p-6 border border-gray-100 hover:border-indigo-400 hover:shadow-indigo-100 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute inset-0 opacity-0 group-hover:opacity-10 bg-gradient-to-r from-blue-500 to-cyan-400 transition-all"></div>
                    <div class="flex flex-col items-center text-center space-y-3">
                        <div class="bg-blue-100 p-4 rounded-full">
                            <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" stroke-width="2"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M3 13a4 4 0 004 4h10a4 4 0 004-4M7 13V9m10 4V9" />
                            </svg>
                        </div>
                        <h3 class="font-semibold text-lg text-blue-600">3. Pemantauan</h3>
                        <p class="text-gray-600 text-sm">Aplikasi berjalan di <em>System Tray</em> dan otomatis melacak aktivitas Anda, seperti durasi penggunaan dan aktivitas keyboard/mouse.</p>
                    </div>
                </div>

                <!-- STEP 4 -->
                <div class="group bg-white rounded-2xl shadow-lg p-6 border border-gray-100 hover:border-indigo-400 hover:shadow-indigo-100 transition-all duration-300 relative overflow-hidden">
                    <div class="absolute inset-0 opacity-0 group-hover:opacity-10 bg-gradient-to-r from-yellow-400 to-rose-500 transition-all"></div>
                    <div class="flex flex-col items-center text-center space-y-3">
                        <div class="bg-yellow-100 p-4 rounded-full">
                            <svg class="w-8 h-8 text-yellow-600" fill="none" stroke="currentColor" stroke-width="2"
                                viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 8v8m4-4H8m8 4a8 8 0 11-8-8 8 8 0 018 8z" />
                            </svg>
                        </div>
                        <h3 class="font-semibold text-lg text-yellow-600">4. Sinkronisasi Data</h3>
                        <p class="text-gray-600 text-sm">Data aktivitas dikirim otomatis ke server <strong>PM Tokoweb</strong> setiap 1 jam tanpa perlu tindakan tambahan.</p>
                    </div>
                </div>
            </div>

            <!-- ACCORDION DOCUMENTATION -->
            <div class="space-y-6">
                <style>
                    details summary {
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        list-style: none;
                    }

                    details summary::-webkit-details-marker {
                        display: none;
                    }

                    details summary::after {
                        content: "›";
                        transition: transform 0.3s ease;
                        font-size: 1.5rem;
                        color: #6366f1;
                    }

                    details[open] summary::after {
                        transform: rotate(90deg);
                    }
                </style>

                <!-- Accordion items (same as before) -->
                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">1. Pendahuluan</summary>
                    <p class="mt-4 text-gray-700 leading-relaxed">
                        Aplikasi <strong>Desktop Activity Monitor</strong> digunakan untuk memantau aktivitas pengguna —
                        melacak aplikasi aktif, aktivitas keyboard dan mouse, serta mengirim data ke dashboard <strong>PM Tokoweb</strong> untuk pemantauan produktivitas.
                    </p>
                </details>

                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">2. Persyaratan Sistem</summary>
                    <ul class="list-disc list-inside mt-4 text-gray-700 space-y-1">
                        <li>Sistem Operasi: Windows, macOS, atau Linux</li>
                        <li>Koneksi Internet diperlukan untuk sinkronisasi data</li>
                        <li>Memiliki akun aktif di <strong>PM Tokoweb</strong></li>
                    </ul>
                </details>

                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">3. Instalasi & Persiapan</summary>
                    <ol class="list-decimal list-inside mt-4 text-gray-700 space-y-2">
                        <li>Unduh file aplikasi sesuai OS Anda.</li>
                        <li>Pastikan sudah melakukan <strong>Clock In</strong> di website PM Tokoweb.</li>
                        <li>Jalankan aplikasi.</li>
                    </ol>
                </details>

                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">4. Panduan Penggunaan</summary>
                    <div class="mt-4 space-y-4 text-gray-700">
                        <h4 class="font-semibold text-indigo-600">A. Login / Verifikasi Email</h4>
                        <ul class="list-disc list-inside">
                            <li>Masukkan email terdaftar di PM Tokoweb</li>
                            <li>Klik tombol <strong>Confirm</strong></li>
                            <li>Jika belum Clock In, aplikasi menampilkan peringatan</li>
                        </ul>
                        <h4 class="font-semibold text-indigo-600 mt-4">B. Antarmuka Utama</h4>
                        <ul class="list-disc list-inside">
                            <li><strong>Active Application</strong>: aplikasi yang sedang digunakan</li>
                            <li><strong>Activity Metric</strong>: aktivitas keyboard/mouse</li>
                            <li><strong>User Info</strong>: info akun dan lokasi</li>
                        </ul>
                        <h4 class="font-semibold text-indigo-600 mt-4">C. System Tray</h4>
                        <p>Aplikasi tetap berjalan di background — klik kanan ikon untuk <em>Show, Hide, atau Quit</em>.</p>
                    </div>
                </details>

                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">5. Fitur Utama</summary>
                    <table class="w-full mt-4 border border-gray-200 rounded-lg overflow-hidden text-sm">
                        <thead class="bg-indigo-100 text-indigo-800">
                            <tr>
                                <th class="py-2 px-3 text-left">Fitur</th>
                                <th class="py-2 px-3 text-left">Deskripsi</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white">
                            <tr>
                                <td class="py-2 px-3 font-semibold">Aplikasi Monitoring</td>
                                <td>Mencatat waktu aktif setiap aplikasi</td>
                            </tr>
                            <tr>
                                <td class="py-2 px-3 font-semibold">Keyboard/Mouse Tracking</td>
                                <td>Menghitung intensitas aktivitas input</td>
                            </tr>
                            <tr>
                                <td class="py-2 px-3 font-semibold">Data Synchronization</td>
                                <td>Sinkronisasi otomatis setiap 1 jam</td>
                            </tr>
                            <tr>
                                <td class="py-2 px-3 font-semibold">Lokasi & Perangkat</td>
                                <td>Mendeteksi lokasi (IP) dan perangkat pengguna</td>
                            </tr>
                        </tbody>
                    </table>
                </details>

                <details class="glass p-6 rounded-2xl">
                    <summary class="font-bold text-lg cursor-pointer text-indigo-700">6. Pemecahan Masalah</summary>
                    <ul class="list-disc list-inside mt-4 text-gray-700 space-y-2">
                        <li><strong>Aplikasi tidak bisa di-Confirm:</strong> Pastikan email benar & sudah Clock In.</li>
                        <li><strong>Data tidak terupdate:</strong> Periksa koneksi internet Anda.</li>
                        <li><strong>Aplikasi error:</strong> Cek file <code>error.log</code> di folder instalasi.</li>
                    </ul>
                </details>
            </div>

            <div class="mt-10 text-center text-sm text-gray-500">
                Dikembangkan oleh <strong>Puji Ermanto</strong> — Senior Developer @ Tokoweb.co
            </div>
        </div>
    </section>

    <script>
        // Particle animation
        const canvas = document.getElementById('bgCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = innerWidth;
        canvas.height = innerHeight;
        let particlesArray = [];
        class Particle {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.size = Math.random() * 2;
                this.speedX = (Math.random() - 0.5) * 0.5;
                this.speedY = (Math.random() - 0.5) * 0.5;
            }
            update() {
                this.x += this.speedX;
                this.y += this.speedY;
                if (this.x < 0 || this.x > canvas.width) this.speedX *= -1;
                if (this.y < 0 || this.y > canvas.height) this.speedY *= -1;
            }
            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                ctx.fillStyle = 'rgba(255,255,255,0.7)';
                ctx.fill();
            }
        }

        function init() {
            particlesArray = [];
            for (let i = 0; i < 70; i++) particlesArray.push(new Particle());
        }

        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            particlesArray.forEach(p => {
                p.update();
                p.draw();
            });
            requestAnimationFrame(animate);
        }
        init();
        animate();
        window.addEventListener('resize', () => {
            canvas.width = innerWidth;
            canvas.height = innerHeight;
            init();
        });

        // Parallax mouse move
        const orbs = document.querySelectorAll('.orb');
        const spotlight = document.querySelector('.spotlight');
        document.addEventListener('mousemove', e => {
            const x = (e.clientX / window.innerWidth - 0.5) * 40;
            const y = (e.clientY / window.innerHeight - 0.5) * 40;
            orbs[0].style.transform = `translate(${x}px, ${y}px)`;
            orbs[1].style.transform = `translate(${-x}px, ${-y}px)`;
            spotlight.style.transform = `translate(${e.clientX - 100}px, ${e.clientY - 100}px)`;
        });

        // === Statistik Download ===
        const downloadBtn = document.getElementById('downloadBtn');
        const downloadCount = document.getElementById('downloadCount');

        // Ambil data awal
        fetch('/api/download-stats')
            .then(res => res.json())
            .then(data => {
                if (data.status === 'success') {
                    downloadCount.textContent = data.total_downloads;
                }
            });

        // Saat tombol diklik
        downloadBtn.addEventListener('click', () => {
            fetch('/api/record-download')
                .then(res => res.json())
                .then(data => {
                    if (data.status === 'success') {
                        downloadCount.textContent = data.total_downloads;
                    }
                });
        });

        // Smooth scroll
        document.getElementById('scrollDown').addEventListener('click', () => {
            document.getElementById('docs').scrollIntoView({
                behavior: 'smooth'
            });
        });
    </script>
</body>

</html>