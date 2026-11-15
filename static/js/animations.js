document.addEventListener("DOMContentLoaded", () => {
    // 1. Inicializa Ícones Lucide e animações AOS
    if (typeof lucide !== "undefined") {
        lucide.createIcons();
    }
    if (typeof AOS !== "undefined") {
        AOS.init({ duration: 650, once: true, offset: 30 });
    }

    // 2. Efeito Spotlight nos Bento Cards
    document.querySelectorAll(".bento-card").forEach((card) => {
        card.addEventListener("mousemove", (e) => {
            const rect = card.getBoundingClientRect();
            card.style.setProperty("--mouse-x", `${e.clientX - rect.left}px`);
            card.style.setProperty("--mouse-y", `${e.clientY - rect.top}px`);
        });
    });

    // 3. Animação de entrada GSAP
    if (typeof gsap !== "undefined" && document.querySelector(".gsap-hero")) {
        gsap.from(".gsap-hero", {
            y: 22,
            opacity: 0,
            duration: 0.8,
            stagger: 0.12,
            ease: "power3.out",
        });
    }

    // 4. Filtro Instantâneo nas Tabelas
    document.querySelectorAll("table.table").forEach((table) => {
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
            table.querySelectorAll("tbody tr").forEach((row) => {
                row.style.display = row.textContent.toLowerCase().includes(val) ? "" : "none";
            });
        });
    });
});