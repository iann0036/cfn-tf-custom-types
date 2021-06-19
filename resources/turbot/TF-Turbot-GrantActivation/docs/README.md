# TF::Turbot::GrantActivation

The `Turbot Grant Activation` resource helps activate grants for Turbot users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Turbot::GrantActivation",
    "Properties" : {
        "<a href="#grant" title="Grant">Grant</a>" : <i>String</i>,
        "<a href="#resource" title="Resource">Resource</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Turbot::GrantActivation
Properties:
    <a href="#grant" title="Grant">Grant</a>: <i>String</i>
    <a href="#resource" title="Resource">Resource</a>: <i>String</i>
</pre>

## Properties

#### Grant

The `aka` of the grant to activate.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Resource

The id or `aka` of the resource for which the grant is activated.
- `grant` - (Required) The `aka` of the grant to activate.

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

#### ResourceAkas

Returns the <code>ResourceAkas</code> value.

