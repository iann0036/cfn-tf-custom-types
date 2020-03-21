# Terraform::NS1::Notifylist

Provides a NS1 Notify List resource. This can be used to create, modify, and delete notify lists.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NS1::Notifylist",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#notifications" title="Notifications">Notifications</a>" : <i>[ <a href="notifications.md">Notifications</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NS1::Notifylist
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#notifications" title="Notifications">Notifications</a>: <i>
      - <a href="notifications.md">Notifications</a></i>
</pre>

## Properties

#### Name

The free-form display name for the notify list.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notifications

_Required_: No

_Type_: List of <a href="notifications.md">Notifications</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

