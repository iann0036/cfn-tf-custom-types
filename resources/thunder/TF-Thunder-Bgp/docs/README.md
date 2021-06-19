# TF::Thunder::Bgp

`thunder_bgp` Provides details about thunder bgp

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Thunder::Bgp",
    "Properties" : {
        "<a href="#action" title="Action">Action</a>" : <i>String</i>,
        "<a href="#asnumber" title="AsNumber">AsNumber</a>" : <i>String</i>,
        "<a href="#extendedasncap" title="ExtendedAsnCap">ExtendedAsnCap</a>" : <i>Double</i>,
        "<a href="#processid" title="ProcessId">ProcessId</a>" : <i>String</i>,
        "<a href="#sequence" title="Sequence">Sequence</a>" : <i>String</i>,
        "<a href="#uuid" title="Uuid">Uuid</a>" : <i>String</i>,
        "<a href="#nexthoptrigger" title="NexthopTrigger">NexthopTrigger</a>" : <i>[ <a href="nexthoptriggerdefinition.md">NexthopTriggerDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Thunder::Bgp
Properties:
    <a href="#action" title="Action">Action</a>: <i>String</i>
    <a href="#asnumber" title="AsNumber">AsNumber</a>: <i>String</i>
    <a href="#extendedasncap" title="ExtendedAsnCap">ExtendedAsnCap</a>: <i>Double</i>
    <a href="#processid" title="ProcessId">ProcessId</a>: <i>String</i>
    <a href="#sequence" title="Sequence">Sequence</a>: <i>String</i>
    <a href="#uuid" title="Uuid">Uuid</a>: <i>String</i>
    <a href="#nexthoptrigger" title="NexthopTrigger">NexthopTrigger</a>: <i>
      - <a href="nexthoptriggerdefinition.md">NexthopTriggerDefinition</a></i>
</pre>

## Properties

#### Action

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AsNumber

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtendedAsnCap

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProcessId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sequence

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uuid

uuid of the object.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NexthopTrigger

_Required_: No

_Type_: List of <a href="nexthoptriggerdefinition.md">NexthopTriggerDefinition</a>

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

