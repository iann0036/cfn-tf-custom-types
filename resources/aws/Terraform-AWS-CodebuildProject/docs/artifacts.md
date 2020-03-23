# Terraform::AWS::CodebuildProject Artifacts

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#artifactidentifier" title="ArtifactIdentifier">ArtifactIdentifier</a>" : <i>String</i>,
    "<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>" : <i>Boolean</i>,
    "<a href="#location" title="Location">Location</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#namespacetype" title="NamespaceType">NamespaceType</a>" : <i>String</i>,
    "<a href="#overrideartifactname" title="OverrideArtifactName">OverrideArtifactName</a>" : <i>Boolean</i>,
    "<a href="#packaging" title="Packaging">Packaging</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#artifactidentifier" title="ArtifactIdentifier">ArtifactIdentifier</a>: <i>String</i>
<a href="#encryptiondisabled" title="EncryptionDisabled">EncryptionDisabled</a>: <i>Boolean</i>
<a href="#location" title="Location">Location</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#namespacetype" title="NamespaceType">NamespaceType</a>: <i>String</i>
<a href="#overrideartifactname" title="OverrideArtifactName">OverrideArtifactName</a>: <i>Boolean</i>
<a href="#packaging" title="Packaging">Packaging</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>String</i>
</pre>

## Properties

#### ArtifactIdentifier

The artifact identifier. Must be the same specified inside AWS CodeBuild buildspec.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionDisabled

If set to true, output artifacts will not be encrypted. If `type` is set to `NO_ARTIFACTS` then this value will be ignored. Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

Information about the build output artifact location. If `type` is set to `CODEPIPELINE` or `NO_ARTIFACTS` then this value will be ignored. If `type` is set to `S3`, this is the name of the output bucket.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the project. If `type` is set to `S3`, this is the name of the output artifact object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceType

The namespace to use in storing build artifacts. If `type` is set to `S3`, then valid values for this parameter are: `BUILD_ID` or `NONE`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OverrideArtifactName

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Packaging

The type of build output artifact to create. If `type` is set to `S3`, valid values for this parameter are: `NONE` or `ZIP`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

If `type` is set to `S3`, this is the path to the output artifact.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The build output artifact's type. Valid values for this parameter are: `CODEPIPELINE`, `NO_ARTIFACTS` or `S3`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

