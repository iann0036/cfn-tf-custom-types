# TF::FortiOS::FirewallAddress

Configure IPv4 addresses.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FirewallAddress",
    "Properties" : {
        "<a href="#allowrouting" title="AllowRouting">AllowRouting</a>" : <i>String</i>,
        "<a href="#associatedinterface" title="AssociatedInterface">AssociatedInterface</a>" : <i>String</i>,
        "<a href="#cachettl" title="CacheTtl">CacheTtl</a>" : <i>Double</i>,
        "<a href="#clearpassspt" title="ClearpassSpt">ClearpassSpt</a>" : <i>String</i>,
        "<a href="#color" title="Color">Color</a>" : <i>Double</i>,
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#country" title="Country">Country</a>" : <i>String</i>,
        "<a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>" : <i>String</i>,
        "<a href="#endip" title="EndIp">EndIp</a>" : <i>String</i>,
        "<a href="#endmac" title="EndMac">EndMac</a>" : <i>String</i>,
        "<a href="#epgname" title="EpgName">EpgName</a>" : <i>String</i>,
        "<a href="#filter" title="Filter">Filter</a>" : <i>String</i>,
        "<a href="#fqdn" title="Fqdn">Fqdn</a>" : <i>String</i>,
        "<a href="#interface" title="Interface">Interface</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nodeiponly" title="NodeIpOnly">NodeIpOnly</a>" : <i>String</i>,
        "<a href="#objid" title="ObjId">ObjId</a>" : <i>String</i>,
        "<a href="#objtag" title="ObjTag">ObjTag</a>" : <i>String</i>,
        "<a href="#objtype" title="ObjType">ObjType</a>" : <i>String</i>,
        "<a href="#organization" title="Organization">Organization</a>" : <i>String</i>,
        "<a href="#policygroup" title="PolicyGroup">PolicyGroup</a>" : <i>String</i>,
        "<a href="#sdn" title="Sdn">Sdn</a>" : <i>String</i>,
        "<a href="#sdnaddrtype" title="SdnAddrType">SdnAddrType</a>" : <i>String</i>,
        "<a href="#sdntag" title="SdnTag">SdnTag</a>" : <i>String</i>,
        "<a href="#startip" title="StartIp">StartIp</a>" : <i>String</i>,
        "<a href="#startmac" title="StartMac">StartMac</a>" : <i>String</i>,
        "<a href="#subtype" title="SubType">SubType</a>" : <i>String</i>,
        "<a href="#subnet" title="Subnet">Subnet</a>" : <i>String</i>,
        "<a href="#subnetname" title="SubnetName">SubnetName</a>" : <i>String</i>,
        "<a href="#tenant" title="Tenant">Tenant</a>" : <i>String</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#vdomparam" title="Vdomparam">Vdomparam</a>" : <i>String</i>,
        "<a href="#visibility" title="Visibility">Visibility</a>" : <i>String</i>,
        "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>String</i>,
        "<a href="#wildcardfqdn" title="WildcardFqdn">WildcardFqdn</a>" : <i>String</i>,
        "<a href="#fssogroup" title="FssoGroup">FssoGroup</a>" : <i>[ <a href="fssogroupdefinition.md">FssoGroupDefinition</a>, ... ]</i>,
        "<a href="#list" title="List">List</a>" : <i>[ <a href="listdefinition.md">ListDefinition</a>, ... ]</i>,
        "<a href="#tagging" title="Tagging">Tagging</a>" : <i>[ <a href="taggingdefinition.md">TaggingDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FirewallAddress
Properties:
    <a href="#allowrouting" title="AllowRouting">AllowRouting</a>: <i>String</i>
    <a href="#associatedinterface" title="AssociatedInterface">AssociatedInterface</a>: <i>String</i>
    <a href="#cachettl" title="CacheTtl">CacheTtl</a>: <i>Double</i>
    <a href="#clearpassspt" title="ClearpassSpt">ClearpassSpt</a>: <i>String</i>
    <a href="#color" title="Color">Color</a>: <i>Double</i>
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#country" title="Country">Country</a>: <i>String</i>
    <a href="#dynamicsortsubtable" title="DynamicSortSubtable">DynamicSortSubtable</a>: <i>String</i>
    <a href="#endip" title="EndIp">EndIp</a>: <i>String</i>
    <a href="#endmac" title="EndMac">EndMac</a>: <i>String</i>
    <a href="#epgname" title="EpgName">EpgName</a>: <i>String</i>
    <a href="#filter" title="Filter">Filter</a>: <i>String</i>
    <a href="#fqdn" title="Fqdn">Fqdn</a>: <i>String</i>
    <a href="#interface" title="Interface">Interface</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nodeiponly" title="NodeIpOnly">NodeIpOnly</a>: <i>String</i>
    <a href="#objid" title="ObjId">ObjId</a>: <i>String</i>
    <a href="#objtag" title="ObjTag">ObjTag</a>: <i>String</i>
    <a href="#objtype" title="ObjType">ObjType</a>: <i>String</i>
    <a href="#organization" title="Organization">Organization</a>: <i>String</i>
    <a href="#policygroup" title="PolicyGroup">PolicyGroup</a>: <i>String</i>
    <a href="#sdn" title="Sdn">Sdn</a>: <i>String</i>
    <a href="#sdnaddrtype" title="SdnAddrType">SdnAddrType</a>: <i>String</i>
    <a href="#sdntag" title="SdnTag">SdnTag</a>: <i>String</i>
    <a href="#startip" title="StartIp">StartIp</a>: <i>String</i>
    <a href="#startmac" title="StartMac">StartMac</a>: <i>String</i>
    <a href="#subtype" title="SubType">SubType</a>: <i>String</i>
    <a href="#subnet" title="Subnet">Subnet</a>: <i>String</i>
    <a href="#subnetname" title="SubnetName">SubnetName</a>: <i>String</i>
    <a href="#tenant" title="Tenant">Tenant</a>: <i>String</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#vdomparam" title="Vdomparam">Vdomparam</a>: <i>String</i>
    <a href="#visibility" title="Visibility">Visibility</a>: <i>String</i>
    <a href="#wildcard" title="Wildcard">Wildcard</a>: <i>String</i>
    <a href="#wildcardfqdn" title="WildcardFqdn">WildcardFqdn</a>: <i>String</i>
    <a href="#fssogroup" title="FssoGroup">FssoGroup</a>: <i>
      - <a href="fssogroupdefinition.md">FssoGroupDefinition</a></i>
    <a href="#list" title="List">List</a>: <i>
      - <a href="listdefinition.md">ListDefinition</a></i>
    <a href="#tagging" title="Tagging">Tagging</a>: <i>
      - <a href="taggingdefinition.md">TaggingDefinition</a></i>
</pre>

## Properties

#### AllowRouting

Enable/disable use of this address in the static route configuration. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociatedInterface

Network interface associated with address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CacheTtl

Defines the minimal TTL of individual IP addresses in FQDN cache measured in seconds.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ClearpassSpt

SPT (System Posture Token) value. Valid values: `unknown`, `healthy`, `quarantine`, `checkup`, `transient`, `infected`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Color

Color of icon on the GUI.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Country

IP addresses associated to a specific country.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DynamicSortSubtable

true or false, set this parameter to true when using dynamic for_each + toset to configure and sort sub-tables, please do not set this parameter when configuring static sub-tables.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndIp

Final IP address (inclusive) in the range for the address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndMac

Last MAC address in the range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EpgName

Endpoint group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filter

Match criteria filter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Fqdn

Fully Qualified Domain Name address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interface

Name of interface whose IP address is to be used.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Address name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeIpOnly

Enable/disable collection of node addresses only in Kubernetes. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjId

Object ID for NSX.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjTag

Tag of dynamic address object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ObjType

Object type. Valid values: `ip`, `mac`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Organization

Organization domain name (Syntax: organization/domain).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyGroup

Policy group name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sdn

SDN.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnAddrType

Type of addresses to collect. Valid values: `private`, `public`, `all`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SdnTag

SDN Tag.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartIp

First IP address (inclusive) in the range for the address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartMac

First MAC address in the range.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubType

Sub-type of address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnet

IP address and subnet mask of address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetName

Subnet name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tenant

Tenant.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

Universally Unique Identifier (UUID; automatically assigned but can be manually reset).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdomparam

Specifies the vdom to which the resource will be applied when the FortiGate unit is running in VDOM mode. Only one vdom can be specified. If you want to inherit the vdom configuration of the provider, please do not set this parameter.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Visibility

Enable/disable address visibility in the GUI. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

IP address and wildcard netmask.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WildcardFqdn

Fully Qualified Domain Name with wildcard characters.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FssoGroup

_Required_: No

_Type_: List of <a href="fssogroupdefinition.md">FssoGroupDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### List

_Required_: No

_Type_: List of <a href="listdefinition.md">ListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tagging

_Required_: No

_Type_: List of <a href="taggingdefinition.md">TaggingDefinition</a>

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

