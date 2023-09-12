# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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