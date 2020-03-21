# Terraform::Packet::IpAttachment

CloudFormation equivalent of packet_ip_attachment

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Packet::IpAttachment",
    "Properties" : {
        "<a href="#cidrnotation" title="CidrNotation">CidrNotation</a>" : <i>String</i>,
        "<a href="#deviceid" title="DeviceId">DeviceId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Packet::IpAttachment
Properties:
    <a href="#cidrnotation" title="CidrNotation">CidrNotation</a>: <i>String</i>
    <a href="#deviceid" title="DeviceId">DeviceId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
</pre>

## Properties

#### CidrNotation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeviceId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

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

#### Address

Returns the &lt;code&gt;Address&lt;/code&gt; value.

#### AddressFamily

Returns the &lt;code&gt;AddressFamily&lt;/code&gt; value.

#### Cidr

Returns the &lt;code&gt;Cidr&lt;/code&gt; value.

#### Gateway

Returns the &lt;code&gt;Gateway&lt;/code&gt; value.

#### Global

Returns the &lt;code&gt;Global&lt;/code&gt; value.

#### Manageable

Returns the &lt;code&gt;Manageable&lt;/code&gt; value.

#### Management

Returns the &lt;code&gt;Management&lt;/code&gt; value.

#### Netmask

Returns the &lt;code&gt;Netmask&lt;/code&gt; value.

#### Network

Returns the &lt;code&gt;Network&lt;/code&gt; value.

#### Public

Returns the &lt;code&gt;Public&lt;/code&gt; value.

