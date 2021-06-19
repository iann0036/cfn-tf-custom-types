# TF::OCI::CorePublicIpPoolCapacity

This resource is used to manage the `cidr_blocks` of Public Ip Pool resource in Oracle Cloud Infrastructure Core service. 
Adds a Cidr from the named Byoip Range prefix to the referenced Public IP Pool. The cidr must be a subset of the Byoip Range in question. The cidr must not overlap with any other cidr already added to this or any other Public Ip Pool.

**Note:** When a new `oci_core_public_ip_pool_capacity` resource is created or removed, terraform needs to be refreshed to update the `cidr_blocks` of `oci_core_public_ip_pool` resource in state file.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OCI::CorePublicIpPoolCapacity",
    "Properties" : {
        "<a href="#byoipid" title="ByoipId">ByoipId</a>" : <i>String</i>,
        "<a href="#cidrblock" title="CidrBlock">CidrBlock</a>" : <i>String</i>,
        "<a href="#publicippoolid" title="PublicIpPoolId">PublicIpPoolId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OCI::CorePublicIpPoolCapacity
Properties:
    <a href="#byoipid" title="ByoipId">ByoipId</a>: <i>String</i>
    <a href="#cidrblock" title="CidrBlock">CidrBlock</a>: <i>String</i>
    <a href="#publicippoolid" title="PublicIpPoolId">PublicIpPoolId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### ByoipId

The OCID of the Byoip Range Id object to which the cidr block belongs.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CidrBlock

The CIDR IP address range to be added to the Public Ip Pool. Example: `10.0.1.0/24`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpPoolId

The OCID of the pool object created by the current tenancy.

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

#### Id

Returns the <code>Id</code> value.

