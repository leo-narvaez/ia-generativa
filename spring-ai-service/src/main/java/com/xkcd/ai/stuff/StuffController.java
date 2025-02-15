package com.xkcd.ai.stuff;

import org.springframework.ai.chat.ChatClient;
import org.springframework.ai.chat.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class StuffController {

	private final ChatClient chatClient;

	@Value("classpath:/docs/wikipedia-curling.md")
	private Resource docsToStuffResource;

	@Value("classpath:/prompts/qa-prompt.st")
	private Resource qaPromptResource;

	@Autowired
	public StuffController(ChatClient chatClient) {
		this.chatClient = chatClient;
	}

	@GetMapping("/ai/stuff")
	public Completion completion(@RequestParam(value = "message",
			defaultValue = "¿Qué atletas ganaron la medalla de oro en dobles mixtos en curling en los Juegos Olímpicos de Invierno de 2022?'") String message,
			@RequestParam(value = "stuffit", defaultValue = "false") boolean stuffit) {
		PromptTemplate promptTemplate = new PromptTemplate(qaPromptResource);
		Map<String, Object> map = new HashMap<>();
		map.put("question", message);
		if (stuffit) {
			map.put("context", docsToStuffResource);
		}
		else {
			map.put("context", "");
		}
		Prompt prompt = promptTemplate.create(map);
		Generation generation = chatClient.call(prompt).getResult();
		return new Completion(generation.getOutput().getContent());
	}

}
