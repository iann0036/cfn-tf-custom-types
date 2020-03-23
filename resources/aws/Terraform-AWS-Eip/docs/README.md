# Terraform::AWS::Eip

Provides an Elastic IP resource.

~> **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.

~> **Note:** Do not use `network_interface` to associate the EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::Eip",
    "Properties" : {
        "<a href="#associatewithprivateip" title="AssociateWithPrivateIp">AssociateWithPrivateIp</a>" : <i>String</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>String</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>String</i>,
        "<a href="#publicipv4pool" title="PublicIpv4Pool">PublicIpv4Pool</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#vpc" title="Vpc">Vpc</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::Eip
Properties:
    <a href="#associatewithprivateip" title="AssociateWithPrivateIp">AssociateWithPrivateIp</a>: <i>String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>String</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>String</i>
    <a href="#publicipv4pool" title="PublicIpv4Pool">PublicIpv4Pool</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#vpc" title="Vpc">Vpc</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
</pre>

## Properties

#### AssociateWithPrivateIp

A user specified primary or secondary private IP address to
associate with the Elastic IP address. If no private IP address is specified,
the Elastic IP address is associated with the primary private IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

EC2 instance ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkInterface

Network interface ID to associate with.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicIpv4Pool

EC2 IPv4 address pool identifier or `amazon`. This option is only available for VPC EIPs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

Boolean if the EIP is in a VPC or not.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AllocationId

Returns the <code>AllocationId</code> value.

#### AssociationId

Returns the <code>AssociationId</code> value.

#### Domain

Returns the <code>Domain</code> value.

#### Id

Returns the <code>Id</code> value.

#### PrivateDns

Returns the <code>PrivateDns</code> value.

#### PrivateIp

Returns the <code>PrivateIp</code> value.

#### PublicDns

Returns the <code>PublicDns</code> value.

#### PublicIp

Returns the <code>PublicIp</code> value.

