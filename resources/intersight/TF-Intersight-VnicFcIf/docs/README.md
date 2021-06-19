# TF::Intersight::VnicFcIf

Virtual Fibre Channel Interface.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::VnicFcIf",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#fcadapterpolicy" title="FcAdapterPolicy">FcAdapterPolicy</a>" : <i>[ <a href="fcadapterpolicydefinition.md">FcAdapterPolicyDefinition</a>, ... ]</i>,
        "<a href="#fcnetworkpolicy" title="FcNetworkPolicy">FcNetworkPolicy</a>" : <i>[ <a href="fcnetworkpolicydefinition.md">FcNetworkPolicyDefinition</a>, ... ]</i>,
        "<a href="#fcqospolicy" title="FcQosPolicy">FcQosPolicy</a>" : <i>[ <a href="fcqospolicydefinition.md">FcQosPolicyDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#persistentbindings" title="PersistentBindings">PersistentBindings</a>" : <i>Boolean</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placementdefinition.md">PlacementDefinition</a>, ... ]</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>[ <a href="profiledefinition.md">ProfileDefinition</a>, ... ]</i>,
        "<a href="#sanconnectivitypolicy" title="SanConnectivityPolicy">SanConnectivityPolicy</a>" : <i>[ <a href="sanconnectivitypolicydefinition.md">SanConnectivityPolicyDefinition</a>, ... ]</i>,
        "<a href="#scpvhba" title="ScpVhba">ScpVhba</a>" : <i>[ <a href="scpvhbadefinition.md">ScpVhbaDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#spvhbas" title="SpVhbas">SpVhbas</a>" : <i>[ <a href="spvhbasdefinition.md">SpVhbasDefinition</a>, ... ]</i>,
        "<a href="#staticwwpnaddress" title="StaticWwpnAddress">StaticWwpnAddress</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#vifid" title="VifId">VifId</a>" : <i>Double</i>,
        "<a href="#wwpn" title="Wwpn">Wwpn</a>" : <i>String</i>,
        "<a href="#wwpnaddresstype" title="WwpnAddressType">WwpnAddressType</a>" : <i>String</i>,
        "<a href="#wwpnlease" title="WwpnLease">WwpnLease</a>" : <i>[ <a href="wwpnleasedefinition.md">WwpnLeaseDefinition</a>, ... ]</i>,
        "<a href="#wwpnpool" title="WwpnPool">WwpnPool</a>" : <i>[ <a href="wwpnpooldefinition.md">WwpnPoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::VnicFcIf
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#fcadapterpolicy" title="FcAdapterPolicy">FcAdapterPolicy</a>: <i>
      - <a href="fcadapterpolicydefinition.md">FcAdapterPolicyDefinition</a></i>
    <a href="#fcnetworkpolicy" title="FcNetworkPolicy">FcNetworkPolicy</a>: <i>
      - <a href="fcnetworkpolicydefinition.md">FcNetworkPolicyDefinition</a></i>
    <a href="#fcqospolicy" title="FcQosPolicy">FcQosPolicy</a>: <i>
      - <a href="fcqospolicydefinition.md">FcQosPolicyDefinition</a></i>
    <a href="#modtime" title="ModTime">ModTime</a>: <i>String</i>
    <a href="#moid" title="Moid">Moid</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#objecttype" title="ObjectType">ObjectType</a>: <i>String</i>
    <a href="#order" title="Order">Order</a>: <i>Double</i>
    <a href="#owners" title="Owners">Owners</a>: <i>
      - String</i>
    <a href="#parent" title="Parent">Parent</a>: <i>
      - <a href="parentdefinition.md">ParentDefinition</a></i>
    <a href="#permissionresources" title="PermissionResources">PermissionResources</a>: <i>
      - <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a></i>
    <a href="#persistentbindings" title="PersistentBindings">PersistentBindings</a>: <i>Boolean</i>
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placementdefinition.md">PlacementDefinition</a></i>
    <a href="#profile" title="Profile">Profile</a>: <i>
      - <a href="profiledefinition.md">ProfileDefinition</a></i>
    <a href="#sanconnectivitypolicy" title="SanConnectivityPolicy">SanConnectivityPolicy</a>: <i>
      - <a href="sanconnectivitypolicydefinition.md">SanConnectivityPolicyDefinition</a></i>
    <a href="#scpvhba" title="ScpVhba">ScpVhba</a>: <i>
      - <a href="scpvhbadefinition.md">ScpVhbaDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#spvhbas" title="SpVhbas">SpVhbas</a>: <i>
      - <a href="spvhbasdefinition.md">SpVhbasDefinition</a></i>
    <a href="#staticwwpnaddress" title="StaticWwpnAddress">StaticWwpnAddress</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#vifid" title="VifId">VifId</a>: <i>Double</i>
    <a href="#wwpn" title="Wwpn">Wwpn</a>: <i>String</i>
    <a href="#wwpnaddresstype" title="WwpnAddressType">WwpnAddressType</a>: <i>String</i>
    <a href="#wwpnlease" title="WwpnLease">WwpnLease</a>: <i>
      - <a href="wwpnleasedefinition.md">WwpnLeaseDefinition</a></i>
    <a href="#wwpnpool" title="WwpnPool">WwpnPool</a>: <i>
      - <a href="wwpnpooldefinition.md">WwpnPoolDefinition</a></i>
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

#### FcAdapterPolicy

_Required_: No

_Type_: List of <a href="fcadapterpolicydefinition.md">FcAdapterPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcNetworkPolicy

_Required_: No

_Type_: List of <a href="fcnetworkpolicydefinition.md">FcNetworkPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FcQosPolicy

_Required_: No

_Type_: List of <a href="fcqospolicydefinition.md">FcQosPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModTime

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Moid

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjectType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

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

#### PersistentBindings

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

_Required_: No

_Type_: List of <a href="placementdefinition.md">PlacementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: List of <a href="profiledefinition.md">ProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SanConnectivityPolicy

_Required_: No

_Type_: List of <a href="sanconnectivitypolicydefinition.md">SanConnectivityPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ScpVhba

_Required_: No

_Type_: List of <a href="scpvhbadefinition.md">ScpVhbaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpVhbas

_Required_: No

_Type_: List of <a href="spvhbasdefinition.md">SpVhbasDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticWwpnAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VifId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wwpn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WwpnAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WwpnLease

_Required_: No

_Type_: List of <a href="wwpnleasedefinition.md">WwpnLeaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WwpnPool

_Required_: No

_Type_: List of <a href="wwpnpooldefinition.md">WwpnPoolDefinition</a>

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

