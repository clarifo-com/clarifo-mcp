// Run a Clarifo research agent with the Vercel AI SDK.
//
//   npm install
//   ANTHROPIC_API_KEY=... CLARIFO_API_KEY=... node agent.mjs investment-analyst "Investment brief on Kone"
import { generateText, isStepCount } from 'ai';
import { anthropic } from '@ai-sdk/anthropic';
import { getClarifoTools, loadAgentPrompt } from './clarifo.mjs';

const [agent = 'investment-analyst', ...rest] = process.argv.slice(2);
const prompt = rest.join(' ');
if (!prompt) {
  console.error('usage: node agent.mjs <agent-name> "<prompt>"');
  process.exit(1);
}

const { client, tools } = await getClarifoTools();
try {
  const { text } = await generateText({
    model: anthropic(process.env.CLAUDE_MODEL ?? 'claude-sonnet-5-5'),
    system: loadAgentPrompt(agent),
    tools,
    stopWhen: isStepCount(30),
    prompt,
  });
  console.log(text);
} finally {
  await client.close();
}
