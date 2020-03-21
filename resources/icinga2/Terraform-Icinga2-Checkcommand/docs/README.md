# Terraform::Icinga2::Checkcommand

Configures an Icinga2 checkcommand resource. This allows checkcommands to be configured, updated,
and deleted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Icinga2::Checkcommand",
    "Properties" : {
        "<a href="#arguments" title="Arguments">Arguments</a>" : <i>[ <a href="arguments.md">Arguments</a>, ... ]</i>,
        "<a href="#command" title="Command">Command</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#templates" title="Templates">Templates</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Icinga2::Checkcommand
Properties:
    <a href="#arguments" title="Arguments">Arguments</a>: <i>
      - <a href="arguments.md">Arguments</a></i>
    <a href="#command" title="Command">Command</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#templates" title="Templates">Templates</a>: <i>
      - String</i>
</pre>

## Properties

#### Arguments

A mapping of arguments to include with the command.

_Required_: No

_Type_: List of <a href="arguments.md">Arguments</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Command

Path to the command te be executed.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name by which to reference the checkcommand.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Templates

A list of Icinga2 templates to assign to the host.

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

