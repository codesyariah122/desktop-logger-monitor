<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>404 | Validation Is a Trap</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            margin: 0;
            height: 100vh;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(circle at 50% 20%, #0f0f0f, #000);
            color: #fff;
            font-family: 'Inter', sans-serif;
            position: relative;
        }

        /* Neon fractured glow */
        .fracture {
            position: absolute;
            inset: 0;
            background: repeating-linear-gradient(45deg, rgba(236, 72, 153, 0.06) 0 2px, transparent 2px 6px),
                repeating-linear-gradient(-45deg, rgba(99, 102, 241, 0.06) 0 2px, transparent 2px 6px);
            z-index: 0;
            animation: glitch 4s infinite linear alternate;
            filter: blur(20px);
            opacity: 0.8;
        }

        @keyframes glitch {
            0% {
                transform: translate(0, 0);
                opacity: 0.7;
            }

            25% {
                transform: translate(-10px, 5px);
                opacity: 0.6;
            }

            50% {
                transform: translate(10px, -5px);
                opacity: 0.8;
            }

            100% {
                transform: translate(0, 0);
                opacity: 0.7;
            }
        }

        .container {
            text-align: center;
            z-index: 2;
            position: relative;
        }

        .code {
            font-size: 10rem;
            font-weight: 900;
            letter-spacing: -4px;
            background: linear-gradient(90deg, #ec4899, #a78bfa, #facc15);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 50px rgba(236, 72, 153, 0.3);
            animation: pulse 2s infinite alternate ease-in-out;
            transform: skewY(-2deg);
        }

        @keyframes pulse {
            0% {
                filter: brightness(1);
                transform: skewY(-2deg) scale(1);
            }

            100% {
                filter: brightness(1.6);
                transform: skewY(-1deg) scale(1.04);
            }
        }

        .reflection {
            position: absolute;
            top: 55%;
            left: 0;
            width: 100%;
            text-align: center;
            font-size: 10rem;
            font-weight: 900;
            opacity: 0.05;
            color: white;
            transform: scaleY(-1);
            filter: blur(2px);
        }

        .message {
            margin-top: -1rem;
            font-size: 1.25rem;
            font-weight: 600;
            letter-spacing: 2px;
            text-transform: uppercase;
            color: #d1d5db;
            animation: fadeIn 3s ease-in-out;
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(10px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .word {
            color: transparent;
            background: linear-gradient(90deg, #f472b6, #f59e0b, #f43f5e);
            -webkit-background-clip: text;
            animation: flicker 1.5s infinite alternate;
        }

        @keyframes flicker {

            0%,
            18%,
            22%,
            25%,
            53%,
            57%,
            100% {
                opacity: 1;
            }

            20%,
            24%,
            55% {
                opacity: 0.3;
            }
        }

        .button {
            margin-top: 3rem;
            padding: 0.9rem 2.8rem;
            border-radius: 9999px;
            background: linear-gradient(90deg, #6366f1, #ec4899);
            color: white;
            font-weight: 700;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 0 25px rgba(236, 72, 153, 0.4);
        }

        .button:hover {
            transform: scale(1.08);
            box-shadow: 0 0 40px rgba(167, 139, 250, 0.5);
        }

        .quote {
            position: absolute;
            bottom: 40px;
            width: 100%;
            text-align: center;
            font-size: 0.9rem;
            color: #71717a;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .quote span {
            background: linear-gradient(90deg, #a78bfa, #ec4899);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
    </style>
</head>

<body>
    <div class="fracture"></div>

    <div class="container">
        <div class="code">404</div>
        <div class="reflection">404</div>
        <div class="message">You’re not lost — you’re just <span class="word">craving validation.</span></div>
        <a href="/download-page" class="button">Go Touch Grass 🌱</a>
    </div>

    <div class="quote">
        mirrors don’t clap — <span>they reflect your emptiness</span>.
    </div>
</body>

</html>