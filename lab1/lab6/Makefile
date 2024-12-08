.SILENT:
build:
	cd cmd && go build main.go
run: build
	cd cmd && ./main

goose-up:
	cd migrations && goose sqlite "file:../music.db" up
goose-down:
	cd migrations && goose sqlite "file:../music.db" down
goose-down-all:
	cd migrations && goose sqlite "file:../music.db" down-to 0