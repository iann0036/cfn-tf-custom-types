# TF::Intersight::VnicEthIf

Virtual Ethernet Interface.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Intersight::VnicEthIf",
    "Properties" : {
        "<a href="#accountmoid" title="AccountMoid">AccountMoid</a>" : <i>String</i>,
        "<a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>" : <i>String</i>,
        "<a href="#ancestors" title="Ancestors">Ancestors</a>" : <i>[ <a href="ancestorsdefinition.md">AncestorsDefinition</a>, ... ]</i>,
        "<a href="#cdn" title="Cdn">Cdn</a>" : <i>[ <a href="cdndefinition.md">CdnDefinition</a>, ... ]</i>,
        "<a href="#classid" title="ClassId">ClassId</a>" : <i>String</i>,
        "<a href="#createtime" title="CreateTime">CreateTime</a>" : <i>String</i>,
        "<a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>" : <i>String</i>,
        "<a href="#ethadapterpolicy" title="EthAdapterPolicy">EthAdapterPolicy</a>" : <i>[ <a href="ethadapterpolicydefinition.md">EthAdapterPolicyDefinition</a>, ... ]</i>,
        "<a href="#ethnetworkpolicy" title="EthNetworkPolicy">EthNetworkPolicy</a>" : <i>[ <a href="ethnetworkpolicydefinition.md">EthNetworkPolicyDefinition</a>, ... ]</i>,
        "<a href="#ethqospolicy" title="EthQosPolicy">EthQosPolicy</a>" : <i>[ <a href="ethqospolicydefinition.md">EthQosPolicyDefinition</a>, ... ]</i>,
        "<a href="#fabricethnetworkcontrolpolicy" title="FabricEthNetworkControlPolicy">FabricEthNetworkControlPolicy</a>" : <i>[ <a href="fabricethnetworkcontrolpolicydefinition.md">FabricEthNetworkControlPolicyDefinition</a>, ... ]</i>,
        "<a href="#fabricethnetworkgrouppolicy" title="FabricEthNetworkGroupPolicy">FabricEthNetworkGroupPolicy</a>" : <i>[ <a href="fabricethnetworkgrouppolicydefinition.md">FabricEthNetworkGroupPolicyDefinition</a>, ... ]</i>,
        "<a href="#failoverenabled" title="FailoverEnabled">FailoverEnabled</a>" : <i>Boolean</i>,
        "<a href="#iplease" title="IpLease">IpLease</a>" : <i>[ <a href="ipleasedefinition.md">IpLeaseDefinition</a>, ... ]</i>,
        "<a href="#iscsibootpolicy" title="IscsiBootPolicy">IscsiBootPolicy</a>" : <i>[ <a href="iscsibootpolicydefinition.md">IscsiBootPolicyDefinition</a>, ... ]</i>,
        "<a href="#iscsiipv4addressallocationtype" title="IscsiIpV4AddressAllocationType">IscsiIpV4AddressAllocationType</a>" : <i>String</i>,
        "<a href="#iscsiipv4config" title="IscsiIpV4Config">IscsiIpV4Config</a>" : <i>[ <a href="iscsiipv4configdefinition.md">IscsiIpV4ConfigDefinition</a>, ... ]</i>,
        "<a href="#iscsiipv4address" title="IscsiIpv4Address">IscsiIpv4Address</a>" : <i>String</i>,
        "<a href="#lanconnectivitypolicy" title="LanConnectivityPolicy">LanConnectivityPolicy</a>" : <i>[ <a href="lanconnectivitypolicydefinition.md">LanConnectivityPolicyDefinition</a>, ... ]</i>,
        "<a href="#lcpvnic" title="LcpVnic">LcpVnic</a>" : <i>[ <a href="lcpvnicdefinition.md">LcpVnicDefinition</a>, ... ]</i>,
        "<a href="#macaddress" title="MacAddress">MacAddress</a>" : <i>String</i>,
        "<a href="#macaddresstype" title="MacAddressType">MacAddressType</a>" : <i>String</i>,
        "<a href="#maclease" title="MacLease">MacLease</a>" : <i>[ <a href="macleasedefinition.md">MacLeaseDefinition</a>, ... ]</i>,
        "<a href="#macpool" title="MacPool">MacPool</a>" : <i>[ <a href="macpooldefinition.md">MacPoolDefinition</a>, ... ]</i>,
        "<a href="#modtime" title="ModTime">ModTime</a>" : <i>String</i>,
        "<a href="#moid" title="Moid">Moid</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#objecttype" title="ObjectType">ObjectType</a>" : <i>String</i>,
        "<a href="#order" title="Order">Order</a>" : <i>Double</i>,
        "<a href="#owners" title="Owners">Owners</a>" : <i>[ String, ... ]</i>,
        "<a href="#parent" title="Parent">Parent</a>" : <i>[ <a href="parentdefinition.md">ParentDefinition</a>, ... ]</i>,
        "<a href="#permissionresources" title="PermissionResources">PermissionResources</a>" : <i>[ <a href="permissionresourcesdefinition.md">PermissionResourcesDefinition</a>, ... ]</i>,
        "<a href="#placement" title="Placement">Placement</a>" : <i>[ <a href="placementdefinition.md">PlacementDefinition</a>, ... ]</i>,
        "<a href="#profile" title="Profile">Profile</a>" : <i>[ <a href="profiledefinition.md">ProfileDefinition</a>, ... ]</i>,
        "<a href="#sharedscope" title="SharedScope">SharedScope</a>" : <i>String</i>,
        "<a href="#spvnics" title="SpVnics">SpVnics</a>" : <i>[ <a href="spvnicsdefinition.md">SpVnicsDefinition</a>, ... ]</i>,
        "<a href="#standbyvifid" title="StandbyVifId">StandbyVifId</a>" : <i>Double</i>,
        "<a href="#staticmacaddress" title="StaticMacAddress">StaticMacAddress</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#usnicsettings" title="UsnicSettings">UsnicSettings</a>" : <i>[ <a href="usnicsettingsdefinition.md">UsnicSettingsDefinition</a>, ... ]</i>,
        "<a href="#versioncontext" title="VersionContext">VersionContext</a>" : <i>[ <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>, ... ]</i>,
        "<a href="#vifid" title="VifId">VifId</a>" : <i>Double</i>,
        "<a href="#vmqsettings" title="VmqSettings">VmqSettings</a>" : <i>[ <a href="vmqsettingsdefinition.md">VmqSettingsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Intersight::VnicEthIf
Properties:
    <a href="#accountmoid" title="AccountMoid">AccountMoid</a>: <i>String</i>
    <a href="#additionalproperties" title="AdditionalProperties">AdditionalProperties</a>: <i>String</i>
    <a href="#ancestors" title="Ancestors">Ancestors</a>: <i>
      - <a href="ancestorsdefinition.md">AncestorsDefinition</a></i>
    <a href="#cdn" title="Cdn">Cdn</a>: <i>
      - <a href="cdndefinition.md">CdnDefinition</a></i>
    <a href="#classid" title="ClassId">ClassId</a>: <i>String</i>
    <a href="#createtime" title="CreateTime">CreateTime</a>: <i>String</i>
    <a href="#domaingroupmoid" title="DomainGroupMoid">DomainGroupMoid</a>: <i>String</i>
    <a href="#ethadapterpolicy" title="EthAdapterPolicy">EthAdapterPolicy</a>: <i>
      - <a href="ethadapterpolicydefinition.md">EthAdapterPolicyDefinition</a></i>
    <a href="#ethnetworkpolicy" title="EthNetworkPolicy">EthNetworkPolicy</a>: <i>
      - <a href="ethnetworkpolicydefinition.md">EthNetworkPolicyDefinition</a></i>
    <a href="#ethqospolicy" title="EthQosPolicy">EthQosPolicy</a>: <i>
      - <a href="ethqospolicydefinition.md">EthQosPolicyDefinition</a></i>
    <a href="#fabricethnetworkcontrolpolicy" title="FabricEthNetworkControlPolicy">FabricEthNetworkControlPolicy</a>: <i>
      - <a href="fabricethnetworkcontrolpolicydefinition.md">FabricEthNetworkControlPolicyDefinition</a></i>
    <a href="#fabricethnetworkgrouppolicy" title="FabricEthNetworkGroupPolicy">FabricEthNetworkGroupPolicy</a>: <i>
      - <a href="fabricethnetworkgrouppolicydefinition.md">FabricEthNetworkGroupPolicyDefinition</a></i>
    <a href="#failoverenabled" title="FailoverEnabled">FailoverEnabled</a>: <i>Boolean</i>
    <a href="#iplease" title="IpLease">IpLease</a>: <i>
      - <a href="ipleasedefinition.md">IpLeaseDefinition</a></i>
    <a href="#iscsibootpolicy" title="IscsiBootPolicy">IscsiBootPolicy</a>: <i>
      - <a href="iscsibootpolicydefinition.md">IscsiBootPolicyDefinition</a></i>
    <a href="#iscsiipv4addressallocationtype" title="IscsiIpV4AddressAllocationType">IscsiIpV4AddressAllocationType</a>: <i>String</i>
    <a href="#iscsiipv4config" title="IscsiIpV4Config">IscsiIpV4Config</a>: <i>
      - <a href="iscsiipv4configdefinition.md">IscsiIpV4ConfigDefinition</a></i>
    <a href="#iscsiipv4address" title="IscsiIpv4Address">IscsiIpv4Address</a>: <i>String</i>
    <a href="#lanconnectivitypolicy" title="LanConnectivityPolicy">LanConnectivityPolicy</a>: <i>
      - <a href="lanconnectivitypolicydefinition.md">LanConnectivityPolicyDefinition</a></i>
    <a href="#lcpvnic" title="LcpVnic">LcpVnic</a>: <i>
      - <a href="lcpvnicdefinition.md">LcpVnicDefinition</a></i>
    <a href="#macaddress" title="MacAddress">MacAddress</a>: <i>String</i>
    <a href="#macaddresstype" title="MacAddressType">MacAddressType</a>: <i>String</i>
    <a href="#maclease" title="MacLease">MacLease</a>: <i>
      - <a href="macleasedefinition.md">MacLeaseDefinition</a></i>
    <a href="#macpool" title="MacPool">MacPool</a>: <i>
      - <a href="macpooldefinition.md">MacPoolDefinition</a></i>
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
    <a href="#placement" title="Placement">Placement</a>: <i>
      - <a href="placementdefinition.md">PlacementDefinition</a></i>
    <a href="#profile" title="Profile">Profile</a>: <i>
      - <a href="profiledefinition.md">ProfileDefinition</a></i>
    <a href="#sharedscope" title="SharedScope">SharedScope</a>: <i>String</i>
    <a href="#spvnics" title="SpVnics">SpVnics</a>: <i>
      - <a href="spvnicsdefinition.md">SpVnicsDefinition</a></i>
    <a href="#standbyvifid" title="StandbyVifId">StandbyVifId</a>: <i>Double</i>
    <a href="#staticmacaddress" title="StaticMacAddress">StaticMacAddress</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#usnicsettings" title="UsnicSettings">UsnicSettings</a>: <i>
      - <a href="usnicsettingsdefinition.md">UsnicSettingsDefinition</a></i>
    <a href="#versioncontext" title="VersionContext">VersionContext</a>: <i>
      - <a href="versioncontextdefinition3.md">VersionContextDefinition3</a></i>
    <a href="#vifid" title="VifId">VifId</a>: <i>Double</i>
    <a href="#vmqsettings" title="VmqSettings">VmqSettings</a>: <i>
      - <a href="vmqsettingsdefinition.md">VmqSettingsDefinition</a></i>
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

#### Cdn

_Required_: No

_Type_: List of <a href="cdndefinition.md">CdnDefinition</a>

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

#### EthAdapterPolicy

_Required_: No

_Type_: List of <a href="ethadapterpolicydefinition.md">EthAdapterPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthNetworkPolicy

_Required_: No

_Type_: List of <a href="ethnetworkpolicydefinition.md">EthNetworkPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EthQosPolicy

_Required_: No

_Type_: List of <a href="ethqospolicydefinition.md">EthQosPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricEthNetworkControlPolicy

_Required_: No

_Type_: List of <a href="fabricethnetworkcontrolpolicydefinition.md">FabricEthNetworkControlPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FabricEthNetworkGroupPolicy

_Required_: No

_Type_: List of <a href="fabricethnetworkgrouppolicydefinition.md">FabricEthNetworkGroupPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FailoverEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpLease

_Required_: No

_Type_: List of <a href="ipleasedefinition.md">IpLeaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiBootPolicy

_Required_: No

_Type_: List of <a href="iscsibootpolicydefinition.md">IscsiBootPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiIpV4AddressAllocationType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiIpV4Config

_Required_: No

_Type_: List of <a href="iscsiipv4configdefinition.md">IscsiIpV4ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IscsiIpv4Address

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LanConnectivityPolicy

_Required_: No

_Type_: List of <a href="lanconnectivitypolicydefinition.md">LanConnectivityPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LcpVnic

_Required_: No

_Type_: List of <a href="lcpvnicdefinition.md">LcpVnicDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacAddressType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacLease

_Required_: No

_Type_: List of <a href="macleasedefinition.md">MacLeaseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MacPool

_Required_: No

_Type_: List of <a href="macpooldefinition.md">MacPoolDefinition</a>

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

#### Placement

_Required_: No

_Type_: List of <a href="placementdefinition.md">PlacementDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Profile

_Required_: No

_Type_: List of <a href="profiledefinition.md">ProfileDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SharedScope

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpVnics

_Required_: No

_Type_: List of <a href="spvnicsdefinition.md">SpVnicsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StandbyVifId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticMacAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UsnicSettings

_Required_: No

_Type_: List of <a href="usnicsettingsdefinition.md">UsnicSettingsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VersionContext

_Required_: No

_Type_: List of <a href="versioncontextdefinition3.md">VersionContextDefinition3</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VifId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VmqSettings

_Required_: No

_Type_: List of <a href="vmqsettingsdefinition.md">VmqSettingsDefinition</a>

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

