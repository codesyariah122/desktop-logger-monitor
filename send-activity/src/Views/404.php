<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>404 | Lost in Validation</title>
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
            background: radial-gradient(circle at 20% 30%, #0f172a, #000);
            font-family: 'Inter', sans-serif;
            color: #fff;
            position: relative;
        }

        .glow {
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 30% 40%, rgba(139, 92, 246, 0.3), transparent 70%),
                radial-gradient(circle at 70% 60%, rgba(236, 72, 153, 0.3), transparent 70%);
            filter: blur(80px);
            z-index: 0;
        }

        .main {
            text-align: center;
            z-index: 2;
        }

        .code {
            font-size: 9rem;
            font-weight: 900;
            background: linear-gradient(90deg, #a78bfa, #ec4899, #facc15);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 50px rgba(236, 72, 153, 0.3);
            animation: glowPulse 3s infinite alternate;
        }

        @keyframes glowPulse {
            0% {
                filter: brightness(1);
            }

            100% {
                filter: brightness(1.6);
            }
        }

        .message {
            font-size: 1.25rem;
            font-weight: 500;
            color: #d1d5db;
            letter-spacing: 1px;
            margin-top: -10px;
            text-transform: uppercase;
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
            display: inline-block;
            font-weight: 700;
            background: linear-gradient(90deg, #ec4899, #f59e0b);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: flicker 2s infinite alternate;
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
            padding: 0.8rem 2.4rem;
            border-radius: 9999px;
            background: linear-gradient(90deg, #6366f1, #ec4899);
            color: white;
            font-weight: 600;
            letter-spacing: 0.5px;
            transition: all 0.3s ease;
            box-shadow: 0 0 25px rgba(167, 139, 250, 0.3);
        }

        .button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 40px rgba(236, 72, 153, 0.4);
        }

        .quote {
            position: absolute;
            bottom: 40px;
            width: 100%;
            text-align: center;
            font-size: 0.9rem;
            color: #6b7280;
            letter-spacing: 1px;
        }

        .quote span {
            color: #a78bfa;
        }
    </style>
</head>

<body>
    <div class="glow"></div>

    <div class="main">
        <div class="code">404</div>
        <div class="message">VALIDATION IS <span class="word">AN ILLUSION</span></div>
        <a href="/download-page" class="button">RETURN TO REALITY</a>
    </div>

    <div class="quote">
        stop chasing <span>applause</span>, start creating impact.
    </div>
</body>

</html>