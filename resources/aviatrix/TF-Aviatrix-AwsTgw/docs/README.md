# TF::Aviatrix::AwsTgw

The **aviatrix_aws_tgw** resource allows the creation and management of Aviatrix-created AWS TGWs.

~> **NOTE:** If you are planning to attach VPCs to the **aviatrix_aws_tgw** resource and anticipate updating it often and/or using advanced options such as customized route advertisement, we highly recommend managing those VPCs outside this resource by setting `manage_vpc_attachment` to false and using the **aviatrix_aws_tgw_vpc_attachment** resource instead of the in-line `attached_vpc {}` block.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgw",
    "Properties" : {
        "<a href="#accountname" title="AccountName">AccountName</a>" : <i>String</i>,
        "<a href="#attachedaviatrixtransitgateway" title="AttachedAviatrixTransitGateway">AttachedAviatrixTransitGateway</a>" : <i>[ String, ... ]</i>,
        "<a href="#awssideasnumber" title="AwsSideAsNumber">AwsSideAsNumber</a>" : <i>String</i>,
        "<a href="#cidrs" title="Cidrs">Cidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#cloudtype" title="CloudType">CloudType</a>" : <i>Double</i>,
        "<a href="#enablemulticast" title="EnableMulticast">EnableMulticast</a>" : <i>Boolean</i>,
        "<a href="#managesecuritydomain" title="ManageSecurityDomain">ManageSecurityDomain</a>" : <i>Boolean</i>,
        "<a href="#managetransitgatewayattachment" title="ManageTransitGatewayAttachment">ManageTransitGatewayAttachment</a>" : <i>Boolean</i>,
        "<a href="#managevpcattachment" title="ManageVpcAttachment">ManageVpcAttachment</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>,
        "<a href="#securitydomains" title="SecurityDomains">SecurityDomains</a>" : <i>[ <a href="securitydomainsdefinition.md">SecurityDomainsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgw
Properties:
    <a href="#accountname" title="AccountName">AccountName</a>: <i>String</i>
    <a href="#attachedaviatrixtransitgateway" title="AttachedAviatrixTransitGateway">AttachedAviatrixTransitGateway</a>: <i>
      - String</i>
    <a href="#awssideasnumber" title="AwsSideAsNumber">AwsSideAsNumber</a>: <i>String</i>
    <a href="#cidrs" title="Cidrs">Cidrs</a>: <i>
      - String</i>
    <a href="#cloudtype" title="CloudType">CloudType</a>: <i>Double</i>
    <a href="#enablemulticast" title="EnableMulticast">EnableMulticast</a>: <i>Boolean</i>
    <a href="#managesecuritydomain" title="ManageSecurityDomain">ManageSecurityDomain</a>: <i>Boolean</i>
    <a href="#managetransitgatewayattachment" title="ManageTransitGatewayAttachment">ManageTransitGatewayAttachment</a>: <i>Boolean</i>
    <a href="#managevpcattachment" title="ManageVpcAttachment">ManageVpcAttachment</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
    <a href="#securitydomains" title="SecurityDomains">SecurityDomains</a>: <i>
      - <a href="securitydomainsdefinition.md">SecurityDomainsDefinition</a></i>
</pre>

## Properties

#### AccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttachedAviatrixTransitGateway

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsSideAsNumber

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CloudType

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableMulticast

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageSecurityDomain

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageTransitGatewayAttachment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageVpcAttachment

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomains

_Required_: No

_Type_: List of <a href="securitydomainsdefinition.md">SecurityDomainsDefinition</a>

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

#### TgwId

Returns the <code>TgwId</code> value.

