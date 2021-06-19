# TF::FortiOS::SwitchcontrollerManagedswitch IpSourceGuardDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>String</i>,
    "<a href="#bindingentry" title="BindingEntry">BindingEntry</a>" : <i>[ <a href="bindingentrydefinition.md">BindingEntryDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>String</i>
<a href="#bindingentry" title="BindingEntry">BindingEntry</a>: <i>
      - <a href="bindingentrydefinition.md">BindingEntryDefinition</a></i>
</pre>

## Properties

#### Description

Description.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

Ingress interface to which source guard is bound.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BindingEntry

_Required_: No

_Type_: List of <a href="bindingentrydefinition.md">BindingEntryDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

