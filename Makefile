.PHONY: build

build:
	@sudo chmod +x scripts/build.sh
	@sudo ./scripts/build.sh
	@echo "[✔️] Frontend build complete!"

certbot:
	@chmod +x ./webserver/register_ssl.sh
	@sudo ./webserver/register_ssl.sh \
								--domains "$(DOMAINS)" \
								--email $(EMAIL) \
								--data-path ./webserver/certbot \
								--staging 0

deploy:
	@docker-compose \
					-f docker-compose.yml \
					up -d --build --force-recreate

stop:
	@docker stop $$(docker ps -aq)
	@echo "[✔️] All container were stopped!"

rm:
	@docker stop $$(docker ps -aq)
	@docker rm $$(docker ps -aq)
	@echo "[✔️] All container were removed!"