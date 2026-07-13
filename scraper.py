import os
import shutil

def create_website_files():
    """إنشاء موقع فخم لتوليد الصور AI"""
    
    os.makedirs("www", exist_ok=True)
    
    index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Dark AI | Image Generator</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg: #000000;
            --surface: #0a0a0a;
            --border: #1a1a1a;
            --primary: #c9a84c;
            --primary-glow: rgba(201, 168, 76, 0.3);
            --text: #e0d5c0;
            --text-dim: #6b6355;
            --danger: #8b0000;
            --gold-gradient: linear-gradient(135deg, #c9a84c, #e2c97e, #c9a84c);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: var(--bg);
            color: var(--text);
            font-family: 'Cairo', sans-serif;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 16px;
            background-image: 
                radial-gradient(ellipse at top, rgba(201,168,76,0.05) 0%, transparent 60%),
                radial-gradient(ellipse at bottom, rgba(139,0,0,0.05) 0%, transparent 60%);
        }

        .app {
            width: 100%;
            max-width: 480px;
            position: relative;
        }

        /* Header Luxury */
        .header {
            text-align: center;
            margin-bottom: 24px;
            position: relative;
        }

        .logo-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 16px;
            background: var(--gold-gradient);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 0 40px var(--primary-glow), 0 0 80px rgba(201,168,76,0.15);
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }

        .title {
            font-size: 36px;
            font-weight: 900;
            letter-spacing: 3px;
            background: var(--gold-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        .subtitle {
            font-size: 11px;
            color: var(--text-dim);
            letter-spacing: 4px;
            text-transform: uppercase;
        }

        .divider {
            width: 60px;
            height: 1px;
            background: var(--gold-gradient);
            margin: 16px auto;
            opacity: 0.5;
        }

        /* Card Container */
        .card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.5), 0 0 0 1px rgba(255,255,255,0.02) inset;
            backdrop-filter: blur(10px);
        }

        /* Styles Section */
        .styles-section {
            margin-bottom: 16px;
        }

        .styles-label {
            font-size: 9px;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: var(--text-dim);
            margin-bottom: 10px;
        }

        .styles-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 6px;
        }

        .style-btn {
            padding: 10px 8px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-dim);
            cursor: pointer;
            border-radius: 10px;
            font-size: 10px;
            font-family: 'Cairo', sans-serif;
            font-weight: 700;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            letter-spacing: 0.5px;
            position: relative;
            overflow: hidden;
        }

        .style-btn:hover {
            border-color: var(--primary);
            color: var(--primary);
            background: rgba(201,168,76,0.05);
        }

        .style-btn.active {
            background: rgba(201,168,76,0.1);
            border-color: var(--primary);
            color: var(--primary);
            box-shadow: 0 0 20px var(--primary-glow), 0 0 0 1px rgba(201,168,76,0.2) inset;
        }

        .style-btn .icon {
            display: block;
            font-size: 18px;
            margin-bottom: 2px;
        }

        /* Input Section */
        .input-section {
            margin-bottom: 12px;
        }

        .input-wrapper {
            position: relative;
        }

        #prompt {
            width: 100%;
            padding: 14px 16px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text);
            font-size: 13px;
            border-radius: 12px;
            font-family: 'Cairo', sans-serif;
            transition: all 0.3s;
            resize: none;
        }

        #prompt:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px var(--primary-glow);
        }

        #prompt::placeholder {
            color: #3a3530;
        }

        .btn-generate {
            width: 100%;
            padding: 14px;
            background: var(--gold-gradient);
            color: #000;
            border: none;
            font-weight: 900;
            cursor: pointer;
            border-radius: 12px;
            font-family: 'Cairo', sans-serif;
            font-size: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 20px var(--primary-glow);
            position: relative;
            overflow: hidden;
        }

        .btn-generate:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px var(--primary-glow);
        }

        .btn-generate:active {
            transform: scale(0.98);
        }

        .btn-generate:disabled {
            background: #1a1a1a;
            color: #333;
            box-shadow: none;
            cursor: not-allowed;
            transform: none;
        }

        /* Image Container */
        .image-area {
            margin-top: 16px;
            position: relative;
        }

        .image-frame {
            width: 100%;
            aspect-ratio: 1;
            background: var(--bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            overflow: hidden;
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .image-frame .placeholder-content {
            text-align: center;
            color: #1a1a1a;
        }

        .image-frame .placeholder-icon {
            font-size: 60px;
            display: block;
            margin-bottom: 8px;
            opacity: 0.3;
        }

        .image-frame .placeholder-text {
            font-size: 11px;
            letter-spacing: 2px;
            color: #2a2a2a;
            text-transform: uppercase;
        }

        .image-frame img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: none;
        }

        /* Loading Animation */
        .loading-overlay {
            display: none;
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.9);
            border-radius: 16px;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 16px;
        }

        .loading-overlay.active {
            display: flex;
        }

        .spinner {
            width: 50px;
            height: 50px;
            border: 2px solid var(--border);
            border-top-color: var(--primary);
            border-radius: 50%;
            animation: spin 0.8s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .loading-text {
            font-size: 11px;
            letter-spacing: 3px;
            color: var(--primary);
            animation: pulse 1.5s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        /* Download Button */
        .btn-download {
            display: none;
            width: 100%;
            margin-top: 12px;
            padding: 12px;
            background: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
            cursor: pointer;
            border-radius: 12px;
            font-family: 'Cairo', sans-serif;
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s;
        }

        .btn-download:hover {
            background: rgba(201,168,76,0.1);
            box-shadow: 0 0 20px var(--primary-glow);
        }

        .btn-download.visible {
            display: block;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 9px;
            color: #1a1a1a;
            letter-spacing: 2px;
        }

        .footer span {
            color: var(--primary);
        }

        /* Ripple Effect */
        .ripple {
            position: absolute;
            border-radius: 50%;
            background: rgba(255,255,255,0.3);
            transform: scale(0);
            animation: ripple 0.6s linear;
            pointer-events: none;
        }

        @keyframes ripple {
            to {
                transform: scale(4);
                opacity: 0;
            }
        }
    </style>
</head>
<body>
    <div class="app">
        <!-- Header -->
        <div class="header">
            <div class="logo-icon">⚡</div>
            <h1 class="title">Dark AI</h1>
            <p class="subtitle">Image Generator</p>
            <div class="divider"></div>
        </div>

        <!-- Card -->
        <div class="card">
            <!-- Styles -->
            <div class="styles-section">
                <p class="styles-label">✦ Select Style</p>
                <div class="styles-grid">
                    <button class="style-btn active" data-style="">
                        <span class="icon">🎨</span> All
                    </button>
                    <button class="style-btn" data-style="dark fantasy art">
                        <span class="icon">🌑</span> Dark
                    </button>
                    <button class="style-btn" data-style="cyberpunk neon">
                        <span class="icon">🤖</span> Cyber
                    </button>
                    <button class="style-btn" data-style="anime art style">
                        <span class="icon">🌸</span> Anime
                    </button>
                    <button class="style-btn" data-style="photorealistic 8k">
                        <span class="icon">👤</span> Real
                    </button>
                    <button class="style-btn" data-style="horror dark gothic">
                        <span class="icon">💀</span> Horror
                    </button>
                </div>
            </div>

            <!-- Input -->
            <div class="input-section">
                <div class="input-wrapper">
                    <input type="text" id="prompt" placeholder="Describe your vision..." autocomplete="off">
                </div>
            </div>

            <!-- Generate Button -->
            <button class="btn-generate" id="generateBtn" onclick="generateImage()">
                ✦ Generate Image ✦
            </button>

            <!-- Image Area -->
            <div class="image-area">
                <div class="image-frame" id="imageFrame">
                    <div class="placeholder-content" id="placeholder">
                        <span class="placeholder-icon">🖼️</span>
                        <span class="placeholder-text">Your creation</span>
                    </div>
                    <img id="generatedImage" alt="Generated Art">
                    <div class="loading-overlay" id="loadingOverlay">
                        <div class="spinner"></div>
                        <span class="loading-text">Creating...</span>
                    </div>
                </div>
                <button class="btn-download" id="downloadBtn" onclick="downloadImage()">
                    ⬇ Save Image
                </button>
            </div>
        </div>

        <!-- Footer -->
        <p class="footer">Powered by <span>Pollinations.ai</span> • No API Key</p>
    </div>

    <script>
        let currentImage = null;
        let currentStyle = '';

        // Style selection
        document.querySelectorAll('.style-btn').forEach(btn => {
            btn.addEventListener('click', function(e) {
                // Ripple effect
                const ripple = document.createElement('span');
                ripple.className = 'ripple';
                this.appendChild(ripple);
                const rect = this.getBoundingClientRect();
                ripple.style.left = (e.clientX - rect.left - 10) + 'px';
                ripple.style.top = (e.clientY - rect.top - 10) + 'px';
                setTimeout(() => ripple.remove(), 600);

                // Update active state
                document.querySelectorAll('.style-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentStyle = this.dataset.style;
            });
        });

        // Enter key to generate
        document.getElementById('prompt').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') generateImage();
        });

        async function generateImage() {
            const prompt = document.getElementById('prompt').value.trim();
            if (!prompt) {
                document.getElementById('prompt').style.borderColor = '#8b0000';
                setTimeout(() => document.getElementById('prompt').style.borderColor = '', 1500);
                return;
            }

            const fullPrompt = currentStyle ? `${prompt}, ${currentStyle}` : prompt;
            const seed = Math.floor(Math.random() * 99999);
            const imageUrl = `https://image.pollinations.ai/prompt/${encodeURIComponent(fullPrompt)}?width=512&height=512&seed=${seed}&nologo=true`;

            const loadingOverlay = document.getElementById('loadingOverlay');
            const generatedImage = document.getElementById('generatedImage');
            const placeholder = document.getElementById('placeholder');
            const downloadBtn = document.getElementById('downloadBtn');
            const generateBtn = document.getElementById('generateBtn');

            // Show loading
            loadingOverlay.classList.add('active');
            generateBtn.disabled = true;
            generatedImage.style.display = 'none';
            placeholder.style.display = 'block';

            // Load image
            generatedImage.src = imageUrl;
            
            generatedImage.onload = function() {
                loadingOverlay.classList.remove('active');
                generatedImage.style.display = 'block';
                placeholder.style.display = 'none';
                downloadBtn.classList.add('visible');
                generateBtn.disabled = false;
                currentImage = imageUrl;
                
                // Success animation
                generatedImage.style.animation = 'none';
                generatedImage.offsetHeight;
                generatedImage.style.animation = 'fadeIn 0.5s ease';
            };

            generatedImage.onerror = function() {
                loadingOverlay.classList.remove('active');
                generateBtn.disabled = false;
                alert('✦ Failed to generate. Try a different prompt.');
            };
        }

        async function downloadImage() {
            if (!currentImage) return;
            
            const downloadBtn = document.getElementById('downloadBtn');
            const originalText = downloadBtn.textContent;
            downloadBtn.textContent = 'Saving...';
            downloadBtn.disabled = true;
            
            try {
                const response = await fetch(currentImage);
                const blob = await response.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `dark-ai-${Date.now()}.png`;
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                
                downloadBtn.textContent = '✦ Saved! ✦';
                setTimeout(() => {
                    downloadBtn.textContent = originalText;
                    downloadBtn.disabled = false;
                }, 2000);
            } catch (error) {
                downloadBtn.textContent = originalText;
                downloadBtn.disabled = false;
                // Fallback: open in new tab
                window.open(currentImage, '_blank');
            }
        }

        // Add fadeIn animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; transform: scale(0.95); }
                to { opacity: 1; transform: scale(1); }
            }
        `;
        document.head.appendChild(style);
    </script>
</body>
</html>'''

    with open("www/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    print("✅ تم إنشاء موقع Dark AI الفخم")
    print(f"💾 حجم الملف: {os.path.getsize('www/index.html')/1024:.1f} KB")

if __name__ == "__main__":
    create_website_files()
