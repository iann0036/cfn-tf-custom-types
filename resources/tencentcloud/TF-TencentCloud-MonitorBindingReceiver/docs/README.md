# TF::TencentCloud::MonitorBindingReceiver

Provides a resource for bind receivers to a policy group resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::TencentCloud::MonitorBindingReceiver",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>Double</i>,
        "<a href="#receivers" title="Receivers">Receivers</a>" : <i>[ <a href="receiversdefinition.md">ReceiversDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::TencentCloud::MonitorBindingReceiver
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>Double</i>
    <a href="#receivers" title="Receivers">Receivers</a>: <i>
      - <a href="receiversdefinition.md">ReceiversDefinition</a></i>
</pre>

## Properties

#### GroupId

Policy group ID for binding receivers.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Receivers

_Required_: No

_Type_: List of <a href="receiversdefinition.md">ReceiversDefinition</a>

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

