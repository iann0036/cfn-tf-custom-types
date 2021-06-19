# TF::CheckPoint::ManagementSetApiSettings

This command resource allows you to execute Check Point Set Api Settings.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementSetApiSettings",
    "Properties" : {
        "<a href="#acceptedapicallsfrom" title="AcceptedApiCallsFrom">AcceptedApiCallsFrom</a>" : <i>String</i>,
        "<a href="#automaticstart" title="AutomaticStart">AutomaticStart</a>" : <i>Boolean</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementSetApiSettings
Properties:
    <a href="#acceptedapicallsfrom" title="AcceptedApiCallsFrom">AcceptedApiCallsFrom</a>: <i>String</i>
    <a href="#automaticstart" title="AutomaticStart">AutomaticStart</a>: <i>Boolean</i>
</pre>

## Properties

#### AcceptedApiCallsFrom

Clients allowed to connect to the API Server.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AutomaticStart

MGMT API will start after server will start.

_Required_: No

_Type_: Boolean

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

