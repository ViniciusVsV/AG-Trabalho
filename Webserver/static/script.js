const colors = [
    "#FFB6C1", "#FFD700", "#ADFF2F", "#87CEEB", "#FFA07A",
    "#98FB98", "#AFEEEE", "#DB7093", "#FFEFD5", "#FFDAB9",
    "#ADD8E6", "#F08080", "#E6E6FA", "#FFFACD", "#20B2AA",
    "#FF69B4", "#7FFFD4", "#F0E68C", "#E0FFFF", "#FAF0E6",
    "#FFF0F5", "#708090", "#B0E0E6", "#FFFAF0", "#F5F5F5",
];

const tracks = {
    "CCO": [
        {value: "0", text: "Nenhuma"},
        {value: "1", text: "Resolução de Problemas"},
        {value: "2", text: "Desenvolvimento de Sistemas"},
        {value: "3", text: "Ciência, Tecnologia e Inovação"}
    ],
    "SIN": [
        {value: "0", text: "Nenhuma"},
        {value: "1", text: "Persistência e Análise de Dados"},
        {value: "2", text: "Redes e Sistemas Computacionais"},
        {value: "3", text: "Desenvolvimento e Engenharia de Software"}
    ]
};

const horarioMap = {
    'M1': '07:00-07:55',
    'M2': '07:55-08:50',
    'M3': '08:50-09:45',
    'M4': '10:10-11:05',
    'M5': '11:05-12:00',
    'T1': '13:30-14:25',
    'T2': '14:25-15:20',
    'T3': '15:50-16:40',
    'T4': '16:40-17:35',
    'T5': '17:35-18:30',
    'N1': '19:00-19:50',
    'N2': '19:50-20:40',
    'N3': '21:00-21:50',
    'N4': '21:50-22:40',
    'N5': '22:40-23:30'
};

function parseHorario(horarioStr) {
    const groups = [];
    const parts = horarioStr.split(' ');
    parts.forEach(part => {
        const match = part.match(/([1-7]+)([MTN])([1-5]+)/);
        if (match) {
            const daysStr = match[1];
            const turn = match[2];
            const periodStr = match[3];
            const days = daysStr.split('').map(d => parseInt(d));
            // Dividir períodos (ex.: '23' → ['2', '3'])
            const periods = periodStr.split('').map(p => `${turn}${p}`);
            periods.forEach(period => {
                groups.push({days, turn, period});
            });
        }
    });
    return groups;
}

function generateSuggestionHTML(sugestao, index) {
    const allSiglas = sugestao.turmas.map(t => t.sigla);
    const classToColor = {};
    allSiglas.forEach((sigla, i) => {
        classToColor[sigla] = colors[i % colors.length];
    });

    let html = `
    <div class="suggestion">
        <h2>Sugestão ${index + 1}</h2>
        <p>Carga horária: ${sugestao.cargaHoraria}h</p>
        <h3>Lista de Turmas</h3>
        <table class="course-table">
        <tr>
        <th>Sigla</th>
        <th>Nome</th>
        <th>Turma</th>
        <th>Curso</th>
        <th>Tipo</th>
        <th>Horário</th>
        </tr>
    `;
    sugestao.turmas.forEach(class_ => {
        const color = classToColor[class_.sigla];
        html += `
        <tr>
        <td style="background-color: ${color};">${class_.sigla}</td>
        <td>${class_.nome}</td>
        <td>${class_.turma}</td>
        <td>${class_.curso}</td>
        <td>${class_.tipo}</td>
        <td>${class_.horario}</td>
        </tr>
        `;
    });
    html += `</table>`;

    const allTp = new Set();
    sugestao.turmas.forEach(class_ => {
        const groups = parseHorario(class_.horario);
        groups.forEach(group => {
            allTp.add(group.period);
        });
    });

    const turnOrder = {M: 0, T: 1, N: 2};
    const sortedTp = Array.from(allTp).sort((a, b) => {
        const [turnA, periodA] = [a[0], a.slice(1)];
        const [turnB, periodB] = [b[0], b.slice(1)];
        const turnCmp = (turnOrder[turnA] ?? 3) - (turnOrder[turnB] ?? 3);
        if (turnCmp !== 0) return turnCmp;
        return periodA.localeCompare(periodB);
    });

    const days = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"];

    html += `
        <h3>Horário Semanal</h3>
        <table class="schedule-table">
        <tr>
        <th>Horário</th>
        ${days.map(day => `<th>${day}</th>`).join('')}
        </tr>
    `;
    sortedTp.forEach(tp => {
        const horarioReal = horarioMap[tp] || tp;
        html += `<tr><td>${horarioReal}</td>`;
        for (let dayIdx = 0; dayIdx < 7; dayIdx++) {
            const day = dayIdx + 1;
            const classesOn = sugestao.turmas.filter(class_ => {
                const groups = parseHorario(class_.horario);
                return groups.some(group => 
                    group.days.includes(day) && group.period === tp
                );
            });
            const cellContent = classesOn.map(class_ => {
                const color = classToColor[class_.sigla];
                return `<span style="background-color: ${color};">${class_.sigla}</span>`;
            }).join('');
            html += `<td>${cellContent}</td>`;
        }
        html += `</tr>`;
    });
    html += `</table></div>`;

    return html;
}

function generateResultsHTML(data) {
    let html = `
    `;
    const sortedSugestoes = data.sugestoes.sort((a, b) => b.peso - a.peso);
    sortedSugestoes.forEach((sugestao, index) => {
        html += generateSuggestionHTML(sugestao, index);
    });
    return html;
}

document.addEventListener('DOMContentLoaded', function() {
    const cursoSelect = document.getElementById('curso');
    const trilhaContainer = document.getElementById('trilha-container');
    const trilhaSelect = document.getElementById('trilha');

    function populateTrilha(curso) {
        trilhaSelect.innerHTML = '';
        if (tracks[curso]) {
            tracks[curso].forEach(track => {
                const option = document.createElement('option');
                option.value = track.value;
                option.text = track.text;
                trilhaSelect.appendChild(option);
            });
        }
    }

    cursoSelect.addEventListener('change', function() {
        const selectedCurso = this.value;
        if (selectedCurso === 'CCO' || selectedCurso === 'SIN') {
            trilhaContainer.style.display = 'block';
            populateTrilha(selectedCurso);
        } else {
            trilhaContainer.style.display = 'none';
        }
    });

    const initialCurso = cursoSelect.value;
    if (initialCurso === 'CCO' || initialCurso === 'SIN') {
        trilhaContainer.style.display = 'block';
        populateTrilha(initialCurso);
    } else {
        trilhaContainer.style.display = 'none';
    }

    const form = document.getElementById('upload-form');
    
    form.addEventListener('submit', function(event) { 
        const loading = document.getElementById('loading');
        const resultsDiv = document.getElementById('results');

        resultsDiv.innerHTML = ``;
        loading.style.display = 'block';

        event.preventDefault();
        const formData = new FormData(form);
        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                resultsDiv.innerHTML = `<p>Erro: ${data.error}</p>`;
            } else {
                resultsDiv.innerHTML = generateResultsHTML(data);

                loading.style.display = 'none'
            }
        })
        .catch(error => {
            console.error('Error:', error);
            resultsDiv.innerHTML = `<p>Erro: Falha na comunicação com o servidor</p>`;
        });
    });
});