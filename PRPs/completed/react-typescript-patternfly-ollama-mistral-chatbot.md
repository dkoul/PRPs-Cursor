name: "React TypeScript PatternFly Chatbot with Ollama Mistral"
description: |
  Implement a production-ready chatbot interface using React TypeScript, PatternFly components, 
  and local Ollama setup with Mistral model for conversational AI.

## Purpose

Create a modern, responsive chatbot interface that demonstrates real-time streaming AI conversations 
with proper TypeScript typing, PatternFly UI components, and local Ollama integration.

## Core Principles

1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance

---

## Goal

Build a fully functional React TypeScript chatbot application with:
- PatternFly UI components for professional chat interface
- Local Ollama integration with Mistral model
- Real-time streaming message display
- Proper TypeScript typing throughout
- Modern development tooling and build pipeline

## Why

- **Business value**: Demonstrate local AI capabilities without external API dependencies
- **Integration**: Shows how to combine modern React patterns with local LLM infrastructure
- **Learning**: Provides comprehensive example of TypeScript + PatternFly + Ollama integration
- **Problems solved**: Creates template for enterprise-ready local AI chat applications

## What

### User-visible behavior:
- Clean, modern chat interface using PatternFly components
- Real-time streaming responses from Mistral model
- Message history with proper formatting
- Loading states and error handling
- Responsive design that works on desktop and mobile

### Technical requirements:
- React 18+ with TypeScript
- PatternFly React components
- Ollama JavaScript client integration
- Streaming message display
- Local development server setup
- Production build pipeline

### Success Criteria

- [ ] Chat interface loads without errors
- [ ] Users can send messages and receive AI responses
- [ ] Messages stream in real-time character by character
- [ ] UI is responsive and follows PatternFly design principles
- [ ] All components are properly typed with TypeScript
- [ ] Build pipeline works for both development and production
- [ ] Local Ollama integration works with Mistral model

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window
- url: https://www.patternfly.org/components/data-list/
  why: Main component for chat message display, provides flexible layout

- url: https://github.com/patternfly/patternfly-react
  why: Official React components library, check for latest patterns

- url: https://github.com/dditlev/ollama-js-client
  why: JavaScript client for Ollama with streaming support

- url: https://js.langchain.com/v0.2/docs/integrations/llms/ollama/
  why: Alternative integration pattern, shows common pitfalls

- doc: https://ollama.com/library/mistral
  section: Model configuration and parameters
  critical: Proper model setup for conversational AI

- file: claude_md_files/CLAUDE-REACT.md
  why: React 19 patterns, TypeScript requirements, component structure

- file: claude_md_files/CLAUDE-NEXTJS-15.md
  why: TypeScript configuration, build patterns, best practices

- docfile: PRPs/ai_docs/cc_overview.md
  why: Project structure and development workflow patterns
```

### Current Codebase tree

```bash
PRPs-agentic-eng/
├── cursor_workflows/     # Cursor-specific workflows
├── PRPs/
│   ├── templates/        # PRP templates
│   ├── scripts/         # PRP runner and utilities
│   ├── ai_docs/         # Curated documentation
│   └── completed/       # Finished PRPs
├── claude_md_files/     # Framework examples
├── pyproject.toml       # Python configuration
└── README.md
```

### Desired Codebase tree with files to be added

```bash
PRPs-agentic-eng/
├── chatbot-app/         # New React TypeScript app
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.tsx    # Main chat container
│   │   │   ├── MessageList.tsx      # PatternFly DataList for messages
│   │   │   ├── MessageItem.tsx      # Individual message component
│   │   │   ├── MessageInput.tsx     # Input field with send button
│   │   │   └── StreamingMessage.tsx # Real-time streaming display
│   │   ├── hooks/
│   │   │   ├── useOllama.ts         # Ollama integration hook
│   │   │   └── useChat.ts           # Chat state management
│   │   ├── services/
│   │   │   └── ollamaService.ts     # Ollama API service
│   │   ├── types/
│   │   │   └── chat.ts              # TypeScript interfaces
│   │   ├── utils/
│   │   │   └── messageUtils.ts      # Message formatting utilities
│   │   ├── App.tsx                  # Main app component
│   │   └── main.tsx                 # Entry point
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   ├── vite.config.ts
│   └── README.md
└── [existing files...]
```

### Known Gotchas of our codebase & Library Quirks

```typescript
// CRITICAL: PatternFly requires specific CSS imports
// Example: Must import PatternFly CSS before custom styles
// Example: DataList requires specific prop combinations for proper layout

