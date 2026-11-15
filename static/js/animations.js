document.addEventListener("DOMContentLoaded", () => {
    // 1. Inicializa Ícones Lucide e AOS
    if (typeof lucide !== "undefined") {
        lucide.createIcons();
    }
    if (typeof AOS !== "undefined") {
        AOS.init({ duration: 650, once: true, offset: 30 });
    }

    // 2. Alternador de Tema (Claro / Escuro) com memória no navegador
    const htmlEl = document.documentElement;
    const themeBtn = document.getElementById("themeToggleBtn");

    function updateThemeIcon(theme) {
        if (!themeBtn) return;
        const iconName = theme === "light" ? "moon" : "sun";
        const label = theme === "light" ? "Modo Escuro" : "Modo Claro";
        themeBtn.innerHTML = `<i data-lucide="${iconName}" size="16"></i>`;
        themeBtn.setAttribute("title", label);
        if (typeof lucide !== "undefined") {
            lucide.createIcons();
        }
    }

    const currentTheme = localStorage.getItem("salaoapp_theme") || "dark";
    htmlEl.setAttribute("data-bs-theme", currentTheme);
    updateThemeIcon(currentTheme);

    if (themeBtn) {
        themeBtn.addEventListener("click", () => {
            const nextTheme = htmlEl.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
            htmlEl.setAttribute("data-bs-theme", nextTheme);
            localStorage.setItem("salaoapp_theme", nextTheme);
            updateThemeIcon(nextTheme);
        });
    }

    // 3. Efeito Spotlight nos Bento Cards
    document.querySelectorAll(".bento-card").forEach((card) => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            card.style.setProperty("--mouse-x", `${e.clientX - rect.left}px`);
            card.style.setProperty("--mouse-y", `${e.clientY - rect.top}px`);
        });
    });

    // 4. Animação de entrada GSAP
    if (typeof gsap !== "undefined" && document.querySelector(".gsap-hero")) {
        gsap.from(".gsap-hero", {
            y: 22,
            opacity: 0,
            duration: 0.8,
            stagger: 0.12,
            ease: "power3.out",
        });
    }

    // 5. Atalho Ctrl+K para abrir a Paleta de Busca Rápida de Módulos
    const quickSearchModalEl = document.getElementById("quickSearchModal");
    const quickSearchInput = document.getElementById("quickSearchInput");

    if (quickSearchModalEl && typeof bootstrap !== "undefined") {
        const modalInstance = new bootstrap.Modal(quickSearchModalEl);

        document.addEventListener("keydown", (e) => {
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
                e.preventDefault();
                modalInstance.show();
            }
        });

        quickSearchModalEl.addEventListener("shown.bs.modal", () => {
            if (quickSearchInput) {
                quickSearchInput.value = "";
                quickSearchInput.focus();
                filterModules("");
            }
        });
    }

    function filterModules(term) {
        const items = document.querySelectorAll(".quick-module-item");
        const query = term.toLowerCase().trim();
        items.forEach((item) => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(query) ? "flex" : "none";
        });
    }

    if (quickSearchInput) {
        quickSearchInput.addEventListener("input", (e) => {
            filterModules(e.target.value);
        });
    }

    // 6. Busca Instantânea Automática para qualquer Tabela do Sistema
    const tables = document.querySelectorAll("table.table");
    tables.forEach((table) => {
        if (table.dataset.searchEnhanced) return;
        table.dataset.searchEnhanced = "true";

        const wrapper = document.createElement("div");
        wrapper.className = "mb-3 d-flex justify-content-between align-items-center gap-2";
        wrapper.innerHTML = `
            <div class="input-group input-group-sm" style="max-width: 320px;">
                <span class="input-group-text bg-transparent border-secondary border-opacity-25 text-secondary">
                    <i data-lucide="search" size="14"></i>
                </span>
                <input type="text" class="form-control form-control-sm table-live-filter" placeholder="Filtrar registros nesta tabela...">
            </div>
        `;
        table.parentElement.insertBefore(wrapper, table);
        if (typeof lucide !== "undefined") lucide.createIcons();

        const input = wrapper.querySelector(".table-live-filter");
        input.addEventListener("input", (e) => {
            const val = e.target.value.toLowerCase();
            const rows = table.querySelectorAll("tbody tr");
            rows.forEach((row) => {
                const rowText = row.textContent.toLowerCase();
                row.style.display = rowText.includes(val) ? "" : "none";
            });
        });
    });
});