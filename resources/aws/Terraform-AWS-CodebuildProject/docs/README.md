# Terraform::AWS::CodebuildProject

CloudFormation equivalent of aws_codebuild_project

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::CodebuildProject",
    "Properties" : {
        "<a href="#tfcfnid" title="tfcfnid">tfcfnid</a>" : <i>String</i>,
        "<a href="#arn" title="Arn">Arn</a>" : <i>String</i>,
        "<a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>" : <i>Boolean</i>,
        "<a href="#badgeurl" title="BadgeUrl">BadgeUrl</a>" : <i>String</i>,
        "<a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>" : <i>Double</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#sourceversion" title="SourceVersion">SourceVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;, ... ]</i>,
        "<a href="#artifacts" title="Artifacts">Artifacts</a>" : <i>[ &lt;a href=&#34;artifacts.md&#34;&gt;Artifacts&lt;/a&gt;, ... ]</i>,
        "<a href="#cache" title="Cache">Cache</a>" : <i>[ &lt;a href=&#34;cache.md&#34;&gt;Cache&lt;/a&gt;, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;, ... ]</i>,
        "<a href="#logsconfig" title="LogsConfig">LogsConfig</a>" : <i>[ &lt;a href=&#34;logsconfig.md&#34;&gt;LogsConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>" : <i>[ &lt;a href=&#34;secondaryartifacts.md&#34;&gt;SecondaryArtifacts&lt;/a&gt;, ... ]</i>,
        "<a href="#secondarysources" title="SecondarySources">SecondarySources</a>" : <i>[ &lt;a href=&#34;secondarysources.md&#34;&gt;SecondarySources&lt;/a&gt;, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;, ... ]</i>,
        "<a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>" : <i>[ &lt;a href=&#34;environmentvariable.md&#34;&gt;EnvironmentVariable&lt;/a&gt;, ... ]</i>,
        "<a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>" : <i>[ &lt;a href=&#34;registrycredential.md&#34;&gt;RegistryCredential&lt;/a&gt;, ... ]</i>,
        "<a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>" : <i>[ &lt;a href=&#34;cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;, ... ]</i>,
        "<a href="#s3logs" title="S3Logs">S3Logs</a>" : <i>[ &lt;a href=&#34;s3logs.md&#34;&gt;S3Logs&lt;/a&gt;, ... ]</i>,
        "<a href="#auth" title="Auth">Auth</a>" : <i>[ &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;, ... ]</i>,
        "<a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>" : <i>[ &lt;a href=&#34;gitsubmodulesconfig.md&#34;&gt;GitSubmodulesConfig&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::CodebuildProject
Properties:
    <a href="#tfcfnid" title="tfcfnid">tfcfnid</a>: <i>String</i>
    <a href="#arn" title="Arn">Arn</a>: <i>String</i>
    <a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>: <i>Boolean</i>
    <a href="#badgeurl" title="BadgeUrl">BadgeUrl</a>: <i>String</i>
    <a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>: <i>Double</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#sourceversion" title="SourceVersion">SourceVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;</i>
    <a href="#artifacts" title="Artifacts">Artifacts</a>: <i>
      - &lt;a href=&#34;artifacts.md&#34;&gt;Artifacts&lt;/a&gt;</i>
    <a href="#cache" title="Cache">Cache</a>: <i>
      - &lt;a href=&#34;cache.md&#34;&gt;Cache&lt;/a&gt;</i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;</i>
    <a href="#logsconfig" title="LogsConfig">LogsConfig</a>: <i>
      - &lt;a href=&#34;logsconfig.md&#34;&gt;LogsConfig&lt;/a&gt;</i>
    <a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>: <i>
      - &lt;a href=&#34;secondaryartifacts.md&#34;&gt;SecondaryArtifacts&lt;/a&gt;</i>
    <a href="#secondarysources" title="SecondarySources">SecondarySources</a>: <i>
      - &lt;a href=&#34;secondarysources.md&#34;&gt;SecondarySources&lt;/a&gt;</i>
    <a href="#source" title="Source">Source</a>: <i>
      - &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;</i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;</i>
    <a href="#environmentvariable" title="EnvironmentVariable">EnvironmentVariable</a>: <i>
      - &lt;a href=&#34;environmentvariable.md&#34;&gt;EnvironmentVariable&lt;/a&gt;</i>
    <a href="#registrycredential" title="RegistryCredential">RegistryCredential</a>: <i>
      - &lt;a href=&#34;registrycredential.md&#34;&gt;RegistryCredential&lt;/a&gt;</i>
    <a href="#cloudwatchlogs" title="CloudwatchLogs">CloudwatchLogs</a>: <i>
      - &lt;a href=&#34;cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;</i>
    <a href="#s3logs" title="S3Logs">S3Logs</a>: <i>
      - &lt;a href=&#34;s3logs.md&#34;&gt;S3Logs&lt;/a&gt;</i>
    <a href="#auth" title="Auth">Auth</a>: <i>
      - &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;</i>
    <a href="#gitsubmodulesconfig" title="GitSubmodulesConfig">GitSubmodulesConfig</a>: <i>
      - &lt;a href=&#34;gitsubmodulesconfig.md&#34;&gt;GitSubmodulesConfig&lt;/a&gt;</i>
</pre>

## Properties

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Arn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BadgeEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BadgeUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueuedTimeout

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of &lt;a href=&#34;tags.md&#34;&gt;Tags&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Artifacts

_Required_: No

_Type_: List of &lt;a href=&#34;artifacts.md&#34;&gt;Artifacts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cache

_Required_: No

_Type_: List of &lt;a href=&#34;cache.md&#34;&gt;Cache&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of &lt;a href=&#34;environment.md&#34;&gt;Environment&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsConfig

_Required_: No

_Type_: List of &lt;a href=&#34;logsconfig.md&#34;&gt;LogsConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryArtifacts

_Required_: No

_Type_: List of &lt;a href=&#34;secondaryartifacts.md&#34;&gt;SecondaryArtifacts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondarySources

_Required_: No

_Type_: List of &lt;a href=&#34;secondarysources.md&#34;&gt;SecondarySources&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of &lt;a href=&#34;source.md&#34;&gt;Source&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of &lt;a href=&#34;vpcconfig.md&#34;&gt;VpcConfig&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnvironmentVariable

_Required_: No

_Type_: List of &lt;a href=&#34;environmentvariable.md&#34;&gt;EnvironmentVariable&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryCredential

_Required_: No

_Type_: List of &lt;a href=&#34;registrycredential.md&#34;&gt;RegistryCredential&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudwatchLogs

_Required_: No

_Type_: List of &lt;a href=&#34;cloudwatchlogs.md&#34;&gt;CloudwatchLogs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Logs

_Required_: No

_Type_: List of &lt;a href=&#34;s3logs.md&#34;&gt;S3Logs&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Auth

_Required_: No

_Type_: List of &lt;a href=&#34;auth.md&#34;&gt;Auth&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GitSubmodulesConfig

_Required_: No

_Type_: List of &lt;a href=&#34;gitsubmodulesconfig.md&#34;&gt;GitSubmodulesConfig&lt;/a&gt;

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### BadgeUrl

Returns the &lt;code&gt;BadgeUrl&lt;/code&gt; value.

