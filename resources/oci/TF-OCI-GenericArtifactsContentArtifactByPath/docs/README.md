# TF::OCI::GenericArtifactsContentArtifactByPath

Provides the Artifact By Path resource in Oracle Cloud Infrastructure Generic Artifacts Content service. This resource supports upload/download the content of a generic artifact by specifying the repository id, artifact path, and artifact version

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::GenericArtifactsContentArtifactByPath",
    "Properties" : {
        "<a href="#artifactpath" title="ArtifactPath">ArtifactPath</a>" : <i>String</i>,
        "<a href="#content" title="Content">Content</a>" : <i>String</i>,
        "<a href="#repositoryid" title="RepositoryId">RepositoryId</a>" : <i>String</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::GenericArtifactsContentArtifactByPath
Properties:
    <a href="#artifactpath" title="ArtifactPath">ArtifactPath</a>: <i>String</i>
    <a href="#content" title="Content">Content</a>: <i>String</i>
    <a href="#repositoryid" title="RepositoryId">RepositoryId</a>: <i>String</i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ArtifactPath

A user-defined path to describe the location of an artifact. You can use slashes to organize the repository, but slashes do not create a directory structure. An artifact path does not include an artifact version.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Content

The content of the artifact.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepositoryId

The [OCID](/iaas/Content/General/Concepts/identifiers.htm) of the repository.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

A user-defined string to describe the artifact version. Example: `1.1.0` or `1.2-beta-2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ArtifactId

Returns the <code>ArtifactId</code> value.

#### CompartmentId

Returns the <code>CompartmentId</code> value.

#### DefinedTags

Returns the <code>DefinedTags</code> value.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### FreeformTags

Returns the <code>FreeformTags</code> value.

#### Id

Returns the <code>Id</code> value.

#### Sha256

Returns the <code>Sha256</code> value.

#### SizeInBytes

Returns the <code>SizeInBytes</code> value.

#### State

Returns the <code>State</code> value.

#### TimeCreated

Returns the <code>TimeCreated</code> value.

