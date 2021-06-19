# TF::Aviatrix::AwsTgwConnect

The **aviatrix_aws_tgw_connect** resource allows the creation and management of AWS TGW Connect connections. To create
and manage TGW Connect peers, please use `aviatrix_aws_tgw_connect_peer` resources. This resource is available as of
provider version R2.18.1+.

~> **NOTE:** Before creating an AWS TGW Connect, the AWS TGW must have an attached VPC via
the `aviatrix_aws_tgw_vpc_attachment` resource. Also, the AWS TGW must have configured CIDRs via
the `aviatrix_aws_tgw` `cidrs` attribute.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwConnect",
    "Properties" : {
        "<a href="#connectionname" title="ConnectionName">ConnectionName</a>" : <i>String</i>,
        "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>,
        "<a href="#transportvpcid" title="TransportVpcId">TransportVpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwConnect
Properties:
    <a href="#connectionname" title="ConnectionName">ConnectionName</a>: <i>String</i>
    <a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
    <a href="#transportvpcid" title="TransportVpcId">TransportVpcId</a>: <i>String</i>
</pre>

## Properties

#### ConnectionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransportVpcId

_Required_: Yes

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

#### ConnectAttachmentId

Returns the <code>ConnectAttachmentId</code> value.

#### Id

Returns the <code>Id</code> value.

#### TransportAttachmentId

Returns the <code>TransportAttachmentId</code> value.