// CRITICAL: Ollama streaming requires proper cleanup
// Example: AbortController must be used to cancel streaming requests
// Example: Memory leaks possible if streams aren't properly closed

// CRITICAL: React 19 + TypeScript strict mode
// Example: Must use ReactElement instead of JSX.Element
// Example: ExactOptionalPropertyTypes requires careful prop handling

// CRITICAL: Ollama local setup requirements
// Example: Ollama server must be running on localhost:11434
// Example: Mistral model must be pulled before use: `ollama pull mistral`

// CRITICAL: CORS considerations for local development
// Example: Ollama runs on different port than React dev server
// Example: May need proxy configuration or CORS headers
```

## Implementation Blueprint

### Data models and structure

Create the core data models for type safety and consistency.

```typescript
// Chat message interfaces
interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: Date;
  streaming?: boolean;
}

interface ChatState {
  messages: ChatMessage[];
  isLoading: boolean;
  error: string | null;
  currentStreamingMessage: string;
}

// Ollama service interfaces
interface OllamaConfig {
  baseUrl: string;
  model: string;
  temperature?: number;
  maxTokens?: number;
}

interface StreamingResponse {
  response: string;
  done: boolean;
  context?: number[];
}
```

### List of tasks to be completed to fulfill the PRP in the order they should be completed

```yaml
Task 1:
CREATE chatbot-app directory structure:
  - INITIALIZE new Vite React TypeScript project
  - INSTALL dependencies: @patternfly/react-core, @patternfly/react-styles, ollama
  - CONFIGURE TypeScript with strict mode
  - SET UP development server with proxy for Ollama

Task 2:
CREATE src/types/chat.ts:
  - DEFINE ChatMessage interface
  - DEFINE ChatState interface
  - DEFINE OllamaConfig interface
  - EXPORT all types for reuse

Task 3:
CREATE src/services/ollamaService.ts:
  - IMPLEMENT OllamaService class
  - ADD streaming chat method
  - HANDLE connection errors and timeouts
  - IMPLEMENT proper cleanup with AbortController

Task 4:
CREATE src/hooks/useOllama.ts:
  - IMPLEMENT custom hook for Ollama integration
  - MANAGE connection state
  - PROVIDE methods for sending messages
  - HANDLE streaming responses

Task 5:
CREATE src/hooks/useChat.ts:
  - IMPLEMENT chat state management
  - MANAGE message history
  - HANDLE streaming message updates
  - PROVIDE methods for adding/updating messages

Task 6:
CREATE src/components/MessageItem.tsx:
  - IMPLEMENT individual message component
  - USE PatternFly DataListItem
  - HANDLE user vs assistant message styling
  - SUPPORT streaming message display

Task 7:
CREATE src/components/StreamingMessage.tsx:
  - IMPLEMENT real-time streaming display
  - HANDLE character-by-character updates
  - SHOW typing indicators
  - SMOOTH animation effects

Task 8:
CREATE src/components/MessageList.tsx:
  - IMPLEMENT PatternFly DataList
  - RENDER message history
  - HANDLE auto-scrolling to bottom
  - SUPPORT empty state

Task 9:
CREATE src/components/MessageInput.tsx:
  - IMPLEMENT input field with PatternFly components
  - HANDLE send button state
  - SUPPORT Enter key submission
  - VALIDATE message content

