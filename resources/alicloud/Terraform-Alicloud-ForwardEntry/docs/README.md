# Terraform::Alicloud::ForwardEntry

Provides a forward resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::ForwardEntry",
    "Properties" : {
        "<a href="#externalip" title="ExternalIp">ExternalIp</a>" : <i>String</i>,
        "<a href="#externalport" title="ExternalPort">ExternalPort</a>" : <i>String</i>,
        "<a href="#forwardtableid" title="ForwardTableId">ForwardTableId</a>" : <i>String</i>,
        "<a href="#internalip" title="InternalIp">InternalIp</a>" : <i>String</i>,
        "<a href="#internalport" title="InternalPort">InternalPort</a>" : <i>String</i>,
        "<a href="#ipprotocol" title="IpProtocol">IpProtocol</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::ForwardEntry
Properties:
    <a href="#externalip" title="ExternalIp">ExternalIp</a>: <i>String</i>
    <a href="#externalport" title="ExternalPort">ExternalPort</a>: <i>String</i>
    <a href="#forwardtableid" title="ForwardTableId">ForwardTableId</a>: <i>String</i>
    <a href="#internalip" title="InternalIp">InternalIp</a>: <i>String</i>
    <a href="#internalport" title="InternalPort">InternalPort</a>: <i>String</i>
    <a href="#ipprotocol" title="IpProtocol">IpProtocol</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### ExternalIp

The external ip address, the ip must along bandwidth package public ip which `alicloud_nat_gateway` argument `bandwidth_packages`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExternalPort

The external port, valid value is 1~65535|any.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForwardTableId

The value can get from `alicloud_nat_gateway` Attributes "forward_table_ids".

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalIp

The internal ip, must a private ip.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InternalPort

The internal port, valid value is 1~65535|any.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpProtocol

The ip protocal, valid value is tcp|udp|any.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of forward entry.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### ForwardEntryId

Returns the <code>ForwardEntryId</code> value.

