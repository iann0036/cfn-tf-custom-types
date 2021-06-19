# TF::VCD::NsxtNetworkImported

Provides a VMware Cloud Director Org VDC NSX-T Imported Network type. This can be used to create, modify, and delete NSX-T VDC networks of Imported type (backed by NSX-T).

Supported in provider *v3.2+* for NSX-T VDCs only.

-> This is **not Terraform imported** resource, but a special **Imported** type of **Org VDC network** in NSX-T VDC. Read more about Imported Network in [official VCD documentation]((https://docs.vmware.com/en/VMware-Cloud-Director/10.2/VMware-Cloud-Director-Tenant-Portal-Guide/GUID-FB303D62-67EA-4209-BE4D-C3746481BCC8.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::VCD::NsxtNetworkImported",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#dns1" title="Dns1">Dns1</a>" : <i>String</i>,
        "<a href="#dns2" title="Dns2">Dns2</a>" : <i>String</i>,
        "<a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>" : <i>String</i>,
        "<a href="#gateway" title="Gateway">Gateway</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#nsxtlogicalswitchname" title="NsxtLogicalSwitchName">NsxtLogicalSwitchName</a>" : <i>String</i>,
        "<a href="#org" title="Org">Org</a>" : <i>String</i>,
        "<a href="#prefixlength" title="PrefixLength">PrefixLength</a>" : <i>Double</i>,
        "<a href="#vdc" title="Vdc">Vdc</a>" : <i>String</i>,
        "<a href="#staticippool" title="StaticIpPool">StaticIpPool</a>" : <i>[ <a href="staticippooldefinition.md">StaticIpPoolDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::VCD::NsxtNetworkImported
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#dns1" title="Dns1">Dns1</a>: <i>String</i>
    <a href="#dns2" title="Dns2">Dns2</a>: <i>String</i>
    <a href="#dnssuffix" title="DnsSuffix">DnsSuffix</a>: <i>String</i>
    <a href="#gateway" title="Gateway">Gateway</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#nsxtlogicalswitchname" title="NsxtLogicalSwitchName">NsxtLogicalSwitchName</a>: <i>String</i>
    <a href="#org" title="Org">Org</a>: <i>String</i>
    <a href="#prefixlength" title="PrefixLength">PrefixLength</a>: <i>Double</i>
    <a href="#vdc" title="Vdc">Vdc</a>: <i>String</i>
    <a href="#staticippool" title="StaticIpPool">StaticIpPool</a>: <i>
      - <a href="staticippooldefinition.md">StaticIpPoolDefinition</a></i>
</pre>

## Properties

#### Description

An optional description of the network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns1

First DNS server to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Dns2

Second DNS server to use.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsSuffix

A FQDN for the virtual machines on this network.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Gateway

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name for the network.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NsxtLogicalSwitchName

Unique name of an existing NSX-T segment.
**Note** it will never be refreshed because API does not allow reading this name after it is
consumed. Instead ID will be stored in `nsxt_logical_switch_id` attribute.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Org

The name of organization to use, optional if defined at provider level. Useful when
connected as sysadmin working across different organisations.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrefixLength

The prefix length for the new network (e.g. 24 for netmask 255.255.255.0).

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vdc

The name of VDC to use, optional if defined at provider level.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpPool

_Required_: No

_Type_: List of <a href="staticippooldefinition.md">StaticIpPoolDefinition</a>

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

#### NsxtLogicalSwitchId

Returns the <code>NsxtLogicalSwitchId</code> value.

