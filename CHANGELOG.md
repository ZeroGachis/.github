# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.34.2](https://github.com/ZeroGachis/.github/compare/v4.34.1...v4.34.2) (2024-08-19)


### Bug Fixes

* naming of template workflow ([40456ae](https://github.com/ZeroGachis/.github/commit/40456ae22ee50fae6417737b64ee8255c6e59c60))

## [4.34.1](https://github.com/ZeroGachis/.github/compare/v4.34.0...v4.34.1) (2024-08-19)


### Bug Fixes

* **template-workflow:** typo in extension file name ([81dbebd](https://github.com/ZeroGachis/.github/commit/81dbebdaf4233031b0f3909e58b16e4f3cc422c5))

## [4.34.0](https://github.com/ZeroGachis/.github/compare/v4.33.2...v4.34.0) (2024-08-19)


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
* add hadolint report to PR comment ([bbfaed3](https://github.com/ZeroGachis/.github/commit/bbfaed3c821c17a6fea02d1c60add86175f05709))
* add latest tag to ECR ([521b2a9](https://github.com/ZeroGachis/.github/commit/521b2a986feba19f33d7b5dca6bb4ca1894ff10b))
* add python publish workflow ([1e67086](https://github.com/ZeroGachis/.github/commit/1e67086be915fed20e831e77427937367b68c4fc))
* add security scan image with Anchore ([1b8a4eb](https://github.com/ZeroGachis/.github/commit/1b8a4eb6d3eb7ac951cc5c2a1858f1bbe54bffd6))
* Allow passing a docker target ([ede6578](https://github.com/ZeroGachis/.github/commit/ede6578fd3095c6f14751d5735566d3dfb187f67))
* avoid some step in build apk in case of PR ([72168bd](https://github.com/ZeroGachis/.github/commit/72168bd41630ace4c42a4e08495036a80ff535bd))
* disable Vault usage on ECR Push image flow ([4585ef6](https://github.com/ZeroGachis/.github/commit/4585ef66dc97c5edd22cd7a8be518202b766426e))
* **infracost:** init workflow ([ded1355](https://github.com/ZeroGachis/.github/commit/ded13554cc449782e0d0fa23b06f557442e55257))
* **release-please:** add output var for release created or not ([7027d1a](https://github.com/ZeroGachis/.github/commit/7027d1ae5cd17d383f7f1fd3ea68e7df2e585025))
* **release-please:** customize config and manifest file ([4219510](https://github.com/ZeroGachis/.github/commit/42195101758e6e1e58dca3d3553539e6f822f68b))
* **release-please:** customize release type ([4977712](https://github.com/ZeroGachis/.github/commit/4977712faf0be5af6c035be341e4bcec0e8ad508))
* **release-please:** make conditionnal major and minor tags ([c51e46e](https://github.com/ZeroGachis/.github/commit/c51e46ee2c25dbcfb728f8bee04d1433bb4d76de))
* **terraform-infracost:** add tfvars to trigger infracost pipeline ([4c38180](https://github.com/ZeroGachis/.github/commit/4c38180864a721178aafdcbe32700bee0243fba5))
* **terraform:** login to github to use private module hosted in ouy org ([7566198](https://github.com/ZeroGachis/.github/commit/7566198a64a08777dcf118d4c8c7e1eb54f13eb5))
* **terraform:** use dynamic token github generation with vault ([e0d4c5b](https://github.com/ZeroGachis/.github/commit/e0d4c5b9d6922935a9160c7291c0624bfca7980c))


### feature

* handle multiple aws region ([17cf4bb](https://github.com/ZeroGachis/.github/commit/17cf4bb076d53e5ceea9441ef721a66a75d99860))


### Bug Fixes

* (release-please): wrong step order to use config file ([017b1fa](https://github.com/ZeroGachis/.github/commit/017b1fa2a101fe9fc51bc32035b56f1d3c7733a1))
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
* hadolint severity level and report trigger ([fa32491](https://github.com/ZeroGachis/.github/commit/fa32491c6a21590da840a2a78f332939efe27a52))
* increase delay and retry count ([950aca7](https://github.com/ZeroGachis/.github/commit/950aca7bd5379a53c5f5115f5bd8a957022be588))
* linter report file issue ([7cde3a6](https://github.com/ZeroGachis/.github/commit/7cde3a62ac86c6a8d85a2e25397e52ab860d7675))
* missing docker tag command ([b30b90e](https://github.com/ZeroGachis/.github/commit/b30b90e89dd0cb717fab4800941ebbab5d7fc986))
* **release-please:** creation of major tag condition ([bec703b](https://github.com/ZeroGachis/.github/commit/bec703bc3c1b2054f0bad4bd551530a12f541ee1))
* **release-please:** creation of major tag condition  2 ([e99f4b0](https://github.com/ZeroGachis/.github/commit/e99f4b00af4994597ca64025c0fc2905fdc71efd))
* **release-please:** creation of major tag condition  3 ([9f76492](https://github.com/ZeroGachis/.github/commit/9f764922c82f699f56ed11536dc362fe2e21c224))
* **release-please:** creation of major tag condition  4 ([601b27b](https://github.com/ZeroGachis/.github/commit/601b27b0ca1d9c8961b19ff3270d0633f89cbd5a))
* **release-please:** creation of major tag condition  5 ([58fd0e9](https://github.com/ZeroGachis/.github/commit/58fd0e9120fe5625be1c0f98040634c0595797cf))
* **release-please:** creation of major tag condition  6 ([526c641](https://github.com/ZeroGachis/.github/commit/526c641a15ccb8842fc3dbe0bb19100a62cd0b1f))
* **release-please:** don't set terraform_module by default ([6c68bf4](https://github.com/ZeroGachis/.github/commit/6c68bf4202b354a4e8c64eb212689dd9d74bdaf8))
* **release-please:** don't set terraform_module by default  part 2 ([bfad19d](https://github.com/ZeroGachis/.github/commit/bfad19dd7f220a51c06f70af6f8352d19a723ae0))
* **release-please:** fix boolean interpretation inside github workflow ([6e19306](https://github.com/ZeroGachis/.github/commit/6e193069d554deab6e33351de36697a4ac643245))
* **release-please:** fix boolean interpretation inside github workflow  2 ([a0cee5a](https://github.com/ZeroGachis/.github/commit/a0cee5a4497c376403fd19459a448684af4f09ca))
* **release-please:** fix boolean interpretation inside github workflow  3 ([1b2c126](https://github.com/ZeroGachis/.github/commit/1b2c12657be7a48e1e809d0ca1fbfc7df5e24653))
* **release-please:** manifest default filename ([3d8018b](https://github.com/ZeroGachis/.github/commit/3d8018be949f59908a13935bb1499eadae84bc41))
* set trigger for pr comment ([61333f3](https://github.com/ZeroGachis/.github/commit/61333f3024ebf43cbb1fe9275db2af92732cecc4))
* syntax issue on create apk artifact workflow ([9202fec](https://github.com/ZeroGachis/.github/commit/9202fec4959e58f50fb03c08c294f12571ad8016))
* Temporary fix BuildX version ([1e0af30](https://github.com/ZeroGachis/.github/commit/1e0af3040f856792874186caaa8978ae22f63fc0))
* **terrafom:** syntax issue when input/vault_secrets is not empty ([86268d8](https://github.com/ZeroGachis/.github/commit/86268d86189e4961011385147fb193f43901a90b))
* terraform workflows - duplicate bucket variable ([5234e47](https://github.com/ZeroGachis/.github/commit/5234e47bb8b14cab8024f53cc761a91bf8df3f18))
* **terraform:** condition for login to private github org ([9118e67](https://github.com/ZeroGachis/.github/commit/9118e67c2ae5b5004b6ea0842d0e293666c9cbf6))
* **terraform:** extra step ([b51c3f5](https://github.com/ZeroGachis/.github/commit/b51c3f5bf1063fb94e5950dda9708b8b84407f51))
* variabilize bucket for keystore ([755d585](https://github.com/ZeroGachis/.github/commit/755d585db531c42e76228e5c5c1ed92a0f4c867a))
* vault action retry to avoid dns issue ([47d2708](https://github.com/ZeroGachis/.github/commit/47d270860e70ceae773b37ecad8a80972779d969))
* vault url not required anymore ([0b47629](https://github.com/ZeroGachis/.github/commit/0b47629814c7656e0a23ddb93cf4a12f77df7722))
* vault url required 2 ([9d05375](https://github.com/ZeroGachis/.github/commit/9d05375d70c3c9058393c8b96a8f8f61ba9243c5))


### Miscellaneous Chores

* add Cache to APK build workflow ([e70ec7d](https://github.com/ZeroGachis/.github/commit/e70ec7dc43240cc21d1edab4acc22a045aba8d34))
* add capability to log to default ecr registry ([99c3b9a](https://github.com/ZeroGachis/.github/commit/99c3b9a7716a30b04a02cd26964ebf9f64c31149))
* add CODEOWNERS file ([7cc5646](https://github.com/ZeroGachis/.github/commit/7cc56468494192ee6bf551d21afa6f2c8a2be505))
* add env input to publish bundle workflow ([8ba08b0](https://github.com/ZeroGachis/.github/commit/8ba08b0f64c4fd269f5b0e7ffa19e9550575bba2))
* add env input to publish s3 workflow ([e7d4d3f](https://github.com/ZeroGachis/.github/commit/e7d4d3f6e0d2ff52ef19ec153dabcd469f5b1fde))
* Add renovate conf ([ba99a03](https://github.com/ZeroGachis/.github/commit/ba99a035d6009d948736823e93c39e88a5cff6b8))
* autorelease .github repo ([99a4b43](https://github.com/ZeroGachis/.github/commit/99a4b4398c97919ad4db1bf48b92c75e2ce5dd5a))
* **config:** migrate config renovate.json ([4e900fa](https://github.com/ZeroGachis/.github/commit/4e900fad3e150ccbda85a8ff5cdffa8eb1819f8c))
* **deps:** bump anchore/scan-action from 3 to 4 ([79cad7b](https://github.com/ZeroGachis/.github/commit/79cad7b5c68b36a602263b02512c6dbd1eace8ed))
* **deps:** bump aws-actions/aws-secretsmanager-get-secrets from 1 to 2 ([0393950](https://github.com/ZeroGachis/.github/commit/03939500b15e097064b06823575497eb47bee924))
* **deps:** bump docker/build-push-action from 5 to 6 ([6f96c62](https://github.com/ZeroGachis/.github/commit/6f96c62d01ca3876c4a3cb013370a4b9922248d9))
* **deps:** bump dorny/test-reporter from 1.8.0 to 1.9.0 ([d774e0e](https://github.com/ZeroGachis/.github/commit/d774e0eb61e277da8dc182a2c8f3702175243fdf))
* **deps:** bump dorny/test-reporter from 1.9.0 to 1.9.1 ([35d13ca](https://github.com/ZeroGachis/.github/commit/35d13ca3c9b5d1213493066d4f515dfb64492ea7))
* **deps:** bump gradle/wrapper-validation-action from 1 to 2 ([f59417c](https://github.com/ZeroGachis/.github/commit/f59417cd0c3a49820b59e3dd7a19faa0ca80b51d))
* **deps:** bump gradle/wrapper-validation-action from 2 to 3 ([3937ec8](https://github.com/ZeroGachis/.github/commit/3937ec84d0bf0a422e853777fb3b98c59d05355a))
* **deps:** bump softprops/action-gh-release from 1 to 2 ([13333b3](https://github.com/ZeroGachis/.github/commit/13333b38900272b4f0c9fae6d9df5a5ad5675da1))
* **deps:** update actions/github-script action to v7 ([6d449af](https://github.com/ZeroGachis/.github/commit/6d449afa1e62acb4f77a2c2274e5b71c41376f65))
* get last version of buildx ([fb5afc4](https://github.com/ZeroGachis/.github/commit/fb5afc4bc2c80e5ce94ca384488c8a567b280e5a))
* handle multiple regions for terraform backend and aws secrets default ([ebae53b](https://github.com/ZeroGachis/.github/commit/ebae53b26e58c558bd8ee675f0b5878bfdd5dd6e))
* increase sleep time for vault dns issue ([8ba01f1](https://github.com/ZeroGachis/.github/commit/8ba01f158e0fcc964f52835fa6d4c0ce86921e49))
* init catalog-info.yaml ([396111f](https://github.com/ZeroGachis/.github/commit/396111f19337d2f8aa275cb68781a9a5eb587bd3))
* **main:** release 4.25.0 ([f551ee6](https://github.com/ZeroGachis/.github/commit/f551ee6cecb3d7673c8f2ea7726db7ea3a73a612))
* **main:** release 4.26.0 ([2d9d817](https://github.com/ZeroGachis/.github/commit/2d9d8176fd8c4dadf3397fd2375d952b1fde627d))
* **main:** release 4.26.1 ([5320ec1](https://github.com/ZeroGachis/.github/commit/5320ec130c29154acd4f5d5c94ba47c93fe719ad))
* **main:** release 4.26.2 ([1314ea4](https://github.com/ZeroGachis/.github/commit/1314ea41aca18da9f06dbb3ad61e86887e634afd))
* **main:** release 4.27.0 ([5476192](https://github.com/ZeroGachis/.github/commit/5476192ff968730867379755070839b5331a2c21))
* **main:** release 4.27.1 ([898765e](https://github.com/ZeroGachis/.github/commit/898765e357ccda32d700f181ac0bf96636c43952))
* **main:** release 4.27.2 ([d31f7b4](https://github.com/ZeroGachis/.github/commit/d31f7b47990b35c6482d5e875345b6035adc7380))
* **main:** release 4.27.3 ([dcff331](https://github.com/ZeroGachis/.github/commit/dcff33197e35f26cc5715c17913182689dc06200))
* **main:** release 4.28.0 ([c729f17](https://github.com/ZeroGachis/.github/commit/c729f17fd42e645a61f4b2bf71ac4ee5f160a100))
* **main:** release 4.29.0 ([829ce38](https://github.com/ZeroGachis/.github/commit/829ce38c6a2cee1f57e3055476a5ea51dd463bc0))
* **main:** release 4.29.1 ([f74417f](https://github.com/ZeroGachis/.github/commit/f74417f9bf74455da7a3fa8637e9eb32be894e86))
* **main:** release 4.30.0 ([6055b74](https://github.com/ZeroGachis/.github/commit/6055b749a47627d2438a1b247ed734e3c955b314))
* **main:** release 4.31.0 ([42ae178](https://github.com/ZeroGachis/.github/commit/42ae178646fa53af27fe356de694f196bddb5158))
* **main:** release 4.31.1 ([48c3c52](https://github.com/ZeroGachis/.github/commit/48c3c5210528d3cf53b938368d15f87107a5f2e8))
* **main:** release 4.31.10 ([7e9387b](https://github.com/ZeroGachis/.github/commit/7e9387b0ade4bc375794d806f9953ac2bffe817f))
* **main:** release 4.31.2 ([a484213](https://github.com/ZeroGachis/.github/commit/a484213271507cd11059684a77c40e05d6899907))
* **main:** release 4.31.3 ([7e9ce0f](https://github.com/ZeroGachis/.github/commit/7e9ce0f7bf075d96c8973382ac975013b4bd37cd))
* **main:** release 4.31.4 ([c014951](https://github.com/ZeroGachis/.github/commit/c01495163ae89d95f824aaabb0c2a63c54ad1461))
* **main:** release 4.31.5 ([3f0775e](https://github.com/ZeroGachis/.github/commit/3f0775ecd5ab7b9b69854f27367df7de0319cad5))
* **main:** release 4.31.6 ([fc808d0](https://github.com/ZeroGachis/.github/commit/fc808d0221becc4922049fb339892ef0edaa765f))
* **main:** release 4.31.7 ([a45f123](https://github.com/ZeroGachis/.github/commit/a45f123cef20741e4ee7ea650fa2df156d20c688))
* **main:** release 4.31.8 ([1a5d4e4](https://github.com/ZeroGachis/.github/commit/1a5d4e4d61eca5ff24bebaae30b1644cd9324b3c))
* **main:** release 4.31.9 ([ac5f645](https://github.com/ZeroGachis/.github/commit/ac5f64500c615e3b5f8c9ecb7621e3226805ba82))
* **main:** release 4.32.0 ([428bc5e](https://github.com/ZeroGachis/.github/commit/428bc5ea27c63ae8cdd5fb9df84d293a1e8dd5f7))
* **main:** release 4.33.0 ([373f802](https://github.com/ZeroGachis/.github/commit/373f802dc3323a08b8d7106a24b56cb3d0e253c6))
* **main:** release 4.33.1 ([2454c71](https://github.com/ZeroGachis/.github/commit/2454c7191dad250fa263a7798139a3b1e1104014))
* **main:** release 4.33.2 ([9d47a90](https://github.com/ZeroGachis/.github/commit/9d47a906bd70df90daf1f75ffb92da65ed420e8b))
* migrate Release system to ReleasePlease ([473dd97](https://github.com/ZeroGachis/.github/commit/473dd97c1a446a82bcdb97b79e0e3b15b22c2ab0))
* only display failed tests ([16150ba](https://github.com/ZeroGachis/.github/commit/16150ba2402445be8d376aa1bff54334735471a3))
* remove dependabot conf ([c8da77f](https://github.com/ZeroGachis/.github/commit/c8da77ffd320e7d0114a00ad18bac762c013ccbc))
* rename create apk workflow ([13372b1](https://github.com/ZeroGachis/.github/commit/13372b15dd675fd936a472f16287ecaf82ecddcc))
* terraform - add aditional_aws_secrets ([e746c7a](https://github.com/ZeroGachis/.github/commit/e746c7adf5fd9ab9b15cbf4ff1e30419d8eccb3d))
* Update CI smartapp to respect distributed arch ([b4a7685](https://github.com/ZeroGachis/.github/commit/b4a76851d8a33609c10f0a80c5f90be29cc29584))
* update CODEOWNERS ([24501b8](https://github.com/ZeroGachis/.github/commit/24501b80390e41fb26094cce4b820bcddf9601f9))
* update CODEOWNERS file ([114da92](https://github.com/ZeroGachis/.github/commit/114da926f793944de7cf2ca57dac308782e94032))
* update name of containerstructure test workflow ([b51ba82](https://github.com/ZeroGachis/.github/commit/b51ba82ca5701462ec8ec1c0c5efaa9f18f706f6))
* update release please conf ([93235c4](https://github.com/ZeroGachis/.github/commit/93235c41d176b2b1549230b89667445f3aad07e1))
* update test-reporter action ([ec8c133](https://github.com/ZeroGachis/.github/commit/ec8c13334765f85173b4384493838dbc33292da3))
* update vault action to avoid EAI_ADDR issue ([783be2b](https://github.com/ZeroGachis/.github/commit/783be2b8a38cc3d4d0c1c7c5a07302a7df639c0e))
* Upgrade postgresql image from 12 to 16 ([feafa1f](https://github.com/ZeroGachis/.github/commit/feafa1f12a412a6bfaffa4eb5f95fbb3d5c22b55))
* Upgrade upload-artifact action to v4 ([74d561a](https://github.com/ZeroGachis/.github/commit/74d561a6c4007cf9b87b2a8c79cf02f107ebc9d1))
* Upgrade Vault to V3 ([4a51184](https://github.com/ZeroGachis/.github/commit/4a5118486eaf8d8ed0cb5d61fbbce42005d3938a))

## [4.33.2](https://github.com/ZeroGachis/.github/compare/v4.33.1...v4.33.2) (2024-08-14)


### Bug Fixes

* hadolint severity level and report trigger ([fa32491](https://github.com/ZeroGachis/.github/commit/fa32491c6a21590da840a2a78f332939efe27a52))

## [4.33.1](https://github.com/ZeroGachis/.github/compare/v4.33.0...v4.33.1) (2024-08-14)


### Bug Fixes

* set trigger for pr comment ([61333f3](https://github.com/ZeroGachis/.github/commit/61333f3024ebf43cbb1fe9275db2af92732cecc4))

## [4.33.0](https://github.com/ZeroGachis/.github/compare/v4.32.0...v4.33.0) (2024-08-14)


### Features

* add hadolint report to PR comment ([bbfaed3](https://github.com/ZeroGachis/.github/commit/bbfaed3c821c17a6fea02d1c60add86175f05709))

## [4.32.0](https://github.com/ZeroGachis/.github/compare/v4.31.10...v4.32.0) (2024-08-07)


### Features

* **release-please:** add output var for release created or not ([7027d1a](https://github.com/ZeroGachis/.github/commit/7027d1ae5cd17d383f7f1fd3ea68e7df2e585025))

## [4.31.10](https://github.com/ZeroGachis/.github/compare/v4.31.9...v4.31.10) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition  6 ([526c641](https://github.com/ZeroGachis/.github/commit/526c641a15ccb8842fc3dbe0bb19100a62cd0b1f))

## [4.31.9](https://github.com/ZeroGachis/.github/compare/v4.31.8...v4.31.9) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition  5 ([58fd0e9](https://github.com/ZeroGachis/.github/commit/58fd0e9120fe5625be1c0f98040634c0595797cf))

## [4.31.8](https://github.com/ZeroGachis/.github/compare/v4.31.7...v4.31.8) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition  4 ([601b27b](https://github.com/ZeroGachis/.github/commit/601b27b0ca1d9c8961b19ff3270d0633f89cbd5a))

## [4.31.7](https://github.com/ZeroGachis/.github/compare/v4.31.6...v4.31.7) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition  3 ([9f76492](https://github.com/ZeroGachis/.github/commit/9f764922c82f699f56ed11536dc362fe2e21c224))

## [4.31.6](https://github.com/ZeroGachis/.github/compare/v4.31.5...v4.31.6) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition  2 ([e99f4b0](https://github.com/ZeroGachis/.github/commit/e99f4b00af4994597ca64025c0fc2905fdc71efd))

## [4.31.5](https://github.com/ZeroGachis/.github/compare/v4.31.4...v4.31.5) (2024-08-07)


### Bug Fixes

* **release-please:** creation of major tag condition ([bec703b](https://github.com/ZeroGachis/.github/commit/bec703bc3c1b2054f0bad4bd551530a12f541ee1))


### Miscellaneous Chores

* update release please conf ([93235c4](https://github.com/ZeroGachis/.github/commit/93235c41d176b2b1549230b89667445f3aad07e1))

## 4.31.4 (2024-08-07)

**Full Changelog**: https://github.com/ZeroGachis/.github/compare/v4.31.3...v4.31.4

## 4.31.3 (2024-08-07)

**Full Changelog**: https://github.com/ZeroGachis/.github/compare/v4.31.2...v4.31.3

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
