# TF::Panos::PanoramaSecurityRuleGroup TargetDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#serial" title="Serial">Serial</a>" : <i>String</i>,
    "<a href="#vsyslist" title="VsysList">VsysList</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#serial" title="Serial">Serial</a>: <i>String</i>
<a href="#vsyslist" title="VsysList">VsysList</a>: <i>
      - String</i>
</pre>

## Properties

#### Serial

The serial number of the firewall.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VsysList

A subset of all available vsys on the firewall
that should be in this device group.  If the firewall is a virtual firewall,
then this parameter should just be omitted.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

