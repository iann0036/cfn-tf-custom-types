# TF::CheckPoint::ManagementAddApiKey

This command resource allows you to execute Check Point Add Api Key.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementAddApiKey",
    "Properties" : {
        "<a href="#adminname" title="AdminName">AdminName</a>" : <i>String</i>,
        "<a href="#adminuid" title="AdminUid">AdminUid</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementAddApiKey
Properties:
    <a href="#adminname" title="AdminName">AdminName</a>: <i>String</i>
    <a href="#adminuid" title="AdminUid">AdminUid</a>: <i>String</i>
</pre>

## Properties

#### AdminName

Administrator name to generate API key for.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AdminUid

Administrator uid to generate API key for.

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

#### ApiKey

Represents the API Key to be used for Login.

#### Id

Returns the <code>Id</code> value.

