# TF::Aviatrix::AwsTgwVpcAttachment

The **aviatrix_aws_tgw_vpc_attachment** resource manages the attaching & detaching of the VPC to & from an AWS TGW, and FireNet Gateway to TGW Firewall Domain.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::AwsTgwVpcAttachment",
    "Properties" : {
        "<a href="#customizedrouteadvertisement" title="CustomizedRouteAdvertisement">CustomizedRouteAdvertisement</a>" : <i>String</i>,
        "<a href="#customizedroutes" title="CustomizedRoutes">CustomizedRoutes</a>" : <i>String</i>,
        "<a href="#disablelocalroutepropagation" title="DisableLocalRoutePropagation">DisableLocalRoutePropagation</a>" : <i>Boolean</i>,
        "<a href="#edgeattachment" title="EdgeAttachment">EdgeAttachment</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#routetables" title="RouteTables">RouteTables</a>" : <i>String</i>,
        "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>,
        "<a href="#subnets" title="Subnets">Subnets</a>" : <i>String</i>,
        "<a href="#tgwname" title="TgwName">TgwName</a>" : <i>String</i>,
        "<a href="#vpcaccountname" title="VpcAccountName">VpcAccountName</a>" : <i>String</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::AwsTgwVpcAttachment
Properties:
    <a href="#customizedrouteadvertisement" title="CustomizedRouteAdvertisement">CustomizedRouteAdvertisement</a>: <i>String</i>
    <a href="#customizedroutes" title="CustomizedRoutes">CustomizedRoutes</a>: <i>String</i>
    <a href="#disablelocalroutepropagation" title="DisableLocalRoutePropagation">DisableLocalRoutePropagation</a>: <i>Boolean</i>
    <a href="#edgeattachment" title="EdgeAttachment">EdgeAttachment</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#routetables" title="RouteTables">RouteTables</a>: <i>String</i>
    <a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
    <a href="#subnets" title="Subnets">Subnets</a>: <i>String</i>
    <a href="#tgwname" title="TgwName">TgwName</a>: <i>String</i>
    <a href="#vpcaccountname" title="VpcAccountName">VpcAccountName</a>: <i>String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
</pre>

## Properties

#### CustomizedRouteAdvertisement

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomizedRoutes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisableLocalRoutePropagation

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EdgeAttachment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RouteTables

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TgwName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcAccountName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

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

