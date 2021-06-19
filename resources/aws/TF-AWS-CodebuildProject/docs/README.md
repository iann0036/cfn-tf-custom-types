# TF::AWS::CodebuildProject

Provides a CodeBuild Project resource. See also the [`aws_codebuild_webhook` resource](/docs/providers/aws/r/codebuild_webhook.html), which manages the webhook to the source (e.g. the "rebuild every time a code change is pushed" option in the CodeBuild web console).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::CodebuildProject",
    "Properties" : {
        "<a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>" : <i>Boolean</i>,
        "<a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>" : <i>Double</i>,
        "<a href="#concurrentbuildlimit" title="ConcurrentBuildLimit">ConcurrentBuildLimit</a>" : <i>Double</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>" : <i>Double</i>,
        "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
        "<a href="#sourceversion" title="SourceVersion">SourceVersion</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#artifacts" title="Artifacts">Artifacts</a>" : <i>[ <a href="artifactsdefinition.md">ArtifactsDefinition</a>, ... ]</i>,
        "<a href="#buildbatchconfig" title="BuildBatchConfig">BuildBatchConfig</a>" : <i>[ <a href="buildbatchconfigdefinition.md">BuildBatchConfigDefinition</a>, ... ]</i>,
        "<a href="#cache" title="Cache">Cache</a>" : <i>[ <a href="cachedefinition.md">CacheDefinition</a>, ... ]</i>,
        "<a href="#environment" title="Environment">Environment</a>" : <i>[ <a href="environmentdefinition.md">EnvironmentDefinition</a>, ... ]</i>,
        "<a href="#filesystemlocations" title="FileSystemLocations">FileSystemLocations</a>" : <i>[ <a href="filesystemlocationsdefinition.md">FileSystemLocationsDefinition</a>, ... ]</i>,
        "<a href="#logsconfig" title="LogsConfig">LogsConfig</a>" : <i>[ <a href="logsconfigdefinition.md">LogsConfigDefinition</a>, ... ]</i>,
        "<a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>" : <i>[ <a href="secondaryartifactsdefinition.md">SecondaryArtifactsDefinition</a>, ... ]</i>,
        "<a href="#secondarysources" title="SecondarySources">SecondarySources</a>" : <i>[ <a href="secondarysourcesdefinition.md">SecondarySourcesDefinition</a>, ... ]</i>,
        "<a href="#source" title="Source">Source</a>" : <i>[ <a href="sourcedefinition.md">SourceDefinition</a>, ... ]</i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ <a href="vpcconfigdefinition.md">VpcConfigDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::CodebuildProject
Properties:
    <a href="#badgeenabled" title="BadgeEnabled">BadgeEnabled</a>: <i>Boolean</i>
    <a href="#buildtimeout" title="BuildTimeout">BuildTimeout</a>: <i>Double</i>
    <a href="#concurrentbuildlimit" title="ConcurrentBuildLimit">ConcurrentBuildLimit</a>: <i>Double</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#encryptionkey" title="EncryptionKey">EncryptionKey</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#queuedtimeout" title="QueuedTimeout">QueuedTimeout</a>: <i>Double</i>
    <a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
    <a href="#sourceversion" title="SourceVersion">SourceVersion</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#artifacts" title="Artifacts">Artifacts</a>: <i>
      - <a href="artifactsdefinition.md">ArtifactsDefinition</a></i>
    <a href="#buildbatchconfig" title="BuildBatchConfig">BuildBatchConfig</a>: <i>
      - <a href="buildbatchconfigdefinition.md">BuildBatchConfigDefinition</a></i>
    <a href="#cache" title="Cache">Cache</a>: <i>
      - <a href="cachedefinition.md">CacheDefinition</a></i>
    <a href="#environment" title="Environment">Environment</a>: <i>
      - <a href="environmentdefinition.md">EnvironmentDefinition</a></i>
    <a href="#filesystemlocations" title="FileSystemLocations">FileSystemLocations</a>: <i>
      - <a href="filesystemlocationsdefinition.md">FileSystemLocationsDefinition</a></i>
    <a href="#logsconfig" title="LogsConfig">LogsConfig</a>: <i>
      - <a href="logsconfigdefinition.md">LogsConfigDefinition</a></i>
    <a href="#secondaryartifacts" title="SecondaryArtifacts">SecondaryArtifacts</a>: <i>
      - <a href="secondaryartifactsdefinition.md">SecondaryArtifactsDefinition</a></i>
    <a href="#secondarysources" title="SecondarySources">SecondarySources</a>: <i>
      - <a href="secondarysourcesdefinition.md">SecondarySourcesDefinition</a></i>
    <a href="#source" title="Source">Source</a>: <i>
      - <a href="sourcedefinition.md">SourceDefinition</a></i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - <a href="vpcconfigdefinition.md">VpcConfigDefinition</a></i>
</pre>

## Properties

#### BadgeEnabled

Generates a publicly-accessible URL for the projects build badge. Available as `badge_url` attribute when enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildTimeout

Number of minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConcurrentBuildLimit

Specify a maximum number of concurrent builds for the project. The value specified must be greater than 0 and less than the account concurrent running builds limit.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

Short description of the project.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKey

AWS Key Management Service (AWS KMS) customer master key (CMK) to be used for encrypting the build project's build output artifacts.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Project's name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### QueuedTimeout

Number of minutes, from 5 to 480 (8 hours), a build is allowed to be queued before it times out. The default is 8 hours.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceVersion

Version of the build input to be built for this project. If not specified, the latest version is used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Map of tags to assign to the resource. If configured with a provider [`default_tags` configuration block](/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Artifacts

_Required_: No

_Type_: List of <a href="artifactsdefinition.md">ArtifactsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BuildBatchConfig

_Required_: No

_Type_: List of <a href="buildbatchconfigdefinition.md">BuildBatchConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cache

_Required_: No

_Type_: List of <a href="cachedefinition.md">CacheDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Environment

_Required_: No

_Type_: List of <a href="environmentdefinition.md">EnvironmentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileSystemLocations

_Required_: No

_Type_: List of <a href="filesystemlocationsdefinition.md">FileSystemLocationsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogsConfig

_Required_: No

_Type_: List of <a href="logsconfigdefinition.md">LogsConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondaryArtifacts

_Required_: No

_Type_: List of <a href="secondaryartifactsdefinition.md">SecondaryArtifactsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecondarySources

_Required_: No

_Type_: List of <a href="secondarysourcesdefinition.md">SecondarySourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Source

_Required_: No

_Type_: List of <a href="sourcedefinition.md">SourceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of <a href="vpcconfigdefinition.md">VpcConfigDefinition</a>

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

