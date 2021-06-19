# TF::Intersight::HyperflexAppCatalog

A catalog for managing application settings for HyperFlex cluster configuration service.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::HyperflexAppCatalog",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#featurelimitexternal" title="FeatureLimitExternal">FeatureLimitExternal</a>" : <i>[ <a href="featurelimitexternaldefinition.md">FeatureLimitExternalDefinition</a>, ... ]</i>,
        "<a href="#featurelimitinternal" title="FeatureLimitInternal">FeatureLimitInternal</a>" : <i>[ <a href="featurelimitinternaldefinition.md">FeatureLimitInternalDefinition</a>, ... ]</i>,
        "<a href="#hxdpversions" title="HxdpVersions">HxdpVersions</a>" : <i>[ <a href="hxdpversionsdefinition.md">HxdpVersionsDefinition</a>, ... ]</i>,
        "<a href="#hyperflexcapabilityinfos" title="HyperflexCapabilityInfos">HyperflexCapabilityInfos</a>" : <i>[ <a href="hyperflexcapabilityinfosdefinition.md">HyperflexCapabilityInfosDefinition</a>, ... ]</i>,
        "<a href="#hyperflexsoftwarecompatibilityinfos" title="HyperflexSoftwareCompatibilityInfos">HyperflexSoftwareCompatibilityInfos</a>" : <i>[ <a href="hyperflexsoftwarecompatibilityinfosdefinition.md">HyperflexSoftwareCompatibilityInfosDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#nrversion" title="NrVersion">NrVersion</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#serverfirmwareversion" title="ServerFirmwareVersion">ServerFirmwareVersion</a>" : <i>[ <a href="serverfirmwareversiondefinition.md">ServerFirmwareVersionDefinition</a>, ... ]</i>,
        "<a href="#servermodel" title="ServerModel">ServerModel</a>" : <i>[ <a href="servermodeldefinition.md">ServerModelDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#softwaredistributions" title="SoftwareDistributions">SoftwareDistributions</a>" : <i>[ <a href="softwaredistributionsdefinition.md">SoftwareDistributionsDefinition</a>, ... ]</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::HyperflexAppCatalog
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#featurelimitexternal" title="FeatureLimitExternal">FeatureLimitExternal</a>: <i>
      - <a href="featurelimitexternaldefinition.md">FeatureLimitExternalDefinition</a></i>
    <a href="#featurelimitinternal" title="FeatureLimitInternal">FeatureLimitInternal</a>: <i>
      - <a href="featurelimitinternaldefinition.md">FeatureLimitInternalDefinition</a></i>
    <a href="#hxdpversions" title="HxdpVersions">HxdpVersions</a>: <i>
      - <a href="hxdpversionsdefinition.md">HxdpVersionsDefinition</a></i>
    <a href="#hyperflexcapabilityinfos" title="HyperflexCapabilityInfos">HyperflexCapabilityInfos</a>: <i>
      - <a href="hyperflexcapabilityinfosdefinition.md">HyperflexCapabilityInfosDefinition</a></i>
    <a href="#hyperflexsoftwarecompatibilityinfos" title="HyperflexSoftwareCompatibilityInfos">HyperflexSoftwareCompatibilityInfos</a>: <i>
      - <a href="hyperflexsoftwarecompatibilityinfosdefinition.md">HyperflexSoftwareCompatibilityInfosDefinition</a></i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#nrversion" title="NrVersion">NrVersion</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#serverfirmwareversion" title="ServerFirmwareVersion">ServerFirmwareVersion</a>: <i>
      - <a href="serverfirmwareversiondefinition.md">ServerFirmwareVersionDefinition</a></i>
    <a href="#servermodel" title="ServerModel">ServerModel</a>: <i>
      - <a href="servermodeldefinition.md">ServerModelDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#softwaredistributions" title="SoftwareDistributions">SoftwareDistributions</a>: <i>
      - <a href="softwaredistributionsdefinition.md">SoftwareDistributionsDefinition</a></i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
</pre>

## Properties

#### AccountMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdditionalProperties

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ancestors

_Required_: No

_Type_: List of <a href="ancestorsdefinition.md">AncestorsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureLimitExternal

_Required_: No

_Type_: List of <a href="featurelimitexternaldefinition.md">FeatureLimitExternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeatureLimitInternal

_Required_: No

_Type_: List of <a href="featurelimitinternaldefinition.md">FeatureLimitInternalDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HxdpVersions

_Required_: No

_Type_: List of <a href="hxdpversionsdefinition.md">HxdpVersionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HyperflexCapabilityInfos

_Required_: No

_Type_: List of <a href="hyperflexcapabilityinfosdefinition.md">HyperflexCapabilityInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HyperflexSoftwareCompatibilityInfos

_Required_: No

_Type_: List of <a href="hyperflexsoftwarecompatibilityinfosdefinition.md">HyperflexSoftwareCompatibilityInfosDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NrVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Owners

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Parent

_Required_: No

_Type_: List of <a href="parentdefinition.md">ParentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermissionResources

_Required_: No

_Type_: List of <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerFirmwareVersion

_Required_: No

_Type_: List of <a href="serverfirmwareversiondefinition.md">ServerFirmwareVersionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerModel

_Required_: No

_Type_: List of <a href="servermodeldefinition.md">ServerModelDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SoftwareDistributions

_Required_: No

_Type_: List of <a href="softwaredistributionsdefinition.md">SoftwareDistributionsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

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

