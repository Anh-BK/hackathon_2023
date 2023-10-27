BOT_IMAGE = "chatbot_be"
tag = "latest"

build:
	bash tools/build_chatbotbe.sh ${BOT_IMAGE}:${tag}