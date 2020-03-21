# Terraform::Consul::Keys Key

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#default" title="Default">Default</a>" : <i>String</i>,
    "<a href="#delete" title="Delete">Delete</a>" : <i>Boolean</i>,
    "<a href="#flags" title="Flags">Flags</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#value" title="Value">Value</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#default" title="Default">Default</a>: <i>String</i>
<a href="#delete" title="Delete">Delete</a>: <i>Boolean</i>
<a href="#flags" title="Flags">Flags</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#value" title="Value">Value</a>: <i>String</i>
</pre>

## Properties

#### Default

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Delete

If true, then the key will be deleted when
either its configuration block is removed from the configuration or
the entire resource is destroyed. Otherwise, it will be left in Consul.
Defaults to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Flags

An [unsigned integer value](https://www.consul.io/api/kv.html#flags-1)
to attach to the key (defaults to 0).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

This is the path in Consul that should be written to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Value

The value to write to the given path.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

