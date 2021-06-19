# TF::AWS::Eip

Provides an Elastic IP resource.

~> **Note:** EIP may require IGW to exist prior to association. Use `depends_on` to set an explicit dependency on the IGW.

~> **Note:** Do not use `network_interface` to associate the EIP to `aws_lb` or `aws_nat_gateway` resources. Instead use the `allocation_id` available in those resources to allow AWS to manage the association, otherwise you will see `AuthFailure` errors.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::Eip",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#associatewithprivateip" title="AssociateWithPrivateIp">AssociateWithPrivateIp</a>" : <i>String</i>,
        "<a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>" : <i>String</i>,
        "<a href="#instance" title="Instance">Instance</a>" : <i>String</i>,
        "<a href="#networkbordergroup" title="NetworkBorderGroup">NetworkBorderGroup</a>" : <i>String</i>,
        "<a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>" : <i>String</i>,
        "<a href="#publicipv4pool" title="PublicIpv4Pool">PublicIpv4Pool</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
        "<a href="#tagsall" title="TagsAll">TagsAll</a>" : <i>[ <a href="tagsalldefinition.md">TagsAllDefinition</a>, ... ]</i>,
        "<a href="#vpc" title="Vpc">Vpc</a>" : <i>Boolean</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::Eip
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#associatewithprivateip" title="AssociateWithPrivateIp">AssociateWithPrivateIp</a>: <i>String</i>
    <a href="#customerownedipv4pool" title="CustomerOwnedIpv4Pool">CustomerOwnedIpv4Pool</a>: <i>String</i>
    <a href="#instance" title="Instance">Instance</a>: <i>String</i>
    <a href="#networkbordergroup" title="NetworkBorderGroup">NetworkBorderGroup</a>: <i>String</i>
    <a href="#networkinterface" title="NetworkInterface">NetworkInterface</a>: <i>String</i>
    <a href="#publicipv4pool" title="PublicIpv4Pool">PublicIpv4Pool</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
    <a href="#tagsall" title="TagsAll">TagsAll</a>: <i>
      - <a href="tagsalldefinition.md">TagsAllDefinition</a></i>
    <a href="#vpc" title="Vpc">Vpc</a>: <i>Boolean</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### Address

IP address from an EC2 BYOIP pool. This option is only available for VPC EIPs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssociateWithPrivateIp

User-specified primary or secondary private IP address to associate with the Elastic IP address. If no private IP address is specified, the Elastic IP address is associated with the primary private IP address.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerOwnedIpv4Pool

ID  of a customer-owned address pool. For more on customer owned IP addressed check out [Customer-owned IP addresses guide](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#ip-addressing).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Instance

EC2 instance ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkBorderGroup

Location from which the IP address is advertised. Use this parameter to limit the address to this location.

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

Map of tags to assign to the resource. Tags can only be applied to EIPs in a VPC. If configured with a provider [`default_tags` configuration block](https://www.terraform.io/docs/providers/aws/index.html#default_tags-configuration-block) present, tags with matching keys will overwrite those defined at the provider-level.

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagsAll

_Required_: No

_Type_: List of <a href="tagsalldefinition.md">TagsAllDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vpc

Boolean if the EIP is in a VPC or not.

_Required_: No

_Type_: Boolean

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

#### AllocationId

Returns the <code>AllocationId</code> value.

#### AssociationId

Returns the <code>AssociationId</code> value.

#### CarrierIp

Returns the <code>CarrierIp</code> value.

#### CustomerOwnedIp

Returns the <code>CustomerOwnedIp</code> value.

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