Task 10:
CREATE src/components/ChatInterface.tsx:
  - IMPLEMENT main chat container
  - INTEGRATE all chat components
  - HANDLE layout and responsive design
  - MANAGE overall chat state

Task 11:
UPDATE src/App.tsx:
  - INTEGRATE ChatInterface component
  - IMPORT PatternFly CSS
  - HANDLE global app state
  - CONFIGURE error boundaries

Task 12:
CONFIGURE build and development:
  - UPDATE vite.config.ts for Ollama proxy
  - CONFIGURE TypeScript strict mode
  - SET UP development scripts
  - OPTIMIZE production build
```

### Per task pseudocode as needed added to each task

```typescript
// Task 3: OllamaService
class OllamaService {
  private baseUrl: string;
  private model: string;
  
  constructor(config: OllamaConfig) {
    // PATTERN: Validate config first
    this.validateConfig(config);
    this.baseUrl = config.baseUrl;
    this.model = config.model;
  }
  
  async *streamChat(message: string, abortController: AbortController): AsyncGenerator<string> {
    // CRITICAL: Must use AbortController for cleanup
    const response = await fetch(`${this.baseUrl}/api/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ model: this.model, prompt: message, stream: true }),
      signal: abortController.signal
    });
    
    // PATTERN: Handle streaming response
    const reader = response.body?.getReader();
    const decoder = new TextDecoder();
    
    try {
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        
        const chunk = decoder.decode(value);
        const lines = chunk.split('\n').filter(line => line.trim());
        
        for (const line of lines) {
          // GOTCHA: Ollama returns JSONL format
          const parsed = JSON.parse(line);
          if (parsed.response) {
            yield parsed.response;
          }
        }
      }
    } finally {
      // CRITICAL: Always cleanup reader
      reader?.releaseLock();
    }
  }
}

// Task 4: useOllama hook
export const useOllama = (config: OllamaConfig) => {
  const [service] = useState(() => new OllamaService(config));
  const [isConnected, setIsConnected] = useState(false);
  
  const sendMessage = useCallback(async (message: string, onChunk: (chunk: string) => void) => {
    // PATTERN: Use AbortController for cleanup
    const abortController = new AbortController();
    
    try {
      for await (const chunk of service.streamChat(message, abortController)) {
        onChunk(chunk);
      }
    } catch (error) {
      // PATTERN: Handle specific error types
      if (error.name === 'AbortError') {
        console.log('Request aborted');
      } else {
        throw error;
      }
    }
    
    return () => abortController.abort();
  }, [service]);
  
  return { sendMessage, isConnected };
};

// Task 6: MessageItem component
export const MessageItem: React.FC<{ message: ChatMessage }> = ({ message }) => {
  return (
    <DataListItem aria-labelledby={`message-${message.id}`}>
      <DataListItemRow>
        <DataListItemCells
          dataListCells={[
            <DataListCell key="avatar">
              <Avatar src={message.role === 'user' ? '/user-avatar.png' : '/bot-avatar.png'} />
            </DataListCell>,
            <DataListCell key="content">
              <div className={`message-content ${message.role}`}>
                {message.streaming ? (
                  <StreamingMessage content={message.content} />
                ) : (
                  <Text>{message.content}</Text>
                )}
              </div>
            </DataListCell>
          ]}
        />
      </DataListItemRow>
    </DataListItem>
  );
};
```

### Integration Points

```yaml
DEVELOPMENT_SERVER:
  - vite.config.ts: Configure proxy for Ollama API
  - pattern: "proxy: { '/api': 'http://localhost:11434' }"

STYLING:
  - src/main.tsx: Import PatternFly CSS
  - pattern: "import '@patternfly/react-core/dist/styles/base.css';"

OLLAMA_SETUP:
  - local: Ensure Ollama server is running
  - command: "ollama serve"
  - model: "ollama pull mistral"

TYPESCRIPT_CONFIG:
  - tsconfig.json: Enable strict mode
  - pattern: "strict: true, noImplicitAny: true"
```

## Validation Loop

### Level 1: Syntax & Style

```bash
# Run these FIRST - fix any errors before proceeding
npm run lint                    # ESLint checking
npm run type-check             # TypeScript type checking
npm run format                 # Prettier formatting

# Expected: No errors. If errors, READ the error and fix.
```

### Level 2: Unit Tests

```typescript
// CREATE tests for key components:
describe('OllamaService', () => {
  it('should connect to Ollama server', async () => {
    const service = new OllamaService({ baseUrl: 'http://localhost:11434', model: 'mistral' });
    const result = await service.testConnection();
    expect(result).toBe(true);
  });
  
  it('should handle streaming responses', async () => {
    const service = new OllamaService({ baseUrl: 'http://localhost:11434', model: 'mistral' });
    const chunks: string[] = [];
    
    for await (const chunk of service.streamChat('Hello', new AbortController())) {
      chunks.push(chunk);
    }
    
    expect(chunks.length).toBeGreaterThan(0);
  });
});

describe('ChatInterface', () => {
  it('should render message input', () => {
    render(<ChatInterface />);
    expect(screen.getByPlaceholderText('Type a message...')).toBeInTheDocument();
  });
  
  it('should display messages', () => {
    const messages = [{ id: '1', role: 'user', content: 'Hello', timestamp: new Date() }];
    render(<ChatInterface initialMessages={messages} />);
    expect(screen.getByText('Hello')).toBeInTheDocument();
  });
});
```

```bash
# Run and iterate until passing:
npm run test
# If failing: Read error, understand root cause, fix code, re-run
```

### Level 3: Integration Test

```bash
# Start Ollama server (in separate terminal)
ollama serve

# Pull Mistral model
ollama pull mistral

# Start the React development server
npm run dev

# Test the application
# Navigate to http://localhost:5173
# Send a test message: "Hello, how are you?"
# Expected: AI response streams in character by character
# Expected: Message history is maintained
# Expected: UI is responsive and follows PatternFly design
```

### Level 4: Production Build & Creative Validation

```bash
# Build for production
npm run build

# Serve production build
npm run preview

# Test production build
# Navigate to preview URL
# Test full chat functionality
# Verify no console errors
# Check responsive design on mobile

# Performance testing
# Use browser dev tools to check:
# - Bundle size optimization
# - Memory usage during streaming
# - Network request efficiency
```

## Final validation Checklist

- [ ] All TypeScript types are properly defined
- [ ] PatternFly components render correctly
- [ ] Ollama integration works with streaming
- [ ] Messages display in real-time
- [ ] UI is responsive and accessible
- [ ] No console errors in development or production
- [ ] Build pipeline works correctly
- [ ] Local Ollama setup instructions are clear
- [ ] Error handling works for network failures
- [ ] Memory usage is optimized for long conversations

---

## Anti-Patterns to Avoid

- ❌ Don't use any types - leverage TypeScript fully
- ❌ Don't ignore PatternFly CSS import requirements
- ❌ Don't forget to cleanup streaming connections
- ❌ Don't block the UI during streaming responses
- ❌ Don't hardcode Ollama URLs - use configuration
- ❌ Don't skip error handling for network failures
- ❌ Don't use JSX.Element - use ReactElement in React 19
- ❌ Don't ignore accessibility requirements
- ❌ Don't skip responsive design testing

## Additional Resources

- [PatternFly React Documentation](https://www.patternfly.org/v4/get-started/developers)
- [Ollama JavaScript Client](https://github.com/ollama/ollama-js)
- [React TypeScript Cheatsheet](https://react-typescript-cheatsheet.netlify.app/)
- [Vite Configuration Reference](https://vitejs.dev/config/)
- [Mistral Model Documentation](https://ollama.com/library/mistral)

## Confidence Rating

**9/10** - This PRP provides comprehensive context, clear implementation steps, and thorough validation. The combination of well-documented technologies (React, TypeScript, PatternFly) with specific integration patterns should enable successful one-pass implementation. 