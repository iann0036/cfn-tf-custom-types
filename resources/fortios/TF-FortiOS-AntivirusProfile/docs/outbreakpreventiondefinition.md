# TF::FortiOS::AntivirusProfile OutbreakPreventionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#externalblocklist" title="ExternalBlocklist">ExternalBlocklist</a>" : <i>String</i>,
    "<a href="#ftgdservice" title="FtgdService">FtgdService</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#externalblocklist" title="ExternalBlocklist">ExternalBlocklist</a>: <i>String</i>
<a href="#ftgdservice" title="FtgdService">FtgdService</a>: <i>String</i>
</pre>

## Properties

#### ExternalBlocklist

Enable/disable external malware blocklist. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FtgdService

Enable/disable FortiGuard Virus outbreak prevention service. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

