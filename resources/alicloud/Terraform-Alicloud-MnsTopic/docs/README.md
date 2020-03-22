# Terraform::Alicloud::MnsTopic

Provides a MNS topic resource.

-> **NOTE:** Terraform will auto build a mns topic  while it uses `alicloud_mns_topic` to build a mns topic resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::MnsTopic",
    "Properties" : {
        "<a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>" : <i>Boolean</i>,
        "<a href="#maximummessagesize" title="MaximumMessageSize">MaximumMessageSize</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::MnsTopic
Properties:
    <a href="#loggingenabled" title="LoggingEnabled">LoggingEnabled</a>: <i>Boolean</i>
    <a href="#maximummessagesize" title="MaximumMessageSize">MaximumMessageSize</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### LoggingEnabled

Is logging enabled? true or false. Default value to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaximumMessageSize

This indicates the maximum length, in bytes, of any message body sent to the topic. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

