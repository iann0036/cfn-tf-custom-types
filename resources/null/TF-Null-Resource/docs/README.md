# TF::Null::Resource

The `null_resource` resource implements the standard resource lifecycle but takes no further action.

The `triggers` argument allows specifying an arbitrary set of values that, when changed, will cause the resource to be replaced.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Null::Resource",
    "Properties" : {
        "<a href="#triggers" title="Triggers">Triggers</a>" : <i>[ <a href="triggersdefinition.md">TriggersDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Null::Resource
Properties:
    <a href="#triggers" title="Triggers">Triggers</a>: <i>
      - <a href="triggersdefinition.md">TriggersDefinition</a></i>
</pre>

## Properties

#### Triggers

_Required_: No

_Type_: List of <a href="triggersdefinition.md">TriggersDefinition</a>

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

