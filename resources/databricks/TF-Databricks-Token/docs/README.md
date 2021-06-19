# TF::Databricks::Token

CloudFormation equivalent of databricks_token

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::Token",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#creationtime" title="CreationTime">CreationTime</a>" : <i>Double</i>,
        "<a href="#expirytime" title="ExpiryTime">ExpiryTime</a>" : <i>Double</i>,
        "<a href="#lifetimeseconds" title="LifetimeSeconds">LifetimeSeconds</a>" : <i>Double</i>,
        "<a href="#tokenid" title="TokenId">TokenId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::Token
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#creationtime" title="CreationTime">CreationTime</a>: <i>Double</i>
    <a href="#expirytime" title="ExpiryTime">ExpiryTime</a>: <i>Double</i>
    <a href="#lifetimeseconds" title="LifetimeSeconds">LifetimeSeconds</a>: <i>Double</i>
    <a href="#tokenid" title="TokenId">TokenId</a>: <i>String</i>
</pre>

## Properties

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpiryTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifetimeSeconds

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenId

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

#### Id

Returns the <code>Id</code> value.

#### TokenValue

Returns the <code>TokenValue</code> value.

