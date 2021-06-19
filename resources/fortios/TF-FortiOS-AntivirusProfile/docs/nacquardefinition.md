# TF::FortiOS::AntivirusProfile NacQuarDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expiry" title="Expiry">Expiry</a>" : <i>String</i>,
    "<a href="#infected" title="Infected">Infected</a>" : <i>String</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#expiry" title="Expiry">Expiry</a>: <i>String</i>
<a href="#infected" title="Infected">Infected</a>: <i>String</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
</pre>

## Properties

#### Expiry

Duration of quarantine.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Infected

Enable/Disable quarantining infected hosts to the banned user list. Valid values: `none`, `quar-src-ip`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable AntiVirus quarantine logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

