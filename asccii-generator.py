<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ASCII Art Animation with Rainbow Background</title>
    <style>
        body, html {
            height: 100%;
            margin: 0;
            font-family: 'Courier New', Courier, monospace;
            background: linear-gradient(270deg, #f3ec78, #af4261, #28b4e5, #76b852);
            background-size: 800% 800%;
            animation: AnimationName 30s ease infinite;
        }

        @keyframes AnimationName {
            0%{background-position:0% 50%}
            50%{background-position:100% 50%}
            100%{background-position:0% 50%}
        }

        #ascii-art {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            white-space: pre;
            font-size: 16px;
            text-align: center;
            color: white;
        }
    </style>
</head>
<body>
    <div id="ascii-art"></div>
    <script>
        const animations = [
            {
                name: 'Dancing Stick Figure',
                frames: [
                    `
                     O
                    /|\\
                    / \\
                    `,
                    `
                     O
                    \\|/
                     |
                    / \\
                    `,
                    `
                     O
                    /|\\
                     |
                    / \\
                    `
                ],
                interval: 300 // milliseconds
            },
            {
                name: 'Spinning Box',
                frames: [
                    `
                    +---+
                    |   |
                    +---+
                    `,
                    `
                     \\   /
                      ---
                     /   \\
                    `,
                    `
                    +---+
                    |   |
                    +---+
                    `
                ],
                interval: 500 // milliseconds
            }
        ];

        const artContainer = document.getElementById('ascii-art');
        let currentAnimation = 0;
        let frameIndex = 0;

        function animateASCII() {
            const frames = animations[currentAnimation].frames;
            artContainer.textContent = frames[frameIndex];
            frameIndex = (frameIndex + 1) % frames.length;
            setTimeout(animateASCII, animations[currentAnimation].interval);
        }

        function switchAnimation() {
            currentAnimation = (currentAnimation + 1) % animations.length;
            frameIndex = 0; // Reset frame index
        }

        animateASCII(); // Start the first animation
        setInterval(switchAnimation, 10000); // Switch animations every 10 seconds
    </script>
</body>
</html>
