# Terraform::AWS::CodebuildProject

Provides a CodeBuild Project resource. See also the [`aws_codebuild_webhook` resource](/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodebuildProject",
    "Properties" : {
        "<a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>" : <i>Boolean</i>,
        "<a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>" : <i>Double</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#sourceversion" title="SourceVersion">SourceVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#artifacts" title="Artifacts">Artifacts</a>" : <i>[ <a href="artifacts.md">Artifacts</a>, ... ]</i>,
        "<a href="#cache" title="Cache">Cache</a>" : <i>[ <a href="cache.md">Cache</a>, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environment.md">Environment</a>, ... ]</i>,
        "<a href="#logsconfig" title="LogsConfig">LogsConfig</a>" : <i>[ <a href="logsconfig.md">LogsConfig</a>, ... ]</i>,
        "<a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>" : <i>[ <a href="secondaryartifacts.md">SecondaryArtifacts</a>, ... ]</i>,
        "<a href="#secondarysources" title="SecondarySources">SecondarySources</a>" : <i>[ <a href="secondarysources.md">SecondarySources</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="source.md">Source</a>, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ <a href="vpcconfig.md">VpcConfig</a>, ... ]</i>,
        "<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>" : <i>[ <a href="environmentvariable.md">EnvironmentVariable</a>, ... ]</i>,
        "<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>" : <i>[ <a href="registrycredential.md">RegistryCredential</a>, ... ]</i>,
        "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ <a href="cloudwatchlogs.md">CloudwatchLogs</a>, ... ]</i>,
        "<a href="#s3logs" title="S3Logs">S3Logs</a>" : <i>[ <a href="s3logs.md">S3Logs</a>, ... ]</i>,
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ <a href="auth.md">Auth</a>, ... ]</i>,
        "<a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>" : <i>[ <a href="gitsubmodulesconfig.md">GitSubmodulesConfig</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodebuildProject
Properties:
    <a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>: <i>Boolean</i>
    <a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>: <i>Double</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#sourceversion" title="SourceVersion">SourceVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#artifacts" title="Artifacts">Artifacts</a>: <i>
      - <a href="artifacts.md">Artifacts</a></i>
    <a href="#cache" title="Cache">Cache</a>: <i>
      - <a href="cache.md">Cache</a></i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environment.md">Environment</a></i>
    <a href="#logsconfig" title="LogsConfig">LogsConfig</a>: <i>
      - <a href="logsconfig.md">LogsConfig</a></i>
    <a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>: <i>
      - <a href="secondaryartifacts.md">SecondaryArtifacts</a></i>
    <a href="#secondarysources" title="SecondarySources">SecondarySources</a>: <i>
      - <a href="secondarysources.md">SecondarySources</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="source.md">Source</a></i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - <a href="vpcconfig.md">VpcConfig</a></i>
    <a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>: <i>
      - <a href="environmentvariable.md">EnvironmentVariable</a></i>
    <a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>: <i>
      - <a href="registrycredential.md">RegistryCredential</a></i>
    <a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - <a href="cloudwatchlogs.md">CloudwatchLogs</a></i>
    <a href="#s3logs" title="S3Logs">S3Logs</a>: <i>
      - <a href="s3logs.md">S3Logs</a></i>
    <a href="#auth" title="Auth">Auth</a>: <i>
      - <a href="auth.md">Auth</a></i>
    <a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>: <i>
      - <a href="gitsubmodulesconfig.md">GitSubmodulesConfig</a></i>
</pre>

## Properties

#### BadgeEnabled

Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildTimeout

How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

A short description of the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

The AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The projects name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueuedTimeout

How long in minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVersion

A version of the build input to be built for this project. If not specified, the latest version is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Artifacts

_Required_: No

_Type_: List of <a href="artifacts.md">Artifacts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cache

_Required_: No

_Type_: List of <a href="cache.md">Cache</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="environment.md">Environment</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsConfig

_Required_: No

_Type_: List of <a href="logsconfig.md">LogsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryArtifacts

_Required_: No

_Type_: List of <a href="secondaryartifacts.md">SecondaryArtifacts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondarySources

_Required_: No

_Type_: List of <a href="secondarysources.md">SecondarySources</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="source.md">Source</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of <a href="vpcconfig.md">VpcConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariable

_Required_: No

_Type_: List of <a href="environmentvariable.md">EnvironmentVariable</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryCredential

_Required_: No

_Type_: List of <a href="registrycredential.md">RegistryCredential</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLogs

_Required_: No

_Type_: List of <a href="cloudwatchlogs.md">CloudwatchLogs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Logs

_Required_: No

_Type_: List of <a href="s3logs.md">S3Logs</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

_Required_: No

_Type_: List of <a href="auth.md">Auth</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitSubmodulesConfig

_Required_: No

_Type_: List of <a href="gitsubmodulesconfig.md">GitSubmodulesConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### BadgeUrl

Returns the <code>BadgeUrl</code> value.

#### Id

Returns the <code>Id</code> value.

