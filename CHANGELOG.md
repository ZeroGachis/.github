# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 0.1.0 (2024-08-07)

**Full Changelog**: https://github.com/ZeroGachis/.github/compare/v4...v0.1.0

## [4.31.2](https://github.com/ZeroGachis/.github/compare/v4.31.1...v4.31.2) (2024-08-07)


### Bug Fixes

* **release-please:** don't set terraform_module by default ([6c68bf4](https://github.com/ZeroGachis/.github/commit/6c68bf4202b354a4e8c64eb212689dd9d74bdaf8))

## [4.31.1](https://github.com/ZeroGachis/.github/compare/v4.31.0...v4.31.1) (2024-08-07)


### Bug Fixes

* (release-please): wrong step order to use config file ([017b1fa](https://github.com/ZeroGachis/.github/commit/017b1fa2a101fe9fc51bc32035b56f1d3c7733a1))

## [4.31.0](https://github.com/ZeroGachis/.github/compare/v4.30.0...v4.31.0) (2024-08-07)


### Features

* **release-please:** customize config and manifest file ([4219510](https://github.com/ZeroGachis/.github/commit/42195101758e6e1e58dca3d3553539e6f822f68b))

## [4.30.0](https://github.com/ZeroGachis/.github/compare/v4.29.1...v4.30.0) (2024-08-07)


### Features

* **terraform-infracost:** add tfvars to trigger infracost pipeline ([4c38180](https://github.com/ZeroGachis/.github/commit/4c38180864a721178aafdcbe32700bee0243fba5))

## [4.29.1](https://github.com/ZeroGachis/.github/compare/v4.29.0...v4.29.1) (2024-08-06)


### Bug Fixes

* **terraform:** extra step ([b51c3f5](https://github.com/ZeroGachis/.github/commit/b51c3f5bf1063fb94e5950dda9708b8b84407f51))

## [4.29.0](https://github.com/ZeroGachis/.github/compare/v4.28.0...v4.29.0) (2024-08-06)


### Features

* **infracost:** init workflow ([ded1355](https://github.com/ZeroGachis/.github/commit/ded13554cc449782e0d0fa23b06f557442e55257))

## [4.28.0](https://github.com/ZeroGachis/.github/compare/v4.27.3...v4.28.0) (2024-07-31)


### Features

* Add auto definition of ECR url ([b6d454b](https://github.com/ZeroGachis/.github/commit/b6d454b010e9a3bb11baccd6eecb1c1bd59287fb))
* add build args for aws login to docker build workflow ([64d27eb](https://github.com/ZeroGachis/.github/commit/64d27eba797e541ac944618dae3b9156f6356897))
* add capability to build from private ECR base image ([48c5d9e](https://github.com/ZeroGachis/.github/commit/48c5d9e12f0c8d2e63b1bae7c3340e488d731a57))
* add capability to customize ecr repo name ([ddd2ddb](https://github.com/ZeroGachis/.github/commit/ddd2ddb63e442e4fd78d77f33d61aa1a8769a166))
* add capability to handle other tag into push ecr workflow ([dc6fb64](https://github.com/ZeroGachis/.github/commit/dc6fb64a9192c99d55db6eadbfdbc8a6ebf99b9a))
* Add CodePush serverUrl option to use OTA proxy ([9b13631](https://github.com/ZeroGachis/.github/commit/9b13631477bbca57f5b9922b614a69c8cf3c4122))
* Add Configure AWS Credentials optionnal step ([d71fa65](https://github.com/ZeroGachis/.github/commit/d71fa6504f442cb460fae31d32dcc7fc9b31ba97))
* Add Container Structure Tests workflow ([5a6b755](https://github.com/ZeroGachis/.github/commit/5a6b755ea82129f787fcb127ed129ddeab48b06a))
* add Dockerfile linter workflow ([8472cf3](https://github.com/ZeroGachis/.github/commit/8472cf34d5bedb79b20f0af448321362f2b99913))
* add github release notes workflow ([5a55469](https://github.com/ZeroGachis/.github/commit/5a554691cae5f2f572a4d77c1b7d29a4e847bd5e))
* add latest tag to ECR ([521b2a9](https://github.com/ZeroGachis/.github/commit/521b2a986feba19f33d7b5dca6bb4ca1894ff10b))
* add python publish workflow ([1e67086](https://github.com/ZeroGachis/.github/commit/1e67086be915fed20e831e77427937367b68c4fc))
* add security scan image with Anchore ([1b8a4eb](https://github.com/ZeroGachis/.github/commit/1b8a4eb6d3eb7ac951cc5c2a1858f1bbe54bffd6))
* Allow passing a docker target ([ede6578](https://github.com/ZeroGachis/.github/commit/ede6578fd3095c6f14751d5735566d3dfb187f67))
* avoid some step in build apk in case of PR ([72168bd](https://github.com/ZeroGachis/.github/commit/72168bd41630ace4c42a4e08495036a80ff535bd))
* disable Vault usage on ECR Push image flow ([4585ef6](https://github.com/ZeroGachis/.github/commit/4585ef66dc97c5edd22cd7a8be518202b766426e))
* handle multiple aws region ([17cf4bb](https://github.com/ZeroGachis/.github/commit/17cf4bb076d53e5ceea9441ef721a66a75d99860))
* **release-please:** customize release type ([4977712](https://github.com/ZeroGachis/.github/commit/4977712faf0be5af6c035be341e4bcec0e8ad508))
* **release-please:** make conditionnal major and minor tags ([c51e46e](https://github.com/ZeroGachis/.github/commit/c51e46ee2c25dbcfb728f8bee04d1433bb4d76de))
* **terraform:** login to github to use private module hosted in ouy org ([7566198](https://github.com/ZeroGachis/.github/commit/7566198a64a08777dcf118d4c8c7e1eb54f13eb5))
* **terraform:** use dynamic token github generation with vault ([e0d4c5b](https://github.com/ZeroGachis/.github/commit/e0d4c5b9d6922935a9160c7291c0624bfca7980c))


### Bug Fixes

* Add missing permission to publish report ([5dd1e53](https://github.com/ZeroGachis/.github/commit/5dd1e532af1c6017de129052137be0a0150c8de8))
* add output for push ecr ([03ae984](https://github.com/ZeroGachis/.github/commit/03ae98424d3f51b34b9ec98c2a9ad8188c7da063))
* build failed when vault is disable ([79605a9](https://github.com/ZeroGachis/.github/commit/79605a95fc246d6ed02323443acf1926361fe0ff))
* build image aws only readonly ([b51c996](https://github.com/ZeroGachis/.github/commit/b51c996c394e7b209bda47d1a04b41454134f974))
* build image workflow - add domain owner ([7be8d66](https://github.com/ZeroGachis/.github/commit/7be8d662c31ee71cb6c1f733d45e2eef8573f927))
* build workflow - enable aws creds outputs vars ([00418e3](https://github.com/ZeroGachis/.github/commit/00418e375ae00ec986260318dd2f739fa65cc4dd))
* build x temp version ([1d5bd19](https://github.com/ZeroGachis/.github/commit/1d5bd19efa1132c5b0e8c37ae56e4fe8797e4858))
* catalog info ([f89940d](https://github.com/ZeroGachis/.github/commit/f89940de996ce09be5f540e9447b74d4dc90898c))
* catalog-info yaml ([214b2d4](https://github.com/ZeroGachis/.github/commit/214b2d4ccb7d4efbbe21605a498d4c66134632cf))
* codepush ci ([c934195](https://github.com/ZeroGachis/.github/commit/c934195501fcdd982b6894b4bb7ecdf85ea8f257))
* create APK if condition issue ([73a9ae1](https://github.com/ZeroGachis/.github/commit/73a9ae18c203c0e7c11001a45e523d6e69723e24))
* delete test-report hadolint ([529e19b](https://github.com/ZeroGachis/.github/commit/529e19b33ffe9d24e12c29e7fd1f658eb2ccff3c))
* disable auto latest label ([2b0cd1e](https://github.com/ZeroGachis/.github/commit/2b0cd1ed871d7173cf740b967ad598a60d8925e6))
* github secret variable interpolation ([a77f150](https://github.com/ZeroGachis/.github/commit/a77f15053533575c45c804c0315021dd48cf0c37))
* increase delay and retry count ([950aca7](https://github.com/ZeroGachis/.github/commit/950aca7bd5379a53c5f5115f5bd8a957022be588))
* linter report file issue ([7cde3a6](https://github.com/ZeroGachis/.github/commit/7cde3a62ac86c6a8d85a2e25397e52ab860d7675))
* missing docker tag command ([b30b90e](https://github.com/ZeroGachis/.github/commit/b30b90e89dd0cb717fab4800941ebbab5d7fc986))
* **release-please:** fix boolean interpretation inside github workflow ([6e19306](https://github.com/ZeroGachis/.github/commit/6e193069d554deab6e33351de36697a4ac643245))
* **release-please:** fix boolean interpretation inside github workflow  2 ([a0cee5a](https://github.com/ZeroGachis/.github/commit/a0cee5a4497c376403fd19459a448684af4f09ca))
* **release-please:** fix boolean interpretation inside github workflow  3 ([1b2c126](https://github.com/ZeroGachis/.github/commit/1b2c12657be7a48e1e809d0ca1fbfc7df5e24653))
* syntax issue on create apk artifact workflow ([9202fec](https://github.com/ZeroGachis/.github/commit/9202fec4959e58f50fb03c08c294f12571ad8016))
* Temporary fix BuildX version ([1e0af30](https://github.com/ZeroGachis/.github/commit/1e0af3040f856792874186caaa8978ae22f63fc0))
* **terrafom:** syntax issue when input/vault_secrets is not empty ([86268d8](https://github.com/ZeroGachis/.github/commit/86268d86189e4961011385147fb193f43901a90b))
* terraform workflows - duplicate bucket variable ([5234e47](https://github.com/ZeroGachis/.github/commit/5234e47bb8b14cab8024f53cc761a91bf8df3f18))
* **terraform:** condition for login to private github org ([9118e67](https://github.com/ZeroGachis/.github/commit/9118e67c2ae5b5004b6ea0842d0e293666c9cbf6))
* variabilize bucket for keystore ([755d585](https://github.com/ZeroGachis/.github/commit/755d585db531c42e76228e5c5c1ed92a0f4c867a))
* vault action retry to avoid dns issue ([47d2708](https://github.com/ZeroGachis/.github/commit/47d270860e70ceae773b37ecad8a80972779d969))
* vault url not required anymore ([0b47629](https://github.com/ZeroGachis/.github/commit/0b47629814c7656e0a23ddb93cf4a12f77df7722))
* vault url required 2 ([9d05375](https://github.com/ZeroGachis/.github/commit/9d05375d70c3c9058393c8b96a8f8f61ba9243c5))

## [4.27.3](https://github.com/ZeroGachis/.github/compare/v4.27.2...v4.27.3) (2024-07-31)


### Bug Fixes

* **release-please:** fix boolean interpretation inside github workflow  3 ([1b2c126](https://github.com/ZeroGachis/.github/commit/1b2c12657be7a48e1e809d0ca1fbfc7df5e24653))

## [4.27.2](https://github.com/ZeroGachis/.github/compare/v4.27.1...v4.27.2) (2024-07-31)


### Bug Fixes

* **release-please:** fix boolean interpretation inside github workflow  2 ([a0cee5a](https://github.com/ZeroGachis/.github/commit/a0cee5a4497c376403fd19459a448684af4f09ca))

## [4.27.1](https://github.com/ZeroGachis/.github/compare/v4.27.0...v4.27.1) (2024-07-31)


### Bug Fixes

* **release-please:** fix boolean interpretation inside github workflow ([6e19306](https://github.com/ZeroGachis/.github/commit/6e193069d554deab6e33351de36697a4ac643245))

## [4.27.0](https://github.com/ZeroGachis/.github/compare/v4.26.2...v4.27.0) (2024-07-31)


### Features

* Add auto definition of ECR url ([b6d454b](https://github.com/ZeroGachis/.github/commit/b6d454b010e9a3bb11baccd6eecb1c1bd59287fb))
* add build args for aws login to docker build workflow ([64d27eb](https://github.com/ZeroGachis/.github/commit/64d27eba797e541ac944618dae3b9156f6356897))
* add capability to build from private ECR base image ([48c5d9e](https://github.com/ZeroGachis/.github/commit/48c5d9e12f0c8d2e63b1bae7c3340e488d731a57))
* add capability to customize ecr repo name ([ddd2ddb](https://github.com/ZeroGachis/.github/commit/ddd2ddb63e442e4fd78d77f33d61aa1a8769a166))
* add capability to handle other tag into push ecr workflow ([dc6fb64](https://github.com/ZeroGachis/.github/commit/dc6fb64a9192c99d55db6eadbfdbc8a6ebf99b9a))
* Add CodePush serverUrl option to use OTA proxy ([9b13631](https://github.com/ZeroGachis/.github/commit/9b13631477bbca57f5b9922b614a69c8cf3c4122))
* Add Configure AWS Credentials optionnal step ([d71fa65](https://github.com/ZeroGachis/.github/commit/d71fa6504f442cb460fae31d32dcc7fc9b31ba97))
* Add Container Structure Tests workflow ([5a6b755](https://github.com/ZeroGachis/.github/commit/5a6b755ea82129f787fcb127ed129ddeab48b06a))
* add Dockerfile linter workflow ([8472cf3](https://github.com/ZeroGachis/.github/commit/8472cf34d5bedb79b20f0af448321362f2b99913))
* add github release notes workflow ([5a55469](https://github.com/ZeroGachis/.github/commit/5a554691cae5f2f572a4d77c1b7d29a4e847bd5e))
* add latest tag to ECR ([521b2a9](https://github.com/ZeroGachis/.github/commit/521b2a986feba19f33d7b5dca6bb4ca1894ff10b))
* add python publish workflow ([1e67086](https://github.com/ZeroGachis/.github/commit/1e67086be915fed20e831e77427937367b68c4fc))
* add security scan image with Anchore ([1b8a4eb](https://github.com/ZeroGachis/.github/commit/1b8a4eb6d3eb7ac951cc5c2a1858f1bbe54bffd6))
* Allow passing a docker target ([ede6578](https://github.com/ZeroGachis/.github/commit/ede6578fd3095c6f14751d5735566d3dfb187f67))
* avoid some step in build apk in case of PR ([72168bd](https://github.com/ZeroGachis/.github/commit/72168bd41630ace4c42a4e08495036a80ff535bd))
* disable Vault usage on ECR Push image flow ([4585ef6](https://github.com/ZeroGachis/.github/commit/4585ef66dc97c5edd22cd7a8be518202b766426e))
* handle multiple aws region ([17cf4bb](https://github.com/ZeroGachis/.github/commit/17cf4bb076d53e5ceea9441ef721a66a75d99860))
* **release-please:** make conditionnal major and minor tags ([c51e46e](https://github.com/ZeroGachis/.github/commit/c51e46ee2c25dbcfb728f8bee04d1433bb4d76de))
* **terraform:** login to github to use private module hosted in ouy org ([7566198](https://github.com/ZeroGachis/.github/commit/7566198a64a08777dcf118d4c8c7e1eb54f13eb5))
* **terraform:** use dynamic token github generation with vault ([e0d4c5b](https://github.com/ZeroGachis/.github/commit/e0d4c5b9d6922935a9160c7291c0624bfca7980c))


### Bug Fixes

* Add missing permission to publish report ([5dd1e53](https://github.com/ZeroGachis/.github/commit/5dd1e532af1c6017de129052137be0a0150c8de8))
* add output for push ecr ([03ae984](https://github.com/ZeroGachis/.github/commit/03ae98424d3f51b34b9ec98c2a9ad8188c7da063))
* build failed when vault is disable ([79605a9](https://github.com/ZeroGachis/.github/commit/79605a95fc246d6ed02323443acf1926361fe0ff))
* build image aws only readonly ([b51c996](https://github.com/ZeroGachis/.github/commit/b51c996c394e7b209bda47d1a04b41454134f974))
* build image workflow - add domain owner ([7be8d66](https://github.com/ZeroGachis/.github/commit/7be8d662c31ee71cb6c1f733d45e2eef8573f927))
* build workflow - enable aws creds outputs vars ([00418e3](https://github.com/ZeroGachis/.github/commit/00418e375ae00ec986260318dd2f739fa65cc4dd))
* build x temp version ([1d5bd19](https://github.com/ZeroGachis/.github/commit/1d5bd19efa1132c5b0e8c37ae56e4fe8797e4858))
* catalog info ([f89940d](https://github.com/ZeroGachis/.github/commit/f89940de996ce09be5f540e9447b74d4dc90898c))
* catalog-info yaml ([214b2d4](https://github.com/ZeroGachis/.github/commit/214b2d4ccb7d4efbbe21605a498d4c66134632cf))
* codepush ci ([c934195](https://github.com/ZeroGachis/.github/commit/c934195501fcdd982b6894b4bb7ecdf85ea8f257))
* create APK if condition issue ([73a9ae1](https://github.com/ZeroGachis/.github/commit/73a9ae18c203c0e7c11001a45e523d6e69723e24))
* delete test-report hadolint ([529e19b](https://github.com/ZeroGachis/.github/commit/529e19b33ffe9d24e12c29e7fd1f658eb2ccff3c))
* disable auto latest label ([2b0cd1e](https://github.com/ZeroGachis/.github/commit/2b0cd1ed871d7173cf740b967ad598a60d8925e6))
* github secret variable interpolation ([a77f150](https://github.com/ZeroGachis/.github/commit/a77f15053533575c45c804c0315021dd48cf0c37))
* increase delay and retry count ([950aca7](https://github.com/ZeroGachis/.github/commit/950aca7bd5379a53c5f5115f5bd8a957022be588))
* linter report file issue ([7cde3a6](https://github.com/ZeroGachis/.github/commit/7cde3a62ac86c6a8d85a2e25397e52ab860d7675))
* missing docker tag command ([b30b90e](https://github.com/ZeroGachis/.github/commit/b30b90e89dd0cb717fab4800941ebbab5d7fc986))
* syntax issue on create apk artifact workflow ([9202fec](https://github.com/ZeroGachis/.github/commit/9202fec4959e58f50fb03c08c294f12571ad8016))
* Temporary fix BuildX version ([1e0af30](https://github.com/ZeroGachis/.github/commit/1e0af3040f856792874186caaa8978ae22f63fc0))
* **terrafom:** syntax issue when input/vault_secrets is not empty ([86268d8](https://github.com/ZeroGachis/.github/commit/86268d86189e4961011385147fb193f43901a90b))
* terraform workflows - duplicate bucket variable ([5234e47](https://github.com/ZeroGachis/.github/commit/5234e47bb8b14cab8024f53cc761a91bf8df3f18))
* **terraform:** condition for login to private github org ([9118e67](https://github.com/ZeroGachis/.github/commit/9118e67c2ae5b5004b6ea0842d0e293666c9cbf6))
* variabilize bucket for keystore ([755d585](https://github.com/ZeroGachis/.github/commit/755d585db531c42e76228e5c5c1ed92a0f4c867a))
* vault action retry to avoid dns issue ([47d2708](https://github.com/ZeroGachis/.github/commit/47d270860e70ceae773b37ecad8a80972779d969))
* vault url not required anymore ([0b47629](https://github.com/ZeroGachis/.github/commit/0b47629814c7656e0a23ddb93cf4a12f77df7722))
* vault url required 2 ([9d05375](https://github.com/ZeroGachis/.github/commit/9d05375d70c3c9058393c8b96a8f8f61ba9243c5))

## [4.26.2](https://github.com/ZeroGachis/.github/compare/v4.26.1...v4.26.2) (2024-07-24)


### Bug Fixes

* **terraform:** condition for login to private github org ([9118e67](https://github.com/ZeroGachis/.github/commit/9118e67c2ae5b5004b6ea0842d0e293666c9cbf6))

## [4.26.1](https://github.com/ZeroGachis/.github/compare/v4.26.0...v4.26.1) (2024-07-24)


### Bug Fixes

* **terrafom:** syntax issue when input/vault_secrets is not empty ([86268d8](https://github.com/ZeroGachis/.github/commit/86268d86189e4961011385147fb193f43901a90b))

## [4.26.0](https://github.com/ZeroGachis/.github/compare/v4.25.0...v4.26.0) (2024-07-24)


### Features

* Add auto definition of ECR url ([b6d454b](https://github.com/ZeroGachis/.github/commit/b6d454b010e9a3bb11baccd6eecb1c1bd59287fb))
* add build args for aws login to docker build workflow ([64d27eb](https://github.com/ZeroGachis/.github/commit/64d27eba797e541ac944618dae3b9156f6356897))
* add capability to build from private ECR base image ([48c5d9e](https://github.com/ZeroGachis/.github/commit/48c5d9e12f0c8d2e63b1bae7c3340e488d731a57))
* add capability to customize ecr repo name ([ddd2ddb](https://github.com/ZeroGachis/.github/commit/ddd2ddb63e442e4fd78d77f33d61aa1a8769a166))
* add capability to handle other tag into push ecr workflow ([dc6fb64](https://github.com/ZeroGachis/.github/commit/dc6fb64a9192c99d55db6eadbfdbc8a6ebf99b9a))
* Add CodePush serverUrl option to use OTA proxy ([9b13631](https://github.com/ZeroGachis/.github/commit/9b13631477bbca57f5b9922b614a69c8cf3c4122))
* Add Configure AWS Credentials optionnal step ([d71fa65](https://github.com/ZeroGachis/.github/commit/d71fa6504f442cb460fae31d32dcc7fc9b31ba97))
* Add Container Structure Tests workflow ([5a6b755](https://github.com/ZeroGachis/.github/commit/5a6b755ea82129f787fcb127ed129ddeab48b06a))
* add Dockerfile linter workflow ([8472cf3](https://github.com/ZeroGachis/.github/commit/8472cf34d5bedb79b20f0af448321362f2b99913))
* add github release notes workflow ([5a55469](https://github.com/ZeroGachis/.github/commit/5a554691cae5f2f572a4d77c1b7d29a4e847bd5e))
* add latest tag to ECR ([521b2a9](https://github.com/ZeroGachis/.github/commit/521b2a986feba19f33d7b5dca6bb4ca1894ff10b))
* add python publish workflow ([1e67086](https://github.com/ZeroGachis/.github/commit/1e67086be915fed20e831e77427937367b68c4fc))
* add security scan image with Anchore ([1b8a4eb](https://github.com/ZeroGachis/.github/commit/1b8a4eb6d3eb7ac951cc5c2a1858f1bbe54bffd6))
* Allow passing a docker target ([ede6578](https://github.com/ZeroGachis/.github/commit/ede6578fd3095c6f14751d5735566d3dfb187f67))
* avoid some step in build apk in case of PR ([72168bd](https://github.com/ZeroGachis/.github/commit/72168bd41630ace4c42a4e08495036a80ff535bd))
* disable Vault usage on ECR Push image flow ([4585ef6](https://github.com/ZeroGachis/.github/commit/4585ef66dc97c5edd22cd7a8be518202b766426e))
* handle multiple aws region ([17cf4bb](https://github.com/ZeroGachis/.github/commit/17cf4bb076d53e5ceea9441ef721a66a75d99860))
* **terraform:** login to github to use private module hosted in ouy org ([7566198](https://github.com/ZeroGachis/.github/commit/7566198a64a08777dcf118d4c8c7e1eb54f13eb5))
* **terraform:** use dynamic token github generation with vault ([e0d4c5b](https://github.com/ZeroGachis/.github/commit/e0d4c5b9d6922935a9160c7291c0624bfca7980c))


### Bug Fixes

* Add missing permission to publish report ([5dd1e53](https://github.com/ZeroGachis/.github/commit/5dd1e532af1c6017de129052137be0a0150c8de8))
* add output for push ecr ([03ae984](https://github.com/ZeroGachis/.github/commit/03ae98424d3f51b34b9ec98c2a9ad8188c7da063))
* build failed when vault is disable ([79605a9](https://github.com/ZeroGachis/.github/commit/79605a95fc246d6ed02323443acf1926361fe0ff))
* build image aws only readonly ([b51c996](https://github.com/ZeroGachis/.github/commit/b51c996c394e7b209bda47d1a04b41454134f974))
* build image workflow - add domain owner ([7be8d66](https://github.com/ZeroGachis/.github/commit/7be8d662c31ee71cb6c1f733d45e2eef8573f927))
* build workflow - enable aws creds outputs vars ([00418e3](https://github.com/ZeroGachis/.github/commit/00418e375ae00ec986260318dd2f739fa65cc4dd))
* build x temp version ([1d5bd19](https://github.com/ZeroGachis/.github/commit/1d5bd19efa1132c5b0e8c37ae56e4fe8797e4858))
* catalog info ([f89940d](https://github.com/ZeroGachis/.github/commit/f89940de996ce09be5f540e9447b74d4dc90898c))
* catalog-info yaml ([214b2d4](https://github.com/ZeroGachis/.github/commit/214b2d4ccb7d4efbbe21605a498d4c66134632cf))
* codepush ci ([c934195](https://github.com/ZeroGachis/.github/commit/c934195501fcdd982b6894b4bb7ecdf85ea8f257))
* create APK if condition issue ([73a9ae1](https://github.com/ZeroGachis/.github/commit/73a9ae18c203c0e7c11001a45e523d6e69723e24))
* delete test-report hadolint ([529e19b](https://github.com/ZeroGachis/.github/commit/529e19b33ffe9d24e12c29e7fd1f658eb2ccff3c))
* disable auto latest label ([2b0cd1e](https://github.com/ZeroGachis/.github/commit/2b0cd1ed871d7173cf740b967ad598a60d8925e6))
* github secret variable interpolation ([a77f150](https://github.com/ZeroGachis/.github/commit/a77f15053533575c45c804c0315021dd48cf0c37))
* increase delay and retry count ([950aca7](https://github.com/ZeroGachis/.github/commit/950aca7bd5379a53c5f5115f5bd8a957022be588))
* linter report file issue ([7cde3a6](https://github.com/ZeroGachis/.github/commit/7cde3a62ac86c6a8d85a2e25397e52ab860d7675))
* missing docker tag command ([b30b90e](https://github.com/ZeroGachis/.github/commit/b30b90e89dd0cb717fab4800941ebbab5d7fc986))
* syntax issue on create apk artifact workflow ([9202fec](https://github.com/ZeroGachis/.github/commit/9202fec4959e58f50fb03c08c294f12571ad8016))
* Temporary fix BuildX version ([1e0af30](https://github.com/ZeroGachis/.github/commit/1e0af3040f856792874186caaa8978ae22f63fc0))
* terraform workflows - duplicate bucket variable ([5234e47](https://github.com/ZeroGachis/.github/commit/5234e47bb8b14cab8024f53cc761a91bf8df3f18))
* variabilize bucket for keystore ([755d585](https://github.com/ZeroGachis/.github/commit/755d585db531c42e76228e5c5c1ed92a0f4c867a))
* vault action retry to avoid dns issue ([47d2708](https://github.com/ZeroGachis/.github/commit/47d270860e70ceae773b37ecad8a80972779d969))
* vault url not required anymore ([0b47629](https://github.com/ZeroGachis/.github/commit/0b47629814c7656e0a23ddb93cf4a12f77df7722))
* vault url required 2 ([9d05375](https://github.com/ZeroGachis/.github/commit/9d05375d70c3c9058393c8b96a8f8f61ba9243c5))

## [4.25.0](https://github.com/ZeroGachis/.github/compare/4.24.0...v4.25.0) (2024-07-23)


### Features

* **terraform:** login to github to use private module hosted in ouy org ([7566198](https://github.com/ZeroGachis/.github/commit/7566198a64a08777dcf118d4c8c7e1eb54f13eb5))

## [1.0.0] - 2022-11-30

### Added
- Init Github Action template for Terraform and Docker steps

## [1.0.1] - 2022-12-05

### Fixed
- Variabilize repo for ECR push github template

## [1.1.0] - 2022-12-08

### Added
- Create template workflow to run docker command and upload artifact

## [1.2.0] - 2022-12-12

### Added
- Add capability to enable test report to docker workflows

## [1.3.0] - 2022-12-13

### Added
- Add capability to disable github checkout for docker workflows

## [1.3.1] - 2022-12-14

### Fixed
- Test Report actions issue with git repository

## [1.3.2] - 2022-12-14

### Fixed
- Test Report actions issue with git repository - workdir
- Terraform summary issue in some usecase

## [1.4.0] - 2022-12-15

### Fixed
- Use legacy Test report plugin to disable git ls command

## [2.0.0] - 2023-02-03

### Added
- Use Hashicorp Vault to store AWS secret for Terraform workflow

## [2.1.0] - 2023-02-07

### Added
- Add Terraform substep name input
- Add working dir in terraform workflow

## [2.2.0] - 2023-02-16

### Added
- Add Vault secrets handle to all workflows

## [2.3.0] - 2023-02-17

### Added
- Generic new workflows : Run python command and Run aws command
- Simplify Terraform workflow (AWS Key as Env variable)

## [2.4.0] - 2023-05-17
### Fixed
- Dependabot bump versions
 
## [2.5.0] - 2023-05-24 
### Fixed
- Terraform status
 
## [2.6.0] - 2023-06-07
### Added
- Vault custom secret for Docker upload artifact workflow

## [2.7.0] - 2023-07-24
### Added
- Customize capability for terraform parallelism


## [2.8.0] - 2023-08-11
### Updated
- Tailscale v1 to v2


## [3.0.0] - 2023-08-11

### Breaking Change
- AWS auth change, be careful to declare all needed vars as inputs or envs vars to use this version
### Updated
- Github OIDC auth for AWS and multiaccount
- Support for multi account on Datadog and AWS

## [3.1.0] - 2023-09-12

### Added
- Terraform workflow have capabity to work on subdirectory
- Terraform workflow - Variabilize AWS Secrets to be override

## [3.2.0] - 2023-09-12

### Added
- Terraform backend configuration customization

## [3.7.0] - 2023-11-15

### Added
-  Vault custom secret for Datadog client API key entry for Vault
