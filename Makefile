BUILD_DIRECTORY := ./build

clean:
	rm -rf $(BUILD_DIRECTORY)

build: clean
	mkdir -p $(BUILD_DIRECTORY)
	cp ./releases/latest/mysql-bundle.yaml $(BUILD_DIRECTORY)/bundle.yaml
	cp ./charmcraft.yaml $(BUILD_DIRECTORY)
	cp ./metadata.yaml $(BUILD_DIRECTORY)
	cp ./README.md $(BUILD_DIRECTORY)
	charmcraft pack --destructive-mode --project-dir $(BUILD_DIRECTORY)

deploy: build
	juju deploy $(BUILD_DIRECTORY)/mysql-bundle.zip

destroy-model:
	juju destroy-model --force --destroy-storage $(shell juju models --format=yaml | yq ".current-model")

release: build
	charmcraft upload $(BUILD_DIRECTORY)/*.zip --name mysql-bundle --release=latest/edge

remove:
	$(eval apps := $(shell cat releases/latest/mysql-bundle.yaml |yq '.applications|keys' -o t))
	juju remove-application $(apps)

