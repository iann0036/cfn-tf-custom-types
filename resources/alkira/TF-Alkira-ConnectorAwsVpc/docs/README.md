# TF::Alkira::ConnectorAwsVpc

CloudFormation equivalent of alkira_connector_aws_vpc

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::ConnectorAwsVpc",
    "Properties" : {
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#awsregion" title="AwsRegion">AwsRegion</a>" : <i>String</i>,
        "<a href="#billingtags" title="BillingTags">BillingTags</a>" : <i>[ Double, ... ]</i>,
        "<a href="#credentialid" title="CredentialId">CredentialId</a>" : <i>String</i>,
        "<a href="#cxp" title="Cxp">Cxp</a>" : <i>String</i>,
        "<a href="#group" title="Group">Group</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#segment" title="Segment">Segment</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>,
        "<a href="#vpccidr" title="VpcCidr">VpcCidr</a>" : <i>[ String, ... ]</i>,
        "<a href="#vpcid" title="VpcId">VpcId</a>" : <i>String</i>,
        "<a href="#vpcroutetable" title="VpcRouteTable">VpcRouteTable</a>" : <i>[ <a href="vpcroutetabledefinition.md">VpcRouteTableDefinition</a>, ... ]</i>,
        "<a href="#vpcsubnet" title="VpcSubnet">VpcSubnet</a>" : <i>[ <a href="vpcsubnetdefinition.md">VpcSubnetDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::ConnectorAwsVpc
Properties:
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#awsregion" title="AwsRegion">AwsRegion</a>: <i>String</i>
    <a href="#billingtags" title="BillingTags">BillingTags</a>: <i>
      - Double</i>
    <a href="#credentialid" title="CredentialId">CredentialId</a>: <i>String</i>
    <a href="#cxp" title="Cxp">Cxp</a>: <i>String</i>
    <a href="#group" title="Group">Group</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#segment" title="Segment">Segment</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
    <a href="#vpccidr" title="VpcCidr">VpcCidr</a>: <i>
      - String</i>
    <a href="#vpcid" title="VpcId">VpcId</a>: <i>String</i>
    <a href="#vpcroutetable" title="VpcRouteTable">VpcRouteTable</a>: <i>
      - <a href="vpcroutetabledefinition.md">VpcRouteTableDefinition</a></i>
    <a href="#vpcsubnet" title="VpcSubnet">VpcSubnet</a>: <i>
      - <a href="vpcsubnetdefinition.md">VpcSubnetDefinition</a></i>
</pre>

## Properties

#### AwsAccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingTags

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CredentialId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cxp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Group

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Segment

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Size

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcCidr

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcRouteTable

_Required_: No

_Type_: List of <a href="vpcroutetabledefinition.md">VpcRouteTableDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcSubnet

_Required_: No

_Type_: List of <a href="vpcsubnetdefinition.md">VpcSubnetDefinition</a>

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

