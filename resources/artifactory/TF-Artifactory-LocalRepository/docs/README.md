# TF::Artifactory::LocalRepository

CloudFormation equivalent of artifactory_local_repository

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Artifactory::LocalRepository",
    "Properties" : {
        "<a href="#archivebrowsingenabled" title="ArchiveBrowsingEnabled">ArchiveBrowsingEnabled</a>" : <i>Boolean</i>,
        "<a href="#blackedout" title="BlackedOut">BlackedOut</a>" : <i>Boolean</i>,
        "<a href="#calculateyummetadata" title="CalculateYumMetadata">CalculateYumMetadata</a>" : <i>Boolean</i>,
        "<a href="#checksumpolicytype" title="ChecksumPolicyType">ChecksumPolicyType</a>" : <i>String</i>,
        "<a href="#debiantriviallayout" title="DebianTrivialLayout">DebianTrivialLayout</a>" : <i>Boolean</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dockerapiversion" title="DockerApiVersion">DockerApiVersion</a>" : <i>String</i>,
        "<a href="#enablefilelistsindexing" title="EnableFileListsIndexing">EnableFileListsIndexing</a>" : <i>Boolean</i>,
        "<a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>" : <i>String</i>,
        "<a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>" : <i>Boolean</i>,
        "<a href="#handlereleases" title="HandleReleases">HandleReleases</a>" : <i>Boolean</i>,
        "<a href="#handlesnapshots" title="HandleSnapshots">HandleSnapshots</a>" : <i>Boolean</i>,
        "<a href="#includespattern" title="IncludesPattern">IncludesPattern</a>" : <i>String</i>,
        "<a href="#key" title="Key">Key</a>" : <i>String</i>,
        "<a href="#maxuniquesnapshots" title="MaxUniqueSnapshots">MaxUniqueSnapshots</a>" : <i>Double</i>,
        "<a href="#maxuniquetags" title="MaxUniqueTags">MaxUniqueTags</a>" : <i>Double</i>,
        "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
        "<a href="#packagetype" title="PackageType">PackageType</a>" : <i>String</i>,
        "<a href="#propertysets" title="PropertySets">PropertySets</a>" : <i>[ String, ... ]</i>,
        "<a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>" : <i>String</i>,
        "<a href="#snapshotversionbehavior" title="SnapshotVersionBehavior">SnapshotVersionBehavior</a>" : <i>String</i>,
        "<a href="#suppresspomconsistencychecks" title="SuppressPomConsistencyChecks">SuppressPomConsistencyChecks</a>" : <i>Boolean</i>,
        "<a href="#xrayindex" title="XrayIndex">XrayIndex</a>" : <i>Boolean</i>,
        "<a href="#yumrootdepth" title="YumRootDepth">YumRootDepth</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Artifactory::LocalRepository
Properties:
    <a href="#archivebrowsingenabled" title="ArchiveBrowsingEnabled">ArchiveBrowsingEnabled</a>: <i>Boolean</i>
    <a href="#blackedout" title="BlackedOut">BlackedOut</a>: <i>Boolean</i>
    <a href="#calculateyummetadata" title="CalculateYumMetadata">CalculateYumMetadata</a>: <i>Boolean</i>
    <a href="#checksumpolicytype" title="ChecksumPolicyType">ChecksumPolicyType</a>: <i>String</i>
    <a href="#debiantriviallayout" title="DebianTrivialLayout">DebianTrivialLayout</a>: <i>Boolean</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dockerapiversion" title="DockerApiVersion">DockerApiVersion</a>: <i>String</i>
    <a href="#enablefilelistsindexing" title="EnableFileListsIndexing">EnableFileListsIndexing</a>: <i>Boolean</i>
    <a href="#excludespattern" title="ExcludesPattern">ExcludesPattern</a>: <i>String</i>
    <a href="#forcenugetauthentication" title="ForceNugetAuthentication">ForceNugetAuthentication</a>: <i>Boolean</i>
    <a href="#handlereleases" title="HandleReleases">HandleReleases</a>: <i>Boolean</i>
    <a href="#handlesnapshots" title="HandleSnapshots">HandleSnapshots</a>: <i>Boolean</i>
    <a href="#includespattern" title="IncludesPattern">IncludesPattern</a>: <i>String</i>
    <a href="#key" title="Key">Key</a>: <i>String</i>
    <a href="#maxuniquesnapshots" title="MaxUniqueSnapshots">MaxUniqueSnapshots</a>: <i>Double</i>
    <a href="#maxuniquetags" title="MaxUniqueTags">MaxUniqueTags</a>: <i>Double</i>
    <a href="#notes" title="Notes">Notes</a>: <i>String</i>
    <a href="#packagetype" title="PackageType">PackageType</a>: <i>String</i>
    <a href="#propertysets" title="PropertySets">PropertySets</a>: <i>
      - String</i>
    <a href="#repolayoutref" title="RepoLayoutRef">RepoLayoutRef</a>: <i>String</i>
    <a href="#snapshotversionbehavior" title="SnapshotVersionBehavior">SnapshotVersionBehavior</a>: <i>String</i>
    <a href="#suppresspomconsistencychecks" title="SuppressPomConsistencyChecks">SuppressPomConsistencyChecks</a>: <i>Boolean</i>
    <a href="#xrayindex" title="XrayIndex">XrayIndex</a>: <i>Boolean</i>
    <a href="#yumrootdepth" title="YumRootDepth">YumRootDepth</a>: <i>Double</i>
</pre>

## Properties

#### ArchiveBrowsingEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlackedOut

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CalculateYumMetadata

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChecksumPolicyType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DebianTrivialLayout

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DockerApiVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableFileListsIndexing

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludesPattern

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceNugetAuthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandleReleases

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HandleSnapshots

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

#### MaxUniqueSnapshots

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxUniqueTags

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PackageType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PropertySets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RepoLayoutRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnapshotVersionBehavior

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SuppressPomConsistencyChecks

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XrayIndex

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YumRootDepth

_Required_: No

_Type_: Double

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

