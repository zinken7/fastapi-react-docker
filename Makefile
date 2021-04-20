.PHONY: build

certbot:
	@chmod +x ./webserver/register_ssl.sh
	@sudo ./webserver/register_ssl.sh \
								--domains "$(DOMAINS)" \
								--email $(EMAIL) \
								--data-path ./webserver/certbot \
								--staging 0

build:
	@sudo chmod +x scripts/build.sh
	@sudo ./scripts/build.sh
	@echo "[✔️] Build complete!"

stop:
	@docker stop $$(docker ps -aq)
	@echo "[✔️] All container were stopped!"

rm:
	@docker stop $$(docker ps -aq)
	@docker rm $$(docker ps -aq)
	@echo "[✔️] All container were removed!"