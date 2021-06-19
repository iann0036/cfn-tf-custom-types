# TF::Akamai::NetworklistSubscription

Use the `akamai_networklist_subscription` resource to specify a set of email addresses to be notified of changes to any
of a set of network lists.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Akamai::NetworklistSubscription",
    "Properties" : {
        "<a href="#networklist" title="NetworkList">NetworkList</a>" : <i>[ String, ... ]</i>,
        "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Akamai::NetworklistSubscription
Properties:
    <a href="#networklist" title="NetworkList">NetworkList</a>: <i>
      - String</i>
    <a href="#recipients" title="Recipients">Recipients</a>: <i>
      - String</i>
</pre>

## Properties

#### NetworkList

A list containing one or more IDs of the network lists to which the indicated email
addresses should be subscribed.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

A bracketed, comma-separated list of email addresses that will be notified of changes to any
of the specified network lists.

_Required_: Yes

_Type_: List of String

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

