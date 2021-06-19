# TF::FortiOS::FmgJsonrpcRequest

This resource supports handling JSON RPC request for FortiManager.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::FortiOS::FmgJsonrpcRequest",
    "Properties" : {
        "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
        "<a href="#jsoncontent" title="JsonContent">JsonContent</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::FortiOS::FmgJsonrpcRequest
Properties:
    <a href="#comment" title="Comment">Comment</a>: <i>String</i>
    <a href="#jsoncontent" title="JsonContent">JsonContent</a>: <i>String</i>
</pre>

## Properties

#### Comment

Comment.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### JsonContent

JSON RPC request, which should contain 'method' and 'params' parameters.

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

#### Response

Returns the <code>Response</code> value.

