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

## [1.5.0] - 2022-12-16

### Added
- Push on Pypi repository with poetry workflow
