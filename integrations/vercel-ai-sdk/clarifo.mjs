// Clarifo MCP tools for the Vercel AI SDK. Import getClarifoTools() in a
// script, a Next.js route handler or any server-side code. Never call it
// from the browser: the API key must stay on the server.
import { readFileSync } from 'node:fs';
import { createMCPClient } from '@ai-sdk/mcp';

const AGENTS_DIR = new URL('../../plugins/clarifo/agents/', import.meta.url);

// Workspace write tools. Left out here as well as by the server-side opt-in.
const WRITE_TOOLS = new Set([
  'save_to_workspace', 'save_note', 'preview_document_update', 'apply_document_update',
  'create_automation_draft', 'activate_automation', 'update_automation',
  'move_to_trash', 'restore_from_trash',
]);

/** Agent instructions shared with the Claude Code plugin (plugins/clarifo/agents). */
export function loadAgentPrompt(name) {
  const text = readFileSync(new URL(`${name}.md`, AGENTS_DIR), 'utf8');
  return text.startsWith('---') ? text.split('---').slice(2).join('---').trim() : text;
}

/** Connects to Clarifo and returns { client, tools }. Close the client when done. */
export async function getClarifoTools({ allowWrites = false } = {}) {
  const client = await createMCPClient({
    transport: {
      type: 'http',
      url: process.env.CLARIFO_MCP_URL ?? 'https://mcp.clarifo.com/mcp',
      headers: { Authorization: `Bearer ${process.env.CLARIFO_API_KEY}` },
    },
  });
  const all = await client.tools();
  const tools = allowWrites
    ? all
    : Object.fromEntries(Object.entries(all).filter(([name]) => !WRITE_TOOLS.has(name)));
  return { client, tools };
}
