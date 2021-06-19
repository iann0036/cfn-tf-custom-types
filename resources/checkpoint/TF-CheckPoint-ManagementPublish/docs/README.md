# TF::CheckPoint::ManagementPublish

This command resource allows you to Publish Changes.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::CheckPoint::ManagementPublish",
    "Properties" : {
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ String, ... ]</i>,
        "<a href="#uid" title="Uid">Uid</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::CheckPoint::ManagementPublish
Properties:
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - String</i>
    <a href="#uid" title="Uid">Uid</a>: <i>String</i>
</pre>

## Properties

#### Triggers

Triggers a publish if there are any changes to objects in this list.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uid

Session unique identifier. Specify it to publish a different session than the one you currently use.

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

#### TaskId

Asynchronous task unique identifier.

