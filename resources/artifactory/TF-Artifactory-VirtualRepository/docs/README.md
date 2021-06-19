# TF::Artifactory::VirtualRepository

CloudFormation equivalent of artifactory_virtual_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::VirtualRepository",
    "Properties" : {
        "<a href="#artifactoryrequestscanretrieveremoteartifacts" title="ArtifactoryRequestsCanRetrieveRemoteArtifacts">ArtifactoryRequestsCanRetrieveRemoteArtifacts</a>" : <i>Boolean</i>,
        "<a href="#debiantriviallayout" title="DebianTrivialLayout">DebianTrivialLayout</a>" : <i>Boolean</i>,
        "<a href="#defaultdeploymentrepo" title="DefaultDeploymentRepo">DefaultDeploymentRepo</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>" : <i>String</i>,
        "<a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>" : <i>Boolean</i>,
        "<a href="#includespattern" title="IncludesPattern">IncludesPattern</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#keypair" title="KeyPair">KeyPair</a>" : <i>String</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#pomrepositoryreferencescleanuppolicy" title="PomRepositoryReferencesCleanupPolicy">PomRepositoryReferencesCleanupPolicy</a>" : <i>String</i>,
        "<a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>" : <i>String</i>,
        "<a href="#repositories" title="Repositories">Repositories</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::VirtualRepository
Properties:
    <a href="#artifactoryrequestscanretrieveremoteartifacts" title="ArtifactoryRequestsCanRetrieveRemoteArtifacts">ArtifactoryRequestsCanRetrieveRemoteArtifacts</a>: <i>Boolean</i>
    <a href="#debiantriviallayout" title="DebianTrivialLayout">DebianTrivialLayout</a>: <i>Boolean</i>
    <a href="#defaultdeploymentrepo" title="DefaultDeploymentRepo">DefaultDeploymentRepo</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>: <i>String</i>
    <a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>: <i>Boolean</i>
    <a href="#includespattern" title="IncludesPattern">IncludesPattern</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#keypair" title="KeyPair">KeyPair</a>: <i>String</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#pomrepositoryreferencescleanuppolicy" title="PomRepositoryReferencesCleanupPolicy">PomRepositoryReferencesCleanupPolicy</a>: <i>String</i>
    <a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>: <i>String</i>
    <a href="#repositories" title="Repositories">Repositories</a>: <i>
      - String</i>
</pre>

## Properties

#### ArtifactoryRequestsCanRetrieveRemoteArtifacts

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebianTrivialLayout

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultDeploymentRepo

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludesPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceNugetAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IncludesPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeyPair

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PomRepositoryReferencesCleanupPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoLayoutRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Repositories

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

