sync:
	rsync . -acv --exclude=.git --exclude=.tox spot:terraform-modules

fmt:
	terraform fmt -recursive -list .

lint:
	tflint --recursive

