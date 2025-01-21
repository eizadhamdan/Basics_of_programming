#include <GL/glut.h>
#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>

#define INF 1000000000

using namespace std;

// Global variables for graph and visualization
const int MAX_NODES = 100;
int capacity[MAX_NODES][MAX_NODES];
vector<int> adj[MAX_NODES];
int num_nodes;
float node_positions[MAX_NODES][2]; // Store positions for visualization

// Function to display text on screen
void drawText(float x, float y, const char *text)
{
    glRasterPos2f(x, y);
    for (const char *c = text; *c != '\0'; c++)
    {
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, *c);
    }
}

// BFS to find an augmenting path
bool bfs(int s, int t, vector<int> &parent)
{
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2; // Source node
    queue<pair<int, int>> q;
    q.push({s, INF});

    while (!q.empty())
    {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur])
        {
            if (parent[next] == -1 && capacity[cur][next] > 0)
            {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                {
                    return true;
                }
                q.push({next, new_flow});
            }
        }
    }

    return false;
}

// Ford-Fulkerson algorithm
int fordFulkerson(int s, int t)
{
    int max_flow = 0;
    vector<int> parent(num_nodes);

    while (bfs(s, t, parent))
    {
        int flow = INF;
        int cur = t;
        while (cur != s)
        {
            int prev = parent[cur];
            flow = min(flow, capacity[prev][cur]);
            cur = prev;
        }

        max_flow += flow;
        cur = t;
        while (cur != s)
        {
            int prev = parent[cur];
            capacity[prev][cur] -= flow;
            capacity[cur][prev] += flow;
            cur = prev;
        }
    }

    return max_flow;
}

// Function to draw the graph
void drawGraph()
{
    glClear(GL_COLOR_BUFFER_BIT);

    // Draw edges
    for (int i = 0; i < num_nodes; i++)
    {
        for (int j : adj[i])
        {
            if (capacity[i][j] > 0 || capacity[j][i] > 0)
            {
                glBegin(GL_LINES);
                glVertex2f(node_positions[i][0], node_positions[i][1]);
                glVertex2f(node_positions[j][0], node_positions[j][1]);
                glEnd();
            }
        }
    }

    // Draw nodes
    for (int i = 0; i < num_nodes; i++)
    {
        glBegin(GL_POLYGON);
        for (int j = 0; j < 360; j++)
        {
            float theta = j * 3.14159f / 180;
            float x = 0.02f * cos(theta);
            float y = 0.02f * sin(theta);
            glVertex2f(x + node_positions[i][0], y + node_positions[i][1]);
        }
        glEnd();

        char label[3];
        sprintf(label, "%d", i);
        drawText(node_positions[i][0] - 0.01f, node_positions[i][1] - 0.01f, label);
    }

    glFlush();
}

// Initialize OpenGL settings
void initOpenGL()
{
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glColor3f(0.0, 0.0, 0.0);
    glPointSize(5.0);
    glLineWidth(2.0);
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0);
}

// Input graph from user
void inputGraph()
{
    cout << "Enter the number of nodes: ";
    cin >> num_nodes;

    cout << "Enter the edges (u v capacity), enter -1 -1 -1 to stop:\n";
    int u, v, cap;
    while (true)
    {
        cin >> u >> v >> cap;
        if (u == -1 && v == -1 && cap == -1)
            break;
        adj[u].push_back(v);
        adj[v].push_back(u); // Reverse edge for residual graph
        capacity[u][v] = cap;
    }

    cout << "Enter the positions of nodes (x y between -1 and 1):\n";
    for (int i = 0; i < num_nodes; i++)
    {
        cin >> node_positions[i][0] >> node_positions[i][1];
    }

    int source, sink;
    cout << "Enter the source and sink nodes: ";
    cin >> source >> sink;

    int max_flow = fordFulkerson(source, sink);
    cout << "The maximum flow is: " << max_flow << endl;
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(800, 800);
    glutCreateWindow("Ford-Fulkerson Algorithm Visualization");

    initOpenGL();

    inputGraph();

    glutDisplayFunc(drawGraph);
    glutMainLoop();

    return 0;
}
