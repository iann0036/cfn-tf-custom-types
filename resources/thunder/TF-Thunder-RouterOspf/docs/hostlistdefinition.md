# TF::Thunder::RouterOspf HostListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#hostaddress" title="HostAddress">HostAddress</a>" : <i>String</i>,
    "<a href="#areacfg" title="AreaCfg">AreaCfg</a>" : <i>[ <a href="areacfgdefinition.md">AreaCfgDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#hostaddress" title="HostAddress">HostAddress</a>: <i>String</i>
<a href="#areacfg" title="AreaCfg">AreaCfg</a>: <i>
      - <a href="areacfgdefinition.md">AreaCfgDefinition</a></i>
</pre>

## Properties

#### HostAddress

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AreaCfg

_Required_: No

_Type_: List of <a href="areacfgdefinition.md">AreaCfgDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

