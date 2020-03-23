# Terraform::AWS::CodebuildProject Environment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#computetype" title="ComputeType">ComputeType</a>" : <i>String</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#imagepullcredentialstype" title="ImagePullCredentialsType">ImagePullCredentialsType</a>" : <i>String</i>,
    "<a href="#privilegedmode" title="PrivilegedMode">PrivilegedMode</a>" : <i>Boolean</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>,
    "<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>" : <i>[ <a href="environment-environmentvariable.md">EnvironmentVariable</a>, ... ]</i>,
    "<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>" : <i>[ <a href="environment-registrycredential.md">RegistryCredential</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#computetype" title="ComputeType">ComputeType</a>: <i>String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#imagepullcredentialstype" title="ImagePullCredentialsType">ImagePullCredentialsType</a>: <i>String</i>
<a href="#privilegedmode" title="PrivilegedMode">PrivilegedMode</a>: <i>Boolean</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>: <i>
      - <a href="environment-environmentvariable.md">EnvironmentVariable</a></i>
<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>: <i>
      - <a href="environment-registrycredential.md">RegistryCredential</a></i>
</pre>

## Properties

#### Certificate

The ARN of the S3 bucket, path prefix and object key that contains the PEM-encoded certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ComputeType

Information about the compute resources the build project will use. Available values for this parameter are: `BUILD_GENERAL1_SMALL`, `BUILD_GENERAL1_MEDIUM`, `BUILD_GENERAL1_LARGE` or `BUILD_GENERAL1_2XLARGE`. `BUILD_GENERAL1_SMALL` is only valid if `type` is set to `LINUX_CONTAINER`. When `type` is set to `LINUX_GPU_CONTAINER`, `compute_type` need to be `BUILD_GENERAL1_LARGE`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

The Docker image to use for this build project. Valid values include [Docker images provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html) (e.g `aws/codebuild/standard:2.0`), [Docker Hub images](https://hub.docker.com/) (e.g. `hashicorp/terraform:latest`), and full Docker repository URIs such as those for ECR (e.g. `137112412989.dkr.ecr.us-west-2.amazonaws.com/amazonlinux:latest`).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ImagePullCredentialsType

The type of credentials AWS CodeBuild uses to pull images in your build. Available values for this parameter are `CODEBUILD` or `SERVICE_ROLE`. When you use a cross-account or private registry image, you must use SERVICE_ROLE credentials. When you use an AWS CodeBuild curated image, you must use CODEBUILD credentials. Default to `CODEBUILD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivilegedMode

If set to true, enables running the Docker daemon inside a Docker container. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The type of build environment to use for related builds. Available values are: `LINUX_CONTAINER`, `LINUX_GPU_CONTAINER`, `WINDOWS_CONTAINER` or `ARM_CONTAINER`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariable

_Required_: No

_Type_: List of <a href="environment-environmentvariable.md">EnvironmentVariable</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryCredential

_Required_: No

_Type_: List of <a href="environment-registrycredential.md">RegistryCredential</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

