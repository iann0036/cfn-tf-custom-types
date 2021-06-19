# TF::BIGIP::Command

`bigip_command` Run TMSH commands on F5 devices

This resource is helpful to send TMSH command to an BIG-IP node and returns the results read from the device

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::BIGIP::Command",
    "Properties" : {
        "<a href="#commandresult" title="CommandResult">CommandResult</a>" : <i>[ String, ... ]</i>,
        "<a href="#commands" title="Commands">Commands</a>" : <i>[ String, ... ]</i>,
        "<a href="#when" title="When">When</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::BIGIP::Command
Properties:
    <a href="#commandresult" title="CommandResult">CommandResult</a>: <i>
      - String</i>
    <a href="#commands" title="Commands">Commands</a>: <i>
      - String</i>
    <a href="#when" title="When">When</a>: <i>String</i>
</pre>

## Properties

#### CommandResult

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Commands

The commands to send to the remote BIG-IP device over the configured provider. The resulting output from the command is returned and added to `command_result`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### When

default value will be `apply`,can be set to `destroy` for terraform destroy call.

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

