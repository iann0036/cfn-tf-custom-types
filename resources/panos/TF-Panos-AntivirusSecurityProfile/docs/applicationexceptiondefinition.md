# TF::Panos::AntivirusSecurityProfile ApplicationExceptionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#application" title="Application">Application</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#application" title="Application">Application</a>: <i>String</i>
</pre>

## Properties

#### Action

The action.  Valid values are `default`, `allow`,
`alert`, `block` (PAN-OS 6.1 only), `drop` (PAN-OS 7.0+), `reset-client` (PAN-OS
7.0+), `reset-server` (PAN-OS 7.0+), or `reset-both` (PAN-OS 7.0+).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Application

The application name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

