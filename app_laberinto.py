import streamlit as st
from maze_solver import MAZE, START, END, solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")


def render_maze(maze, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = []

    display_maze = []

    for r_idx, row in enumerate(maze):
        row_display = ""
        for c_idx, col in enumerate(row):

            if (r_idx, c_idx) == START:
                row_display += "🚀"
            elif (r_idx, c_idx) == END:
                row_display += "🏁"
            elif (r_idx, c_idx) in path:
                row_display += "🔷"
            elif (r_idx, c_idx) in visited:
                row_display += "▫️"
            elif col == 1:
                row_display += "⬛"
            else:
                row_display += "⬜"

        display_maze.append(row_display)

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


# --- SIDEBAR ---
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS"])
solve_button = st.sidebar.button("Resolver Laberinto")


# Render inicial
render_maze(MAZE)


# --- EVENTO DE RESOLVER ---
if solve_button:
    if algorithm == "BFS":
        path, visited, exec_time = solve_maze_bfs(MAZE, START, END)

        if path:
            st.success(f"✅ ¡Camino encontrado con BFS!")
            st.info(f"⏱ Tiempo de ejecución: {exec_time:.6f} segundos")
            st.write(f"Nodos visitados: {len(visited)}")

            render_maze(MAZE, path, visited)

        else:
            st.error("❌ No se encontró un camino.")
