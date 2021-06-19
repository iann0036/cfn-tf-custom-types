# TF::Alkira::InternetApplication

CloudFormation equivalent of alkira_internet_application

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alkira::InternetApplication",
    "Properties" : {
        "<a href="#billingtags" title="BillingTags">BillingTags</a>" : <i>[ Double, ... ]</i>,
        "<a href="#connectorid" title="ConnectorId">ConnectorId</a>" : <i>String</i>,
        "<a href="#connectortype" title="ConnectorType">ConnectorType</a>" : <i>String</i>,
        "<a href="#fqdnprefix" title="FqdnPrefix">FqdnPrefix</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privateip" title="PrivateIp">PrivateIp</a>" : <i>String</i>,
        "<a href="#privateport" title="PrivatePort">PrivatePort</a>" : <i>String</i>,
        "<a href="#segment" title="Segment">Segment</a>" : <i>String</i>,
        "<a href="#size" title="Size">Size</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alkira::InternetApplication
Properties:
    <a href="#billingtags" title="BillingTags">BillingTags</a>: <i>
      - Double</i>
    <a href="#connectorid" title="ConnectorId">ConnectorId</a>: <i>String</i>
    <a href="#connectortype" title="ConnectorType">ConnectorType</a>: <i>String</i>
    <a href="#fqdnprefix" title="FqdnPrefix">FqdnPrefix</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privateip" title="PrivateIp">PrivateIp</a>: <i>String</i>
    <a href="#privateport" title="PrivatePort">PrivatePort</a>: <i>String</i>
    <a href="#segment" title="Segment">Segment</a>: <i>String</i>
    <a href="#size" title="Size">Size</a>: <i>String</i>
</pre>

## Properties

#### BillingTags

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ConnectorType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnPrefix

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateIp

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivatePort

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

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### GroupId

Returns the <code>GroupId</code> value.

#### Id

Returns the <code>Id</code> value.

#### InternetApplicationId

Returns the <code>InternetApplicationId</code> value.

