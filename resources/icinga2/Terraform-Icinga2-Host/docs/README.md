# Terraform::Icinga2::Host

Configures an Icinga2 host resource. This allows hosts to be configured, updated,
and deleted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Icinga2::Host",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#checkcommand" title="CheckCommand">CheckCommand</a>" : <i>String</i>,
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#templates" title="Templates">Templates</a>" : <i>[ String, ... ]</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="vars.md">Vars</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Icinga2::Host
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#checkcommand" title="CheckCommand">CheckCommand</a>: <i>String</i>
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#templates" title="Templates">Templates</a>: <i>
      - String</i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="vars.md">Vars</a></i>
</pre>

## Properties

#### Address

The address of the host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CheckCommand

The name of an existing Icinga2 CheckCommand object that is used to determine if the host is available or not.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Groups

The groups of the host.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The hostname of the host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Templates

A list of Icinga2 templates to assign to the host.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

A mapping of variables to assign to the host.

_Required_: No

_Type_: List of <a href="vars.md">Vars</a>

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

