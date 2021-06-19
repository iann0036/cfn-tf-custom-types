# TF::FortiOS::SwitchcontrollerManagedswitch SwitchLogDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#localoverride" title="LocalOverride">LocalOverride</a>" : <i>String</i>,
    "<a href="#severity" title="Severity">Severity</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#localoverride" title="LocalOverride">LocalOverride</a>: <i>String</i>
<a href="#severity" title="Severity">Severity</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
</pre>

## Properties

#### LocalOverride

Enable to configure local logging settings that override global logging settings. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Severity

Severity of FortiSwitch logs that are added to the FortiGate event log. Valid values: `emergency`, `alert`, `critical`, `error`, `warning`, `notification`, `information`, `debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

Enable/disable adding FortiSwitch logs to the FortiGate event log. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

