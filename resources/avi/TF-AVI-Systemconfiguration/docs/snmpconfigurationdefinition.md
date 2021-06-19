# TF::AVI::Systemconfiguration SnmpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#community" title="Community">Community</a>" : <i>String</i>,
    "<a href="#largetrappayload" title="LargeTrapPayload">LargeTrapPayload</a>" : <i>Boolean</i>,
    "<a href="#syscontact" title="SysContact">SysContact</a>" : <i>String</i>,
    "<a href="#syslocation" title="SysLocation">SysLocation</a>" : <i>String</i>,
    "<a href="#version" title="Version">Version</a>" : <i>String</i>,
    "<a href="#snmpv3config" title="SnmpV3Config">SnmpV3Config</a>" : <i>[ <a href="snmpv3configdefinition.md">SnmpV3ConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#community" title="Community">Community</a>: <i>String</i>
<a href="#largetrappayload" title="LargeTrapPayload">LargeTrapPayload</a>: <i>Boolean</i>
<a href="#syscontact" title="SysContact">SysContact</a>: <i>String</i>
<a href="#syslocation" title="SysLocation">SysLocation</a>: <i>String</i>
<a href="#version" title="Version">Version</a>: <i>String</i>
<a href="#snmpv3config" title="SnmpV3Config">SnmpV3Config</a>: <i>
      - <a href="snmpv3configdefinition.md">SnmpV3ConfigDefinition</a></i>
</pre>

## Properties

#### Community

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LargeTrapPayload

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysContact

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SysLocation

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SnmpV3Config

_Required_: No

_Type_: List of <a href="snmpv3configdefinition.md">SnmpV3ConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

