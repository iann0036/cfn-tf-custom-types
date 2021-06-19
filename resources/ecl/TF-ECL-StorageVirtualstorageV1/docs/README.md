# TF::ECL::StorageVirtualstorageV1

Manages a V1 virtual storage resource within Enterprise Cloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::ECL::StorageVirtualstorageV1",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#errormessage" title="ErrorMessage">ErrorMessage</a>" : <i>String</i>,
        "<a href="#ipaddrpool" title="IpAddrPool">IpAddrPool</a>" : <i>[ <a href="ipaddrpooldefinition.md">IpAddrPoolDefinition</a>, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#networkid" title="NetworkId">NetworkId</a>" : <i>String</i>,
        "<a href="#subnetid" title="SubnetId">SubnetId</a>" : <i>String</i>,
        "<a href="#volumetypeid" title="VolumeTypeId">VolumeTypeId</a>" : <i>String</i>,
        "<a href="#volumetypename" title="VolumeTypeName">VolumeTypeName</a>" : <i>String</i>,
        "<a href="#hostroutes" title="HostRoutes">HostRoutes</a>" : <i>[ <a href="hostroutesdefinition.md">HostRoutesDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::ECL::StorageVirtualstorageV1
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#errormessage" title="ErrorMessage">ErrorMessage</a>: <i>String</i>
    <a href="#ipaddrpool" title="IpAddrPool">IpAddrPool</a>: <i>
      - <a href="ipaddrpooldefinition.md">IpAddrPoolDefinition</a></i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#networkid" title="NetworkId">NetworkId</a>: <i>String</i>
    <a href="#subnetid" title="SubnetId">SubnetId</a>: <i>String</i>
    <a href="#volumetypeid" title="VolumeTypeId">VolumeTypeId</a>: <i>String</i>
    <a href="#volumetypename" title="VolumeTypeName">VolumeTypeName</a>: <i>String</i>
    <a href="#hostroutes" title="HostRoutes">HostRoutes</a>: <i>
      - <a href="hostroutesdefinition.md">HostRoutesDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Description

Description of Virtual Storage.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpAddrPool

IP address pool which specifies IP address range
used by the Virtual Storage.
The ip_addr_pool structure is documented below.

_Required_: Yes

_Type_: List of <a href="ipaddrpooldefinition.md">IpAddrPoolDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of Virtual Storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkId

ID(UUID) for network to be connected to the Virtual Storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetId

ID(UUID) for subnet to be connected to the Virtual Storage.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeTypeId

ID of volume type used for this Virtual Storage (UUID).
User must specify either volume_type_id or volume_type_name.
This parameter conflicts with `volume_type_name` .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VolumeTypeName

Name of volume type used for this Virtual Storage.
User must specify either volume_type_id or volume_type_name.
This parameter conflicts with `volume_type_id` .

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HostRoutes

_Required_: No

_Type_: List of <a href="hostroutesdefinition.md">HostRoutesDefinition</a>

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

#### Id

Returns the <code>Id</code> value.

