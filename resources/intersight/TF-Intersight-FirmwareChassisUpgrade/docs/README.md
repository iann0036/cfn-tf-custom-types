# TF::Intersight::FirmwareChassisUpgrade

Firmware upgrade operation for chassis that downloads the image located at Cisco/appliance/user provided HTTP repository or uses the image from a network share and upgrade. Direct download is used for upgrade that uses the image from a Cisco repository or an appliance repository. Network share is used for upgrade that use the image from a network share from your data center.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::FirmwareChassisUpgrade",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#chassis" title="Chassis">Chassis</a>" : <i>[ <a href="chassisdefinition.md">ChassisDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#device" title="Device">Device</a>" : <i>[ <a href="devicedefinition.md">DeviceDefinition</a>, ... ]</i>,
        "<a href="#directdownload" title="DirectDownload">DirectDownload</a>" : <i>[ <a href="directdownloaddefinition2.md">DirectDownloadDefinition2</a>, ... ]</i>,
        "<a href="#distributable" title="Distributable">Distributable</a>" : <i>[ <a href="distributabledefinition.md">DistributableDefinition</a>, ... ]</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#excludecomponentlist" title="ExcludeComponentList">ExcludeComponentList</a>" : <i>[ String, ... ]</i>,
        "<a href="#fileserver" title="FileServer">FileServer</a>" : <i>[ <a href="fileserverdefinition.md">FileServerDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#networkshare" title="NetworkShare">NetworkShare</a>" : <i>[ <a href="networksharedefinition4.md">NetworkShareDefinition4</a>, ... ]</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#release" title="Release">Release</a>" : <i>[ <a href="releasedefinition.md">ReleaseDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#skipestimateimpact" title="SkipEstimateImpact">SkipEstimateImpact</a>" : <i>Boolean</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#upgradeimpact" title="UpgradeImpact">UpgradeImpact</a>" : <i>[ <a href="upgradeimpactdefinition.md">UpgradeImpactDefinition</a>, ... ]</i>,
        "<a href="#upgradestatus" title="UpgradeStatus">UpgradeStatus</a>" : <i>[ <a href="upgradestatusdefinition.md">UpgradeStatusDefinition</a>, ... ]</i>,
        "<a href="#upgradetype" title="UpgradeType">UpgradeType</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::FirmwareChassisUpgrade
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#chassis" title="Chassis">Chassis</a>: <i>
      - <a href="chassisdefinition.md">ChassisDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#device" title="Device">Device</a>: <i>
      - <a href="devicedefinition.md">DeviceDefinition</a></i>
    <a href="#directdownload" title="DirectDownload">DirectDownload</a>: <i>
      - <a href="directdownloaddefinition2.md">DirectDownloadDefinition2</a></i>
    <a href="#distributable" title="Distributable">Distributable</a>: <i>
      - <a href="distributabledefinition.md">DistributableDefinition</a></i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#excludecomponentlist" title="ExcludeComponentList">ExcludeComponentList</a>: <i>
      - String</i>
    <a href="#fileserver" title="FileServer">FileServer</a>: <i>
      - <a href="fileserverdefinition.md">FileServerDefinition</a></i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#networkshare" title="NetworkShare">NetworkShare</a>: <i>
      - <a href="networksharedefinition4.md">NetworkShareDefinition4</a></i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#release" title="Release">Release</a>: <i>
      - <a href="releasedefinition.md">ReleaseDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#skipestimateimpact" title="SkipEstimateImpact">SkipEstimateImpact</a>: <i>Boolean</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#upgradeimpact" title="UpgradeImpact">UpgradeImpact</a>: <i>
      - <a href="upgradeimpactdefinition.md">UpgradeImpactDefinition</a></i>
    <a href="#upgradestatus" title="UpgradeStatus">UpgradeStatus</a>: <i>
      - <a href="upgradestatusdefinition.md">UpgradeStatusDefinition</a></i>
    <a href="#upgradetype" title="UpgradeType">UpgradeType</a>: <i>String</i>
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

#### Chassis

_Required_: No

_Type_: List of <a href="chassisdefinition.md">ChassisDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClassId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Device

_Required_: No

_Type_: List of <a href="devicedefinition.md">DeviceDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectDownload

_Required_: No

_Type_: List of <a href="directdownloaddefinition2.md">DirectDownloadDefinition2</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Distributable

_Required_: No

_Type_: List of <a href="distributabledefinition.md">DistributableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainGroupMoid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExcludeComponentList

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FileServer

_Required_: No

_Type_: List of <a href="fileserverdefinition.md">FileServerDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkShare

_Required_: No

_Type_: List of <a href="networksharedefinition4.md">NetworkShareDefinition4</a>

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

#### Release

_Required_: No

_Type_: List of <a href="releasedefinition.md">ReleaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SkipEstimateImpact

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeImpact

_Required_: No

_Type_: List of <a href="upgradeimpactdefinition.md">UpgradeImpactDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeStatus

_Required_: No

_Type_: List of <a href="upgradestatusdefinition.md">UpgradeStatusDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeType

_Required_: No

_Type_: String

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

