# TF::Aviatrix::AwsTgwDirectconnect

The **aviatrix_aws_tgw_directconnect** resource allows the creation and management of Aviatrix-created AWS TGW DirectConnect connections.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwDirectconnect",
    "Properties" : {
        "<a href="#allowedprefix" title="AllowedPrefix">AllowedPrefix</a>" : <i>String</i>,
        "<a href="#directconnectaccountname" title="DirectconnectAccountName">DirectconnectAccountName</a>" : <i>String</i>,
        "<a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>" : <i>String</i>,
        "<a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>" : <i>Boolean</i>,
        "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwDirectconnect
Properties:
    <a href="#allowedprefix" title="AllowedPrefix">AllowedPrefix</a>: <i>String</i>
    <a href="#directconnectaccountname" title="DirectconnectAccountName">DirectconnectAccountName</a>: <i>String</i>
    <a href="#dxgatewayid" title="DxGatewayId">DxGatewayId</a>: <i>String</i>
    <a href="#enablelearnedcidrsapproval" title="EnableLearnedCidrsApproval">EnableLearnedCidrsApproval</a>: <i>Boolean</i>
    <a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
</pre>

## Properties

#### AllowedPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DirectconnectAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DxGatewayId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableLearnedCidrsApproval

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

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

#### Id

Returns the <code>Id</code> value.

