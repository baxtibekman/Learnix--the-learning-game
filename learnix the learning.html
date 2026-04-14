<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learnix - Python Online</title>
    <style>
        :root {
            --green: #58cc02;
            --blue: #1cb0f6;
            --red: #ff4b4b;
            --bg: #f0f4f7;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
        }
        #app-container {
            width: 400px;
            height: 700px;
            background: white;
            border-radius: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }
        .screen { display: none; padding: 20px; text-align: center; height: 100%; }
        .active { display: flex; flex-direction: column; justify-content: center; }

        /* Splash Screen */
        #splash { background: white; font-size: 40px; font-weight: bold; color: var(--green); }
        .fade-out { animation: fadeOut 1.5s forwards; }
        @keyframes fadeOut { from { opacity: 1; } to { opacity: 0; visibility: hidden; } }

        /* General Styles */
        input { padding: 10px; border: 2px solid #ddd; border-radius: 10px; width: 80%; margin: 10px 0; font-size: 16px; }
        button { 
            padding: 12px; background: var(--blue); color: white; border: none; 
            border-radius: 15px; cursor: pointer; font-weight: bold; margin: 5px;
            box-shadow: 0 4px #1899d6;
        }
        button:active { transform: translateY(4px); box-shadow: none; }
        
        /* Pet Image */
        .pet { width: 120px; margin-bottom: 20px; }

        /* Progress & Health */
        .top-bar { display: flex; justify-content: space-between; padding: 10px 20px; background: white; border-bottom: 2px solid #eee; }
        .health { color: var(--red); font-weight: bold; }

        /* Map Road */
        .road { display: flex; flex-direction: column-reverse; align-items: center; gap: 40px; padding: 40px 0; }
        .node { width: 60px; height: 60px; background: #e5e5e5; border-radius: 50%; display: flex; 
                justify-content: center; align-items: center; font-weight: bold; color: white; cursor: pointer; }
        .node.active { background: var(--green); box-shadow: 0 6px #46a302; }
    </style>
</head>
<body>

<div id="app-container">
    <div id="splash" class="screen active">LEARNIX</div>

    <div id="reg-name" class="screen">
        <img src="pet.png" alt="Pet" class="pet" onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
        <h3>Salom! Isming nima?</h3>
        <input type="text" id="userNameInput" placeholder="Ismingiz...">
        <button onclick="saveName()">Keyingisi</button>
    </div>

    <div id="reg-goal" class="screen">
        <h3>Nega Python o'rganasiz?</h3>
        <button onclick="saveGoal('O\'yin yaratish')">O'yin yaratish</button>
        <button onclick="saveGoal('Ish topish')">Ish topish</button>
        <button onclick="saveGoal('Maktab uchun')">Maktab uchun</button>
    </div>

    <div id="map-screen" class="screen">
        <div class="top-bar">
            <span id="display-name">Ism</span>
            <span class="health">❤️ <span id="health-val">5</span></span>
        </div>
        <div class="road">
            <div class="node active" onclick="startQuiz()">1</div>
            <div class="node">2</div>
            <div class="node">3</div>
            <div class="node">4</div>
            <div class="node">5</div>
        </div>
    </div>

    <div id="quiz-screen" class="screen">
        <h4 id="question-text">Savol?</h4>
        <div id="options-container" style="display:flex; flex-direction:column;"></div>
        <p id="feedback"></p>
    </div>

    <div id="final-screen" class="screen">
        <img src="pet.png" id="final-pet" class="pet" onerror="this.src='https://cdn-icons-png.flaticon.com/512/4712/4712035.png'">
        <h2 id="result-msg">Natija</h2>
        <button onclick="location.reload()">Qayta boshlash</button>
    </div>
</div>

<script>
    let userName = "";
    let userGoal = "";
    let health = 5;
    let score = 0;
    let currentQ = 0;

    const questions = [
        {q: "Python nima?", o: ["Dasturlash tili", "Ilon turi", "O'yin"], c: 0},
        {q: "Ekranga chiqarish?", o: ["input()", "print()", "save()"], c: 1},
        {q: "Butun son turi?", o: ["float", "int", "str"], c: 1},
        {q: "Izoh belgisi?", o: ["//", "#", "/*"], c: 1}
    ];

    // Splash to Name
    setTimeout(() => {
        showScreen('reg-name');
    }, 2000);

    function showScreen(id) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById(id).classList.add('active');
    }

    function saveName() {
        userName = document.getElementById('userNameInput').value;
        if(userName.length > 1) showScreen('reg-goal');
    }

    function saveGoal(goal) {
        userGoal = goal;
        document.getElementById('display-name').innerText = userName;
        showScreen('map-screen');
    }

    function startQuiz() {
        showScreen('quiz-screen');
        loadQuestion();
    }

    function loadQuestion() {
        const q = questions[currentQ];
        document.getElementById('question-text').innerText = q.q;
        const container = document.getElementById('options-container');
        container.innerHTML = "";
        q.o.forEach((opt, idx) => {
            const btn = document.createElement('button');
            btn.innerText = opt;
            btn.onclick = () => checkAnswer(idx);
            container.appendChild(btn);
        });
    }

    function checkAnswer(idx) {
        if(idx === questions[currentQ].c) {
            score++;
            document.getElementById('feedback').innerText = "To'g'ri! ✅";
            document.getElementById('feedback').style.color = "var(--green)";
        } else {
            health--;
            document.getElementById('health-val').innerText = health;
            document.getElementById('feedback').innerText = "Xato! ❌";
            document.getElementById('feedback').style.color = "var(--red)";
        }

        setTimeout(() => {
            document.getElementById('feedback').innerText = "";
            if(currentQ < questions.length - 1) {
                currentQ++;
                loadQuestion();
            } else {
                finishQuiz();
            }
        }, 1000);
    }

    function finishQuiz() {
        showScreen('final-screen');
        const percentage = (score / questions.length) * 100;
        if(percentage >= 75) {
            document.getElementById('result-msg').innerText = "Barakalla! " + userName + " 😊";
            document.getElementById('result-msg').style.color = "var(--green)";
        } else {
            document.getElementById('result-msg').innerText = "Robot xafa bo'ldi... 😟";
            document.getElementById('result-msg').style.color = "var(--red)";
        }
    }
</script>

</body>
</html>
